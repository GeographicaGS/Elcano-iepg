new_year = 2014
input_file = '../csv/popgdp2014.csv'

import sys

sys.path.append('../../www-srv/src')

from maplex.maplexmodel import MaplexModel

mm = MaplexModel()

import csv
with open(input_file, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    
    sql = ""

    for row in spamreader:
        countryname = row[0] 
        gdp = row[1].replace(",",".")
        population = row[2].replace(",",".")

        if countryname.strip() == "":
            continue

        geoentity = mm.getIdGeoentityByName(countryname,2)
        if not geoentity:
            raise Exception('Not found geoentity for ' + countryname)

        geoentity_id = geoentity[0]["id_geoentity"]
        
        geoentity_names = mm.getGeoentityNames(geoentity_id,1)
        if not geoentity_names:
            raise Exception('Not found geoentity code name for ' + countryname)            

        geoentity_code = geoentity_names[0]["names"][0]

        sql += "INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,pib,population) VALUES ('%s','%s','%s',%f,%f);\n" % \
                    (geoentity_code,str(new_year) + "-01-01",\
                        str(new_year) + "-12-31",float(gdp)* (10**9),\
                        float(population)* (10**6))


print sql