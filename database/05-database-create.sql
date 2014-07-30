\i 00-config.sql
\c postgres :superuser :host :port

create role :user with login password :'pass';

create database :dbname owner :user;

\c :dbname :superuser :host :port
\i :postgis
\i :spatial_ref_sys
\i :array

alter schema public owner to :user;
alter table spatial_ref_sys owner to :user;
alter table geometry_columns owner to :user;
alter table geography_columns owner to :user;

\c :dbname :user :host :port
