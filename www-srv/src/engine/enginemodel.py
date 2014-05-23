# coding=UTF8

"""

Variable engine model.

"""
from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel


class EngineModel(PostgreSQLModel):
    """Variable engine model."""
    def addVariable(self, nameEn, nameEs, continuous, idFamily, varTable, varColumn, 
                    descriptionEn=None, descriptionEs=None):
        """Adds a variable."""
        values = {
            "name_en": nameEn,
            "name_es": nameEs,
            "continuous": continuous,
            "id_family": idFamily,
            "var_table": varTable,
            "var_column": varColumn
        }
        if descriptionEn:
            values["description_en"] = descriptionEn
        if descriptionEs:
            values["description_es"] = descriptionEs
        a = self.insert("engine.variable",
                        values,
                        returnID="id_variable")

        return(a)

    
    def addFamily(self, nameEn, nameEs, descriptionEn=None, descriptionEs=None):
        """Adds a family."""
        values = {
            "name_en": nameEn,
            "name_es": nameEs
        }
        if descriptionEn:
            values["description_en"] = descriptionEn
        if descriptionEs:
            values["description_es"] = descriptionEs
        a = self.insert("engine.family",
                        values,
                        returnID="id_family")

        return(a)


    def getVariables(self):
        """Returns variables."""
        sql = """
        select *
        from engine.variable;
        """
        return(self.query(sql).result())


    def getVariable(self, idVariable):
        """Returns variable with ID idVariable."""
        sql = """
        select *
        from engine.variable
        where id_variable=%s;
        """
        return(self.query(sql, bindings=[idVariable]).row())


    def getFamilies(self):
        """Returns families."""
        sql = """
        select *
        from engine.family;
        """
        return(self.query(sql).result())


    def getVariableCodes(self, table, year):
        """Returns variable codes between date in and date out (optional). TODO: fixed to year."""
        sql = """
        select distinct code
        from {}
        """.format(table)

        bindings = []
        if year:
            sql += "where date_part('YEAR', date_in)=%s"
            bindings.append(year)

        sql += ";"
        return(self.query(sql, bindings=bindings).result())


    def getVariableYears(self, table):
        """Returns variable years."""
        sql = """
        select distinct
        date_part('YEAR', date_in) as year
        from {};
        """.format(table)
        return(self.query(sql).result())
