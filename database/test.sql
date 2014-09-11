create view trash.names as
select
  a.name as aname,
  b.name as bname,
  c.name as cname,
  d.name as dname
from
  maplex.vw__names a inner join
  maplex.vw__names b on 
  a.id_geoentity=b.id_geoentity inner join
  maplex.vw__names c on
  a.id_geoentity=c.id_geoentity inner join
  maplex.vw__names d on
  a.id_geoentity=d.id_geoentity
where
  a.id_name_family=3 and 
  b.id_name_family=5 and
  c.id_name_family=2 and
  d.id_name_family=3 and
  b.name::integer in (012,024,032,036,040,050,056,076,100,124,152,156,170,191,196,203,208,233,246,250,276,300,348,352,
                      356,360,364,368,372,376,380,392,398,410,414,428,440,442,458,470,484,528,554,566,578,586,604,608,
                      616,620,634,642,643,682,702,703,704,705,710,724,752,756,764,784,792,804,818,826,840,862)

order by
  bname
;
