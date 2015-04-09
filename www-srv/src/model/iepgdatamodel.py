# coding=UTF8

"""

IEPG data model.

TODO: check all select * and state the fields.
TODO: review SQL parsing. Use bindings.

"""
from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel
from common.errorhandling import DataValidator
import common.helpers


class IepgDataModel(PostgreSQLModel):
    """IEPG data manipulation model."""
    def countries(self, lang, year):
        """Returns the list of geopolitical blocks and its countries for a language and a year, for home page."""
        a = """
        select
          a.id_master_country,
          b.full_name_{} as country_name,
          f.full_name_{} as block_name
        from
          iepg_data.iepg_final_data a 
          inner join iepg_data.master_country b
          on a.id_master_country=b.id_master_country
          inner join iepg_data.country_relation c
          on a.id_master_country=c.id_child
          inner join iepg_data.master_country d
          on c.id_parent=d.id_master_country
          inner join iepg_data.country_relation e
          on d.id_master_country=e.id_child
          inner join iepg_data.master_country f
          on e.id_parent=f.id_master_country
        where
          date_part('year', a.date_in+(365/2))={}
        order by f.full_name_{}, b.full_name_{};""".format(lang,lang,year,lang,lang)

        return(self.query(a).result())

    def years(self):
        """Returns the years of IEPG data stored in the database."""
        a = """
        select distinct date_part('year', (date_in+(365/2)))::varchar as year 
        from iepg_data.iepg_final_data order by year desc;"""

        return(self.query(a).result())

    def countryFilter(self, lang):
        """Returns the list of countries."""
        dv = DataValidator()
        dv.checkLang(lang)
        sql = """
        select distinct
        iso_3166_1_2_code as id,
        short_name_{}1 as name,
        short_name_{}_order
        from
        iepg_data.iepg_final_data a inner join
        iepg_data.master_country b on
        a.id_master_country=b.id_master_country
        where country
        order by short_name_{}_order;""".format(lang, lang, lang)
        return(self.query(sql).result())

    def ranking(self, lang, countryCode, family, variable, year, filter=None, toolFilter=None):
        """Returns the ranking and the value for a variable and a country."""
        dv = DataValidator()
        dv.checkVariable(family, variable)
        dv.checkLang(lang)
        var = common.helpers.getVariableData(family, variable)

        if filter:
            f = "array["
            for fi in filter:
                f=f+"'"+fi+"',"
            f = f.rstrip(",")+"]::varchar[]"

        if toolFilter:
            tf = "array["
            for fi in toolFilter:
                tf=tf+"'"+fi+"',"
            tf = tf.rstrip(",")+"]::varchar[]"

        sql = """
        select
        c.iso_3166_1_2_code as code,
        '{}' as variable,
        b.ranking as ranking,
        a.{} as value,
        %s as year
        from
        {} a inner join
        (
        select
        row_number() over (order by {} desc) as ranking,
        {}
        from (
        select
        {}
        from
        {} a inner join
        iepg_data.master_country b on
        a.id_master_country=b.id_master_country
        where {} is not null and """.format(var["name_"+lang], var["column"], var["table"], var["column"], 
                                            var["column"], var["column"], var["table"], var["column"])

        if filter:
            sql += """
            array[b.iso_3166_1_2_code]::varchar[] <@ {} and
            """.format(f)

        if toolFilter:
            sql += """
            array[b.iso_3166_1_2_code]::varchar[] <@ {} and
            """.format(tf)

        sql += """
        date_part('year', a.date_in)=%s
        ) as f) as b on a.{}=b.{} and date_part('year', a.date_in)=%s inner join
        iepg_data.master_country c on
        a.id_master_country=c.id_master_country
        where c.iso_3166_1_2_code=%s
        order by ranking;
        """.format(var["column"], var["column"])

        return(self.query(sql, bindings=[year, year, year, countryCode]).result())

    def rankingComplete(self, lang, family, variable, year, filter=None, toolFilter=None):
        """Returns the ranking and the value for a variable for all countries."""
        dv = DataValidator()
        dv.checkVariable(family, variable)
        dv.checkLang(lang)
        dv.checkYear(year)
        var = common.helpers.getVariableData(family, variable)

        if filter:
            f = "array["
            for fi in filter:
                f=f+"'"+fi+"',"
            f = f.rstrip(",")+"]::varchar[]"

        if toolFilter:
            tf = "array["
            for fi in toolFilter:
                tf=tf+"'"+fi+"',"
            tf = tf.rstrip(",")+"]::varchar[]"

        sql = """
        select
        c.iso_3166_1_2_code as code,
        '{}' as variable,
        b.ranking as ranking,
        a.{} as value,
        %s as year
        from
        {} a inner join
        (
        select
        row_number() over (order by {} desc) as ranking,
        {}
        from (
        select
        {}
        from
        {} a inner join
        iepg_data.master_country b on
        a.id_master_country=b.id_master_country
        where {} is not null and """.format(var["name_"+lang], var["column"], var["table"], var["column"], 
                                            var["column"], var["column"], var["table"], var["column"])

        if filter:
            sql += """
            array[b.iso_3166_1_2_code]::varchar[] <@ {} and
            """.format(f)

        if toolFilter:
            sql += """
            array[b.iso_3166_1_2_code]::varchar[] <@ {} and
            """.format(tf)

        sql += """
        date_part('year', a.date_in)=%s
        ) as f) as b on a.{}=b.{} and date_part('year', a.date_in)=%s inner join
        iepg_data.master_country c on
        a.id_master_country=c.id_master_country
        order by ranking;
        """.format(var["column"], var["column"])
        return(self.query(sql, bindings=[year, year, year]).result())

    def getIepgComment(self, lang, countryCode, year):
        """Returns the IEPG comment for the given country and year."""
        sql = """
        select
        code,
        date_part('year', date_in) as year,
        comment
        from
        iepg_data_redux.iepg_comment 
        where
        code=%s and date_part('year', date_in)=%s and language=%s;"""
        return(self.query(sql, bindings=[countryCode, year, lang]).result())


    def variableData(self, family, variable, year, filter=None, toolFilter=None):
        """Returns variable data for a year."""
        dv = DataValidator()
        dv.checkVariable(family, variable)
        dv.checkYear(year)
        var = common.helpers.getVariableData(family, variable)

        if filter:
            f = "("
            for fi in filter:
                f=f+"'"+fi+"',"
            f = f.rstrip(",")+")"

        if toolFilter:
            tf = "("
            for fi in toolFilter:
                tf=tf+"'"+fi+"',"
            tf = tf.rstrip(",")+")"

        sql = """
        select
        a.iso_3166_1_2_code as code,
        {} as value
        from
        iepg_data.master_country a inner join
        {} b on
        a.id_master_country=b.id_master_country
        where date_part('YEAR', b.date_in)=%s
        """.format(var["column"], var["table"])

        if toolFilter:
            sql += " and iso_3166_1_2_code in {}".format(tf)

        if filter:
            sql += " and iso_3166_1_2_code in {}".format(f)
                
        sql += ';'
        return(self.query(sql, bindings=[year]).result())


    def getCountriesData(self, countries, year, family, variable):
        """Returns the selected variable for a year and selected countries."""
        dv = DataValidator()
        dv.checkVariable(family, variable)
        var = common.helpers.getVariableData(family, variable)

        f = "("
        for c in countries:
            f += "'"+c+"',"
        f = f.rstrip(",")+")"

        sql = """
        select
        a.iso_3166_1_2_code as code,
        b.{} as value
        from
        iepg_data.master_country a inner join
        {} b on
        a.id_master_country=b.id_master_country
        where
        a.iso_3166_1_2_code in {} and
        date_part('year', b.date_in)=%s;
        """.format(var["column"], var["table"], f)

        return(self.query(sql, bindings=[year]).result())


    def getCountryNameByIso2(self, countryCode, lang):
        """Returns the country name by an ISO2 code."""
        dv = DataValidator()
        dv.checkLang(lang)

        sql = """
        select
        short_name_{}1 as name
        from iepg_data.master_country
        where
        iso_3166_1_2_code=%s;
        """.format(lang)

        return(self.query(sql, bindings=[countryCode]).result())


    def getIepgCountriesIso(self, year):
        """Returns all the ISO codes of IEPG countries."""
        sql = """
        select array_agg(iso_code) as iepg_codes
        from iepg_data.iepg_countries;
        """

        return(self.query(sql).row()["iepg_codes"])

    def getCountryIso2ByName(self,countryName,lang):
        
        sql = "SELECT iso_3166_1_2_code as code from iepg_data_redux.master_country \
                WHERE short_name_{}1=%s".format(lang)

        row = self.query(sql,[countryName.encode('UTF-8')]).row()

        return row["code"] if row else None
