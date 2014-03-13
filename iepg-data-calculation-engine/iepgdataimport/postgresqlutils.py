# coding=UTF8

"""
This class extends the PostgreSQLModel to implement utilities to deal
with a PostgreSQL database.
"""

from model.base.PostgreSQL.PostgreSQLModel import PostgreSQLModel

class PostgreSqlUtils(PostgreSQLModel):
    """Database utilities for PostgreSQL to use with Flask."""
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
