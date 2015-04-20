ALTER SCHEMA engine RENAME TO engine_deprecated;
ALTER SCHEMA iepg_data RENAME TO iepg_data_deprecated;
ALTER SCHEMA store RENAME TO store_deprecated;
ALTER SCHEMA varengine RENAME TO varengine_deprecated;

ALTER TABLE iepg_data_redux.iepg_individual_contribution RENAME TO iepg_individual_contribution_deprecated;
ALTER TABLE iepg_data_redux.iepe_individual_contribution RENAME TO iepe_individual_contribution_deprecated;

CREATE OR REPLACE FUNCTION clone_schema(source_schema text, dest_schema text) RETURNS void AS
$$
 
DECLARE
  object text;
  buffer text;
  default_ text;
  column_ text;
BEGIN
  EXECUTE 'CREATE SCHEMA ' || dest_schema ;
 
  -- TODO: Find a way to make this sequence's owner is the correct table.
  FOR object IN
    SELECT sequence_name::text FROM information_schema.SEQUENCES WHERE sequence_schema = source_schema
  LOOP
    EXECUTE 'CREATE SEQUENCE ' || dest_schema || '.' || object;
  END LOOP;
 
  FOR object IN
    SELECT table_name::text FROM information_schema.TABLES WHERE table_schema = source_schema
  LOOP
    buffer := dest_schema || '.' || object;
    EXECUTE 'CREATE TABLE ' || buffer || ' (LIKE ' || source_schema || '.' || object || ' INCLUDING CONSTRAINTS INCLUDING INDEXES INCLUDING DEFAULTS)';
 
    FOR column_, default_ IN
      SELECT column_name::text, REPLACE(column_default::text, source_schema, dest_schema) FROM information_schema.COLUMNS WHERE table_schema = dest_schema AND table_name = object AND column_default LIKE 'nextval(%' || source_schema || '%::regclass)'
    LOOP
      EXECUTE 'ALTER TABLE ' || buffer || ' ALTER COLUMN ' || column_ || ' SET DEFAULT ' || default_;
    END LOOP;

    EXECUTE 'INSERT INTO ' || buffer || '(SELECT * FROM ' || source_schema || '.' || object || ')';

  END LOOP;
 
END;
 
$$ LANGUAGE plpgsql VOLATILE;


CREATE TABLE iepg_data_redux.master_country
(
  id_master_country character varying(10) NOT NULL,
  cod_unstats_num character(3),
  cod_unstats_alpha character(3),
  cod_eurostat character(2),
  full_name_en_order character varying(500),
  full_name_es_order character varying(500),
  full_name_en character varying(500),
  full_name_es character varying(500),
  short_name_en_order character varying(500),
  short_name_es_order character varying(500),
  short_name_en1 character varying(500),
  short_name_en2 character varying(500),
  short_name_es1 character varying(500),
  short_name_es2 character varying(500),
  capital character varying(500),
  iso_4217_currency_code character varying(3),
  iso_4217_currency_name character varying(25),
  itu_t_telephone_code character varying(50),
  iso_3166_1_2_code character varying(2),
  iso_3166_1_3_code character varying(3),
  iso_3166_1_number character varying(5),
  iana_country_code_tld character varying(25),
  date_in date,
  date_out date,
  country boolean,
  geom geometry,
  CONSTRAINT master_country_pkey PRIMARY KEY (id_master_country),
  CONSTRAINT master_country_unique_cod_eurostat UNIQUE (cod_eurostat),
  CONSTRAINT master_country_unique_cod_unstats_alpha UNIQUE (cod_unstats_alpha),
  CONSTRAINT master_country_unique_cod_unstats_num UNIQUE (cod_unstats_num),
  CONSTRAINT enforce_dims_geom CHECK (st_ndims(geom) = 2),
  CONSTRAINT enforce_geotype_geom CHECK (geometrytype(geom) = 'MULTIPOLYGON'::text OR geom IS NULL),
  CONSTRAINT enforce_srid_geom CHECK (st_srid(geom) = 4326)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE iepg_data_redux.master_country
  OWNER TO elcano_iepg_admin;

INSERT INTO iepg_data_redux.master_country SELECT * FROM iepg_data_deprecated.master_country;

UPDATE iepg_data_redux.master_country set full_name_es='México' WHERE full_name_es='Méjico';
UPDATE iepg_data_redux.master_country set full_name_es_order='México' WHERE full_name_es_order='Méjico';
UPDATE iepg_data_redux.master_country set short_name_es1='México' WHERE short_name_es1='Méjico';
UPDATE iepg_data_redux.master_country set short_name_es2='México' WHERE short_name_es2='Méjico';
UPDATE iepg_data_redux.master_country set short_name_es_order='México' WHERE short_name_es_order='Méjico';

UPDATE iepg_data_redux.master_country set full_name_es='Venezuela' WHERE full_name_es='Venezuela ';
UPDATE iepg_data_redux.master_country set full_name_es_order='Venezuela' WHERE full_name_es_order='Venezuela ';
UPDATE iepg_data_redux.master_country set short_name_es1='Venezuela' WHERE short_name_es1='Venezuela ';
UPDATE iepg_data_redux.master_country set short_name_es2='Venezuela' WHERE short_name_es2='Venezuela ';
UPDATE iepg_data_redux.master_country set short_name_es_order='Venezuela' WHERE short_name_es_order='Venezuela ';


UPDATE iepg_data_redux.master_country set full_name_es='Vietnam' WHERE full_name_es='Viet Nam';
UPDATE iepg_data_redux.master_country set full_name_es_order='Vietnam' WHERE full_name_es_order='Viet Nam';
UPDATE iepg_data_redux.master_country set short_name_es1='Vietnam' WHERE short_name_es1='Viet Nam';
UPDATE iepg_data_redux.master_country set short_name_es2='Vietnam' WHERE short_name_es2='Viet Nam';
UPDATE iepg_data_redux.master_country set short_name_es_order='Vietnam' WHERE short_name_es_order='Viet Nam';
--select to_char(now(),'YYYYMMDD_HHMMSS');
--select clone_schema('iepg_data_redux','iepg_data_redux_'||to_char(now(),'YYYYMMDD_HHMMSS'));


---2014 blocks update

---
-- Asia & Pacific
---

-- Sri Lanka
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Asia & Pacific' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Sri Lanka' and gn.id_name_family=2));

---
-- Europe
---
-- Azerbajan
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Europe' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Azerbaijan' and gn.id_name_family=2));

---
-- Belarus
---
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Europe' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Belarus' and gn.id_name_family=2));

---
-- Latin america
---

--Cuba
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Latin America' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Cuba' and gn.id_name_family=2));

-- Ecuador
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Latin America' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Ecuador' and gn.id_name_family=2));


---
-- Magreb & Middle East
---
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Magreb & Middle East' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Libya' and gn.id_name_family=2));

INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Magreb & Middle East' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Oman' and gn.id_name_family=2));


INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Magreb & Middle East' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Morocco' and gn.id_name_family=2));

INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Magreb & Middle East' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Syrian' and gn.id_name_family=2));

---
-- Subsaharian Africa
---
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Subsaharian Africa' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Sudan' and gn.id_name_family=2));

---
-- Population 2014
---
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('DZ','2014-01-01','2014-12-31',210180000000.000000,9350000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('AO','2014-01-01','2014-12-31',124180000000.000000,21470000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('AR','2014-01-01','2014-12-31',609890000000.000000,41450000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('AU','2014-01-01','2014-12-31',1560370000000.000000,23130000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('AT','2014-01-01','2014-12-31',428320000000.000000,8470000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('AZ','2014-01-01','2014-12-31',73560000000.000000,9420000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('BD','2014-01-01','2014-12-31',149990000000.000000,156590000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('BY','2014-01-01','2014-12-31',71710000000.000000,9470000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('BE','2014-01-01','2014-12-31',524809999999.999939,11200000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('BR','2014-01-01','2014-12-31',2245670000000.000000,200360000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('BG','2014-01-01','2014-12-31',54480000000.000000,7270000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('CA','2014-01-01','2014-12-31',1826770000000.000000,316130000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('CL','2014-01-01','2014-12-31',277200000000.000000,17620000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('CN','2014-01-01','2014-12-31',9240270000000.000000,1357380000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('CO','2014-01-01','2014-12-31',378420000000.000000,48320000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('HR','2014-01-01','2014-12-31',57870000000.000000,4250000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('CU','2014-01-01','2014-12-31',68230000000.000008,11270000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('CY','2014-01-01','2014-12-31',21910000000.000000,1140000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('CZ','2014-01-01','2014-12-31',208800000000.000000,10520000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('DK','2014-01-01','2014-12-31',335880000000.000000,5610000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('EC','2014-01-01','2014-12-31',94470000000.000000,15740000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('EG','2014-01-01','2014-12-31',271970000000.000031,39210000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('EE','2014-01-01','2014-12-31',24880000000.000000,1320000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('FI','2014-01-01','2014-12-31',267329999999.999969,5440000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('FR','2014-01-01','2014-12-31',2806430000000.000000,66030000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('DE','2014-01-01','2014-12-31',3730260000000.000000,80620000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('GR','2014-01-01','2014-12-31',242230000000.000000,11030000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('HU','2014-01-01','2014-12-31',133419999999.999985,9900000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('IS','2014-01-01','2014-12-31',15330000000.000000,320000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('IN','2014-01-01','2014-12-31',1876800000000.000000,1252140000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('ID','2014-01-01','2014-12-31',868350000000.000000,249870000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('IR','2014-01-01','2014-12-31',368900000000.000000,82060000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('IQ','2014-01-01','2014-12-31',229330000000.000000,77450000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('IE','2014-01-01','2014-12-31',232080000000.000000,4600000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('IL','2014-01-01','2014-12-31',290550000000.000000,33420000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('IT','2014-01-01','2014-12-31',2149480000000.000000,59830000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('JP','2014-01-01','2014-12-31',4919560000000.000000,127340000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('KZ','2014-01-01','2014-12-31',231880000000.000000,17040000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('KR','2014-01-01','2014-12-31',1304550000000.000000,50220000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('KW','2014-01-01','2014-12-31',175830000000.000000,8060000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('LV','2014-01-01','2014-12-31',30960000000.000000,2010000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('LY','2014-01-01','2014-12-31',74200000000.000000,3370000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('LT','2014-01-01','2014-12-31',45930000000.000000,2960000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('LU','2014-01-01','2014-12-31',60130000000.000000,540000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('MY','2014-01-01','2014-12-31',313160000000.000000,29720000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('MT','2014-01-01','2014-12-31',9640000000.000000,420000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('MX','2014-01-01','2014-12-31',1260910000000.000000,122330000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('MA','2014-01-01','2014-12-31',103840000000.000000,6200000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('NL','2014-01-01','2014-12-31',853540000000.000000,16800000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('NZ','2014-01-01','2014-12-31',185790000000.000000,4470000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('NG','2014-01-01','2014-12-31',521799999999.999939,173620000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('NO','2014-01-01','2014-12-31',512580000000.000061,5080000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('PK','2014-01-01','2014-12-31',232290000000.000000,3630000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('PE','2014-01-01','2014-12-31',202350000000.000000,182140000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('PH','2014-01-01','2014-12-31',272070000000.000000,30380000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('PL','2014-01-01','2014-12-31',525870000000.000000,98390000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('PT','2014-01-01','2014-12-31',227320000000.000000,38530000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('QA','2014-01-01','2014-12-31',203240000000.000000,10460000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('RO','2014-01-01','2014-12-31',189640000000.000000,33010000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('RU','2014-01-01','2014-12-31',2096780000000.000244,19960000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('SA','2014-01-01','2014-12-31',748450000000.000000,143500000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('OM','2014-01-01','2014-12-31',79660000000.000000,2170000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('SG','2014-01-01','2014-12-31',297940000000.000000,5400000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('SK','2014-01-01','2014-12-31',97710000000.000000,5410000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('SI','2014-01-01','2014-12-31',47990000000.000000,2060000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('ZA','2014-01-01','2014-12-31',350630000000.000000,37960000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('ES','2014-01-01','2014-12-31',1393040000000.000000,46650000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('LK','2014-01-01','2014-12-31',67180000000.000008,20480000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('SD','2014-01-01','2014-12-31',66569999999.999992,52980000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('SE','2014-01-01','2014-12-31',579680000000.000000,9590000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('CH','2014-01-01','2014-12-31',685430000000.000000,8080000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('SY','2014-01-01','2014-12-31',40410000000.000000,28830000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('TH','2014-01-01','2014-12-31',387250000000.000000,67010000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('TR','2014-01-01','2014-12-31',822140000000.000000,74930000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('UA','2014-01-01','2014-12-31',177430000000.000000,45490000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('AE','2014-01-01','2014-12-31',402340000000.000000,22850000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('GB','2014-01-01','2014-12-31',2678450000000.000000,64100000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('US','2014-01-01','2014-12-31',16768099999999.998047,35160000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('VE','2014-01-01','2014-12-31',438280000000.000000,30410000.000000);

---
-- New countries 2014
---
DELETE FROM iepg_data_redux.pob_pib WHERE code='AZ';
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('AZ','1990-01-01','1990-12-31',7160000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('AZ','1995-01-01','1995-12-31',7690000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('AZ','2000-01-01','2000-12-31',8050000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('AZ','2005-01-01','2005-12-31',8390000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('AZ','2010-01-01','2010-12-31',8950000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('AZ','2011-01-01','2011-12-31',9050000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('AZ','2012-01-01','2012-12-31',9170000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('AZ','2013-01-01','2013-12-31',9300000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('AZ','2014-01-01','2014-12-31',9420000.000000);
DELETE FROM iepg_data_redux.pob_pib WHERE code='BY';
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('BY','1990-01-01','1990-12-31',10190000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('BY','1995-01-01','1995-12-31',10190000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('BY','2000-01-01','2000-12-31',10010000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('BY','2005-01-01','2005-12-31',9660000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('BY','2010-01-01','2010-12-31',9510000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('BY','2011-01-01','2011-12-31',9490000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('BY','2012-01-01','2012-12-31',9470000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('BY','2013-01-01','2013-12-31',9460000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('BY','2014-01-01','2014-12-31',9470000.000000);
DELETE FROM iepg_data_redux.pob_pib WHERE code='CU';
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('CU','1990-01-01','1990-12-31',10600000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('CU','1995-01-01','1995-12-31',10930000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('CU','2000-01-01','2000-12-31',11140000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('CU','2005-01-01','2005-12-31',11290000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('CU','2010-01-01','2010-12-31',11290000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('CU','2011-01-01','2011-12-31',11280000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('CU','2012-01-01','2012-12-31',11280000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('CU','2013-01-01','2013-12-31',11270000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('CU','2014-01-01','2014-12-31',11270000.000000);
DELETE FROM iepg_data_redux.pob_pib WHERE code='EC';
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('EC','1990-01-01','1990-12-31',10120000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('EC','1995-01-01','1995-12-31',11320000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('EC','2000-01-01','2000-12-31',12530000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('EC','2005-01-01','2005-12-31',13780000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('EC','2010-01-01','2010-12-31',14760000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('EC','2011-01-01','2011-12-31',15000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('EC','2012-01-01','2012-12-31',15250000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('EC','2013-01-01','2013-12-31',15490000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('EC','2014-01-01','2014-12-31',15740000.000000);
DELETE FROM iepg_data_redux.pob_pib WHERE code='LY';
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('LY','1990-01-01','1990-12-31',4260000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('LY','1995-01-01','1995-12-31',4750000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('LY','2000-01-01','2000-12-31',5180000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('LY','2005-01-01','2005-12-31',5590000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('LY','2010-01-01','2010-12-31',5960000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('LY','2011-01-01','2011-12-31',6040000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('LY','2012-01-01','2012-12-31',6100000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('LY','2013-01-01','2013-12-31',6150000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('LY','2014-01-01','2014-12-31',6200000.000000);
DELETE FROM iepg_data_redux.pob_pib WHERE code='LK';
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('LK','1990-01-01','1990-12-31',17020000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('LK','1995-01-01','1995-12-31',18140000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('LK','2000-01-01','2000-12-31',19100000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('LK','2005-01-01','2005-12-31',19640000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('LK','2010-01-01','2010-12-31',20450000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('LK','2011-01-01','2011-12-31',20650000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('LK','2012-01-01','2012-12-31',20870000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('LK','2013-01-01','2013-12-31',20330000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('LK','2014-01-01','2014-12-31',20480000.000000);
DELETE FROM iepg_data_redux.pob_pib WHERE code='MA';
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('MA','1990-01-01','1990-12-31',24670000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('MA','1995-01-01','1995-12-31',26830000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('MA','2000-01-01','2000-12-31',28710000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('MA','2005-01-01','2005-12-31',30130000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('MA','2010-01-01','2010-12-31',31280000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('MA','2011-01-01','2011-12-31',31640000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('MA','2012-01-01','2012-12-31',32060000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('MA','2013-01-01','2013-12-31',32520000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('MA','2014-01-01','2014-12-31',33010000.000000);
DELETE FROM iepg_data_redux.pob_pib WHERE code='OM';
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('OM','1990-01-01','1990-12-31',1810000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('OM','1995-01-01','1995-12-31',2150000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('OM','2000-01-01','2000-12-31',2190000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('OM','2005-01-01','2005-12-31',2520000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('OM','2010-01-01','2010-12-31',2660000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('OM','2011-01-01','2011-12-31',2800000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('OM','2012-01-01','2012-12-31',3020000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('OM','2013-01-01','2013-12-31',3310000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('OM','2014-01-01','2014-12-31',3630000.000000);
DELETE FROM iepg_data_redux.pob_pib WHERE code='SD';
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('SD','1990-01-01','1990-12-31',20010000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('SD','1995-01-01','1995-12-31',24530000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('SD','2000-01-01','2000-12-31',27730000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('SD','2005-01-01','2005-12-31',31590000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('SD','2010-01-01','2010-12-31',34850000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('SD','2011-01-01','2011-12-31',35650000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('SD','2012-01-01','2012-12-31',36430000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('SD','2013-01-01','2013-12-31',37200000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('SD','2014-01-01','2014-12-31',37960000.000000);
DELETE FROM iepg_data_redux.pob_pib WHERE code='SY';
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('SY','1990-01-01','1990-12-31',12450000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('SY','1995-01-01','1995-12-31',14340000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('SY','2000-01-01','2000-12-31',16370000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('SY','2005-01-01','2005-12-31',18170000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('SY','2010-01-01','2010-12-31',21030000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('SY','2011-01-01','2011-12-31',21530000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('SY','2012-01-01','2012-12-31',21960000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('SY','2013-01-01','2013-12-31',22400000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population) VALUES ('SY','2014-01-01','2014-12-31',22850000.000000);
DELETE FROM iepg_data_redux.pob_pib WHERE code='AZ';
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('AZ','1990-01-01','1990-12-31',8860000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('AZ','1995-01-01','1995-12-31',3050000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('AZ','2000-01-01','2000-12-31',5270000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('AZ','2005-01-01','2005-12-31',13250000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('AZ','2010-01-01','2010-12-31',44290000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('AZ','2011-01-01','2011-12-31',52900000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('AZ','2012-01-01','2012-12-31',65950000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('AZ','2013-01-01','2013-12-31',68730000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('AZ','2014-01-01','2014-12-31',73560000000.000000);
DELETE FROM iepg_data_redux.pob_pib WHERE code='BY';
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('BY','1990-01-01','1990-12-31',17370000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('BY','1995-01-01','1995-12-31',13970000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('BY','2000-01-01','2000-12-31',12740000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('BY','2005-01-01','2005-12-31',30210000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('BY','2010-01-01','2010-12-31',49210000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('BY','2011-01-01','2011-12-31',55220000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('BY','2012-01-01','2012-12-31',59730000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('BY','2013-01-01','2013-12-31',63620000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('BY','2014-01-01','2014-12-31',71710000000.000000);
DELETE FROM iepg_data_redux.pob_pib WHERE code='CU';
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('CU','1990-01-01','1990-12-31',28650000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('CU','1995-01-01','1995-12-31',30430000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('CU','2000-01-01','2000-12-31',30570000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('CU','2005-01-01','2005-12-31',42640000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('CU','2010-01-01','2010-12-31',62080000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('CU','2011-01-01','2011-12-31',64330000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('CU','2012-01-01','2012-12-31',68230000000.000008);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('CU','2013-01-01','2013-12-31',68230000000.000008);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('CU','2014-01-01','2014-12-31',68230000000.000008);
DELETE FROM iepg_data_redux.pob_pib WHERE code='EC';
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('EC','1990-01-01','1990-12-31',15240000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('EC','1995-01-01','1995-12-31',24430000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('EC','2000-01-01','2000-12-31',18330000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('EC','2005-01-01','2005-12-31',41510000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('EC','2010-01-01','2010-12-31',62520000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('EC','2011-01-01','2011-12-31',69560000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('EC','2012-01-01','2012-12-31',79280000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('EC','2013-01-01','2013-12-31',87620000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('EC','2014-01-01','2014-12-31',94470000000.000000);
DELETE FROM iepg_data_redux.pob_pib WHERE code='LY';
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('LY','1990-01-01','1990-12-31',28900000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('LY','1995-01-01','1995-12-31',25540000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('LY','2000-01-01','2000-12-31',33900000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('LY','2005-01-01','2005-12-31',44000000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('LY','2010-01-01','2010-12-31',62360000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('LY','2011-01-01','2011-12-31',74760000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('LY','2012-01-01','2012-12-31',34700000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('LY','2013-01-01','2013-12-31',81870000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('LY','2014-01-01','2014-12-31',74200000000.000000);
DELETE FROM iepg_data_redux.pob_pib WHERE code='LK';
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('LK','1990-01-01','1990-12-31',8029999999.999999);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('LK','1995-01-01','1995-12-31',13030000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('LK','2000-01-01','2000-12-31',16329999999.999998);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('LK','2005-01-01','2005-12-31',24410000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('LK','2010-01-01','2010-12-31',42070000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('LK','2011-01-01','2011-12-31',49570000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('LK','2012-01-01','2012-12-31',59180000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('LK','2013-01-01','2013-12-31',59390000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('LK','2014-01-01','2014-12-31',67180000000.000008);
DELETE FROM iepg_data_redux.pob_pib WHERE code='MA';
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('MA','1990-01-01','1990-12-31',28840000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('MA','1995-01-01','1995-12-31',37180000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('MA','2000-01-01','2000-12-31',37020000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('MA','2005-01-01','2005-12-31',59520000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('MA','2010-01-01','2010-12-31',90910000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('MA','2011-01-01','2011-12-31',90770000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('MA','2012-01-01','2012-12-31',99210000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('MA','2013-01-01','2013-12-31',95900000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('MA','2014-01-01','2014-12-31',103840000000.000000);
DELETE FROM iepg_data_redux.pob_pib WHERE code='OM';
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('OM','1990-01-01','1990-12-31',11690000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('OM','1995-01-01','1995-12-31',13800000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('OM','2000-01-01','2000-12-31',19510000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('OM','2005-01-01','2005-12-31',31080000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('OM','2010-01-01','2010-12-31',48390000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('OM','2011-01-01','2011-12-31',58640000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('OM','2012-01-01','2012-12-31',69520000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('OM','2013-01-01','2013-12-31',77500000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('OM','2014-01-01','2014-12-31',79660000000.000000);
DELETE FROM iepg_data_redux.pob_pib WHERE code='SD';
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('SD','1990-01-01','1990-12-31',12410000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('SD','1995-01-01','1995-12-31',13830000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('SD','2000-01-01','2000-12-31',12260000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('SD','2005-01-01','2005-12-31',26520000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('SD','2010-01-01','2010-12-31',53150000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('SD','2011-01-01','2011-12-31',65629999999.999992);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('SD','2012-01-01','2012-12-31',67319999999.999992);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('SD','2013-01-01','2013-12-31',63150000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('SD','2014-01-01','2014-12-31',66569999999.999992);
DELETE FROM iepg_data_redux.pob_pib WHERE code='SY';
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('SY','1990-01-01','1990-12-31',12310000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('SY','1995-01-01','1995-12-31',11400000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('SY','2000-01-01','2000-12-31',19330000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('SY','2005-01-01','2005-12-31',28860000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('SY','2010-01-01','2010-12-31',40410000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('SY','2011-01-01','2011-12-31',40410000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('SY','2012-01-01','2012-12-31',40410000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('SY','2013-01-01','2013-12-31',40410000000.000000);
INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib) VALUES ('SY','2014-01-01','2014-12-31',40410000000.000000);

-- Update countries short name
update iepg_data_redux.master_country set short_name_es_order='Reino Unido',short_name_en_order='United Kingdom'  WHERE iso_3166_1_2_code='GB';
update iepg_data_redux.master_country set short_name_es_order='EE. UU.'  WHERE iso_3166_1_2_code='US';
update iepg_data_redux.master_country set short_name_es_order='Rep. Checa'  WHERE iso_3166_1_2_code='CZ';
update iepg_data_redux.master_country set short_name_es_order='EAU',short_name_en_order='UAE' WHERE iso_3166_1_2_code='AE';


-- Languages changes

UPDATE www.translation 
    SET en='Elcano Global Presence Index studies the global presence of a selection of 80 countries: the first 75 world economies according to World Bank data (nations with the highest GDP in current US dollars) as well as countries that are smaller in their economic size but are members of the Organisation for Economic Cooperation and Development (OECD) and/or the European Union',
        es='El Índice Elcano de presencia global cubre una selección de 80 países. Éstos son las primeras 75 economías mundiales según datos del Banco Mundial (países con mayor PIB en dólares corrientes), además de los países con menor tamaño económico miembros de la Organización para la Cooperación y el Desarrollo Económico (OCDE) y/o de la Unión Europea' 
WHERE key='_methodology p1';

UPDATE www.translation
    SET en='We should note that by making calculations at time intervals that go back to 1990, the intention of the project is to show the ‘two-bloc world’, even if in decline. Thus, Russia’s 1990 values refer to those of the Soviet Union, those of Germany to the German Federal Republic. Moreover, East European countries that became independent after 1990 have no value assigned in that year. This is the case for Azerbaijan, Belarus, Estonia, Latvia, Lithuania, Kazakhstan, and Ukraine as part of the Soviet Union, Slovakia as part of Czechoslovakia, and Croatia and Slovenia as part of Yugoslavia',
        es='En relación a la selección de países, hay que tener en cuenta que al calcularse calas temporales que se remontan a 1990, la intención del proyecto es la de mostrar el ‘mundo de los dos bloques’ –aunque sea en su ocaso–. De este modo, los valores de 1990 de Rusia se refieren, evidentemente, a los de la Unión Soviética, los de Alemania a la República Federal Alemana. Además, los países de Europa del Este que alcanzaron su independencia tras 1990 no tienen valor asignado para ese año. Es el caso de Azerbaiyán, Bielorrusia, Estonia, Letonia, Lituania, Kazajistán y Ucrania como parte de la Unión Soviética, de Eslovaquia como parte de Checoslovaquia y de Croacia y Eslovenia como parte de Yugoslavia'
    WHERE key='_methodology países p';

UPDATE www.translation
    SET en='In such cases we have also referred to experts’ opinions, or hot deck. In this 2014 edition, 1,393 cases have been estimated. Thus the proportion of missing and estimated cases represents only 4.9% of a database of more than 28,000 observations',
        es='En este punto, también se ha recurrido al criterio del experto (o hot deck). En la edición 2014, 1.393 datos han sido estimados. Así, nos encontramos con una proporción de casos perdidos y estimados de tan sólo el 4,9% para la base total de más de 28.000 observaciones'
   WHERE key='_faq text 9';

UPDATE www.translation
    SET en='The Elcano Global Presence Index is calculated for 80 countries: the first 75 world economies, the member countries of the Organisation for Economic Co-operation and Development (OECD), and the member states of the European Union',
        es='El Índice Elcano de Presencia Global se calcula para 80 países: las primeras 75 economías mundiales, los países miembros de la OCDE y los de la Unión Europea'
   WHERE key='_faq text 12';

UPDATE www.translation
    SET en='Not exactly. Presence of different countries can be combined, showing regional trends of global presence. Moreover, as new editions include an increasing number of countries, for some regions (i.e. Latin America or East Asia) the number of countries selected for the Index is high enough to consider the aggregated index value as a fair reflection of the external projection of the whole region. <br/> However, it is important to note that, in these cases, the total index value is recording the relative presence of some countries in others of the same group or region (i.e. the global presence index value of Latin America includes the relative presence of Argentina in Brazil). Thus, the adding together of global presences should not be considered a metric of a given region’s external projection outside its bou',
        es='No exactamente. La presencia de distintos países puede sumarse, mostrando tendencias regionales de presencia global. Además, a medida que nuevas ediciones van incorporando un número creciente de países, para algunas regiones (como América Latina o Asia), el número de éstos incluidos en el índice es suficientemente grande como para considerar que su valor agregado es un buen reflejo de la proyección combinada del conjunto de la región. <br/>No obstante, también es importante señalar que, en estos casos, el valor total del índice está recogiendo la presencia relativa de unos países en otros del mismo grupo o región (siguiendo el ejemplo anterior, el valor de la presencia agregada de América Latina estaría incluyendo la presencia relativa de Argentina en Brasil). Siendo así, la presencia global total no debería ser considerada como la proyección de una región fuera de sus fronteras'
   WHERE key='_faq text 13';

update iepg_data_redux.master_country 
    set short_name_es_order='Vietnam',
        short_name_en_order='Vietnam',
        short_name_en1='Vietnam',
        full_name_en='Vietnam',
        full_name_en_order='Vietnam',
  WHERE iso_3166_1_2_code='VN';

update iepg_data_redux.master_country 
    set 
        short_name_en1='Syria'        
  WHERE iso_3166_1_2_code='SY';

update maplex.name
    set name='Syria'
    where name='Syrian';

UPDATE www.translation
    set en='The <a class=\"nostyle\" href=\"%s\"><strong>Elcano Global Presence Index</strong></a> is an annual measurement of the projection in the world of 80 countries based on three dimensions:',
        es='El <a class=\"nostyle\" href=\"%s\"><strong>Índice Elcano de Presencia Global</strong></a> calcula anualmente la proyección de 80 países fuera de sus fronteras en función de tres dimensiones:'
    WHERE
    key='_home IEPG explora desc';
