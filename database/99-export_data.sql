\i 00-config.sql

\c :dbname :superuser

copy iepg_data.master_country
to :'copy_master_country'
with delimiter ';'
csv header quote '"';

copy iepg_data.country_relation
to :'copy_country_relation'
with delimiter ';'
csv header quote '"';

copy iepg_data.iepg_final_data
to :'copy_iepg_final_data'
with delimiter ';'
csv header quote '"';

\c :dbname :user
