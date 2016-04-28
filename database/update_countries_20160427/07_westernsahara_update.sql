--
--UPDATE Western Sahara
--

BEGIN;
INSERT INTO maplex.name
  (id_name, name, description)
VALUES (
  734,'EH','[Western Sahara] ISO-3166-1 2 digits.'
);

UPDATE maplex.geoentity_name
  SET id_name_family = 1
  WHERE id_geoentity = 29;

INSERT INTO maplex.geoentity_name
  (id_geoentity,id_name, id_name_family)
VALUES (
  29,734,1
);

UPDATE iepg_data_redux.master_country
  SET iso_3166_1_2_code = 'EH'
  WHERE id_master_country = 'un732';
COMMIT;
