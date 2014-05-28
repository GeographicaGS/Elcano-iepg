select
  c.name as code,
  a.date_members_first_entry as date_members_first_entry,
  a.date_members_last_exit as date_members_last_exit,
  a.description_block as description_block,
  a.date_in_block as date_in_block,
  a.date_out_block as date_out_block
from
  maplex.vw__blocks a left join 
  maplex.geoentity_name b on
  a.id_geoentity_block=b.id_geoentity left join
  maplex.name c on
  b.id_name=c.id_name
where
  id_name_family=1;

select
  a.id_geoentity_block as code, 
  a.date_members_first_entry as date_members_first_entry,
  a.date_members_last_exit as date_members_last_exit,
  a.description_block as description_block,
  a.date_in_block as date_in_block,
  a.date_out_block as date_out_block
from
  maplex.vw__blocks a;


select
  c.name as id_geoentity_block,
  a.description_block as description_block,
  a.date_in_block as date_in_block,
  a.date_out_block as date_out_block,
  a.date_in_membership as date_in_membership,
  a.date_out_membership as date_out_membership,
  e.name as id_geoentity_child,
  a.description_child as description_child,
  a.date_in_child as date_in_child,
  a.date_out_child as date_out_child
from
  maplex.vw__blocks_membership a left join 
  maplex.geoentity_name b on
  a.id_geoentity_block=b.id_geoentity left join
  maplex.name c on
  b.id_name=c.id_name left join
  maplex.geoentity_name d on
  a.id_geoentity_child=d.id_geoentity left join
  maplex.name e on
  d.id_name = e.id_name
where
  b.id_name_family=3 and d.id_name_family=3 and c.name='XBAP';
