# coding=UTF8

"""

Maplex model.

TODO: create functions that returns the database information in dictionaries but keyed with a name family.

"""
from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel
# import common.timelapse

class MaplexModel(PostgreSQLModel):
    """Maplex model."""
    def newName(self, name, description):
        """Creates a new name. Returns new name ID."""
        a = self.insert("maplex.name",
                        {"name": name,
                         "description": description},
                        returnID="id_name")

        return(a)


    def getGeoentityBlocks(self, idGeoentity, year):
        """Returns blocks idGeoentity is in for the given year."""
        bindings = [idGeoentity]
        sql = """
        select *
        from maplex.vw__blocks_membership
        where id_geoentity_child=%s
        """

        if year: 
            sql += " and (date_part('YEAR', date_in_membership)<=%s or date_in_membership is null)"
            bindings.append(year)

        return(self.query(sql, bindings=bindings).result())


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


    def getNames(self, idNameFamily=None):
        """Return names. Check if time is involved. If not, add it."""
        sql = """
        select *
        from maplex.vw__names"""

        bindings = []
        if idNameFamily:
            sql += " where id_name_family=%s"
            bindings = [idNameFamily]

        sql += ';'
        return(self.query(sql, bindings=bindings).result())


    def getName(self, idName):
        """Return name with ID idName."""
        sql = """
        select *
        from maplex.name
        where id_name = %s
        order by id_name;"""
        return(self.query(sql, bindings=[idName]).result())

    
    def getGeoentityNames(self, idGeoentity, idNameFamily):
        """Returns the names for idGeoentity and idNameFamily."""
        sql = """
        select array_agg(name) as names
        from maplex.vw__names
        where id_geoentity=%s and id_name_family=%s;"""

        return(self.query(sql,bindings=[idGeoentity, idNameFamily]).result())


    def getBlocks(self, timeLapseBlock=None, timeLapseMembers=None):
        """Retrieves list of blocks, given a time lapse (either given by the block
        timeline itself or that of its members membership."""
        sql = """
        select *
        from maplex.vw__blocks
        """
        bindings=[]
        filter = ""
        if timeLapseBlock:
            a = timeLapseBlock.getSqlFilter(["date_in_block", "date_out_block"])
            filter = " where "+a["sql"]
            bindings.extend(a["bindings"])
        if timeLapseMembers:
            a = timeLapseMembers.getSqlFilter(["date_members_first_entry", "date_members_last_exit"])
            filter = " where " if filter=="" else filter+" and "
            filter += a["sql"]
            bindings.extend(a["bindings"])

        sql = sql+filter+";" if filter<>"" else sql+";"
        return(self.query(sql, bindings=bindings).result())


    def getBlockMembers(self, idGeoentityBlock, year):
        """Retrieves block members. TODO: go beyond year."""
        bindings=[idGeoentityBlock]
        sql = """
        select *
        from
        maplex.vw__blocks_membership
        where id_geoentity_block = %s"""

        if year:
            sql += " and (date_part('YEAR', date_in_membership)<=%s or date_in_membership is null)"
            bindings.append(year)

        sql += ";"

        return(self.query(sql, bindings=bindings).result())


    def getIdGeoentityByName(self, name, idNameFamily):
        """Retrieves ID geoentity of name and ID name family."""
        sql="""
        select id_geoentity
        from maplex.vw__geoentity_names
        where name=%s and id_name_family=%s;
        """
        return(self.query(sql, bindings=[name, idNameFamily]).result())
