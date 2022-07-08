-- Update: spanish name of Malawi and Rwanda

BEGIN;

  UPDATE iepg_data_redux.master_country
    SET
      short_name_es_order = 'Ruanda',
      short_name_es1 = 'Ruanda',
      short_name_es2 = 'Ruanda',
      full_name_es_order = 'Ruanda',
      full_name_es = 'Ruanda'
   WHERE id_master_country = 'un646'
    AND short_name_en1='Rwanda';
  
  UPDATE maplex.name
    SET name = 'Ruanda'
  WHERE id_name = 698;

  UPDATE iepg_data_redux.master_country
    SET
      short_name_es_order = 'Malaui',
      short_name_es1 = 'Malaui',
      short_name_es2 = 'Malaui',
      full_name_es_order = 'Malaui',
      full_name_es = 'Malaui'
   WHERE id_master_country = 'un454'
    AND short_name_en1='Malawi';

  UPDATE maplex.name
    SET name = 'Malaui'
  WHERE id_name = 566;

COMMIT;