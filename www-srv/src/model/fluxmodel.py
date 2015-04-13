# coding=UTF8

"""

Flux model.

"""
from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel


class FluxModel(PostgreSQLModel):
    
    def prepareSchemaIEPGDataRedux(self):
        # Copy current schema. Just for security
        sql = "SELECT clone_schema('iepg_data_redux','iepg_data_redux_'||to_char(now(),'YYYYMMDD_HHMMSS'))";
        self.queryCommit(sql)

        # IEPG
        sql = "DELETE FROM iepg_data_redux.iepg_data"
        self.queryCommit(sql)

        # IEPE
        sql = "DELETE FROM iepg_data_redux.iepe_data"
        self.queryCommit(sql)

        # Quotes
        sql = "DELETE FROM iepg_data_redux.iepg_quota"
        self.queryCommit(sql)

        sql = "DELETE FROM iepg_data_redux.iepe_quota"
        self.queryCommit(sql)

        # Contributions
        sql = "DELETE FROM iepg_data_redux.iepg_relative_contribution"
        self.queryCommit(sql)
        
        sql = "DELETE FROM iepg_data_redux.iepe_relative_contribution"
        self.queryCommit(sql)

    def addDataIEPG(self,datadb):
        # TODO: Improve using copyto
        self.insertBatch("iepg_data_redux.iepg_data",datadb)

    def addDataIEPE(self,datadb):
        # TODO: Improve using copyto
        self.insertBatch("iepg_data_redux.iepe_data",datadb)

    def addDataIEPGQuote(self,datadb):
        # TODO: Improve using copyto
        self.insertBatch("iepg_data_redux.iepg_quota",datadb)

    def addDataIEPEQuote(self,datadb):
        # TODO: Improve using copyto
        self.insertBatch("iepg_data_redux.iepe_quota",datadb)

    def addDataIEPGContribituon(self,datadb):
        # TODO: Improve using copyto
        self.insertBatch("iepg_data_redux.iepg_relative_contribution",datadb)

    def addDataIEPEContribituon(self,datadb):
        # TODO: Improve using copyto
        self.insertBatch("iepg_data_redux.iepe_relative_contribution",datadb)
    




        
