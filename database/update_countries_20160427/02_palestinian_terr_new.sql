--
--NEW COUNTRY: Palestinian territories
--

BEGIN;
INSERT INTO maplex.geometry
  (id_geometry, description, geom)
VALUES (
  174, '[Palestinian territories] simplified for GeoJSON real-time vector.',
  ST_Multi('SRID=4326;POLYGON((35.54566531753454228 32.39399201103057635,35.54525190607620289 31.78250478772083909,35.39756066258604505 31.48908600516758227,34.92740848159456846 31.35343537040141371,34.97050662612599581 31.61677846936080982,35.22589155451242959 31.75434113212176612,34.97464074070933293 31.86658234305972215,35.18393029149143558 32.5325106877889425,35.54566531753454228 32.39399201103057635))')
);

INSERT INTO maplex.geoentity
  (id_geoentity, description)
VALUES (
  250, 'Palestinian territories for Elcano IEPG 2015. Data source: Natural Earth, 2016.'
);

INSERT INTO maplex.geoentity_geometry
  (id_geoentity,id_geometry_family, id_geometry)
VALUES (
  250,1,174
);

INSERT INTO maplex.name
  (id_name, name, description)
VALUES (
  727,'Palestinian territories','Invented code by Geographica for Palestinian territories in the context of Elcano IEPG project.'
);
INSERT INTO maplex.name
  (id_name, name, description)
VALUES (
  733,'PS','[Palestinian territories] ISO-3166-1 2 digits.'
);

INSERT INTO maplex.geoentity_name
  (id_geoentity,id_name, id_name_family)
VALUES (
  250,727,1
);
INSERT INTO maplex.geoentity_name
  (id_geoentity,id_name, id_name_family)
VALUES (
  250,733,1
);

UPDATE iepg_data_redux.master_country
  SET iso_3166_1_2_code = 'PS'
  WHERE id_master_country = 'un275';
COMMIT;
