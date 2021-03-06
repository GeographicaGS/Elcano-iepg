BEGIN;

-- Bahrain
INSERT INTO maplex.geometry
  (id_geometry, description, geom)
VALUES (
  178, '[Bahrain] simplified for GeoJSON real-time vector.',
  ST_GeomFromEWKT('SRID=4326;MULTIPOLYGON(((50.5859375 26.24072265625, 50.44773242018982984 26.19329138050045813, 50.46591796875000568 25.96552734374999716, 50.57490234375001137 25.80678710937499432, 50.60722656250001705 25.88310546875000284, 50.60976562500002274 26.12446289062499716, 50.5859375 26.24072265625)))')
);

INSERT INTO maplex.geoentity_geometry
  (id_geoentity,id_geometry_family, id_geometry)
VALUES (
  28,1,178
);

COMMIT;
