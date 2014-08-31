select
  a.name as aname,
  b.name as bname
from
  maplex.vw__names a inner join
  maplex.vw__names b on
  a.id_geoentity=b.id_geoentity
where
  a.id_name_family=3 and 
  b.id_name_family=5
order by
  aname
;


