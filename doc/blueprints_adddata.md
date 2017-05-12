# Blueprints to add a new new year

Instructions to follow to add a new year

#Backend

## Countries at iepg_data_redux.master_country.
Check that all the countries who come from the input of the data engine (XLSX) are at the table iepg_data_redux.master_country. The mapping field between the xlsx and this table is short_name_es. If an error happens, flux throws an exception.


## Edit common.const.py
To know what we should change you can search the pattern @@@YEARS, it gives you an idea which parts do you need to change. 

###Variable years. 
Add the new year. EG: 2014.
```
years = [1990, 1995, 2000, 2005, 2010, 2011, 2012, 2013,2014]
```

###Blocks

#### Database: Add new countries to blocks

List all blocks:
```
SELECT distinct gn.id_geoentity, n.name
FROM maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
INNER JOIN maplex.block mb on gn.id_geoentity=mb.id_geoentity_block
WHERE gn.id_name_family=2;
```

INSERT INTO maplex.block the new members of the block.

EG: for 2014 we need to add Sri Lanka (CODE LK) to Asia & Pacific (XBAP). We need to found the geonetity id of this two geoentities.
XBAP
```
select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Asia & Pacific' and gn.id_name_family=2;
 ```
 LK
```
select gn.id_geoentity as id_geoentity_lk from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Sri Lanka' and gn.id_name_family=2;
 ```

 Query to execute (all together): 
 ```
 INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Asia & Pacific' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Sri Lanka' and gn.id_name_family=2))
```

###Countries data

#### Add PIB/population for new year
Data needs to be inserted at table iepg_data_redux.pob_pib. For more info check: database/scripts/popgdp_newyear.py

#### New countries
Insert the new PIB and the new population for the new countries. For more info check: database/scripts/popgdp_newcountries_newyear.py

#Frontend

- Update the blocks.json with the content of the service /api/blocks
- Update countries.geojson with the content of the service /api/mapgeojson
- Add new year to src/explora/config.js and src/frontend/config.js



    


