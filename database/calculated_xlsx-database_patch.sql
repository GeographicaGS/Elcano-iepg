alter table iepg_data_redux.master_country add column xlsx_column_name varchar(150);

alter table iepg_data_redux.master_country alter column iso_3166_1_2_code type varchar(4);

update iepg_data_redux.master_country set xlsx_column_name=full_name_en_order;

update iepg_data_redux.master_country set xlsx_column_name='Viet Nam'
where trim(short_name_en_order)='Vietnam';

update iepg_data_redux.master_country set xlsx_column_name='United Republic of Tanzania'
where trim(short_name_en_order)='Tanzania';

update iepg_data_redux.master_country set xlsx_column_name='United Kingdom'
where trim(short_name_en_order)='United Kingdom';

update iepg_data_redux.master_country set xlsx_column_name='Syria'
where trim(short_name_en_order)='Syria';

update iepg_data_redux.master_country set xlsx_column_name='Korea'
where trim(short_name_en_order)='South Korea';

insert into iepg_data_redux.master_country(
  id_master_country, short_name_en_order, iso_3166_1_2_code, xlsx_column_name)
values ('un999', 'European Union', 'XBEU', 'European Union');
