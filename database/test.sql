with name_a as(
  select 
    a.id_geoentity, 
    b.name
  from 
    maplex.geoentity_name a inner join 
    maplex.name b on
    a.id_name=b.id_name
  where id_name_family=1),
name_b as(
  select 
    a.id_geoentity, 
    b.name
  from 
    maplex.geoentity_name a inner join 
    maplex.name b on
    a.id_name=b.id_name
  where id_name_family=2)
select
  a.name as name_a,
  b.name as name_b
from
  name_a a full outer join
  name_b b on
  a.id_geoentity=b.id_geoentity;


