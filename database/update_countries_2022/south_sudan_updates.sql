
-- Update South Sudan id_name_family and xlsx_column_name

BEGIN;

    UPDATE maplex.geoentity_name
        SET id_name_family = 2
    WHERE id_geoentity = 123 AND id_name = 345;

    UPDATE maplex.geoentity_name
        SET id_name_family = 3
    WHERE id_geoentity = 123 AND id_name = 586;


    UPDATE iepg_data_redux.master_country
        SET xlsx_column_name='Sudan (South)'
    WHERE id_master_country ='un728';

COMMIT;