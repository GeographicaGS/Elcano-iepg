select
  a.id_geoentity,
  a.name,
  b.name
from
  maplex.vw__names a inner join
  maplex.vw__names b on
  a.id_geoentity=b.id_geoentity
where 
  a.id_name_family=2 and
  b.id_name_family=5
order by a.name;
