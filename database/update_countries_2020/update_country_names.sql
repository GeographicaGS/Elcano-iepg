-- Update name of North Macedonia: "North Macedonia (until February 2019, Macedonia), officially the Republic of North Macedonia"

BEGIN;
  UPDATE iepg_data_redux.master_country
    SET
      short_name_en_order = 'North Macedonia',
      short_name_es_order = 'Macedonia del Norte',
      short_name_en1 = 'North Macedonia',
      short_name_en2 = 'North Macedonia',
      short_name_es1 = 'Macedonia del Norte',
      short_name_es2 = 'Macedonia del Norte',
      full_name_en_order = 'North Macedonia (Republic of)',
      full_name_es_order = 'Macedonia del Norte (República de)',
      full_name_en = 'Republic of North Macedonia',
      full_name_es = 'República de Macedonia del Norte',
      xlsx_column_name = 'North Macedonia'
   WHERE id_master_country = 'un807'
    AND short_name_en1='Macedonia';

  UPDATE maplex.name
    SET name = 'Macedonia del Norte'
  WHERE id_name=656;

  UPDATE maplex.name
    SET name = 'North Macedonia'
  WHERE id_name=415;
COMMIT;

--update Laos XLSX column name
UPDATE iepg_data_redux.master_country
  SET
    xlsx_column_name = 'Laos'
 WHERE id_master_country = 'un418'
  AND short_name_en1='Laos';

-- Update Bahrein Spanish name
BEGIN;
  UPDATE iepg_data_redux.master_country
    SET
      short_name_es_order = 'Baréin',
      short_name_es1 = 'Baréin',
      short_name_es2 = 'Baréin',
      full_name_es_order = 'Baréin',
      full_name_es = 'Baréin'
   WHERE id_master_country = 'un048'
    AND short_name_en1='Bahrain';

  UPDATE maplex.name
    SET name = 'Baréin'
  WHERE id_name=491;
COMMIT;

-- Update Qatar Spanish name
BEGIN;
  UPDATE iepg_data_redux.master_country
    SET
      short_name_es_order = 'Catar',
      short_name_es1 = 'Catar',
      short_name_es2 = 'Catar',
      full_name_es_order = 'Catar',
      full_name_es = 'Catar'
   WHERE id_master_country = 'un634'
    AND short_name_en1='Qatar';

  UPDATE maplex.name
    SET name = 'Catar'
  WHERE id_name=543;
COMMIT;

-- Update Costa de Marfil order
BEGIN;
  UPDATE iepg_data_redux.master_country
    SET
      short_name_en_order = E'Côte D\'Ivoire',
      short_name_es_order = 'Costa De Marfil'
   WHERE id_master_country = 'un384'
    AND short_name_en1=E'Côte d\'Ivoire';
COMMIT;
