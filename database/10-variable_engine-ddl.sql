/*

  Variable engine.

  TODO: Try to parametrize the schema name :schema, test with \copy too.

*/

\i 00-config.sql
\c :dbname :user :host :port


begin;

create schema engine authorization :user;

create table engine.family(
  id_family varchar(25),
  name_en varchar(250),
  name_es varchar(250),
  description_en text,
  description_es text
);

alter table engine.family
add constraint family_pkey
primary key (id_family);


create table engine.variable(
  id_variable varchar(25),
  name_en varchar(250),
  name_es varchar(250),
  description_en text,
  description_es text,
  continuous boolean,      -- T for continuous variables, F for discrete
  id_family varchar(25),
  var_table varchar(100),
  var_column varchar(100)
);

alter table engine.variable
add constraint variable_pkey
primary key (id_variable, id_family);


-- Foreign keys

alter table engine.variable
add constraint variable_family_fkey
foreign key (id_family) references engine.family(id_family);


-- Data import

\copy engine.family from 'csv/engine_family.csv' with delimiter '|' csv header quote '"'

\copy engine.variable from 'csv/engine_variable.csv' with delimiter '|' csv header quote '"'


commit;
