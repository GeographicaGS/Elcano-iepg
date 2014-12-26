-- Exports data to Excel format

create or replace view iepg_data_redux.vw__energy as
with names as(
  select
    a.name as iso,
    b.name as spanish
  from 
    maplex.vw__names a inner join
    maplex.vw__names b on
    a.id_geoentity=b.id_geoentity
    where
      a.id_name_family=1 and 
      b.id_name_family=3
), data as(
  select
    b.spanish, date_part('year', date_in) as year, energy as data
  from
    iepg_data_redux.iepg_data a inner join
    names b on
    a.code=b.iso
  order by code, year
), distinct_names as(
  select distinct
    spanish
  from
    data
  order by spanish
), data1990 as(
  select
    spanish, data
  from 
    data
  where
    year=1990
), data1995 as(
  select
    spanish, data
  from 
    data
  where
    year=1995
), data2000 as(
  select
    spanish, data
  from 
    data
  where
    year=2000
), data2005 as(
  select
    spanish, data
  from 
    data
  where
    year=2005
), data2010 as(
  select
    spanish, data
  from 
    data
  where
    year=2010
), data2011 as(
  select
    spanish, data
  from 
    data
  where
    year=2011
), data2012 as(
  select
    spanish, data
  from 
    data
  where
    year=2012
), data2013 as(
  select
    spanish, data
  from 
    data
  where
    year=2013
)
select
  a.spanish as spanish,
  b.data as d1990,
  c.data as d1995,
  d.data as d2000,
  e.data as d2005,
  f.data as d2010,
  g.data as d2011,
  h.data as d2012,
  i.data as d2013
from
  distinct_names a left join
  data1990 b on
  a.spanish=b.spanish left join
  data1995 c on
  a.spanish=c.spanish left join
  data2000 d on
  a.spanish=d.spanish left join
  data2005 e on
  a.spanish=e.spanish left join
  data2010 f on
  a.spanish=f.spanish left join
  data2011 g on
  a.spanish=g.spanish left join
  data2012 h on
  a.spanish=h.spanish left join
  data2013 i on
  a.spanish=i.spanish
order by spanish;
  


create or replace view iepg_data_redux.vw__primary_goods as
with names as(
  select
    a.name as iso,
    b.name as spanish
  from 
    maplex.vw__names a inner join
    maplex.vw__names b on
    a.id_geoentity=b.id_geoentity
    where
      a.id_name_family=1 and 
      b.id_name_family=3
), data as(
  select
    b.spanish, date_part('year', date_in) as year, primary_goods as data
  from
    iepg_data_redux.iepg_data a inner join
    names b on
    a.code=b.iso
  order by code, year
), distinct_names as(
  select distinct
    spanish
  from
    data
  order by spanish
), data1990 as(
  select
    spanish, data
  from 
    data
  where
    year=1990
), data1995 as(
  select
    spanish, data
  from 
    data
  where
    year=1995
), data2000 as(
  select
    spanish, data
  from 
    data
  where
    year=2000
), data2005 as(
  select
    spanish, data
  from 
    data
  where
    year=2005
), data2010 as(
  select
    spanish, data
  from 
    data
  where
    year=2010
), data2011 as(
  select
    spanish, data
  from 
    data
  where
    year=2011
), data2012 as(
  select
    spanish, data
  from 
    data
  where
    year=2012
), data2013 as(
  select
    spanish, data
  from 
    data
  where
    year=2013
)
select
  a.spanish as spanish,
  b.data as d1990,
  c.data as d1995,
  d.data as d2000,
  e.data as d2005,
  f.data as d2010,
  g.data as d2011,
  h.data as d2012,
  i.data as d2013
from
  distinct_names a left join
  data1990 b on
  a.spanish=b.spanish left join
  data1995 c on
  a.spanish=c.spanish left join
  data2000 d on
  a.spanish=d.spanish left join
  data2005 e on
  a.spanish=e.spanish left join
  data2010 f on
  a.spanish=f.spanish left join
  data2011 g on
  a.spanish=g.spanish left join
  data2012 h on
  a.spanish=h.spanish left join
  data2013 i on
  a.spanish=i.spanish
order by spanish;
  


create or replace view iepg_data_redux.vw__manufactures as
with names as(
  select
    a.name as iso,
    b.name as spanish
  from 
    maplex.vw__names a inner join
    maplex.vw__names b on
    a.id_geoentity=b.id_geoentity
    where
      a.id_name_family=1 and 
      b.id_name_family=3
), data as(
  select
    b.spanish, date_part('year', date_in) as year, manufactures as data
  from
    iepg_data_redux.iepg_data a inner join
    names b on
    a.code=b.iso
  order by code, year
), distinct_names as(
  select distinct
    spanish
  from
    data
  order by spanish
), data1990 as(
  select
    spanish, data
  from 
    data
  where
    year=1990
), data1995 as(
  select
    spanish, data
  from 
    data
  where
    year=1995
), data2000 as(
  select
    spanish, data
  from 
    data
  where
    year=2000
), data2005 as(
  select
    spanish, data
  from 
    data
  where
    year=2005
), data2010 as(
  select
    spanish, data
  from 
    data
  where
    year=2010
), data2011 as(
  select
    spanish, data
  from 
    data
  where
    year=2011
), data2012 as(
  select
    spanish, data
  from 
    data
  where
    year=2012
), data2013 as(
  select
    spanish, data
  from 
    data
  where
    year=2013
)
select
  a.spanish as spanish,
  b.data as d1990,
  c.data as d1995,
  d.data as d2000,
  e.data as d2005,
  f.data as d2010,
  g.data as d2011,
  h.data as d2012,
  i.data as d2013
from
  distinct_names a left join
  data1990 b on
  a.spanish=b.spanish left join
  data1995 c on
  a.spanish=c.spanish left join
  data2000 d on
  a.spanish=d.spanish left join
  data2005 e on
  a.spanish=e.spanish left join
  data2010 f on
  a.spanish=f.spanish left join
  data2011 g on
  a.spanish=g.spanish left join
  data2012 h on
  a.spanish=h.spanish left join
  data2013 i on
  a.spanish=i.spanish
order by spanish;
  


create or replace view iepg_data_redux.vw__services as
with names as(
  select
    a.name as iso,
    b.name as spanish
  from 
    maplex.vw__names a inner join
    maplex.vw__names b on
    a.id_geoentity=b.id_geoentity
    where
      a.id_name_family=1 and 
      b.id_name_family=3
), data as(
  select
    b.spanish, date_part('year', date_in) as year, services as data
  from
    iepg_data_redux.iepg_data a inner join
    names b on
    a.code=b.iso
  order by code, year
), distinct_names as(
  select distinct
    spanish
  from
    data
  order by spanish
), data1990 as(
  select
    spanish, data
  from 
    data
  where
    year=1990
), data1995 as(
  select
    spanish, data
  from 
    data
  where
    year=1995
), data2000 as(
  select
    spanish, data
  from 
    data
  where
    year=2000
), data2005 as(
  select
    spanish, data
  from 
    data
  where
    year=2005
), data2010 as(
  select
    spanish, data
  from 
    data
  where
    year=2010
), data2011 as(
  select
    spanish, data
  from 
    data
  where
    year=2011
), data2012 as(
  select
    spanish, data
  from 
    data
  where
    year=2012
), data2013 as(
  select
    spanish, data
  from 
    data
  where
    year=2013
)
select
  a.spanish as spanish,
  b.data as d1990,
  c.data as d1995,
  d.data as d2000,
  e.data as d2005,
  f.data as d2010,
  g.data as d2011,
  h.data as d2012,
  i.data as d2013
from
  distinct_names a left join
  data1990 b on
  a.spanish=b.spanish left join
  data1995 c on
  a.spanish=c.spanish left join
  data2000 d on
  a.spanish=d.spanish left join
  data2005 e on
  a.spanish=e.spanish left join
  data2010 f on
  a.spanish=f.spanish left join
  data2011 g on
  a.spanish=g.spanish left join
  data2012 h on
  a.spanish=h.spanish left join
  data2013 i on
  a.spanish=i.spanish
order by spanish;
  


create or replace view iepg_data_redux.vw__investments as
with names as(
  select
    a.name as iso,
    b.name as spanish
  from 
    maplex.vw__names a inner join
    maplex.vw__names b on
    a.id_geoentity=b.id_geoentity
    where
      a.id_name_family=1 and 
      b.id_name_family=3
), data as(
  select
    b.spanish, date_part('year', date_in) as year, investments as data
  from
    iepg_data_redux.iepg_data a inner join
    names b on
    a.code=b.iso
  order by code, year
), distinct_names as(
  select distinct
    spanish
  from
    data
  order by spanish
), data1990 as(
  select
    spanish, data
  from 
    data
  where
    year=1990
), data1995 as(
  select
    spanish, data
  from 
    data
  where
    year=1995
), data2000 as(
  select
    spanish, data
  from 
    data
  where
    year=2000
), data2005 as(
  select
    spanish, data
  from 
    data
  where
    year=2005
), data2010 as(
  select
    spanish, data
  from 
    data
  where
    year=2010
), data2011 as(
  select
    spanish, data
  from 
    data
  where
    year=2011
), data2012 as(
  select
    spanish, data
  from 
    data
  where
    year=2012
), data2013 as(
  select
    spanish, data
  from 
    data
  where
    year=2013
)
select
  a.spanish as spanish,
  b.data as d1990,
  c.data as d1995,
  d.data as d2000,
  e.data as d2005,
  f.data as d2010,
  g.data as d2011,
  h.data as d2012,
  i.data as d2013
from
  distinct_names a left join
  data1990 b on
  a.spanish=b.spanish left join
  data1995 c on
  a.spanish=c.spanish left join
  data2000 d on
  a.spanish=d.spanish left join
  data2005 e on
  a.spanish=e.spanish left join
  data2010 f on
  a.spanish=f.spanish left join
  data2011 g on
  a.spanish=g.spanish left join
  data2012 h on
  a.spanish=h.spanish left join
  data2013 i on
  a.spanish=i.spanish
order by spanish;
  


create or replace view iepg_data_redux.vw__troops as
with names as(
  select
    a.name as iso,
    b.name as spanish
  from 
    maplex.vw__names a inner join
    maplex.vw__names b on
    a.id_geoentity=b.id_geoentity
    where
      a.id_name_family=1 and 
      b.id_name_family=3
), data as(
  select
    b.spanish, date_part('year', date_in) as year, troops as data
  from
    iepg_data_redux.iepg_data a inner join
    names b on
    a.code=b.iso
  order by code, year
), distinct_names as(
  select distinct
    spanish
  from
    data
  order by spanish
), data1990 as(
  select
    spanish, data
  from 
    data
  where
    year=1990
), data1995 as(
  select
    spanish, data
  from 
    data
  where
    year=1995
), data2000 as(
  select
    spanish, data
  from 
    data
  where
    year=2000
), data2005 as(
  select
    spanish, data
  from 
    data
  where
    year=2005
), data2010 as(
  select
    spanish, data
  from 
    data
  where
    year=2010
), data2011 as(
  select
    spanish, data
  from 
    data
  where
    year=2011
), data2012 as(
  select
    spanish, data
  from 
    data
  where
    year=2012
), data2013 as(
  select
    spanish, data
  from 
    data
  where
    year=2013
)
select
  a.spanish as spanish,
  b.data as d1990,
  c.data as d1995,
  d.data as d2000,
  e.data as d2005,
  f.data as d2010,
  g.data as d2011,
  h.data as d2012,
  i.data as d2013
from
  distinct_names a left join
  data1990 b on
  a.spanish=b.spanish left join
  data1995 c on
  a.spanish=c.spanish left join
  data2000 d on
  a.spanish=d.spanish left join
  data2005 e on
  a.spanish=e.spanish left join
  data2010 f on
  a.spanish=f.spanish left join
  data2011 g on
  a.spanish=g.spanish left join
  data2012 h on
  a.spanish=h.spanish left join
  data2013 i on
  a.spanish=i.spanish
order by spanish;
  


create or replace view iepg_data_redux.vw__military_equipment as
with names as(
  select
    a.name as iso,
    b.name as spanish
  from 
    maplex.vw__names a inner join
    maplex.vw__names b on
    a.id_geoentity=b.id_geoentity
    where
      a.id_name_family=1 and 
      b.id_name_family=3
), data as(
  select
    b.spanish, date_part('year', date_in) as year, military_equipment as data
  from
    iepg_data_redux.iepg_data a inner join
    names b on
    a.code=b.iso
  order by code, year
), distinct_names as(
  select distinct
    spanish
  from
    data
  order by spanish
), data1990 as(
  select
    spanish, data
  from 
    data
  where
    year=1990
), data1995 as(
  select
    spanish, data
  from 
    data
  where
    year=1995
), data2000 as(
  select
    spanish, data
  from 
    data
  where
    year=2000
), data2005 as(
  select
    spanish, data
  from 
    data
  where
    year=2005
), data2010 as(
  select
    spanish, data
  from 
    data
  where
    year=2010
), data2011 as(
  select
    spanish, data
  from 
    data
  where
    year=2011
), data2012 as(
  select
    spanish, data
  from 
    data
  where
    year=2012
), data2013 as(
  select
    spanish, data
  from 
    data
  where
    year=2013
)
select
  a.spanish as spanish,
  b.data as d1990,
  c.data as d1995,
  d.data as d2000,
  e.data as d2005,
  f.data as d2010,
  g.data as d2011,
  h.data as d2012,
  i.data as d2013
from
  distinct_names a left join
  data1990 b on
  a.spanish=b.spanish left join
  data1995 c on
  a.spanish=c.spanish left join
  data2000 d on
  a.spanish=d.spanish left join
  data2005 e on
  a.spanish=e.spanish left join
  data2010 f on
  a.spanish=f.spanish left join
  data2011 g on
  a.spanish=g.spanish left join
  data2012 h on
  a.spanish=h.spanish left join
  data2013 i on
  a.spanish=i.spanish
order by spanish;
  


create or replace view iepg_data_redux.vw__migrations as
with names as(
  select
    a.name as iso,
    b.name as spanish
  from 
    maplex.vw__names a inner join
    maplex.vw__names b on
    a.id_geoentity=b.id_geoentity
    where
      a.id_name_family=1 and 
      b.id_name_family=3
), data as(
  select
    b.spanish, date_part('year', date_in) as year, migrations as data
  from
    iepg_data_redux.iepg_data a inner join
    names b on
    a.code=b.iso
  order by code, year
), distinct_names as(
  select distinct
    spanish
  from
    data
  order by spanish
), data1990 as(
  select
    spanish, data
  from 
    data
  where
    year=1990
), data1995 as(
  select
    spanish, data
  from 
    data
  where
    year=1995
), data2000 as(
  select
    spanish, data
  from 
    data
  where
    year=2000
), data2005 as(
  select
    spanish, data
  from 
    data
  where
    year=2005
), data2010 as(
  select
    spanish, data
  from 
    data
  where
    year=2010
), data2011 as(
  select
    spanish, data
  from 
    data
  where
    year=2011
), data2012 as(
  select
    spanish, data
  from 
    data
  where
    year=2012
), data2013 as(
  select
    spanish, data
  from 
    data
  where
    year=2013
)
select
  a.spanish as spanish,
  b.data as d1990,
  c.data as d1995,
  d.data as d2000,
  e.data as d2005,
  f.data as d2010,
  g.data as d2011,
  h.data as d2012,
  i.data as d2013
from
  distinct_names a left join
  data1990 b on
  a.spanish=b.spanish left join
  data1995 c on
  a.spanish=c.spanish left join
  data2000 d on
  a.spanish=d.spanish left join
  data2005 e on
  a.spanish=e.spanish left join
  data2010 f on
  a.spanish=f.spanish left join
  data2011 g on
  a.spanish=g.spanish left join
  data2012 h on
  a.spanish=h.spanish left join
  data2013 i on
  a.spanish=i.spanish
order by spanish;
  


create or replace view iepg_data_redux.vw__tourism as
with names as(
  select
    a.name as iso,
    b.name as spanish
  from 
    maplex.vw__names a inner join
    maplex.vw__names b on
    a.id_geoentity=b.id_geoentity
    where
      a.id_name_family=1 and 
      b.id_name_family=3
), data as(
  select
    b.spanish, date_part('year', date_in) as year, tourism as data
  from
    iepg_data_redux.iepg_data a inner join
    names b on
    a.code=b.iso
  order by code, year
), distinct_names as(
  select distinct
    spanish
  from
    data
  order by spanish
), data1990 as(
  select
    spanish, data
  from 
    data
  where
    year=1990
), data1995 as(
  select
    spanish, data
  from 
    data
  where
    year=1995
), data2000 as(
  select
    spanish, data
  from 
    data
  where
    year=2000
), data2005 as(
  select
    spanish, data
  from 
    data
  where
    year=2005
), data2010 as(
  select
    spanish, data
  from 
    data
  where
    year=2010
), data2011 as(
  select
    spanish, data
  from 
    data
  where
    year=2011
), data2012 as(
  select
    spanish, data
  from 
    data
  where
    year=2012
), data2013 as(
  select
    spanish, data
  from 
    data
  where
    year=2013
)
select
  a.spanish as spanish,
  b.data as d1990,
  c.data as d1995,
  d.data as d2000,
  e.data as d2005,
  f.data as d2010,
  g.data as d2011,
  h.data as d2012,
  i.data as d2013
from
  distinct_names a left join
  data1990 b on
  a.spanish=b.spanish left join
  data1995 c on
  a.spanish=c.spanish left join
  data2000 d on
  a.spanish=d.spanish left join
  data2005 e on
  a.spanish=e.spanish left join
  data2010 f on
  a.spanish=f.spanish left join
  data2011 g on
  a.spanish=g.spanish left join
  data2012 h on
  a.spanish=h.spanish left join
  data2013 i on
  a.spanish=i.spanish
order by spanish;
  


create or replace view iepg_data_redux.vw__sports as
with names as(
  select
    a.name as iso,
    b.name as spanish
  from 
    maplex.vw__names a inner join
    maplex.vw__names b on
    a.id_geoentity=b.id_geoentity
    where
      a.id_name_family=1 and 
      b.id_name_family=3
), data as(
  select
    b.spanish, date_part('year', date_in) as year, sports as data
  from
    iepg_data_redux.iepg_data a inner join
    names b on
    a.code=b.iso
  order by code, year
), distinct_names as(
  select distinct
    spanish
  from
    data
  order by spanish
), data1990 as(
  select
    spanish, data
  from 
    data
  where
    year=1990
), data1995 as(
  select
    spanish, data
  from 
    data
  where
    year=1995
), data2000 as(
  select
    spanish, data
  from 
    data
  where
    year=2000
), data2005 as(
  select
    spanish, data
  from 
    data
  where
    year=2005
), data2010 as(
  select
    spanish, data
  from 
    data
  where
    year=2010
), data2011 as(
  select
    spanish, data
  from 
    data
  where
    year=2011
), data2012 as(
  select
    spanish, data
  from 
    data
  where
    year=2012
), data2013 as(
  select
    spanish, data
  from 
    data
  where
    year=2013
)
select
  a.spanish as spanish,
  b.data as d1990,
  c.data as d1995,
  d.data as d2000,
  e.data as d2005,
  f.data as d2010,
  g.data as d2011,
  h.data as d2012,
  i.data as d2013
from
  distinct_names a left join
  data1990 b on
  a.spanish=b.spanish left join
  data1995 c on
  a.spanish=c.spanish left join
  data2000 d on
  a.spanish=d.spanish left join
  data2005 e on
  a.spanish=e.spanish left join
  data2010 f on
  a.spanish=f.spanish left join
  data2011 g on
  a.spanish=g.spanish left join
  data2012 h on
  a.spanish=h.spanish left join
  data2013 i on
  a.spanish=i.spanish
order by spanish;
  


create or replace view iepg_data_redux.vw__culture as
with names as(
  select
    a.name as iso,
    b.name as spanish
  from 
    maplex.vw__names a inner join
    maplex.vw__names b on
    a.id_geoentity=b.id_geoentity
    where
      a.id_name_family=1 and 
      b.id_name_family=3
), data as(
  select
    b.spanish, date_part('year', date_in) as year, culture as data
  from
    iepg_data_redux.iepg_data a inner join
    names b on
    a.code=b.iso
  order by code, year
), distinct_names as(
  select distinct
    spanish
  from
    data
  order by spanish
), data1990 as(
  select
    spanish, data
  from 
    data
  where
    year=1990
), data1995 as(
  select
    spanish, data
  from 
    data
  where
    year=1995
), data2000 as(
  select
    spanish, data
  from 
    data
  where
    year=2000
), data2005 as(
  select
    spanish, data
  from 
    data
  where
    year=2005
), data2010 as(
  select
    spanish, data
  from 
    data
  where
    year=2010
), data2011 as(
  select
    spanish, data
  from 
    data
  where
    year=2011
), data2012 as(
  select
    spanish, data
  from 
    data
  where
    year=2012
), data2013 as(
  select
    spanish, data
  from 
    data
  where
    year=2013
)
select
  a.spanish as spanish,
  b.data as d1990,
  c.data as d1995,
  d.data as d2000,
  e.data as d2005,
  f.data as d2010,
  g.data as d2011,
  h.data as d2012,
  i.data as d2013
from
  distinct_names a left join
  data1990 b on
  a.spanish=b.spanish left join
  data1995 c on
  a.spanish=c.spanish left join
  data2000 d on
  a.spanish=d.spanish left join
  data2005 e on
  a.spanish=e.spanish left join
  data2010 f on
  a.spanish=f.spanish left join
  data2011 g on
  a.spanish=g.spanish left join
  data2012 h on
  a.spanish=h.spanish left join
  data2013 i on
  a.spanish=i.spanish
order by spanish;
  


create or replace view iepg_data_redux.vw__information as
with names as(
  select
    a.name as iso,
    b.name as spanish
  from 
    maplex.vw__names a inner join
    maplex.vw__names b on
    a.id_geoentity=b.id_geoentity
    where
      a.id_name_family=1 and 
      b.id_name_family=3
), data as(
  select
    b.spanish, date_part('year', date_in) as year, information as data
  from
    iepg_data_redux.iepg_data a inner join
    names b on
    a.code=b.iso
  order by code, year
), distinct_names as(
  select distinct
    spanish
  from
    data
  order by spanish
), data1990 as(
  select
    spanish, data
  from 
    data
  where
    year=1990
), data1995 as(
  select
    spanish, data
  from 
    data
  where
    year=1995
), data2000 as(
  select
    spanish, data
  from 
    data
  where
    year=2000
), data2005 as(
  select
    spanish, data
  from 
    data
  where
    year=2005
), data2010 as(
  select
    spanish, data
  from 
    data
  where
    year=2010
), data2011 as(
  select
    spanish, data
  from 
    data
  where
    year=2011
), data2012 as(
  select
    spanish, data
  from 
    data
  where
    year=2012
), data2013 as(
  select
    spanish, data
  from 
    data
  where
    year=2013
)
select
  a.spanish as spanish,
  b.data as d1990,
  c.data as d1995,
  d.data as d2000,
  e.data as d2005,
  f.data as d2010,
  g.data as d2011,
  h.data as d2012,
  i.data as d2013
from
  distinct_names a left join
  data1990 b on
  a.spanish=b.spanish left join
  data1995 c on
  a.spanish=c.spanish left join
  data2000 d on
  a.spanish=d.spanish left join
  data2005 e on
  a.spanish=e.spanish left join
  data2010 f on
  a.spanish=f.spanish left join
  data2011 g on
  a.spanish=g.spanish left join
  data2012 h on
  a.spanish=h.spanish left join
  data2013 i on
  a.spanish=i.spanish
order by spanish;
  


create or replace view iepg_data_redux.vw__technology as
with names as(
  select
    a.name as iso,
    b.name as spanish
  from 
    maplex.vw__names a inner join
    maplex.vw__names b on
    a.id_geoentity=b.id_geoentity
    where
      a.id_name_family=1 and 
      b.id_name_family=3
), data as(
  select
    b.spanish, date_part('year', date_in) as year, technology as data
  from
    iepg_data_redux.iepg_data a inner join
    names b on
    a.code=b.iso
  order by code, year
), distinct_names as(
  select distinct
    spanish
  from
    data
  order by spanish
), data1990 as(
  select
    spanish, data
  from 
    data
  where
    year=1990
), data1995 as(
  select
    spanish, data
  from 
    data
  where
    year=1995
), data2000 as(
  select
    spanish, data
  from 
    data
  where
    year=2000
), data2005 as(
  select
    spanish, data
  from 
    data
  where
    year=2005
), data2010 as(
  select
    spanish, data
  from 
    data
  where
    year=2010
), data2011 as(
  select
    spanish, data
  from 
    data
  where
    year=2011
), data2012 as(
  select
    spanish, data
  from 
    data
  where
    year=2012
), data2013 as(
  select
    spanish, data
  from 
    data
  where
    year=2013
)
select
  a.spanish as spanish,
  b.data as d1990,
  c.data as d1995,
  d.data as d2000,
  e.data as d2005,
  f.data as d2010,
  g.data as d2011,
  h.data as d2012,
  i.data as d2013
from
  distinct_names a left join
  data1990 b on
  a.spanish=b.spanish left join
  data1995 c on
  a.spanish=c.spanish left join
  data2000 d on
  a.spanish=d.spanish left join
  data2005 e on
  a.spanish=e.spanish left join
  data2010 f on
  a.spanish=f.spanish left join
  data2011 g on
  a.spanish=g.spanish left join
  data2012 h on
  a.spanish=h.spanish left join
  data2013 i on
  a.spanish=i.spanish
order by spanish;
  


create or replace view iepg_data_redux.vw__science as
with names as(
  select
    a.name as iso,
    b.name as spanish
  from 
    maplex.vw__names a inner join
    maplex.vw__names b on
    a.id_geoentity=b.id_geoentity
    where
      a.id_name_family=1 and 
      b.id_name_family=3
), data as(
  select
    b.spanish, date_part('year', date_in) as year, science as data
  from
    iepg_data_redux.iepg_data a inner join
    names b on
    a.code=b.iso
  order by code, year
), distinct_names as(
  select distinct
    spanish
  from
    data
  order by spanish
), data1990 as(
  select
    spanish, data
  from 
    data
  where
    year=1990
), data1995 as(
  select
    spanish, data
  from 
    data
  where
    year=1995
), data2000 as(
  select
    spanish, data
  from 
    data
  where
    year=2000
), data2005 as(
  select
    spanish, data
  from 
    data
  where
    year=2005
), data2010 as(
  select
    spanish, data
  from 
    data
  where
    year=2010
), data2011 as(
  select
    spanish, data
  from 
    data
  where
    year=2011
), data2012 as(
  select
    spanish, data
  from 
    data
  where
    year=2012
), data2013 as(
  select
    spanish, data
  from 
    data
  where
    year=2013
)
select
  a.spanish as spanish,
  b.data as d1990,
  c.data as d1995,
  d.data as d2000,
  e.data as d2005,
  f.data as d2010,
  g.data as d2011,
  h.data as d2012,
  i.data as d2013
from
  distinct_names a left join
  data1990 b on
  a.spanish=b.spanish left join
  data1995 c on
  a.spanish=c.spanish left join
  data2000 d on
  a.spanish=d.spanish left join
  data2005 e on
  a.spanish=e.spanish left join
  data2010 f on
  a.spanish=f.spanish left join
  data2011 g on
  a.spanish=g.spanish left join
  data2012 h on
  a.spanish=h.spanish left join
  data2013 i on
  a.spanish=i.spanish
order by spanish;
  


create or replace view iepg_data_redux.vw__education as
with names as(
  select
    a.name as iso,
    b.name as spanish
  from 
    maplex.vw__names a inner join
    maplex.vw__names b on
    a.id_geoentity=b.id_geoentity
    where
      a.id_name_family=1 and 
      b.id_name_family=3
), data as(
  select
    b.spanish, date_part('year', date_in) as year, education as data
  from
    iepg_data_redux.iepg_data a inner join
    names b on
    a.code=b.iso
  order by code, year
), distinct_names as(
  select distinct
    spanish
  from
    data
  order by spanish
), data1990 as(
  select
    spanish, data
  from 
    data
  where
    year=1990
), data1995 as(
  select
    spanish, data
  from 
    data
  where
    year=1995
), data2000 as(
  select
    spanish, data
  from 
    data
  where
    year=2000
), data2005 as(
  select
    spanish, data
  from 
    data
  where
    year=2005
), data2010 as(
  select
    spanish, data
  from 
    data
  where
    year=2010
), data2011 as(
  select
    spanish, data
  from 
    data
  where
    year=2011
), data2012 as(
  select
    spanish, data
  from 
    data
  where
    year=2012
), data2013 as(
  select
    spanish, data
  from 
    data
  where
    year=2013
)
select
  a.spanish as spanish,
  b.data as d1990,
  c.data as d1995,
  d.data as d2000,
  e.data as d2005,
  f.data as d2010,
  g.data as d2011,
  h.data as d2012,
  i.data as d2013
from
  distinct_names a left join
  data1990 b on
  a.spanish=b.spanish left join
  data1995 c on
  a.spanish=c.spanish left join
  data2000 d on
  a.spanish=d.spanish left join
  data2005 e on
  a.spanish=e.spanish left join
  data2010 f on
  a.spanish=f.spanish left join
  data2011 g on
  a.spanish=g.spanish left join
  data2012 h on
  a.spanish=h.spanish left join
  data2013 i on
  a.spanish=i.spanish
order by spanish;
  


create or replace view iepg_data_redux.vw__cooperation as
with names as(
  select
    a.name as iso,
    b.name as spanish
  from 
    maplex.vw__names a inner join
    maplex.vw__names b on
    a.id_geoentity=b.id_geoentity
    where
      a.id_name_family=1 and 
      b.id_name_family=3
), data as(
  select
    b.spanish, date_part('year', date_in) as year, cooperation as data
  from
    iepg_data_redux.iepg_data a inner join
    names b on
    a.code=b.iso
  order by code, year
), distinct_names as(
  select distinct
    spanish
  from
    data
  order by spanish
), data1990 as(
  select
    spanish, data
  from 
    data
  where
    year=1990
), data1995 as(
  select
    spanish, data
  from 
    data
  where
    year=1995
), data2000 as(
  select
    spanish, data
  from 
    data
  where
    year=2000
), data2005 as(
  select
    spanish, data
  from 
    data
  where
    year=2005
), data2010 as(
  select
    spanish, data
  from 
    data
  where
    year=2010
), data2011 as(
  select
    spanish, data
  from 
    data
  where
    year=2011
), data2012 as(
  select
    spanish, data
  from 
    data
  where
    year=2012
), data2013 as(
  select
    spanish, data
  from 
    data
  where
    year=2013
)
select
  a.spanish as spanish,
  b.data as d1990,
  c.data as d1995,
  d.data as d2000,
  e.data as d2005,
  f.data as d2010,
  g.data as d2011,
  h.data as d2012,
  i.data as d2013
from
  distinct_names a left join
  data1990 b on
  a.spanish=b.spanish left join
  data1995 c on
  a.spanish=c.spanish left join
  data2000 d on
  a.spanish=d.spanish left join
  data2005 e on
  a.spanish=e.spanish left join
  data2010 f on
  a.spanish=f.spanish left join
  data2011 g on
  a.spanish=g.spanish left join
  data2012 h on
  a.spanish=h.spanish left join
  data2013 i on
  a.spanish=i.spanish
order by spanish;
  


create or replace view iepg_data_redux.vw__economic_presence as
with names as(
  select
    a.name as iso,
    b.name as spanish
  from 
    maplex.vw__names a inner join
    maplex.vw__names b on
    a.id_geoentity=b.id_geoentity
    where
      a.id_name_family=1 and 
      b.id_name_family=3
), data as(
  select
    b.spanish, date_part('year', date_in) as year, economic_presence as data
  from
    iepg_data_redux.iepg_data a inner join
    names b on
    a.code=b.iso
  order by code, year
), distinct_names as(
  select distinct
    spanish
  from
    data
  order by spanish
), data1990 as(
  select
    spanish, data
  from 
    data
  where
    year=1990
), data1995 as(
  select
    spanish, data
  from 
    data
  where
    year=1995
), data2000 as(
  select
    spanish, data
  from 
    data
  where
    year=2000
), data2005 as(
  select
    spanish, data
  from 
    data
  where
    year=2005
), data2010 as(
  select
    spanish, data
  from 
    data
  where
    year=2010
), data2011 as(
  select
    spanish, data
  from 
    data
  where
    year=2011
), data2012 as(
  select
    spanish, data
  from 
    data
  where
    year=2012
), data2013 as(
  select
    spanish, data
  from 
    data
  where
    year=2013
)
select
  a.spanish as spanish,
  b.data as d1990,
  c.data as d1995,
  d.data as d2000,
  e.data as d2005,
  f.data as d2010,
  g.data as d2011,
  h.data as d2012,
  i.data as d2013
from
  distinct_names a left join
  data1990 b on
  a.spanish=b.spanish left join
  data1995 c on
  a.spanish=c.spanish left join
  data2000 d on
  a.spanish=d.spanish left join
  data2005 e on
  a.spanish=e.spanish left join
  data2010 f on
  a.spanish=f.spanish left join
  data2011 g on
  a.spanish=g.spanish left join
  data2012 h on
  a.spanish=h.spanish left join
  data2013 i on
  a.spanish=i.spanish
order by spanish;
  


create or replace view iepg_data_redux.vw__military_presence as
with names as(
  select
    a.name as iso,
    b.name as spanish
  from 
    maplex.vw__names a inner join
    maplex.vw__names b on
    a.id_geoentity=b.id_geoentity
    where
      a.id_name_family=1 and 
      b.id_name_family=3
), data as(
  select
    b.spanish, date_part('year', date_in) as year, military_presence as data
  from
    iepg_data_redux.iepg_data a inner join
    names b on
    a.code=b.iso
  order by code, year
), distinct_names as(
  select distinct
    spanish
  from
    data
  order by spanish
), data1990 as(
  select
    spanish, data
  from 
    data
  where
    year=1990
), data1995 as(
  select
    spanish, data
  from 
    data
  where
    year=1995
), data2000 as(
  select
    spanish, data
  from 
    data
  where
    year=2000
), data2005 as(
  select
    spanish, data
  from 
    data
  where
    year=2005
), data2010 as(
  select
    spanish, data
  from 
    data
  where
    year=2010
), data2011 as(
  select
    spanish, data
  from 
    data
  where
    year=2011
), data2012 as(
  select
    spanish, data
  from 
    data
  where
    year=2012
), data2013 as(
  select
    spanish, data
  from 
    data
  where
    year=2013
)
select
  a.spanish as spanish,
  b.data as d1990,
  c.data as d1995,
  d.data as d2000,
  e.data as d2005,
  f.data as d2010,
  g.data as d2011,
  h.data as d2012,
  i.data as d2013
from
  distinct_names a left join
  data1990 b on
  a.spanish=b.spanish left join
  data1995 c on
  a.spanish=c.spanish left join
  data2000 d on
  a.spanish=d.spanish left join
  data2005 e on
  a.spanish=e.spanish left join
  data2010 f on
  a.spanish=f.spanish left join
  data2011 g on
  a.spanish=g.spanish left join
  data2012 h on
  a.spanish=h.spanish left join
  data2013 i on
  a.spanish=i.spanish
order by spanish;
  


create or replace view iepg_data_redux.vw__soft_presence as
with names as(
  select
    a.name as iso,
    b.name as spanish
  from 
    maplex.vw__names a inner join
    maplex.vw__names b on
    a.id_geoentity=b.id_geoentity
    where
      a.id_name_family=1 and 
      b.id_name_family=3
), data as(
  select
    b.spanish, date_part('year', date_in) as year, soft_presence as data
  from
    iepg_data_redux.iepg_data a inner join
    names b on
    a.code=b.iso
  order by code, year
), distinct_names as(
  select distinct
    spanish
  from
    data
  order by spanish
), data1990 as(
  select
    spanish, data
  from 
    data
  where
    year=1990
), data1995 as(
  select
    spanish, data
  from 
    data
  where
    year=1995
), data2000 as(
  select
    spanish, data
  from 
    data
  where
    year=2000
), data2005 as(
  select
    spanish, data
  from 
    data
  where
    year=2005
), data2010 as(
  select
    spanish, data
  from 
    data
  where
    year=2010
), data2011 as(
  select
    spanish, data
  from 
    data
  where
    year=2011
), data2012 as(
  select
    spanish, data
  from 
    data
  where
    year=2012
), data2013 as(
  select
    spanish, data
  from 
    data
  where
    year=2013
)
select
  a.spanish as spanish,
  b.data as d1990,
  c.data as d1995,
  d.data as d2000,
  e.data as d2005,
  f.data as d2010,
  g.data as d2011,
  h.data as d2012,
  i.data as d2013
from
  distinct_names a left join
  data1990 b on
  a.spanish=b.spanish left join
  data1995 c on
  a.spanish=c.spanish left join
  data2000 d on
  a.spanish=d.spanish left join
  data2005 e on
  a.spanish=e.spanish left join
  data2010 f on
  a.spanish=f.spanish left join
  data2011 g on
  a.spanish=g.spanish left join
  data2012 h on
  a.spanish=h.spanish left join
  data2013 i on
  a.spanish=i.spanish
order by spanish;
  


create or replace view iepg_data_redux.vw__iepg as
with names as(
  select
    a.name as iso,
    b.name as spanish
  from 
    maplex.vw__names a inner join
    maplex.vw__names b on
    a.id_geoentity=b.id_geoentity
    where
      a.id_name_family=1 and 
      b.id_name_family=3
), data as(
  select
    b.spanish, date_part('year', date_in) as year, iepg as data
  from
    iepg_data_redux.iepg_data a inner join
    names b on
    a.code=b.iso
  order by code, year
), distinct_names as(
  select distinct
    spanish
  from
    data
  order by spanish
), data1990 as(
  select
    spanish, data
  from 
    data
  where
    year=1990
), data1995 as(
  select
    spanish, data
  from 
    data
  where
    year=1995
), data2000 as(
  select
    spanish, data
  from 
    data
  where
    year=2000
), data2005 as(
  select
    spanish, data
  from 
    data
  where
    year=2005
), data2010 as(
  select
    spanish, data
  from 
    data
  where
    year=2010
), data2011 as(
  select
    spanish, data
  from 
    data
  where
    year=2011
), data2012 as(
  select
    spanish, data
  from 
    data
  where
    year=2012
), data2013 as(
  select
    spanish, data
  from 
    data
  where
    year=2013
)
select
  a.spanish as spanish,
  b.data as d1990,
  c.data as d1995,
  d.data as d2000,
  e.data as d2005,
  f.data as d2010,
  g.data as d2011,
  h.data as d2012,
  i.data as d2013
from
  distinct_names a left join
  data1990 b on
  a.spanish=b.spanish left join
  data1995 c on
  a.spanish=c.spanish left join
  data2000 d on
  a.spanish=d.spanish left join
  data2005 e on
  a.spanish=e.spanish left join
  data2010 f on
  a.spanish=f.spanish left join
  data2011 g on
  a.spanish=g.spanish left join
  data2012 h on
  a.spanish=h.spanish left join
  data2013 i on
  a.spanish=i.spanish
order by spanish;
