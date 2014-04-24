/*

  Elcano IEPG data schema DDL.

*/

\i 00-config.sql
\c :dbname :user :host :port

create schema iepg_data authorization :user;

create table iepg_data.master_country(
  id_master_country varchar(10),
  cod_unstats_num char(3),
  cod_unstats_alpha char(3),
  cod_eurostat char(2),
  full_name_en_order varchar(500),
  full_name_es_order varchar(500),
  full_name_en varchar(500),
  full_name_es varchar(500),
  short_name_en_order varchar(500),
  short_name_es_order varchar(500),
  short_name_en1 varchar(500),
  short_name_en2 varchar(500),
  short_name_es1 varchar(500),
  short_name_es2 varchar(500),
  capital varchar(500),
  iso_4217_currency_code varchar(3),
  iso_4217_currency_name varchar(25),
  itu_t_telephone_code varchar(50),
  iso_3166_1_2_code varchar(2),
  iso_3166_1_3_code varchar(3),
  iso_3166_1_number varchar(5),
  iana_country_code_tld varchar(25),
  date_in date,
  date_out date,
  country boolean
);

select addgeometrycolumn(
  'iepg_data',
  'master_country',
  'geom',
  4326,
  'MULTIPOLYGON',
  2);

alter table iepg_data.master_country
add constraint master_country_pkey
primary key(id_master_country);

alter table iepg_data.master_country
add constraint master_country_unique_cod_unstats_num
unique(cod_unstats_num);

alter table iepg_data.master_country
add constraint master_country_unique_cod_unstats_alpha
unique(cod_unstats_alpha);

alter table iepg_data.master_country
add constraint master_country_unique_cod_eurostat
unique(cod_eurostat);


create table iepg_data.country_relation(
  id_child varchar(10),
  id_parent varchar(10)
);

alter table iepg_data.country_relation
add constraint country_relation_pkey
primary key(id_child, id_parent);

alter table iepg_data.country_relation
add constraint country_relation_master_country_child_fkey
foreign key (id_child)
references iepg_data.master_country(id_master_country);

alter table iepg_data.country_relation
add constraint country_relation_master_country_parent_fkey
foreign key (id_parent)
references iepg_data.master_country(id_master_country);


create table iepg_data.pob_pib(
  id_master_country character varying(10),
  pob_1990 float,
  pib_1990 float, 
  pob_1995 float, 
  pib_1995 float, 
  pob_2000 float, 
  pib_2000 float, 
  pob_2005 float, 
  pib_2005 float, 
  pob_2010 float, 
  pib_2010 float, 
  pob_2011 float, 
  pib_2011 float, 
  pob_2012 float, 
  pib_2012 float, 
  pob_2013 float,
  pib_2013 float);

alter table iepg_data.pob_pib
add constraint pob_pib_pkey
primary key(id_master_country);


-- Variable metadata

create table iepg_data.metadata_variable(
  id_variable varchar(250),         -- Same as name_en
  variable_en varchar(250),
  variable_es varchar(250),
  description_en text,
  description_es text,
  info_type varchar(20),                 -- T for discrete variables, F for continuous
  iepg_type varchar(20),
  code_type varchar(20),
  variable_type varchar(20),
  data_type varchar(20)
);

alter table iepg_data.metadata_variable
add constraint metadata_variable_pkey
primary key (id_variable);


create table iepg_data.iepg_final_data(
  id_country varchar(10),
  date_in date,
  date_out date,
  energy float,
  primary_goods float,
  manufactures float,
  services float,
  investments float,
  troops float,
  military_equipment float,
  migrations float,
  tourism float,
  sports float,
  culture float,
  information float,
  technology float,
  science float,
  education float,
  cooperation float,
  economic_presence float,
  military_presence float,
  soft_presence float,
  iepg float
);

alter table iepg_data.iepg_final_data
add constraint iepg_final_data_pkey
primary key (id_country, date_in);

alter table iepg_data.iepg_final_data
add constraint iepg_final_data_master_country_fkey
foreign key (id_country)
references iepg_data.master_country(id_master_country);


-- Copy data

\c :dbname :superuser :host :port

copy iepg_data.master_country
from :'copy_master_country'
with delimiter ';'
csv header quote '"';

copy iepg_data.country_relation
from :'copy_country_relation'
with delimiter ';'
csv header quote '"';

copy iepg_data.iepg_final_data
from :'copy_iepg_final_data'
with delimiter ';'
csv header quote '"';

copy iepg_data.pob_pib
from :'copy_pob_pib'
with delimiter ';'
csv header quote '"';

analyze;

\c :dbname :user :host :port
