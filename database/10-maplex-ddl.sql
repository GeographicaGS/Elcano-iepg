/*

  Maplex time carto schema DDL.

*/

\i 00-config.sql
\c :dbname :user :host :port

begin;

create schema maplex authorization :user;

create table maplex.geoentity(
  id_geoentity integer,
  description text,
  date_in timestamp,
  date_out timestamp
);

alter table maplex.geoentity
add constraint geoentity_pkey
primary key(id_geoentity);


create table maplex.geometry(
  id_geometry integer,
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
  id_geometry_family integer,
  name varchar(100),
  description text
);

alter table maplex.geometry_family
add constraint geometry_family_pkey
primary key(id_geometry_family);


create table maplex.geoentity_geometry(
  id_geoentity integer,
  id_geometry_family integer,
  id_geometry integer,
  date_in timestamp,
  date_out timestamp
);

alter table maplex.geoentity_geometry
add constraint geoentity_geometry_pkey
primary key(id_geoentity, id_geometry_family, id_geometry);


create table maplex.name(
  id_name integer,
  name varchar(500),
  description text
);

alter table maplex.name
add constraint name_pkey
primary key(id_name);


create table maplex.name_family(
  id_name_family integer,
  name varchar(100),
  description text
);

alter table maplex.name_family
add constraint name_family_pkey
primary key(id_name_family);


create table maplex.geoentity_name(
  id_geoentity integer,
  id_name integer,
  id_name_family integer,
  date_in timestamp,
  date_out timestamp
);

alter table maplex.geoentity_name
add constraint geoentity_name_pkey
primary key(id_geoentity, id_name, id_name_family);


create table maplex.block(
  id_geoentity_block integer,
  id_geoentity_child integer,
  date_in timestamp,
  date_out timestamp
);

alter table maplex.block
add constraint block_pkey
primary key(id_geoentity_block, id_geoentity_child);

-- Table off the record for a quick fix in IEPG

create table maplex.iepg_short_names(
  name varchar(100),
  un_code varchar(20),
  short_en varchar(100),
  short_es varchar(100)
);


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

alter table maplex.geoentity_geometry
add constraint geoentity_geometry_geoentity_fkey
foreign key (id_geoentity) references maplex.geoentity(id_geoentity);

alter table maplex.geoentity_geometry
add constraint geoentity_geometry_geometry_fkey
foreign key (id_geometry) references maplex.geometry(id_geometry);

alter table maplex.geoentity_geometry
add constraint geoentity_geometry_geometry_family_fkey
foreign key (id_geometry_family) references maplex.geometry_family(id_geometry_family);


-- Views

create view maplex.vw__names as
select
  a.id_geoentity as id_geoentity,
  a.description as geoentity_description,
  a.date_in as geoentity_date_in,
  a.date_out as geoentity_date_out,
  b.id_name as id_name,
  b.date_in as name_date_in,
  b.date_out as name_date_out,
  c.name as name,
  c.description as name_description,
  d.id_name_family as id_name_family,
  d.name as name_family,
  d.description as name_family_description
from
  maplex.geoentity a inner join
  maplex.geoentity_name b on
  a.id_geoentity=b.id_geoentity inner join
  maplex.name c on
  b.id_name=c.id_name inner join
  maplex.name_family d on
  b.id_name_family=d.id_name_family;


create view maplex.vw__geometries as
select
  a.id_geoentity as id_geoentity,
  a.description as geoentity_description,
  a.date_in as geoentity_date_in,
  a.date_out as geoentity_date_out,
  b.id_geometry as id_geometry,
  b.date_in as geometry_date_in,
  b.date_out as geometry_date_out,
  d.description as geometry_description,
  c.id_geometry_family as id_geometry_family,
  c.name as name_geometry_family,
  c.description as geometry_family_description,
  d.geom as geom
from
  maplex.geoentity a inner join
  maplex.geoentity_geometry b on
  a.id_geoentity=b.id_geoentity inner join
  maplex.geometry_family c on
  b.id_geometry_family=c.id_geometry_family inner join
  maplex.geometry d on
  b.id_geometry=d.id_geometry;


create view maplex.vw__blocks_membership as
select
  a.id_geoentity as id_geoentity_block,
  a.description as description_block,
  a.date_in as date_in_block,
  a.date_out as date_out_block,
  b.date_in as date_in_membership,
  b.date_out as date_out_membership,
  c.id_geoentity as id_geoentity_child,
  c.description as description_child,
  c.date_in as date_in_child,
  c.date_out as date_out_child
from
  maplex.geoentity a inner join
  maplex.block b on
  a.id_geoentity=b.id_geoentity_block inner join
  maplex.geoentity c on
  b.id_geoentity_child=c.id_geoentity;
  

create view maplex.vw__blocks as
with a as (
  select distinct
    id_geoentity_block as id
  from
    maplex.vw__blocks_membership
  where date_out_membership is null
)
select
  id_geoentity_block,
  min(date_in_membership) as date_members_first_entry,
  case when exists(select * from a where id=id_geoentity_block) then null
       else max(date_out_membership)
  end as date_members_last_exit,
  description_block,
  date_in_block,
  date_out_block
from maplex.vw__blocks_membership
group by id_geoentity_block, description_block, date_in_block, date_out_block;


create view maplex.vw__geoentity_names as
select
  a.id_geoentity as id_geoentity,
  a.description as description_geoentity,
  a.date_in as date_in_geoentity,
  a.date_out as date_out_geoentity,
  b.date_in as date_in_name_assignation,
  b.date_out as date_out_name_assignation,
  c.id_name_family as id_name_family,
  c.name as name_family,
  c.description as description_name_family,
  d.id_name as id_name,
  d.name as name,
  d.description as description_name
from
  maplex.geoentity a inner join
  maplex.geoentity_name b on
  a.id_geoentity = b.id_geoentity inner join
  maplex.name_family c on
  b.id_name_family = c.id_name_family inner join
  maplex.name d on
  b.id_name = d.id_name;


create view maplex.vw__iepg_country_data as
with a as(
  select
    a.name as geoentity_desc,
    b.name as un_code,
    c.name as english_long,
    d.name as spanish_long,
    e.name as iso2
  from
    maplex.vw__names a inner join
    maplex.vw__names b on 
    a.id_geoentity=b.id_geoentity inner join
    maplex.vw__names c on
    a.id_geoentity=c.id_geoentity inner join
    maplex.vw__names d on
    a.id_geoentity=d.id_geoentity inner join
    maplex.vw__names e on
    a.id_geoentity=e.id_geoentity
  where
    a.id_name_family=3 and 
    b.id_name_family=5 and
    c.id_name_family=2 and
    d.id_name_family=3 and
    e.id_name_family=1 and
    b.name::integer in (012,024,032,036,040,050,056,076,100,124,152,156,170,191,196,203,208,233,246,250,276,300,348,352,
                        356,360,364,368,372,376,380,392,398,410,414,428,440,442,458,470,484,528,554,566,578,586,604,608,
                        616,620,634,642,643,682,702,703,704,705,710,724,752,756,764,784,792,804,818,826,840,862)
)
select
  coalesce(c.iso_3166_1_2_code, iso2) as iso_3166_1_2_code,
  a.*,
  b.short_en as english_short,
  b.short_es as spanish_short,
  c.name,
  st_asgeojson(c.geom) as geojson
from 
  a inner join
  maplex.iepg_short_names b on
  a.un_code=b.un_code full outer join 
  iepg_data.country_geom c on
  c.iso_3166_1_2_code=a.iso2
order by a.geoentity_desc;


-- Restore data

\copy maplex.geoentity from 'maplex_geoentity.csv' with delimiter '|' csv header quote '"' null '#@#@'

\copy maplex.name_family from 'maplex_name_family.csv' with delimiter '|' csv header quote '"' null '#@#@'

\copy maplex.name from 'maplex_name.csv' with delimiter '|' csv header quote '"' null '#@#@'

\copy maplex.geometry_family from 'maplex_geometry_family.csv' with delimiter '|' csv header quote '"' null '#@#@'

\copy maplex.block from 'maplex_block.csv' with delimiter '|' csv header quote '"' null '#@#@'

\copy maplex.geometry from 'maplex_geometry.csv' with delimiter '|' csv header quote '"' null '#@#@'

\copy maplex.geoentity_geometry from 'maplex_geoentity_geometry.csv' with delimiter '|' csv header quote '"' null '#@#@'

\copy maplex.geoentity_name from 'maplex_geoentity_name.csv' with delimiter '|' csv header quote '"' null '#@#@'

\copy maplex.iepg_short_names from 'csv/maplex-country_short_iepg.csv' with delimiter ',' csv header null '#@#@'

commit;

vacuum analyze;
