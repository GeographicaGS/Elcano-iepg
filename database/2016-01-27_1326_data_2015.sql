-- Costa Rica
 INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Latin America' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Costa Rica' and gn.id_name_family=2));

-- Dominican Republic
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Latin America' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Dominican Republic' and gn.id_name_family=2));

-- Guatemala
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Latin America' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Guatemala' and gn.id_name_family=2));

-- Uruguay
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Latin America' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Uruguay' and gn.id_name_family=2));

-- Ethiopia
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Subsaharian Africa' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Ethiopia' and gn.id_name_family=2));

-- Kenya
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Subsaharian Africa' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Kenya' and gn.id_name_family=2));

-- Tanzania
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Subsaharian Africa' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Tanzania' and gn.id_name_family=2));

-- Uzbekistan
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Asia & Pacific' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Uzbekistan' and gn.id_name_family=2));

-- Turkmenistan
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Asia & Pacific' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Turkmenistan' and gn.id_name_family=2));

--Myanmar
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Asia & Pacific' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Myanmar' and gn.id_name_family=2));


update maplex.name set name='Uruguay' where name='Uriguay';
Update short_name_es_order='Uruguay',short_name_es1='Uruguay' from iepg_data_redux.master_country where short_name_es_order='Uriguay';

-- Move Kazakhstan to Europe
update maplex.block set id_geoentity_block=(select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Asia & Pacific' and gn.id_name_family=2)

WHERE 
id_geoentity_block=(select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
  INNER JOIN maplex.name n ON gn.id_name=n.id_name
   where n.name='Europe' and gn.id_name_family=2)

and 
id_geoentity_child=(select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
  INNER JOIN maplex.name n ON gn.id_name=n.id_name
   where n.name='Kazakhstan' and gn.id_name_family=2);

