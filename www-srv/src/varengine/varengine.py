# coding=UTF8

"""

Variable engine.

TODO: variables should be coded with a date_in/date_out time lapse and a code. 
This code is expressed in whatever code stored as a name family in Maplex, and this family
must be stored in variable metadata. Internally, only id_geoentity must be used. Create 
functions for translation between different codes. Treat codes as arrays, for there can be
in a family more than one name for the same geoentity.

Combine Maplex and Engine?

TODO: Create a class in Elcano to store long lasting dictionaries and translation tables coming from the 
database to retrieve them easily

TODO: create a plugin architecture for both source data and repository data, so metadata and data can
be stored to PostgreSQL, or files, or R datasets, or JSON, etc. DataSource with methods both for reading
and for writing.

"""
import varenginemodel
import numpy


class DataCache(object):
    """Data cache on Numpy ndarrays. Creates an 2 dimensional xy array with codes in
    Y, time in X, indexed with two lists of codes and times (years).
    TODO: restricted to year. Expand to time slice with Maplex."""
    data = None
    codeIndex = None
    timeIndex = None

    def __init__(self, variable):
        """Adds a variable to the cache. Variable is """
        data = variable.getData()
        years = variable.getVariableYears()
        codes = variable.getVariableCodes()
        a = numpy.empty((len(years), len(codes)), float)
        a[:] = numpy.NaN
        for y in years:
            for c in codes:
                fData = [i for i in data if i["code"]==c and i["year"]==y]
                a[years.index(y),codes.index(c)]=fData[0]["value"] if fData<>[] else numpy.NaN
        self.data = a
        self.codeIndex = codes
        self.timeIndex = years

    def getData(self, code=None, year=None):
        """Retrieves a data, either sliced by year of by code.
        TODO: restricted to years."""
        if code and not year:
            a = self.data[0:,self.codeIndex.index(code)]
            return({self.timeIndex[i]: a[i] for i in range(0, len(self.timeIndex))})
        if year and not code:
            a = self.data[self.timeIndex.index(year),0:]
            return({self.codeIndex[i]: a[i] for i in range(0, len(self.codeIndex))})            
        if year and code:
            d = dict()
            d["year"]=year
            d["code"]=code
            d["value"]=self.data[self.timeIndex.index(year),self.codeIndex.index(code)]
            return(d)

        out = []
        for c in self.codeIndex:
            for y in self.timeIndex:
                d = dict()
                d["year"]=y
                d["code"]=c
                d["value"]=self.data[self.timeIndex.index(y),self.codeIndex.index(c)]
                out.append(d)
        return(out)

                    
class Dataset(object):
    """varengine Dataset class. Manages families of variables.
    TODO: delete cascade dataset."""
    idDataset = None
    variables = None

    def __init__(self, idDataset):
        """Constructor."""
        self.idDataset = idDataset
        self.variables = dict()

    def __str__(self):
        """String representation."""
        return(self.idDataset)

    def createVariable(self, idVariable, continuous, dataType):
        """Creates and registers a variable in this dataset. Returns Variable object."""
        self.variables[idVariable] = Variable(self, idVariable, continuous, dataType)
        return(self.variables[idVariable])

    def registerInDatabase(self):
        """Stores the dataset in the database.
        TODO: update existing dataset."""
        m = varenginemodel.VarEngineModel()
        return(m.registerDataset(self))

    def loadFromDatabase(self):
        """Reads dataset data from the database."""
        m = varenginemodel.VarEngineModel()
        data = m.loadVariablesForDataset(self)
        for i in data:
            self.variables[i["id_variable"]] = Variable(self, i["id_variable"], 
                                                        i["continuous"], i["datatype"])


class Variable(object):
    """varengine Variable class. Manages variable data. Should not be created alone.
    Generate variables from dataset."""
    dataset = None
    idVariable = None
    continuous = None
    dataType = None
    cache = None

    def __init__(self, dataset, idVariable, continuous, dataType):
        self.dataset = dataset
        self.idVariable = idVariable
        self.continuous = continuous
        self.dataType = dataType
    
    def __str__(self):
        """String representation."""
        return("Dataset: "+self.dataset.idDataset+", Variable: "+self.idVariable)

    def createVariableTable(self):
        """Creates the table in the database for variable data."""
        m = varenginemodel.VarEngineModel()
        return(m.createVariableTable(self))

    def registerInDatabase(self):
        """Registers variable in the database."""
        m = varenginemodel.VarEngineModel()
        return(m.registerVariable(self))

    def tableName(self):
        """Returns variable table name."""
        return(self.dataset.idDataset+"_"+self.idVariable)

    def getVariableYears(self):
        """Returns years present in a variable. TODO: make it generic."""
        if self.cache:
            return(self.cache.timeIndex)
        else:
            return(list(set([int(i["year"]) for i in self.getData()])))
    
    def getVariableCodes(self):
        """Returns codes present in a variable."""
        if self.cache:
            return(self.cache.codeIndex)
        else:
            return(list(set([i["code"] for i in self.getData()])))

    def getData(self, code=None, year=None):
        """Returns available codes for variable idVariable. TODO: This isn't correct, since in
        the original data not all codes may have a value for the given year. Nulls are only
        well handle with cache."""
        if self.cache:
            return(self.cache.getData(code=code, year=year))
        else:
            m = varenginemodel.VarEngineModel()
            return(m.getData(self, year, code))
    
    def populateFromTable(self, sourceTable, dateInColumn, dateOutColumn, 
                          codeColumn, valueColumn):
        """Populates the variable table from another table.
        TODO: currently, the table must be in the same database. Make it resposive to a PostgreSQL
        connection to get data elsewhere.
        Create also a version in which dateInColumn and dateOutColumn are not columns, but a timelapse."""
        m = varenginemodel.VarEngineModel()
        return(m.populateFromTable(self, sourceTable, dateInColumn, dateOutColumn, codeColumn,
                                         valueColumn))

    def cacheData(self, cacheWrapperFunc=None):
        """Creates a cache with variable data. Returns the cache."""
        if cacheWrapperFunc:
            self.cache = cacheWrapperFunc(DataCache, self)
        else:
            self.cache = DataCache(self)
        return(self.cache)
