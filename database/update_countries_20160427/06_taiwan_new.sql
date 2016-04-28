--
--NEW COUNTRY: Taiwan
--

BEGIN;
INSERT INTO maplex.geometry
  (id_geometry, description, geom)
VALUES (
  176, '[Taiwan] simplified for GeoJSON real-time vector.',
  ST_Multi('SRID=4326;POLYGON((121.77781782438992764 24.39427358651940025,121.17563235889274154 22.79085724536716739,120.74707970589622619 21.97057139738211262,120.22008344938367941 22.81486094816673926,120.10618859261239777 23.5562627222582357,120.69467980355224768 24.53845083261373716,121.49504438688877883 25.29545888925738595,121.95124393116145711 24.99759593352703746,121.77781782438992764 24.39427358651940025))')
);

INSERT INTO maplex.geoentity
  (id_geoentity, description)
VALUES (
  252, 'Taiwan for Elcano IEPG 2015. Data source: Natural Earth, 2016.'
);

INSERT INTO maplex.geoentity_geometry
  (id_geoentity,id_geometry_family, id_geometry)
VALUES (
  252,1,176
);

INSERT INTO maplex.name
  (id_name, name, description)
VALUES (
  729,'Taiwan','Invented code by Geographica for Taiwan in the context of Elcano IEPG project.'
);
INSERT INTO maplex.name
  (id_name, name, description)
VALUES (
  730,'TW','[Taiwan] ISO-3166-1 2 digits.'
);

INSERT INTO maplex.geoentity_name
  (id_geoentity,id_name, id_name_family)
VALUES (
  252,729,1
);
INSERT INTO maplex.geoentity_name
  (id_geoentity,id_name, id_name_family)
VALUES (
  252,730,1
);

INSERT INTO iepg_data_redux.master_country
  (id_master_country, full_name_es, short_name_es_order,
      short_name_en_order, short_name_es1,short_name_en1,
      iso_3166_1_2_code
  )
VALUES (
  'iepg01','Taiwan','Taiwan','Taiwan','Taiwan','Taiwan','TW'
);
COMMIT;
