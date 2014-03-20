# coding=UTF8

"""

IEPG data model.

TODO: check all select * and state the fields.
TODO: review SQL parsing. Use bindings.

"""
from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel


class IepgDataModel(PostgreSQLModel):
    """IEPG data manipulation model."""
    def countries(self, lang, year):
        """Returns the list of geopolitical blocks and its countries for a language and a year."""
        a = """
        select
          a.id_country,
          b.full_name_{} as country_name,
          f.full_name_{} as block_name
        from
          iepg_data.iepg_final_data a 
          inner join iepg_data.master_country b
          on a.id_country=b.id_master_country
          inner join iepg_data.country_relation c
          on a.id_country=c.id_child
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
