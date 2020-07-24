# coding=UTF8

"""

Maplex model.

TODO: create functions that returns the database information in dictionaries but keyed with a name family.

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

    def getTranslationTable(self, idNameFamilyA, idNameFamilyB):
        """Returns the translation table from idNameFamilyA to B."""
        if idNameFamilyB:
            sql = """
            with name_a as(
            select
            a.id_geoentity,
            b.name
            from
            maplex.geoentity_name a inner join
            maplex.name b on
            a.id_name=b.id_name
            where id_name_family=%s),
            name_b as(
            select
            a.id_geoentity,
            b.name
            from
            maplex.geoentity_name a inner join
            maplex.name b on
            a.id_name=b.id_name
            where id_name_family=%s)
            select
            a.name as name_a,
            b.name as name_b
            from
            name_a a full outer join
            name_b b on
            a.id_geoentity=b.id_geoentity;
            """
            return(self.query(sql, bindings=[idNameFamilyA, idNameFamilyB]).result())
        else:
            sql = """
            select
            b.name as name_a,
            a.id_geoentity as name_b
            from
            maplex.geoentity_name a inner join
            maplex.name b on a.id_name=b.id_name
            where id_name_family=%s;
            """
            return(self.query(sql, bindings=[idNameFamilyA]).result())

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

    def getBlocks(self, timeLapseBlock, timeLapseMembers, idNameFamily):
        """Retrieves list of blocks, given a time lapse (either given by the block
        timeline itself or that of its members membership."""
        if idNameFamily:
            sql = """
            select
            c.name as id_geoentity_block,
            a.date_members_first_entry as date_members_first_entry,
            a.date_members_last_exit as date_members_last_exit,
            a.description_block as description_block,
            a.date_in_block as date_in_block,
            a.date_out_block as date_out_block
            from
            maplex.vw__blocks a left join
            maplex.geoentity_name b on
            a.id_geoentity_block=b.id_geoentity left join
            maplex.name c on
            b.id_name=c.id_name
            """
            filter = " where id_name_family=%s "
            bindings = [idNameFamily]
        else:
            sql = """
            select
            a.id_geoentity_block as id_geoentity_block,
            a.date_members_first_entry as date_members_first_entry,
            a.date_members_last_exit as date_members_last_exit,
            a.description_block as description_block,
            a.date_in_block as date_in_block,
            a.date_out_block as date_out_block
            from
            maplex.vw__blocks a
            """
            filter = ""
            bindings=[]

        if timeLapseBlock:
            a = timeLapseBlock.getSqlFilter(["date_in_block", "date_out_block"])
            filter = " where " if filter=="" else filter+" and "
            filter += a["sql"]
            bindings.extend(a["bindings"])
        if timeLapseMembers:
            a = timeLapseMembers.getSqlFilter(["date_members_first_entry", "date_members_last_exit"])
            filter = " where " if filter=="" else filter+" and "
            filter += a["sql"]
            bindings.extend(a["bindings"])

        sql = sql+filter+";" if filter<>"" else sql+";"
        return(self.query(sql, bindings=bindings).result())

    def getBlockMembers(self, idGeoentityBlock, year, idNameFamily):
        """Retrieves block members. TODO: go beyond year. TODO: all members should be multiname."""
        if idNameFamily:
            bindings=[idNameFamily, idNameFamily, idGeoentityBlock]
            sql = """
            select
            c.name as id_geoentity_block,
            a.description_block as description_block,
            a.date_in_block as date_in_block,
            a.date_out_block as date_out_block,
            a.date_in_membership as date_in_membership,
            a.date_out_membership as date_out_membership,
            e.name as id_geoentity_child,
            a.description_child as description_child,
            a.date_in_child as date_in_child,
            a.date_out_child as date_out_child
            from
            maplex.vw__blocks_membership a left join
            maplex.geoentity_name b on
            a.id_geoentity_block=b.id_geoentity left join
            maplex.name c on
            b.id_name=c.id_name left join
            maplex.geoentity_name d on
            a.id_geoentity_child=d.id_geoentity left join
            maplex.name e on
            d.id_name = e.id_name
            where
            b.id_name_family=%s and d.id_name_family=%s and c.name=%s
            """
        else:
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


    def idGeoentitiesBlocks(self, idGeoentity):
        """Returns an array with idGeoentities that are blocks."""
        sql = """
        select
        array_agg(id_geoentity_block) as id_geoentity_blocks
        from
        maplex.vw__blocks;
        """
        return(self.query(sql).row()["id_geoentity_blocks"])
