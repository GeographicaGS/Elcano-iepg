select 
 code                  ,
 date_in               ,
 date_out              ,
 energy                +
 primary_goods         +
 manufactures          +
 services              +
 investments           +
 troops                +
 military_equipment    +
 migrations            +
 tourism               +
 sports                +
 culture               +
 information           +
 technology            +
 science               +
 education             +
 cooperation           ,
 economic_contribution +
 military_contribution +
 soft_contribution     
from iepg_data_redux.iepg_relative_contribution
where code='AE' and date_in='1990-01-01';

select 
 code                  ,
 date_in               ,
 date_out              ,
 energy                +
 primary_goods         +
 manufactures          +
 services              +
 investments           +
 troops                +
 military_equipment    +
 migrations            +
 tourism               +
 sports                +
 culture               +
 information           +
 technology            +
 science               +
 education             +
 cooperation           ,
 economic_presence +
 military_presence +
 soft_presence,
  iepg     
from iepg_data_redux.iepg_data
where code='AE' and date_in='1990-01-01';
