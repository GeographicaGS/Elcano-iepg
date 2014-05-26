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
        data = variable.getVariableData()
        years = variable.getVariableYears()
        codes = variable.getVariableCodes()
        a = numpy.empty((len(years), len(codes)), float)
        a[:] = numpy.NaN
        for y in variable.getVariableYears():
            for c in variable.getVariableCodes(year=y):
                fData = [i for i in data if i["code"]==c and i["date_in"].year==y][0]["value"]
                a[years.index(y),codes.index(c)]=fData
        self.data = a
        self.codeIndex = codes
        self.timeIndex = years

    def getData(self, code, year):
        """Retrieves a data.
        TODO: restricted to years."""
        return(self.data[self.timeIndex.index(year),self.codeIndex.index(code)])

                    
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
        m = varenginemodel.VarEngineModel()
        return(sorted([int(i["year"]) for i in m.getVariableYears(self)]))

    def getVariableCodes(self, year=None):
        """Returns available codes for variable idVariable."""
        m = varenginemodel.VarEngineModel()
        return(sorted([i["code"] for i in m.getVariableCodes(self, year)]))

    def getVariableData(self, year=None, codes=None):
        """Returns variable values. TODO: fixed to years, pass a selection of codes."""
        m = varenginemodel.VarEngineModel()
        return(m.getVariableData(self, year))
    
    def populateFromTable(self, sourceTable, dateInColumn, dateOutColumn, 
                          codeColumn, valueColumn):
        """Populates the variable table from another table.
        TODO: currently, the table must be in the same database. Make it resposive to a PostgreSQL
        connection to get data elsewhere.
        Create also a version in which dateInColumn and dateOutColumn are not columns, but a timelapse."""
        m = varenginemodel.VarEngineModel()
        return(m.populateFromTable(self, sourceTable, dateInColumn, dateOutColumn, codeColumn,
                                         valueColumn))




























# def getVariable(idFamily, idVariable):
#     """Returns variable with ID idVariable."""
#     m = enginemodel.EngineModel()
#     return(m.getVariable(idFamily, idVariable))


# def getVariables(family=None):
#     m = enginemodel.EngineModel()
#     return(m.getVariables(family))


# def getIdFamilyByName(name):
#     """Returns the variable family ID by it's english name."""
#     m = enginemodel.EngineModel()
#     return(m.getIdFamilyByName(name)[0]["id_family"])


# def getVariableValue(idFamily, idVariable, code, year):
#     """Returns the value of a variable."""
#     m = enginemodel.EngineModel()
#     var = getVariable(idFamily, idVariable)
#     d = m.getVariableValue(var["var_table"], var["var_column"], code, year)
#     return(d["data"] if d else None)
