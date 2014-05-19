insert into maplex.geoentity_name
select
  a.id_geoentity,
  b.id_name,
  1
from
  maplex.geoentity a inner join
  maplex.name b on
  left(a.description, strpos(a.description, ']'))=left(b.description, strpos(a.description, ']'));
