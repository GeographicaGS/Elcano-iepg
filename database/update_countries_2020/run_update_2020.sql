--
-- TRANSACTION TO UPDATE countries
--
BEGIN;
  \ir database/update_countries_2020/update_northmacedonia_name.sql
  \ir database/update_countries_2020/update_countries_geometries.sql
  \ir database/update_countries_2020/update_blocks.sql
  \ir database/update_countries_2020/pop_gdp.sql
  \ir database/update_countries_2020/update_countrysheets.sql
COMMIT;
