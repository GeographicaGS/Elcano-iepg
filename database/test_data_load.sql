-- create table iepg_data_redux.iepe_individual_contributions as
-- -- insert into iepg_data_redux.iepg_relative_contributions
-- select
--   a.iso_3166_1_2_code::varchar(10) as code,
--   --'XBEU' as code,
--   b.date_in as date_in,
--   b.date_out as date_out,
--   b.energy as energy,
--   b.primary_goods as primary_goods,
--   b.manufactures as manufactures,
--   b.services as services,
--   b.investments as investments,
--   b.troops              as   troops            ,      
--   b.military_equipment  as   military_equipment,
--   b.migrations          as   migrations        ,
--   b.tourism             as   tourism           ,
--   b.sports              as   sports            ,
--   b.culture             as   culture           ,
--   b.information         as   information       ,
--   b.technology          as   technology        ,
--   b.science             as   science           ,
--   b.education           as   education         ,     
--   b.cooperation         as   cooperation       ,     
--  -- b.economic_presence   as   economic_presence ,     
--  -- b.military_presence   as   military_presence ,     
--  -- b.soft_presence       as   soft_presence     ,

--  b.economic_contribution   as   economic_contribution ,     
--  b.military_contribution   as   military_contribution ,     
--  b.soft_contribution       as   soft_contribution     --,

--  --b.iepg                as   iepg
-- from
--  iepg_data.master_country a inner join
--   iepg_data.iepg_individual_contributions b on
--   a.id_master_country=b.id_master_country
-- order by code, date_in;








-- create table iepg_data_redux.pob_pib as 
-- select
--   a.iso_3166_1_2_code::varchar(10) as code,
--   b.date_in as date_in,
--   b.date_out as date_out,
--   b.population as population,
--   b.pib as pib
-- from
--   iepg_data.master_country a inner join
--   iepg_data.pob_pib b on
--   a.id_master_country=b.id_master_country
-- where a.iso_3166_1_2_code is not null
-- order by code, date_in;





create table iepg_data_redux.iepg_quota as
select 
    a.iso_3166_1_2_code::varchar(10) as code,
  b.date_in as date_in,
  b.date_out as date_out,
  b.global_quota as global_quota,
  b.economic_quota as economic_quota,
  b.military_quota as military_quota,
  b.soft_quota as soft_quota
from
  iepg_data.master_country a inner join
  iepg_data.iepg_quotas b on
  a.id_master_country=b.id_master_country
order by code, date_in;

-- create table iepg_data_redux.iepg_comments as
-- select
--   a.iso_3166_1_2_code as code,
--   b.date_in as date_in,
--   b.date_out as date_out,
--   b.comment as comment,
--   b.language as language
-- from
--   iepg_data.master_country a inner join
--   iepg_data.iepg_comment b on
--   a.id_master_country=b.id_master_country
-- where a.iso_3166_1_2_code is not null and date_part('YEAR', b.date_in)=2013
-- order by code, date_in, language;
