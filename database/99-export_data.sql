\i 00-config.sql

\c :dbname :superuser

copy iepg_data.master_countries
to :'copy_master_countries'
with delimiter ';'
csv header quote '"';

copy iepg_data.country_relation
to :'copy_country_relation'
with delimiter ';'
csv header quote '"';

\c :dbname :user
