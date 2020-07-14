
-- Get countries ids:
---
-- SELECT gn.id_geoentity, n.name
-- FROM maplex.geoentity_name gn
-- INNER JOIN maplex.name n ON gn.id_name=n.id_name
-- WHERE n.name IN ('Bahamas',
 -- 'Afghanistan',
 -- 'Albania',
 -- 'Bahrain',
 -- 'Bosnia and Herzegovina',
 -- 'Cambodia',
 -- 'Georgia',
 -- 'Laos',
 -- 'Madagascar',
 -- 'Nepal',
 -- 'North Macedonia')
-- AND gn.id_name_family=2;
--
-- Get blocks:
--
-- SELECT distinct gn.id_geoentity, n.name
-- FROM maplex.geoentity_name gn
-- INNER JOIN maplex.name n ON gn.id_name=n.id_name
-- INNER JOIN maplex.block mb on gn.id_geoentity=mb.id_geoentity_block
-- WHERE gn.id_name_family=2;


BEGIN;


  INSERT INTO
    maplex.block (id_geoentity_block,id_geoentity_child)
    VALUES (
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name='Maghreb & Middle East' and gn.id_name_family=2
      ),
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name = 'Afghanistan' and gn.id_name_family=2
      )
    );

  INSERT INTO
    maplex.block (id_geoentity_block,id_geoentity_child)
    VALUES (
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name='Europe' and gn.id_name_family=2
      ),
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name = 'Albania' and gn.id_name_family=2
      )
    );

  INSERT INTO
    maplex.block (id_geoentity_block,id_geoentity_child)
    VALUES (
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name='Maghreb & Middle East' and gn.id_name_family=2
      ),
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name = 'Bahrain' and gn.id_name_family=2
      )
    );

  INSERT INTO
    maplex.block (id_geoentity_block,id_geoentity_child)
    VALUES (
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name='Europe' and gn.id_name_family=2
      ),
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name = 'Bosnia and Herzegovina' and gn.id_name_family=2
      )
    );

  INSERT INTO
    maplex.block (id_geoentity_block,id_geoentity_child)
    VALUES (
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name='Asia & Pacific' and gn.id_name_family=2
      ),
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name = 'Cambodia' and gn.id_name_family=2
      )
    );

  INSERT INTO
    maplex.block (id_geoentity_block,id_geoentity_child)
    VALUES (
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name='Europe' and gn.id_name_family=2
      ),
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name = 'Georgia' and gn.id_name_family=2
      )
    );

  INSERT INTO
    maplex.block (id_geoentity_block,id_geoentity_child)
    VALUES (
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name='Asia & Pacific' and gn.id_name_family=2
      ),
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name = 'Laos' and gn.id_name_family=2
      )
    );

  INSERT INTO
    maplex.block (id_geoentity_block,id_geoentity_child)
    VALUES (
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name='Sub-Saharan Africa' and gn.id_name_family=2
      ),
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name = 'Madagascar' and gn.id_name_family=2
      )
    );

  INSERT INTO
    maplex.block (id_geoentity_block,id_geoentity_child)
    VALUES (
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name='Asia & Pacific' and gn.id_name_family=2
      ),
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name = 'Nepal' and gn.id_name_family=2
      )
    );

  INSERT INTO
    maplex.block (id_geoentity_block,id_geoentity_child)
    VALUES (
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name='Europe' and gn.id_name_family=2
      ),
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name = 'North Macedonia' and gn.id_name_family=2
      )
    );

COMMIT;
