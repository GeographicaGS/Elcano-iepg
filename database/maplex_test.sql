-- insert into maplex.geoentity_name
-- select
--   a.id_geoentity,
--   b.id_name,
--   3
-- from
--   maplex.geoentity a inner join
--   maplex.name b on
--   left(a.description, strpos(a.description, ']'))=left(b.description, strpos(a.description, ']'))
-- where
--   strpos(b.description, 'spanish 1.')<>0;



-- insert into maplex.name (description, name)
-- select 
--   '[' || short_name_en1 || '] short name spanish 1.',
--   trim(short_name_es1)
-- from
--   iepg_data.master_country
-- where country;

create view maplex.names as
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
