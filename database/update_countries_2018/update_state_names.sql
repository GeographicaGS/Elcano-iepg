

BEGIN;
  UPDATE maplex.name
    SET name = 'Zimbabue', description = '[Zimbabue] short name spanish 1.'
  WHERE id_name = 609;

  UPDATE iepg_data_redux.master_country
    SET full_name_es_order = 'Zimbabue',
        full_name_es = 'Zimbabue',
        short_name_es_order = 'Zimbabue',
        short_name_es1 = 'Zimbabue',
        short_name_es2 = 'Zimbabue'
  WHERE id_master_country = 'un716';

  UPDATE maplex.name
    SET name = 'Botsuana', description = '[Botsuana] short name spanish 1.'
  WHERE id_name = 525;

  UPDATE iepg_data_redux.master_country
    SET full_name_es_order = 'Botsuana',
        full_name_es = 'Botsuana',
        short_name_es_order = 'Botsuana',
        short_name_es1 = 'Botsuana',
        short_name_es2 = 'Botsuana'
  WHERE id_master_country = 'un072';


COMMIT;
