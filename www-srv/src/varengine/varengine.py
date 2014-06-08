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
import base.PostgreSQL.PostgreSQLModel as PostgreSQLModel
import common.arrayops as arrayops
import maplex as maplex
from psycopg2 import ProgrammingError
import copy
import importlib


class DataSource(object):
    """DataSource base."""
    id = None
    dataSets = None

    def __init__(self, id):
        """Initializator."""
        self.id = id
        self.dataSets = dict()

    def __str__(self):
        return(self.id)
        
    def getData(self, code=None, year=None):
        """Returns all data in all datasets."""
        raise NotImplementedError("DataSource getData not implemented.")



class DataStore(DataSource):
    """Base class for a data store driver."""
    def __init__(self, id):
        """Initializator."""
        DataSource.__init__(self, id)
    
    def __str__(self):
        """String representation."""
        return(self.id)

    # def registerDataset(self, key, dataset):
    #     """Registers a dataset in the DataStore."""
    #     self.datasets[key] = dataset



class DataStorePostgreSql(DataStore, PostgreSQLModel.PostgreSQLModel):
    """DataStore for PostgreSQL.
    TODO: inheriting PostgreSQLModel directly. Check other possibilities."""
    schema = None

    def __init__(self, id, schema):
        """Initializator."""
        DataStore.__init__(self, id)
        PostgreSQLModel.PostgreSQLModel.__init__(self)
        self.schema = schema

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
        return(self)

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



class DataCache(DataSource):
    """Base class for a data cache driver."""
    def __init__(self, id):
        """Initializator."""
        DataSource.__init__(self, id)



class DataCacheNumpy(DataCache):
    """Numpy DataCache."""
    def __init__(self, id):
        """Initializator."""
        DataCache.__init__(self, id)



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
    "CodeYear": {
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
        if self.dataSet:
            self.dataSet.registerVariable(self)

    def __str__(self):
        return(self.id)

    def loadFromDataInterface(self, dataInterface, variable):
        """Load that from a DataInterface.
        TODO: constricted to years"""
        self.data = copy.deepcopy(dataInterface.data[variable])
        for k,v in dataInterface.data[variable].iteritems():
            self.data[k]["type"] = self.defaultDataType
            self.data[k]["year"] = v["year"]

    def addValue(self, code, year, dataType, value):
        """Adds a value. TODO: restricted to years."""
        self.data[code+str(year)] = {
            "code": code, 
            "year": year, 
            "type": dataType, 
            "value": str(value)
        }

    ###HERE
    def getData(self, code=None, year=None):
        """Get data from variable.
        TODO: restricted to years. TODO: Type management can be more sophisticated. Create
        datatype classes and try to pickle it."""
        if code and year:
            a = {code+str(year): {k: v for (k,v) in self.data[code+str(year)].iteritems()}}
            return(self.__processData(a[a.keys()[0]]))
        if code:
            return({k: v for (k,v) in self.data.iteritems() if code in k})
        if year:
            return({k: v for (k,v) in self.data.iteritems() if str(year) in k})
        return(__processData(self.data))
    
    ###HERE end the blockfunc call. Don't forget to change the datatype in the variable data
    # once the function has been executed.

    def __processData(self, data):
        """Process data, without changing them."""
        if "blockfunc::" in data["type"]:
            module, function = data["type"][data["type"].find("::")+2:].rsplit(".",1)
            mod = importlib.import_module(module)
            func = getattr(mod, function)
            data["value"] = func(data)
            data["type"] = self.defaultDataType
            return(data)
            
        if data["type"]=="float":
            data["value"] = float(data["value"])
            data["type"] = self.defaultDataType
            return(data)
            


class DataInterface(object):
    """Data interface base class."""
    def __init__(self):
        """Initializator."""



class DataInterfacePostgreSql(DataInterface, PostgreSQLModel.PostgreSQLModel):
    """Data interface for PostgreSQL."""
    cursor = None
    data = None

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

