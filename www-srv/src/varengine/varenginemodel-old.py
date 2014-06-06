# coding=UTF8

"""

Variable engine model.

"""
from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel


class VarEngineModel(PostgreSQLModel):
    """Variable engine model."""
    def createVariableTable(self, variable):
        """Creates a variable table. 
        TODO: stored in a fixed schema."""
        sql = """
        create table varengine.{}(
        code varchar(50),
        date_in timestamp,
        date_out timestamp,
        value {});

        create index on varengine.{} (code);
        create index on varengine.{} (date_in);
        create index on varengine.{} (date_out);
        create index on varengine.{} (value);
        """.format(variable.tableName(), variable.dataType, variable.tableName(), variable.tableName(),
                   variable.tableName(), variable.tableName())
        self.queryCommit(sql)
        return(variable)

    def getVariableYears(self, variable):
        """Returns variable years. TODO: too Elcano oriented. Thread time 
        in a more generic way."""
        sql = """
        select distinct
        date_part('YEAR', date_in) as year
        from varengine.{};
        """.format(variable.tableName())
        return(self.query(sql).result())

    def getVariableCodes(self, variable, year):
        """Returns variable codes between date in and date out (optional). TODO: fixed to year."""
        sql = """
        select distinct code
        from varengine.{}
        """.format(variable.tableName())
        bindings = []
        if year:
            sql += "where date_part('YEAR', date_in)=%s"
            bindings.append(year)
        sql += ";"
        return(self.query(sql, bindings=bindings).result())

    def loadVariablesForDataset(self, dataset):
        """Load variable data for a given dataset."""
        sql = """
        select *
        from varengine.variable
        where id_dataset=%s;
        """
        return(self.query(sql, bindings=[dataset.idDataset]).result())

    def populateFromTable(self, variable, sourceTable, dateInColumn, dateOutColumn, codeColumn,
                          valueColumn):
        """Populates a variable table from another table."""
        sql = """
        insert into varengine.{}
        select
        {},
        {},
        {},
        {}::{}
        from {}
        """.format(variable.tableName(), codeColumn, dateInColumn, dateOutColumn, 
                   valueColumn, variable.dataType, sourceTable)
        self.queryCommit(sql)
        return(variable)

    def getData(self, variable, year, code):
        """Returns variable values for a year.
        TODO: fixed to years"""
        sql = """
        select 
        code,
        date_part('YEAR', date_in) as year,
        value
        from varengine.{}
        """.format(variable.tableName())
        bindings=[]
        if year or code:
            sql += " where "
        if year:
            sql += """
            date_part('YEAR', date_in)=%s
            """
            bindings.append(year)
        if code:
            if year:
                sql += " and "
            sql += """
            code=%s
            """
            bindings.append(code)
        sql += ";"
        return(self.query(sql, bindings=bindings).result())

    def registerVariable(self, variable):
        """Registers variable info into the database."""
        sql = """
        insert into varengine.variable
        values(%s, %s, %s, %s);"""
        self.queryCommit(sql, bindings=[variable.dataset.idDataset, variable.idVariable, 
                                        variable.continuous, variable.dataType])

        return(variable)

    def registerDataset(self, dataset):
        """Creates the database in the database. Receives a dataset object, return dataset object back."""
        sql = """
        insert into varengine.dataset values(%s);
        """
        self.queryCommit(sql, bindings=[dataset.idDataset])
        return(dataset)

        

















        








    # def addVariable(self, nameEn, nameEs, continuous, idFamily, varTable, varColumn, 
    #                 descriptionEn=None, descriptionEs=None):
    #     """Adds a variable."""
    #     values = {
    #         "name_en": nameEn,
    #         "name_es": nameEs,
    #         "continuous": continuous,
    #         "id_family": idFamily,
    #         "var_table": varTable,
    #         "var_column": varColumn
    #     }
    #     if descriptionEn:
    #         values["description_en"] = descriptionEn
    #     if descriptionEs:
    #         values["description_es"] = descriptionEs
    #     a = self.insert("engine.variable",
    #                     values,
    #                     returnID="id_variable")

    #     return(a)

    
    # def addFamily(self, nameEn, nameEs, descriptionEn=None, descriptionEs=None):
    #     """Adds a family."""
    #     values = {
    #         "name_en": nameEn,
    #         "name_es": nameEs
    #     }
    #     if descriptionEn:
    #         values["description_en"] = descriptionEn
    #     if descriptionEs:
    #         values["description_es"] = descriptionEs
    #     a = self.insert("engine.family",
    #                     values,
    #                     returnID="id_family")

    #     return(a)


    # def getVariables(self, family):
    #     """Returns variables."""
    #     sql = """
    #     select *
    #     from engine.variable
    #     """
    #     bindings = []
    #     if family:
    #         sql += " where id_family=%s"
    #         bindings.append(family)
    #     sql += ";"

    #     return(self.query(sql, bindings=bindings).result())


    # def getVariable(self, idFamily, idVariable):
    #     """Returns variable with ID idVariable."""
    #     sql = """
    #     select *
    #     from engine.variable
    #     where id_family=%s and id_variable=%s;
    #     """
    #     return(self.query(sql, bindings=[idFamily, idVariable]).row())


    # def getFamilies(self):
    #     """Returns families."""
    #     sql = """
    #     select *
    #     from engine.family;
    #     """
    #     return(self.query(sql).result())


    # def getIdFamilyByName(self, name):
    #     """Returns the variable family ID by it's english name."""
    #     sql = """
    #     select id_family
    #     from engine.family
    #     where name_en=%s;
    #     """
    #     return(self.query(sql, bindings=[name]).result())





