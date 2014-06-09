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
import numpy
import copy
import base.PostgreSQL.PostgreSQLModel as PostgreSQLModel
import common.arrayops as arrayops
import maplex as maplex
from psycopg2 import ProgrammingError
import importlib



class DataStore(object):
    """Base class for a data store driver."""
    id = None
    dataSets = None

    def __init__(self, id):
        """Initializator."""
        self.id = id
        self.dataSets = dict()
    
    def __str__(self):
        """String representation."""
        return(self.id)



class DataStorePostgreSql(DataStore, PostgreSQLModel.PostgreSQLModel):
    """DataStore for PostgreSQL.
    TODO: inheriting PostgreSQLModel directly. Check other possibilities."""
    schema = None

    def __init__(self, id, schema):
        """Initializator."""
        DataStore.__init__(self, id)
        PostgreSQLModel.PostgreSQLModel.__init__(self)
        self.schema = schema

    def createDataSet(self, dataSetName):
        """Creates a new DataSet."""
        sql = """
        insert into {}.dataset
        values(%s);
        """.format(self.schema)
        self.queryCommit(sql, bindings=[dataSetName])
        self.dataSets[dataSetName] = DataSet(dataSetName)

    def createVariable(self, dataSet, variableName, continuous, dataType):
        """Creates a new variable."""
        sql = """
        insert into {}.variable
        values(%s,%s,%s,%s);
        """.format(self.schema)
        self.queryCommit(sql, bindings=[dataSet, variableName, continuous, dataType])
        var = Variable(id, continuous, dataType, dataSet=self.dataSets[dataSet])

    ###HERE, create a function to get a DataInterface and populate variables based on it's name by default
    # from DataInterface data. Optionally, create a map for DataInterfaceName>VariableName. Don't load
    # data into variables, left them unloaded. Write to the DataStore < as an option.
    def loadFromDataInterface(self, dataSet

    def registerDataSet(self, dataSet):
        """Registers a DataSet in the DataStore.
        TODO: PostgreSQL exceptions."""
        sql = """
        insert into {}.dataset values(%s);
        """.format(self.schema)
        self.queryCommit(sql, bindings=[dataSet.id])

        for i,v in dataSet.variables.iteritems():
            sql = """
            insert into {}.variable
            values(%s, %s, %s, %s);""".format(self.schema)
            self.queryCommit(sql, bindings=[v.dataSet.id, v.id, v.continuous,
                                            v.defaultDataType])

        # TODO: use COPY
        # (http://stackoverflow.com/questions/1869973/recreating-postgres-copy-directly-in-python)
        for i,j in dataSet.variables.iteritems():
            self.__createVariableTable(j.id)
            for k,v in j.data.iteritems():
                sql = """
                insert into {}.{}
                values(%s, %s, %s, %s);""".format(self.schema, j.id)
                self.queryCommit(sql, bindings=[v["code"], v["type"], v["value"], v["year"]])
        return(self)

    # def getVariableData(self, dataSet, 

    def getDataSetNames(self):
        """Returns DataSet names."""
        sql = """
        select * from {}.dataset;
        """.format(self.schema)
        return([v["id_dataset"] for v in self.query(sql).result()])

    def getVariables(self, dataSetName):
        """Returns variables of the given DataSet."""
        sql = """
        select * from {}.variable;
        """.format(self.schema)
        out = []
        for v in self.query(sql).result():
            var = Variable(v["id_variable"], v["continuous"], v["datatype"])
            out.append(var)
        return(out)

    def getDataSet(self, dataSetName):
        """Returns a DataSet with all variables loaded."""
        ds = DataSet(dataSetName)

    def __createVariableTable(self, name):
        """Creates a table for a variable. TODO: restricted to years."""
        sql = """
        create table {}.{}(
        code varchar(250),
        type varchar(250),
        value varchar(500),
        year integer);
        """.format(self.schema, name)
        self.queryCommit(sql)

    def remove(self):
        """Removes the DataStore from database.
        TODO: PostgreSQL exceptions."""
        sql = """
        drop schema {} cascade;
        """.format(self.schema)
        self.queryCommit(sql)
        return(self)

    def setup(self):
        """Set ups the database structure.
        TODO: check ownership of this when a proper PostgreSQL connection
        is in place."""
        sql = """
        create schema {};

        create table {}.dataset(
        id_dataset varchar(250)
        );
        
        alter table {}.dataset
        add constraint family_pkey
        primary key (id_dataset);

        create table {}.variable(
        id_dataset varchar(250),
        id_variable varchar(250),
        continuous boolean,
        dataType varchar(25)    
        );

        alter table {}.variable
        add constraint variable_pkey
        primary key (id_variable, id_dataset);

        alter table {}.variable
        add constraint variable_dataset_fkey
        foreign key (id_dataset) references {}.dataset(id_dataset);
        """.format(self.schema, self.schema, self.schema, self.schema, self.schema, 
                   self.schema, self.schema)
        try:
            self.queryCommit(sql)
        except ProgrammingError as e:
            raise VarEngineDataStorePostgreSqlException("PostgreSQL error: "+str(e))



class DataCache(object):
    """Base class for a data cache driver."""
    id = None
    data = None
    dataType = None

    def __init__(self, id):
        """Initializator."""
        self.id = id
        self.data = None
        self.dataType = None



class DataCacheNumpy(DataCache):
    """Numpy DataCache. Data cache on Numpy ndarrays. Creates an 2 dimensional xy array with codes in
    Y, time in X, indexed with two lists of codes and times (years).
    TODO: restricted to year. Expand to time slice with Maplex."""
    codeIndex = None
    timeIndex = None

    def __init__(self, id):
        """Initializator."""
        DataCache.__init__(self, id)
        codeIndex = None
        timeIndex = None

    def cacheData(self, variable):
        """Gets the data from the variable and caches them."""
        varData = variable.getData()
        self.dataType = variable.defaultDataType
        years = variable.getVariableYears()
        codes = variable.getVariableCodes()
        a = numpy.empty((len(years), len(codes)), float)
        a[:] = numpy.NaN
        for y in years:
            for c in codes:
                fData = [v for (k,v) in varData.iteritems() if v["code"]==c and v["year"]==y]
                a[years.index(y),codes.index(c)]=fData[0]["value"] if fData<>[] else None
        self.data = a
        self.codeIndex = codes
        self.timeIndex = years

    def getData(self, code=None, year=None):
        """Retrieves a data, either sliced by year of by code.
        TODO: restricted to years."""
        if code and not year:
            if code not in self.codeIndex:
                return([None])
            a = self.data[0:,self.codeIndex.index(code)]
            v = {code+str(self.timeIndex[int(i)]): 
                 {"code": code,
                  "type": self.dataType,
                  "value": a[i] if not numpy.isnan(a[i]) else None,
                  "year": self.timeIndex[int(i)]}
                 for i in range(0, len(self.timeIndex))}
            return(v)
        if year and not code:
            if year not in self.timeIndex:
                return([None])
            a = self.data[self.timeIndex.index(year),0:]
            v = {self.codeIndex[i]+str(year):
                 {"code": self.codeIndex[i],
                  "type": self.dataType,
                  "value": a[i] if not numpy.isnan(a[i]) else None,
                  "year": year}
                 for i in range(0, len(self.codeIndex))}
            return(v)
        if year and code:
            if code not in self.codeIndex or year not in self.timeIndex:
                return([None])
            d = dict()
            d["year"]=year
            d["code"]=code
            d["type"]=self.dataType
            v =self.data[self.timeIndex.index(year),self.codeIndex.index(code)]
            d["value"] = v if not numpy.isnan(v) else None
            return({code+str(year): d})

        out = {}
        for c in self.codeIndex:
            for y in self.timeIndex:
                d = dict()
                d["year"]=y
                d["code"]=c
                d["type"]=self.dataType
                v =self.data[self.timeIndex.index(y),self.codeIndex.index(c)]
                d["value"] = v if not numpy.isnan(v) else None
                out[c+str(y)] = d
        return(out)



class DataSet(object):
    """Dataset."""
    id = None
    variables = None

    def __init__(self, id):
        """Initializator."""
        self.id = id
        self.variables = dict()

    def __str__(self):
        return(self.id)

    def registerVariable(self, variable):
        self.variables[variable.id] = variable
        return(variable)



class Variable(object):
    """Variable. This is a mix of variable metadata and a data structure. Currently is 
    restricted to years. Data structure is:

    {
    "Code+Year": {
    "code": code,
    "type": type,
    "value": value,
    "year": year}
    }"""
    id = None
    dataSet = None
    continuous = None
    defaultDataType = None
    data = None

    def __init__(self, id, continuous, defaultDataType, dataSet=None):
        """Initializator."""
        self.id = id
        self.dataSet = dataSet
        self.continuous = continuous
        self.defaultDataType = defaultDataType
        self.data = dict()
        self.codeIndex = []
        self.yearIndex = []
        self.cache = None
        if self.dataSet:
            self.dataSet.registerVariable(self)

    def __str__(self):
        return(self.id)

    def loadFromDataInterface(self, dataInterface, variable):
        """Load that from a DataInterface. Erases any data in variable data.
        TODO: constricted to years"""
        self.data = copy.deepcopy(dataInterface.data[variable])
        for k,v in dataInterface.data[variable].iteritems():
            self.data[k]["type"] = self.defaultDataType
            self.data[k]["year"] = v["year"]

    def loadFromDataStore(self, dataStore, dataSet, variable):
        """Loads from a DataStore. Erases any data in variable data."""
        # self.data = 

    def addValue(self, code, year, dataType, value):
        """Adds a value. TODO: restricted to years."""
        self.data[code+str(year)] = {
            "code": code, 
            "year": year, 
            "type": dataType, 
            "value": str(value)
        }

    def getVariableYears(self):
        """Returns years in the variable. TODO: Restricted to years."""
        return(list(set([v["year"] for (k,v) in self.data.iteritems()])))

    def getVariableCodes(self):
        """Returns codes in the variable."""
        return(list(set([v["code"] for (k,v) in self.data.iteritems()])))

    def getData(self, code=None, year=None):
        """Get data from variable.
        TODO: restricted to years. TODO: Type management can be more sophisticated. Create
        datatype classes and try to pickle it."""
        if code and year:
            try:
                return({code+str(year): self.__processData(self.data[code+str(year)])})
            except:
                return({code+str(year): {"code": code, "type": self.defaultDataType,
                                         "value": None, "year": year}})
        if code:
            try: 
                return({k: self.__processData(v) for (k,v) in self.data.iteritems() if code in k})
            except:
                return({code+str(year): {"code": code, "type": self.defaultDataType,
                                         "value": None, "year": year}})
        if year:
            try:
                return({k: self.__processData(v) for (k,v) in self.data.iteritems() if str(year) in k})
            except:
                return({code+str(year): {"code": code, "type": self.defaultDataType,
                                         "value": None, "year": year}})
        return({k: self.__processData(v) for (k,v) in self.data.iteritems()})
    
    def __processData(self, data):
        """Process data, without changing them."""
        if "blockfunc::" in data["type"]:
            d = copy.deepcopy(data)
            module, function = d["type"][d["type"].find("::")+2:].rsplit(".",1)
            mod = importlib.import_module(module)
            func = getattr(mod, function)
            d["value"] = func(d)
            d["type"] = self.defaultDataType
            return(d)
            
        if data["type"]=="float":
            d = copy.deepcopy(data)
            d["value"] = float(d["value"])
            d["type"] = self.defaultDataType
            return(d)
            


class DataInterface(object):
    """Data interface base class."""
    data = None

    def __init__(self):
        """Initializator."""
        self.data = None

    def clearData(self):
        """Clears data from the DataInterface."""
        self.data = None

        

class DataInterfacePostgreSql(DataInterface, PostgreSQLModel.PostgreSQLModel):
    """Data interface for PostgreSQL."""
    cursor = None

    def __init__(self):
        """Initializator. TODO: create a custom connection."""
        PostgreSQLModel.PostgreSQLModel.__init__(self)
        self.cursor = None
        self.data = dict()

    def readAll(self, table, codeColumn, dateInColumn, dateOutColumn):
        """Reads all data from a table.
        TODO: make it with a cursor.
        TODO: restricted to years."""
        sql = """
        select *
        from {};
        """.format(table)
        query = self.query(sql).result()
        variables = arrayops.arraySubstraction(query[0].keys(), [codeColumn, dateInColumn, dateOutColumn])
        for i in variables:
            variable = dict()
            for a in query:
                d = {
                    "code": a[codeColumn], 
                    "year": a[dateInColumn].year,
                    "value": a[i]
                }
                variable[str(d["code"])+str(d["year"])] = d
            self.data[i] = variable
        print self.data

    def read(self, table, codeColumn, dateInColumn, dateOutColumn, valueColumn):
        """Reads all data from a column of a PostgreSQL table.
        TODO: restricted to years."""
        sql = """
        select 
        {} as code,
        {} as date_in,
        {} as date_out,
        {} as value
        from {};
        """.format(codeColumn, dateInColumn, dateOutColumn, valueColumn, table)
        query = self.query(sql).result()
        variable = {}
        for a in query:
            d = {
                "code": a["code"], 
                "year": a["date_in"].year,
                "value": a["value"]
            }
            variable[str(d["code"])+str(d["year"])] = d

        self.data[valueColumn] = variable



class VarEngineException(Exception):
    """Generic VarEngineException."""
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)



class VarEngineDataStorePostgreSqlException(VarEngineException):
    """Generic exception for PostgreSQL DataStore."""
    def __init__(self, value):
        VarEngineException.__init__(self, value)

    def __str__(self):
        return repr(self.value)

