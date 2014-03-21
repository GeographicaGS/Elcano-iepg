/*

  Drop backend schema.

*/

\i 00-config.sql
\c :dbname :user :host :port

drop schema www cascade;
