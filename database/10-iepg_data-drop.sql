/*

  Drops Elcano IEPG data schema.

*/

\i 00-config.sql

\c :dbname :user :host :port

drop schema if exists iepg_data cascade;

\c :dbname :superuser :host :port

analyze;

\c :dbname :user :host :port
