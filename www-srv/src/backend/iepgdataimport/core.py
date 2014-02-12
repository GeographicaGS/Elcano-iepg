# coding=UTF8

"""
This module takes a plain text, CSV interchange format of IEPG data
and load them into the database.
"""

import io
from model.base.PostgreSQL.PostgreSQLModel import PostgreSQLModel
from backend.iepgerror import IepgError

class FileLoader(object):
    """IEPG CSV file loader."""
    __fileName = ''
    """File name."""
    __newLine = ''
    """New line character."""
    __encoding = ''
    """Encoding of the file."""

    def __init__(self, fileName, newLine, encoding):
        """Constructor."""
        self.__fileName = fileName
        self.__newLine = newLine
        self.__encoding = encoding

    def readFile(self):
        """Reads the file."""
        dataFile = io.open(self.__fileName, 'r', newline=self.__newLine, encoding=self.__encoding)
        data = []
        
        for a in dataFile.readlines():
            a = a.rstrip(self.__newLine)
            if not self.__checkVoidLine(a):
                data.append(a)

        dataFile.close()
        return data

    def __checkVoidLine(self, line):
        """Checks if a line is void (all ;)."""
        for i in line:
            if i!=';':
                return False
             
        return True



class ImportModel(PostgreSQLModel):
    """Model for importing IEPG CSV into the PostgreSQL."""
    __insertData = []
    __insertDataSchema = []

    def __init__(self):
        """Constructor."""
        PostgreSQLModel.__init__(self)
        self.__insertData = []
        self.__insertDataSchema = []

    def createTable(self, tableSchema, tableName, fieldName, fieldType):
        """
        Creates a table with a given schema. The 'field*' parameter are
        lists containing the schema of the table obviously they have
        to match in dimensions.
        """
        sql = 'create table '+tableSchema+'.'+tableName+'('

        for i in range(0, len(fieldName)):
            print(fieldName[i])
            sql += fieldName[i]+' '+fieldType[i]+','

        sql = sql.rstrip(',')+');'

        print(sql)

    def insertMetadata(self, id_variable, variable_en, variable_es, description_en, description_es, \
                       info_type, iepg_type, code_type, variable_type, data_type):
        """Inserts dataset metadata."""

        self.insert('iepg_data.metadata_variable', \
                    {'id_variable': id_variable, \
                     'variable_en': variable_en, \
                     'variable_es': variable_es, \
                     'description_en': description_en, \
                     'description_es': description_en, \
                     'info_type': info_type, \
                     'iepg_type': iepg_type, \
                     'code_type': code_type, \
                     'variable_type': variable_type, \
                     'data_type': data_type})

        sql = 'create table iepg_data.'+variable_en+'('+ \
              'id_master_country varchar(10),'+ \
              'date integer,'+ \
              'value float);'
        self.queryCommit(sql)

    def updateMetadata(self, id_variable, variable_en, variable_es, description_en, description_es, \
                       info_type, iepg_type, code_type, variable_type, data_type):
        """Updates dataset metadata."""

        self.update('iepg_data.metadata_variable', \
                    {'id_variable': id_variable, \
                     'variable_en': variable_en, \
                     'variable_es': variable_es, \
                     'description_en': description_en, \
                     'description_es': description_en, \
                     'info_type': info_type, \
                     'iepg_type': iepg_type, \
                     'code_type': code_type, \
                     'variable_type': variable_type, \
                     'data_type': data_type}, \
                    {'id_variable': id_variable})

        sql = 'delete from iepg_data.'+variable_en+';'
        self.queryCommit(sql)

    def setInsertDataSchema(self, schema):
        self.__insertDataSchema = schema

    def clearInsertData(self):
        """Clears the insertion data buffer."""
        self.__insertData = []

    def addToInsertData(self, data):
        """Inserts a dictionary row into the insert buffer."""
        self.__insertData.append(data)

    def flushInsertData(self, table):
        """Makes the inserts."""
        sql = ''

        print(self.__insertData[0])

        for row in self.__insertData:
            print(row)
            sql = 'insert into iepg_data.'+table+'('

            for field in row:
                sql += field+','

            sql = sql.rstrip(',')+') values('

            for a in range(0,len(self.__insertDataSchema)):
                sql += row # +self.__insertDataSchema[a]

        print sql

    



































class ImportIepgData(object):
    """Main module interface."""
    __data = ''
    """Data to be imported."""
    __conn = None
    """Import model."""

    def __init__(self, data):
        """Constructor. Data must be a list with all the lines contained in the CSV file."""
        self.__data = data
        self.__conn = ImportModel()

    def getData(self):
        """Returns data to be imported."""
        return self.__data

    def processData(self):
        """Process data."""

        # Read metadata and register the dataset
        meta = self.__getMetadataDictionary(self.__data[0])

        # Check metadata
        try:
            meta['variable_en']
        except KeyError:
            raise IepgError('-1000', 'Metadata variable_en does not exists.')

        try:
            meta['variable_es']
        except KeyError:
            raise IepgError('-1001', 'Metadata variable_es does not exists.')

        try:
            meta['description_en']
        except KeyError:
            raise IepgError('-1007', 'Metadata description_en does not exists.')

        try:
            meta['description_es']
        except KeyError:
            raise IepgError('-1008', 'Metadata description_es does not exists.')

        try:
            if meta['info_type'] not in ['continuous', 'discrete']:
                raise IepgError('-1009', 'Value: '+meta['info_type']+' invalid for metadata info_type.')
        except KeyError:
            raise IepgError('-1002', 'Metadata info_type does not exists.')

        try:
            if meta['iepg_type'] not in ['raw', 'estimations']:
                raise IepgError('-1010', 'Value: '+meta['iepg_type']+' invalid for metadata iepg_type.')
        except KeyError:
            raise IepgError('-1003', 'Metadata iepg_type does not exists.')

        try:
            if meta['code_type'] not in ['iepg', 'un', 'eu']:
                raise IepgError('-1011', 'Value: '+meta['code_type']+' invalid for metadata code_type.')
        except KeyError:
            raise IepgError('-1004', 'Metadata code_type does not exists.')

        try:
            if meta['variable_type'] not in ['iepg', 'context']:
                raise IepgError('-1012', 'Value: '+meta['variable_type']+' invalid for metadata variable_type.')
        except KeyError:
            raise IepgError('-1005', 'Metadata variable_type does not exists.')

        try:
            if meta['data_type'] not in ['text', 'integer', 'float']:
                raise IepgError('-1013', 'Value: '+meta['data_type']+' invalid for metadata data_type.')
        except KeyError:
            raise IepgError('-1006', 'Metadata data_type does not exists.')

        # Check if the registry already exists
        res = self.__conn.query("select * from iepg_data.metadata_variable "+ \
                                "where id_variable='"+meta['variable_en']+"';")

        if res.row() is None:
            self.__conn.insertMetadata(meta['variable_en'], \
                                       meta['variable_en'], \
                                       meta['variable_es'], \
                                       meta['description_en'], \
                                       meta['description_en'], \
                                       meta['info_type'], \
                                       meta['iepg_type'], \
                                       meta['code_type'], \
                                       meta['variable_type'], \
                                       meta['data_type'])
        else:
            self.__conn.updateMetadata(meta['variable_en'], \
                                       meta['variable_en'], \
                                       meta['variable_es'], \
                                       meta['description_en'], \
                                       meta['description_en'], \
                                       meta['info_type'], \
                                       meta['iepg_type'], \
                                       meta['code_type'], \
                                       meta['variable_type'], \
                                       meta['data_type'])

        # Analyze the data series
        fields = self.__data[1].split(';')
        a = 0

        while a<len(fields):
            if fields[a]!='':
                if fields[a][0]=='a':
                    fields[a] = fields[a][1:]
                a += 1
            else:
                del fields[a]

        data = []

        for a in self.__data[2:]:
            dataRow = dict()
            da = a.split(';')

            for f in range(0, len(fields)):
                dataRow[fields[f]] = da[f]

            data.append(dataRow)

        self.__conn.clearInsertData()

        for a in data:
            for f in range(1, len(fields)):
                d = dict()
                if a[fields[f]]!='###N/A###':
                    d['code'] = a['code']
                    d['date'] = fields[f]

                    if a[fields[f]]=='':
                        d['value'] = 'null'
                    else:
                        d['value'] = a[fields[f]]

                    self.__conn.addToInsertData(d)

        self.__conn.setInsertDataSchema(['varchar(10)', 'integer', 'value'])
        self.__conn.flushInsertData(meta['variable_en'])

    def __getMetadataDictionary(self, meta):
        """Builds a dictionary from separated data."""
        d = dict()
        s = meta.split(';')
        for a in range(0, len(s)-1, 2):
            d[s[a]] = s[a+1]

        return d
