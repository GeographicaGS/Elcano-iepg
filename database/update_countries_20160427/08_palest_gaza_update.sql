--
--SOMALIA POLYGON UPDATE (ADDED SOMALILAND REGION TO COUNTRY)
--
UPDATE maplex.geometry
SET geom = ST_Multi(
  ST_Union(
    (SELECT geom FROM maplex.geometry WHERE id_geometry=174),
    ST_GeomFromEWKT('SRID=4326;POLYGON((34.48810713068135669 31.60553884533732116,34.5563716977389106 31.54882396089699625,34.26544000000000523 31.21935999999999822,34.48810713068135669 31.60553884533732116))')))
WHERE id_geometry=174;
