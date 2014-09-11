# coding=UTF8

"""

Base model for map data.

"""
from base.PostgreSQL.PostgreSQLModel import PostgreSQLModel
from common.errorhandling import DataValidator
from common.const import variables


class GeometryData(PostgreSQLModel):
    """Base geometry data."""
    def geometryData(self):
        """Returns the GeoJSON country data coupled with some context data.
        Returns a dictionary."""
        a = """
        select
        iso_3166_1_2_code as iso_3166_1_2_code,
        english_long as name_en,
        spanish_long as name_es,
        english_short as name_en_s,
        spanish_short as name_es_s,
        geojson
        from
        maplex.vw__iepg_country_data
        order by iso_3166_1_2_code;
        """

        return(self.query(a).result())
