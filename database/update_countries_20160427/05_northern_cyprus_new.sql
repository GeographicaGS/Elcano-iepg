--
--NEW COUNTRY: Northern Cyprus
--

BEGIN;
INSERT INTO maplex.geometry
  (id_geometry, description, geom)
VALUES (
  175, '[Northern Cyprus] simplified for GeoJSON real-time vector.',
  ST_Multi('SRID=4326;POLYGON((32.73178022637745244 35.14002594658843748,32.8024735857527503 35.14550364841137764,32.94696089044080622 35.3867033961336972,33.66722700372494614 35.37321584730551649,34.57647382990046481 35.67159556735879278,33.90080447768420413 35.24575592705761551,33.97361657078346298 35.05850637464800457,33.86643965021011127 35.09359467217419137,33.67539188002706396 35.01786286065045317,33.52568525567750157 35.0386884628640729,33.47581749851585187 35.00034455010350598,33.45592207208346736 35.10142365166640843,33.38383344903630245 35.16271190036457028,33.19097700372304871 35.17312470147138015,32.91957238132613384 35.08783274997364288,32.73178022637745244 35.14002594658843748))')
);

INSERT INTO maplex.geoentity
  (id_geoentity, description)
VALUES (
  251, 'Northern Cyprus for Elcano IEPG 2015. Data source: Natural Earth, 2016.'
);

INSERT INTO maplex.geoentity_geometry
  (id_geoentity,id_geometry_family, id_geometry)
VALUES (
  251,1,175
);

INSERT INTO maplex.name
  (id_name, name, description)
VALUES (
  728,'Northern Cyprus','Invented code by Geographica for Northern Cyprus in the context of Elcano IEPG project.'
);
INSERT INTO maplex.name
  (id_name, name, description)
VALUES (
  732,'g1','[Northern Cyprus] ISO-3166-1 2 digits (Invented code by Geographica in the context of Elcano IEPG project)'
);

INSERT INTO maplex.geoentity_name
  (id_geoentity,id_name, id_name_family)
VALUES (
  251,728,1
);
INSERT INTO maplex.geoentity_name
  (id_geoentity,id_name, id_name_family)
VALUES (
  251,732,1
);

INSERT INTO iepg_data_redux.master_country
  (id_master_country, full_name_es, short_name_es_order,
      short_name_en_order, short_name_es1,short_name_en1,
      iso_3166_1_2_code
  )
VALUES (
  'iepg03','República Turca del Norte de Chipre','R.T. Norte de Chipre','N. Cyprus','R.T. Norte de Chipre','Northern Cyprus','g1'
);
COMMIT;
