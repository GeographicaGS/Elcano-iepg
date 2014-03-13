/*

  Drops Elcano IEPG data schema.

*/

\i 00-config.sql

\c :dbname :user

\i 99-export_data.sql

drop schema iepg_data cascade;

\c :dbname :superuser

analyze;

\c :dbname :user
