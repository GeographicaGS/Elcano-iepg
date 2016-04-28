--
-- TRANSACTION TO UPDATE countries - 27/04/2016
--
BEGIN;
\i database/update_countries_20160427/01_kosovo_new.sql
\i database/update_countries_20160427/02_palestinian_terr_new.sql
\i database/update_countries_20160427/03_somalia_update.sql
\i database/update_countries_20160427/04_southsudan_update.sql
\i database/update_countries_20160427/05_northern_cyprus_new.sql
\i database/update_countries_20160427/06_taiwan_new.sql
\i database/update_countries_20160427/07_westernsahara_update.sql
\i database/update_countries_20160427/08_palest_gaza_update.sql
COMMIT;
