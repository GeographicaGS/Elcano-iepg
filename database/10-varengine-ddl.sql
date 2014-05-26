/*

  Variable engine.

*/

\i 00-config.sql
\c :dbname :user :host :port


begin;


create schema varengine authorization :user;

create table varengine.dataset(
  id_dataset varchar(25)
);

alter table varengine.dataset
add constraint family_pkey
primary key (id_dataset);


create table varengine.variable(
  id_dataset varchar(25),
  id_variable varchar(25),
  continuous boolean,      -- T for continuous variables, F for discrete
    dataType varchar(25)
);

alter table varengine.variable
add constraint variable_pkey
primary key (id_variable, id_dataset);


-- Foreign keys

alter table varengine.variable
add constraint variable_dataset_fkey
foreign key (id_dataset) references varengine.dataset(id_dataset);


commit;
