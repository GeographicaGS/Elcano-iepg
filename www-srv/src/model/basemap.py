# coding=UTF8

"""

Base model for map data.

"""
from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel
from common.errorhandling import DataValidator
from common.const import iepg_variables, context_variables


class GeometryData(PostgreSQLModel):
    """Base geometry data."""
    def geometryData(self):
        """Returns the GeoJSON country data coupled with some context data.
        Returns a dictionary."""
        a = """
        select
        a.iso_3166_1_2_code as iso_3166_1_2_code,
        coalesce(b.short_name_en1, a.name) as name_en,
        coalesce(b.short_name_es1, a.name) as name_es,
        st_asgeojson(a.geom) as geojson
        from
        iepg_data.country_geom a left join
        iepg_data.master_country b on
        a.iso_3166_1_2_code=b.iso_3166_1_2_code
        order by iso_3166_1_2_code;
        """

        return(self.query(a).result())
