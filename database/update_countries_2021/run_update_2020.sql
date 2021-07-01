-- --
-- -- TRANSACTION TO UPDATE countries
-- --
BEGIN;
  \ir database/update_countries_2021/update_blocks.sql
  \ir database/update_countries_2021/pop_gdp.sql
  \ir database/update_countries_2021/update_countrysheets.sql
  \ir database/update_countries_2021/update_translations.sql
COMMIT;
