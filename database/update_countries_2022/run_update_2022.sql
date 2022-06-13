-- --
-- -- TRANSACTION TO UPDATE countries
-- --
BEGIN;
  \ir database/update_countries_2022/update_blocks.sql
  \ir database/update_countries_2022/pop_gdp.sql
  \ir database/update_countries_2022/update_countrysheets.sql
  \ir database/update_countries_2022/update_translations.sql
COMMIT;
