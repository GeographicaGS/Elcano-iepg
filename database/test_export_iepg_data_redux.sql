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
  
