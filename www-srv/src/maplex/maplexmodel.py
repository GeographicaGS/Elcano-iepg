# coding=UTF8

"""

Maplex model.

"""
from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel

class MaplexModel(PostgreSQLModel):
    """Maplex model."""
    def newName(self, name, description):
        """Creates a new name. Returns new name ID."""
        a = self.insert("maplex.name",
                        {"name": name,
                         "description": description},
                        returnID="id_name")

        return(a)


    def getNameFamilies(self):
        """Returns name families."""
        sql = """
        select
        *
        from
        maplex.name_family
        order by
        id_name_family;"""

        return(self.query(sql).result())

    
    def assignGeoentityName(self, idGeoentity, idName, idNameFamily, dateIn=None, dateOut=None):
        """Assign a name to a geoentity."""
        values = {"id_geoentity": idGeoentity,
                  "id_name": idName,
                  "id_name_family": idNameFamily}

        if dateIn:
            values["date_in"] = dateIn
        if dateOut:
            values["date_out"] = dateOut

        a = self.insert("maplex.geoentity_name",
                        values,
                        returnID="id_name")
        return(a)

        
    def getGeoentities(self):
        """Return geoentities."""
        sql = """
        select *
        from maplex.geoentity
        order by id_geoentity;"""
        return(self.query(sql).result())


    def getNames(self):
        """Return names."""
        sql = """
        select *
        from maplex.name
        order by id_name;"""
        return(self.query(sql).result())
