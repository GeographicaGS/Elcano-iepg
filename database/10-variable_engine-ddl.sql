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
  date_in date,
  date_out date,
  population integer,
  pib float);

alter table iepg_data.pob_pib
add constraint pob_pib_pkey
primary key(id_master_country, date_in);


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
  id_master_country varchar(10),
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
primary key (id_master_country, date_in);

alter table iepg_data.iepg_final_data
add constraint iepg_final_data_master_country_fkey
foreign key (id_master_country)
references iepg_data.master_country(id_master_country);


create table iepg_data.iepe_final_data(
  id_master_country varchar(10),
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
  iepe float
);

alter table iepg_data.iepe_final_data
add constraint iepe_final_data_pkey
primary key (id_master_country, date_in);

alter table iepg_data.iepe_final_data
add constraint iepe_final_data_master_country_fkey
foreign key (id_master_country)
references iepg_data.master_country(id_master_country);


create table iepg_data.iepg_comment(
  id_master_country varchar(10),
  date_in date,
  date_out date,
  comment text,
  language varchar(2)
);

alter table iepg_data.iepg_comment
add constraint iepg_comment_pkey
primary key (id_master_country, date_in, language);


create table iepg_data.country_geom(
  gid integer,
  iso_3166_1_2_code varchar(2),
  name varchar(500)
);

alter table iepg_data.country_geom
add constraint country_geom_pkey
primary key (gid);

select addgeometrycolumn(
  'iepg_data',
  'country_geom', 
  'geom',
  4326,
  'MULTIPOLYGON',
  2);


-- Views

create view iepg_data.iepg_countries as
select distinct 
  a.id_master_country,
  b.short_name_en1,
  b.short_name_es1
from
  iepg_data.iepg_final_data a inner join
  iepg_data.master_country b on
  a.id_master_country=b.id_master_country
where country
order by id_master_country;


create view iepg_data.iepg_blocks as
select distinct 
  a.id_master_country,
  b.short_name_en1,
  b.short_name_es1
from
  iepg_data.iepg_final_data a inner join
  iepg_data.master_country b on
  a.id_master_country=b.id_master_country
where not country
order by id_master_country;


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

copy iepg_data.iepg_comment
from :'copy_iepg_comment'
with delimiter '|'
csv header quote '"';

copy iepg_data.country_geom
from :'copy_country_geom'
with delimiter '|'
csv header quote '"';

copy iepg_data.iepe_final_data
from :'copy_iepe_final_data'
with delimiter '|'
csv header quote '"';


analyze;

\c :dbname :user :host :port
