\i 00-config.sql
\c postgres :superuser
create role :user with login password :'pass';
create database :dbname owner :user;
\c :dbname :superuser
\i :postgis
\i :spatial_ref_sys
alter table spatial_ref_sys owner to :user;
alter table geometry_columns owner to :user;
\c :dbname :user
