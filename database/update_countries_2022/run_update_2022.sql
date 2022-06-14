-- --
-- -- TRANSACTION TO UPDATE countries
-- --
BEGIN;
  \ir database/update_countries_2022/south_sudan_updates.sql
  \ir database/update_countries_2022/update_blocks.sql
  \ir database/update_countries_2022/pop_gdp2021.sql
  \ir database/update_countries_2022/update_countrysheets.sql
  \ir database/update_countries_2022/update_translations.sql
COMMIT;
