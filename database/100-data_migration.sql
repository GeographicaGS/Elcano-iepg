ALTER SCHEMA engine RENAME TO engine_deprecated;
ALTER SCHEMA iepg_data RENAME TO iepg_data_deprecated;
ALTER SCHEMA store RENAME TO store_deprecated;
ALTER SCHEMA varengine RENAME TO store_deprecated;

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
