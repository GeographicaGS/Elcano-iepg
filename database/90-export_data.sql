\i 00-config.sql
\c :dbname :superuser :host :port

copy iepg_data.master_country
to :'copy_master_country'
with delimiter ';'
csv header quote '"';

copy iepg_data.country_relation
to :'copy_country_relation'
with delimiter ';'
csv header quote '"';

copy iepg_data.iepg_final_data
to :'copy_iepg_final_data'
with delimiter ';'
csv header quote '"';

copy iepg_data.pob_pib
to :'copy_pob_pib'
with delimiter ';'
csv header quote '"';

copy iepg_data.iepg_comment
to :'copy_iepg_comment'
with delimiter '|'
csv header quote '"';

copy iepg_data.country_geom
to :'copy_country_geom'
with delimiter '|'
csv header quote '"';

copy iepg_data.iepe_final_data
to :'copy_iepe_final_data'
with delimiter '|'
csv header quote '"';

copy iepg_data.iepe_quotas
to :'copy_iepe_quotas'
with delimiter '|'
csv header quote '"';

\copy iepg_data.iepe_individual_contributions to 'iepe_individual_contributions.csv' with delimiter '|' csv header quote '"'

\copy iepg_data.iepe_relative_contributions to 'iepe_relative_contributions.csv' with delimiter '|' csv header quote '"'

\copy iepg_data.iepg_quotas to 'iepg_quotas.csv' with delimiter '|' csv header quote '"'

\copy iepg_data.iepg_individual_contributions to 'iepg_individual_contributions.csv' with delimiter '|' csv header quote '"'

\copy iepg_data.iepg_relative_contributions to 'iepg_relative_contributions.csv' with delimiter '|' csv header quote '"'

\copy iepg_data.iepg_final_data_eu to 'iepg_final_data_eu.csv' with delimiter '|' csv header quote '"'

\copy iepg_data.iepg_individual_contributions_eu to 'iepg_individual_contributions_eu.csv' with delimiter '|' csv header quote '"'

\copy iepg_data.iepg_relative_contributions_eu to 'iepg_relative_contributions_eu.csv' with delimiter '|' csv header quote '"'


\c :dbname :user :host :port
