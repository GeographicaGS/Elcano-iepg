
select 
  id_geoentity_block, 
  min(date_in_membership) as date_founding,
  case  
  max(date_out_membership) as date_terminate
from maplex.vw__blocks
group by id_geoentity_block;
