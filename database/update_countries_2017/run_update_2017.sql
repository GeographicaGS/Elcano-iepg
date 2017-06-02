--
-- TRANSACTION TO UPDATE countries - 30/05/2017
--
BEGIN;
\i database/update_countries_2017/update_blocks.sql
\i database/update_countries_2017/update_congord_name.sql
\i database/update_countries_2017/update_countrysheets.sql
\i database/update_countries_2017/update_www_translation.sql
COMMIT;