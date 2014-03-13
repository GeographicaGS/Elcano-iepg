/*

  Drop backend schema.

*/

\i 00-config.sql

\c :dbname :user

drop schema www cascade;
