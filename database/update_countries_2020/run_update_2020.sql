--
-- TRANSACTION TO UPDATE countries
--
BEGIN;
  \ir database/update_countries_2020/update_country_names.sql
  \ir database/update_countries_2020/update_countries_geometries.sql
  \ir database/update_countries_2020/update_blocks.sql
  \ir database/update_countries_2020/pop_gdp.sql
  \ir database/update_countries_2020/update_countrysheets.sql
  \ir database/update_countries_2020/update_countrysheets_2.sql
  \ir database/update_countries_2020/update_translations.sql
  \ir database/update_countries_2020/update_translations_2.sql
COMMIT;
