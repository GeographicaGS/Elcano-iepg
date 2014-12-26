\i 00-config.sql
\c postgres :superuser :host :port

drop database :dbname;
drop role :user;
