/*

  Elcano IEPG data schema DDL.

*/

\i 00-config.sql

begin;

\c :dbname :user

create schema iepg_data authorization :user;

create table iepg_data.master_countries(
  id varchar(10),
  cod_unstats_num char(3),
  cod_unstats_alpha char(3),
  cod_eurostat char(2),  
  name_en varchar(500),
  name_es varchar(500),
  country boolean
);

alter table iepg_data.master_countries
add constraint master_countries_pkey
primary key(id);

alter table iepg_data.master_countries
add constraint master_countries_unique_cod_unstats_num
unique(cod_unstats_num);

alter table iepg_data.master_countries
add constraint master_countries_unique_cod_unstats_alpha
unique(cod_unstats_alpha);

alter table iepg_data.master_countries
add constraint master_countries_unique_cod_eurostat
unique(cod_eurostat);

alter table iepg_data.master_countries
add constraint master_countries_unique_name_en
unique(name_en);

alter table iepg_data.master_countries
add constraint master_countries_unique_name_es
unique(name_es);


create table iepg_data.country_relation(
  id_child varchar(10),
  id_parent varchar(10)
);

alter table iepg_data.country_relation
add constraint country_relation_pkey
primary key(id_child, id_parent);

alter table iepg_data.country_relation
add constraint country_relation_master_countries_child_fkey
foreign key (id_child)
references iepg_data.master_countries(id);

alter table iepg_data.country_relation
add constraint country_relation_master_countries_parent_fkey
foreign key (id_parent)
references iepg_data.master_countries(id);


-- Copy country data

\c :dbname :superuser

copy iepg_data.master_countries
from :'copy_master_countries'
with delimiter ';'
csv header quote '"';

copy iepg_data.country_relation
from :'copy_country_relation'
with delimiter ';'
csv header quote '"';

\c :dbname :user


create table iepg_data.metadata_variable(
  id_variable char(32),
  name_en varchar(250),
  name_es varchar(250),
  description_en text,
  description_es text,
  discrete boolean,  
  code_type varchar(25),
  data_type varchar(25)
);

alter table iepg_data.metadata_variable
add constraint metadata_variable_pkey
primary key (id_variable);
  

commit;

analyze;
