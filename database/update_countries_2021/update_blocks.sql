
-- -- Get countries ids:
-- ---
-- SELECT gn.id_geoentity, n.name
-- FROM maplex.geoentity_name gn
-- INNER JOIN maplex.name n ON gn.id_name=n.id_name
-- WHERE n.name IN ('Papua New Guinea',
--  'Benin',
--  'Mongolia',
--  'Armenia',
--  'Guinea',
--  'Brunei',
--  'Niger',
--  'Moldova',
--  'Chad',
--  'Congo DR')
-- AND gn.id_name_family=2;
-- --
-- -- Get blocks:
-- --
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
        where n.name='Europe' and gn.id_name_family=2
      ),
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name = 'Armenia' and gn.id_name_family=2
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
        where n.name = 'Moldova' and gn.id_name_family=2
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
        where n.name = 'Papua New Guinea' and gn.id_name_family=2
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
        where n.name = 'Mongolia' and gn.id_name_family=2
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
        where n.name = 'Brunei' and gn.id_name_family=2
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
        where n.name = 'Niger' and gn.id_name_family=2
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
        where n.name = 'Benin' and gn.id_name_family=2
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
        where n.name = 'Guinea' and gn.id_name_family=2
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
        where n.name = 'Chad' and gn.id_name_family=2
      )
    );

  -- INSERT INTO
  --   maplex.block (id_geoentity_block,id_geoentity_child)
  --   VALUES (
  --     (
  --       select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
  --       INNER JOIN maplex.name n ON gn.id_name=n.id_name
  --       where n.name='Sub-Saharan Africa' and gn.id_name_family=2
  --     ),
  --     (
  --       select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
  --       INNER JOIN maplex.name n ON gn.id_name=n.id_name
  --       where n.name = 'Congo DR' and gn.id_name_family=2
  --     )
  --   );

COMMIT;
