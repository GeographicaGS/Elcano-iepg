#!/bin/bash

mkdir -p excels_export

# Views to export
VIEWS=('iepg_data_redux.vw__iepe_cooperation' 'iepg_data_redux.vw__iepe_culture' 'iepg_data_redux.vw__iepe_economic_presence' 'iepg_data_redux.vw__iepe_education' 'iepg_data_redux.vw__iepe_energy' 'iepg_data_redux.vw__iepe_iepe' 'iepg_data_redux.vw__iepe_information' 'iepg_data_redux.vw__iepe_investments' 'iepg_data_redux.vw__iepe_manufactures' 'iepg_data_redux.vw__iepe_migrations' 'iepg_data_redux.vw__iepe_military_equipment' 'iepg_data_redux.vw__iepe_military_presence' 'iepg_data_redux.vw__iepe_primary_goods' 'iepg_data_redux.vw__iepe_science' 'iepg_data_redux.vw__iepe_services' 'iepg_data_redux.vw__iepe_soft_presence' 'iepg_data_redux.vw__iepe_sports' 'iepg_data_redux.vw__iepe_technology' 'iepg_data_redux.vw__iepe_tourism' 'iepg_data_redux.vw__iepe_troops' 'iepg_data_redux.vw__iepg_cooperation' 'iepg_data_redux.vw__iepg_culture' 'iepg_data_redux.vw__iepg_economic_presence' 'iepg_data_redux.vw__iepg_education' 'iepg_data_redux.vw__iepg_energy' 'iepg_data_redux.vw__iepg_iepg' 'iepg_data_redux.vw__iepg_information' 'iepg_data_redux.vw__iepg_investments' 'iepg_data_redux.vw__iepg_manufactures' 'iepg_data_redux.vw__iepg_migrations' 'iepg_data_redux.vw__iepg_military_equipment' 'iepg_data_redux.vw__iepg_military_presence' 'iepg_data_redux.vw__iepg_primary_goods' 'iepg_data_redux.vw__iepg_science' 'iepg_data_redux.vw__iepg_services' 'iepg_data_redux.vw__iepg_soft_presence' 'iepg_data_redux.vw__iepg_sports' 'iepg_data_redux.vw__iepg_technology' 'iepg_data_redux.vw__iepg_tourism' 'iepg_data_redux.vw__iepg_troops')

CONN="dbname=elcano_iepg host=localhost port=5432 user=elcano_iepg_admin"

for VIEW in "${VIEWS[@]}"
do
    echo $VIEW
    ogr2ogr -overwrite -gt 5000 -preserve_fid -f XLSX excels_export/$VIEW.xlsx PG:"${CONN}" $VIEW
done;

