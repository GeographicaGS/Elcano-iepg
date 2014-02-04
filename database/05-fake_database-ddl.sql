/*

  version(): PostgreSQL 9.1.2 on x86_64-unknown-linux-gnu, compiled by
  gcc (Ubuntu/Linaro 4.6.3-1ubuntu5) 4.6.3, 64-bit

  postgis_full_version(): POSTGIS="1.5.8" GEOS="3.3.7-CAPI-1.7.7"
  PROJ="Rel. 4.8.0, 6 March 2012" LIBXML="2.7.8" USE_STATS

  Database creation script. (Re)creates the database from the ground
  up, including all its schemas.

*/
\i 00-config.sql

\c postgres :superuser

create role :user with login password :'pass';

create database :dbname owner :user encoding 'UTF8';

\c :dbname :superuser

\i lib/postgis.sql
\i lib/spatial_ref_sys.sql

alter table public.geometry_columns
owner to :user;

alter table public.spatial_ref_sys
owner to :user;

alter view public.geography_columns
owner to :user;

alter schema public owner to :user;

\c :dbname :user

\c :dbname :superuser

analyze;

\c :dbname :user
