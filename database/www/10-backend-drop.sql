/*

  Drop backend schema.

*/

\i config.sql

\c :dbname :user

drop schema www cascade;
