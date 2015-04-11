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
        SELECT st_asgeojson(geom.geom) as geojson,n.name as code,
            mc.full_name_es as name_es,mc.full_name_en as name_en,
            mc.short_name_es1 as name_en_s,
            mc.short_name_en1 as name_es_s
            FROM maplex.geoentity g
            INNER JOIN maplex.geoentity_geometry gg ON gg.id_geoentity=g.id_geoentity
            INNER JOIN maplex.geometry geom ON gg.id_geometry=geom.id_geometry
            INNER JOIN maplex.geoentity_name gn ON gn.id_geoentity = g.id_geoentity
            INNER JOIN maplex.name n ON n.id_name = gn.id_name
            INNER JOIN iepg_data_redux.master_country mc ON mc.iso_3166_1_2_code=n.name

            WHERE gn.id_name_family=1
 
        """

        return self.query(a).result()
