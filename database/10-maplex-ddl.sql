/*

  Maplex time carto schema DDL.

*/

\i 00-config.sql
\c :dbname :user :host :port

begin;

create schema maplex authorization :user;

create table maplex.geoentity(
  id_geoentity serial,
  description text,
  date_in timestamp,
  date_out timestamp
);

alter table maplex.geoentity
add constraint geoentity_pkey
primary key(id_geoentity);


create table maplex.geometry(
  id_geometry serial,
  description text
);

select addgeometrycolumn(
  'maplex',
  'geometry',
  'geom',
  4326,
  'MULTIPOLYGON',
  2);

alter table maplex.geometry
add constraint geometry_pkey
primary key(id_geometry);

create index geometry_geom_gist
on maplex.geometry
using gist(geom);


create table maplex.geometry_family(
  id_geometry_family serial,
  name varchar(100),
  description text
);

alter table maplex.geometry_family
add constraint geometry_family_pkey
primary key(id_geometry_family);


create table maplex.geoentity_geometry(
  id_geoentity integer,
  id_geometry_family integer,
  id_geometry integer
);

alter table maplex.geoentity_geometry
add constraint geoentity_geometry_pkey
primary key(id_geoentity, id_geometry_family, id_geometry);


create table maplex.name(
  id_name serial,
  name varchar(500),
  description text
);

alter table maplex.name
add constraint name_pkey
primary key(id_name);


create table maplex.name_family(
  id_name_family serial,
  name varchar(100),
  description text
);

alter table maplex.name_family
add constraint name_family_pkey
primary key(id_name_family);


create table maplex.geoentity_name(
  id_geoentity integer,
  id_name integer,
  id_name_family integer
);

alter table maplex.geoentity_name
add constraint geoentity_name_pkey
primary key(id_geoentity, id_name, id_name_family);


create table maplex.block(
  id_geoentity_block integer,
  id_geoentity_child integer
);

alter table maplex.block
add constraint block_pkey
primary key(id_geoentity_block, id_geoentity_child);


create table maplex.timeline(
  id_timeline integer,
  name varchar(500),
  description text
);

alter table maplex.timeline
add constraint timeline_pkey
primary key(id_timeline);


create table maplex.geoentity_timeline(
  id_geoentity integer,
  id_timeline integer
);

alter table maplex.geoentity_timeline
add constraint geoentity_timeline_pkey
primary key(id_geoentity, id_timeline);


-- Foreign keys

alter table maplex.geoentity_name
add constraint geoentity_name_geoentity_fkey
foreign key (id_geoentity) references maplex.geoentity(id_geoentity);

alter table maplex.geoentity_name
add constraint geoentity_name_name_fkey
foreign key (id_name) references maplex.name(id_name);

alter table maplex.geoentity_name
add constraint geoentity_name_name_family_fkey
foreign key (id_name_family) references maplex.name_family(id_name_family);

alter table maplex.block
add constraint block_geoentity_parent_fkey
foreign key (id_geoentity_block) references maplex.geoentity(id_geoentity);

alter table maplex.block
add constraint block_geoentity_child_fkey
foreign key (id_geoentity_child) references maplex.geoentity(id_geoentity);

alter table maplex.geoentity_timeline
add constraint geoentity_timeline_geoentity_fkey
foreign key (id_geoentity) references maplex.geoentity(id_geoentity);

alter table maplex.geoentity_timeline
add constraint geoentity_timeline_timeline_fkey
foreign key (id_timeline) references maplex.timeline(id_timeline);

alter table maplex.geoentity_geometry
add constraint geoentity_geometry_geoentity_fkey
foreign key (id_geoentity) references maplex.geoentity(id_geoentity);

alter table maplex.geoentity_geometry
add constraint geoentity_geometry_geometry_fkey
foreign key (id_geometry) references maplex.geometry(id_geometry);

alter table maplex.geoentity_geometry
add constraint geoentity_geometry_geometry_family_fkey
foreign key (id_geometry_family) references maplex.geometry_family(id_geometry_family);


commit;
