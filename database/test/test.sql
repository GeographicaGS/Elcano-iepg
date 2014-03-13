create table import.iepg_trat5 as 
select
  "país",
  num_pais,
  b.id_master_country,
  '20120101'::date as date_in,
  '20121231'::date as date_out,
  energy,
  "primary goods",
  manufactures,
  services,
  investments,
  troops,
  "military equipment",
  migrations,
  tourism,
  sports,
  culture,
  information,
  technology,
  science,
  education,
  cooperation,
  "economía",
  militar,
  "poder blando",
  iepg
from
  import.sheet7 a left join
  iepg_data.master_country b
  on a."país"=b.short_name_es;
