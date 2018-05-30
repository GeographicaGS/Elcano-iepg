
-- Get countries ids:
---
-- SELECT gn.id_geoentity, n.name
-- FROM maplex.geoentity_name gn
-- INNER JOIN maplex.name n ON gn.id_name=n.id_name
-- WHERE n.name IN ('Serbia','The Congo','Bolivia','Tunisia','Lebanon','Panama','Jordan','Yemen','Ghana',E'Côte d\'Ivoire')
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
        where n.name = 'Paraguay' and gn.id_name_family=2
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
        where n.name = 'Trinidad and Tobago' and gn.id_name_family=2
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
        where n.name = 'Honduras' and gn.id_name_family=2
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
        where n.name = 'El Salvador' and gn.id_name_family=2
      )
    );

  INSERT INTO
    maplex.block (id_geoentity_block,id_geoentity_child)
    VALUES (
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name='Sub-saharan Africa' and gn.id_name_family=2
      ),
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name = 'Senegal' and gn.id_name_family=2
      )
    );

  INSERT INTO
    maplex.block (id_geoentity_block,id_geoentity_child)
    VALUES (
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name='Sub-saharan Africa' and gn.id_name_family=2
      ),
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name = 'Botswana' and gn.id_name_family=2
      )
    );

  INSERT INTO
    maplex.block (id_geoentity_block,id_geoentity_child)
    VALUES (
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name='Sub-saharan Africa' and gn.id_name_family=2
      ),
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name = 'Cameroon' and gn.id_name_family=2
      )
    );

  INSERT INTO
    maplex.block (id_geoentity_block,id_geoentity_child)
    VALUES (
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name='Sub-saharan Africa' and gn.id_name_family=2
      ),
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name = 'Uganda' and gn.id_name_family=2
      )
    );

  INSERT INTO
    maplex.block (id_geoentity_block,id_geoentity_child)
    VALUES (
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name='Sub-saharan Africa' and gn.id_name_family=2
      ),
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name = 'Zambia' and gn.id_name_family=2
      )
    );

  INSERT INTO
    maplex.block (id_geoentity_block,id_geoentity_child)
    VALUES (
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name='Sub-saharan Africa' and gn.id_name_family=2
      ),
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name = 'Zimbabwe' and gn.id_name_family=2
      )
    );

COMMIT;
