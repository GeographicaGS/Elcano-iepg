
/*
  Update short name of Democratic Republic of the Congo:
    - ES / EN: “El Congo”/“The Congo” --> “Congo, RD”/“Congo, DR”.
*/
BEGIN;
  UPDATE iepg_data_redux.master_country
    SET 
      short_name_en_order = 'Congo (DR)', 
      short_name_es_order = 'Congo (RD)', 
      short_name_en1 = 'Congo DR', 
      short_name_en2 = 'Congo DR', 
      short_name_es1 = 'Congo RD', 
      short_name_es2 = 'Congo RD' 
   WHERE id_master_country = 'un180' 
    AND short_name_en1='The Congo';

  UPDATE maplex.name
    SET name = 'Congo RD'
  WHERE id_name=654;

  UPDATE maplex.name
    SET name = 'Congo DR'
  WHERE id_name=413;
COMMIT;