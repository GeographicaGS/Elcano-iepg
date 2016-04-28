--
--UPDATE South Sudan
--

BEGIN;
INSERT INTO maplex.name
  (id_name, name, description)
VALUES (
  735,'SS','[South Sudan] ISO-3166-1 2 digits.'
);

UPDATE maplex.geoentity_name
  SET id_name_family = 1
  WHERE id_geoentity = 123;

INSERT INTO maplex.geoentity_name
  (id_geoentity,id_name, id_name_family)
VALUES (
  123,735,1
);

UPDATE iepg_data_redux.master_country
  SET iso_3166_1_2_code = 'SS'
  WHERE id_master_country = 'un728';
COMMIT;
