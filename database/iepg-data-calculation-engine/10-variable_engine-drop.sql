/*

  Drops Elcano IEPG data schema.

*/

\i 00-config.sql

\c :dbname :user

drop schema if exists iepg_data cascade;

\c :dbname :superuser

analyze;

\c :dbname :user
