/*

  Drop iepg_data_redux schema.

*/

\i 00-config.sql
\c :dbname :user :host :port

drop schema iepg_data_redux cascade;
