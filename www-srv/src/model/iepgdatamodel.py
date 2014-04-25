# coding=UTF8

"""

IEPG data model.

TODO: check all select * and state the fields.
TODO: review SQL parsing. Use bindings.

"""
from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel
from common.errorhandling import DataValidator
from common.const import variables


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
        """Returns the list of countries for country filter."""
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

    def ranking(self, countryCode, variable, year, filter=None):
        """Returns the ranking and the value for a variable and a country."""
        dv = DataValidator()
        dv.checkVariable(variable)
        var = variables[variable]

        if filter:
            f = "array["
            for fi in filter:
                f=f+"'"+fi+"',"
            f = f.rstrip(",")+"]::varchar[]"

            sql = """
            select
            c.iso_3166_1_2_code as code,
            b.ranking as ranking,
            a.{} as value
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
            where
            array[b.iso_3166_1_2_code]::varchar[] <@ {} and
            date_part('year', a.date_in)=%s
            ) as f) as b on a.{}=b.{} and date_part('year', a.date_in)=%s inner join
            iepg_data.master_country c on
            a.id_master_country=c.id_master_country
            where c.iso_3166_1_2_code=%s
            order by ranking;
            """.format(var["column"], var["table"], var["column"], var["column"], var["column"],
                       var["table"], f, var["column"], var["column"])
            return(self.query(sql, bindings=[year, year, countryCode]).result())
        else:
            sql = """
            select
            a.iso_3166_1_2_code as code,
            b.ranking,
            b.{} as value,
            %s as year
            from 
            iepg_data.master_country a inner join (
            select
            b.id_master_country,
            a.ranking,
            a.{}
            from (
            select
            row_number() over (order by {} desc) as ranking,
            {}
            from (
            select distinct
            {}
            from
            {}
            where
            date_part('year', date_in)=%s and {} is not null and 
            id_master_country in(
            select id_master_country
            from iepg_data.iepg_countries)
            ) as f
            ) as a inner join 
            {} b on
            a.{}=b.{} and date_part('year', b.date_in)=%s) b on
            a.id_master_country=b.id_master_country
            where a.iso_3166_1_2_code=%s
            order by b.ranking;
            """.format(var["column"], var["column"], var["column"], var["column"], 
                       var["column"], var["table"], var["column"], var["table"], 
                       var["column"], var["column"])
            return(self.query(sql, bindings=[year, year, year, countryCode]).result())


    def getIepgComment(self, lang, countryCode, year):
        """Returns the IEPG comment for the given country and year."""
        sql = """
        select
        a.iso_3166_1_2_code as code,
        date_part('year', b.date_in) as year,
        b.comment
        from
        iepg_data.master_country a inner join
        iepg_data.iepg_comment b on
        a.id_master_country=b.id_master_country
        where
        a.iso_3166_1_2_code=%s and date_part('year', b.date_in)=%s;"""

        return(self.query(sql, bindings=[countryCode, year]).result())
