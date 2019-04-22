
-- Get countries ids:
---
-- SELECT gn.id_geoentity, n.name
-- FROM maplex.geoentity_name gn
-- INNER JOIN maplex.name n ON gn.id_name=n.id_name
-- WHERE n.name IN ('Bahamas',
 -- 'Burkina Faso',
 -- 'Equatorial Guinea',
 -- 'Gabon',
 -- 'Jamaica',
 -- 'Mali',
 -- 'Mauritius',
 -- 'Mozambique',
 -- 'Namibia',
 -- 'Nicaragua')
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
        where n.name='Latin America' and gn.id_name_family=2
      ),
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name = 'Bahamas' and gn.id_name_family=2
      )
    );

  INSERT INTO
    maplex.block (id_geoentity_block,id_geoentity_child)
    VALUES (
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name='Latin America' and gn.id_name_family=2
      ),
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name = 'Jamaica' and gn.id_name_family=2
      )
    );

  INSERT INTO
    maplex.block (id_geoentity_block,id_geoentity_child)
    VALUES (
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name='Latin America' and gn.id_name_family=2
      ),
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name = 'Nicaragua' and gn.id_name_family=2
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
        where n.name = 'Burkina Faso' and gn.id_name_family=2
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
        where n.name = 'Equatorial Guinea' and gn.id_name_family=2
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
        where n.name = 'Mozambique' and gn.id_name_family=2
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
        where n.name = 'Gabon' and gn.id_name_family=2
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
        where n.name = 'Mali' and gn.id_name_family=2
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
        where n.name = 'Mauritius' and gn.id_name_family=2
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
        where n.name = 'Namibia' and gn.id_name_family=2
      )
    );

COMMIT;
