/*

  Elcano IEPG data redux schema DDL.

*/

\i 00-config.sql
\c :dbname :user :host :port

begin;

create schema iepg_data_redux authorization :user;

 
create table iepg_data_redux.iepe_data(
  code varchar(10),
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

alter table iepg_data_redux.iepe_data
add constraint iepe_data_pkey
primary key (code, date_in);


create table iepg_data_redux.iepe_individual_contribution(
  code varchar(10),
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
  economic_contribution float,
  military_contribution float,
  soft_contribution float
);

alter table iepg_data_redux.iepe_individual_contribution
add constraint iepe_individual_contribution_pkey
primary key (code, date_in);


create table iepg_data_redux.iepe_quota(
  code varchar(10),
  date_in date,
  date_out date,
  global_quota float,
  economic_quota float,
  soft_quota float
);

alter table iepg_data_redux.iepe_quota
add constraint iepe_quota_pkey
primary key (code, date_in);


create table iepg_data_redux.iepe_relative_contribution(
  code varchar(10),
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
  economic_contribution float,
  military_contribution float,
  soft_contribution float
);

alter table iepg_data_redux.iepe_relative_contribution
add constraint iepe_relative_contribution_pkey
primary key (code, date_in);


create table iepg_data_redux.iepg_comment(
  code varchar(10),
  date_in date,
  date_out date,
  comment text,
  language varchar(2)
);

alter table iepg_data_redux.iepg_comment
add constraint iepg_comment_pkey
primary key (code, date_in, language);


create table iepg_data_redux.iepg_data(
  code varchar(10),
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

alter table iepg_data_redux.iepg_data
add constraint iepg_data_pkey
primary key (code, date_in);


create table iepg_data_redux.iepg_individual_contribution(
  code varchar(10),
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
  economic_contribution float,
  military_contribution float,
  soft_contribution float
);

alter table iepg_data_redux.iepg_individual_contribution
add constraint iepg_individual_contribution_pkey
primary key (code, date_in);


create table iepg_data_redux.iepg_quota(
  code varchar(10),
  date_in date,
  date_out date,
  global_quota float,
  economic_quota float,
  military_quota float,
  soft_quota float
);

alter table iepg_data_redux.iepg_quota
add constraint iepg_quota_pkey
primary key (code, date_in);


create table iepg_data_redux.iepg_relative_contribution(
  code varchar(10),
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
  economic_contribution float,
  military_contribution float,
  soft_contribution float
);

alter table iepg_data_redux.iepg_relative_contribution
add constraint iepg_relative_contribution_pkey
primary key (code, date_in);


create table iepg_data_redux.pob_pib(
  code varchar(10),
  date_in date,
  date_out date,
  population integer,
  pib float
);

alter table iepg_data_redux.pob_pib
add constraint pob_pib_pkey
primary key(code, date_in);


-- Import iepg_data_redux

\copy iepg_data_redux.iepe_data from 'redux_iepe_data.csv' with delimiter '|' csv header quote '"'

\copy iepg_data_redux.iepe_individual_contribution from 'redux_iepe_individual_contribution.csv' with delimiter '|' csv header quote '"'

\copy iepg_data_redux.iepe_quota from 'redux_iepe_quota.csv' with delimiter '|' csv header quote '"'

\copy iepg_data_redux.iepe_relative_contribution from 'redux_iepe_relative_contribution.csv' with delimiter '|' csv header quote '"'

\copy iepg_data_redux.iepg_data from 'redux_iepg_data.csv' with delimiter '|' csv header quote '"'

\copy iepg_data_redux.iepg_individual_contribution from 'redux_iepg_individual_contribution.csv' with delimiter '|' csv header quote '"'

\copy iepg_data_redux.iepg_quota from 'redux_iepg_quota.csv' with delimiter '|' csv header quote '"'

\copy iepg_data_redux.iepg_relative_contribution from 'redux_iepg_relative_contribution.csv' with delimiter '|' csv header quote '"'

\copy iepg_data_redux.pob_pib from 'redux_pob_pib.csv' with delimiter '|' csv header quote '"'

\copy iepg_data_redux.iepg_comment from 'redux_iepg_comment.csv' with delimiter '|' csv header quote '"'


commit;
