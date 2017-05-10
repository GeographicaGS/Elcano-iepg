
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
        where n.name='Sub-saharan Africa' and gn.id_name_family=2
      ),
      (
        select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
        INNER JOIN maplex.name n ON gn.id_name=n.id_name
        where n.name = 'Ghana' and gn.id_name_family=2
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
        where n.name = 'The Congo' and gn.id_name_family=2
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
        where n.name = E'Côte d\'Ivoire' and gn.id_name_family=2
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
        where n.name = 'Bolivia' and gn.id_name_family=2
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
        where n.name = 'Panama' and gn.id_name_family=2
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
        where n.name = 'Yemen' and gn.id_name_family=2
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
        where n.name = 'Lebanon' and gn.id_name_family=2
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
        where n.name = 'Jordan' and gn.id_name_family=2
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
        where n.name = 'Tunisia' and gn.id_name_family=2
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
        where n.name = 'Serbia' and gn.id_name_family=2
      )
    );
  
COMMIT;