input_file_gdp = '../csv/gdpnewcountries2014.csv'
input_file_pop = '../csv/popnewcountries2014.csv'

import sys

sys.path.append('../../www-srv/src')

from maplex.maplexmodel import MaplexModel
from common import const

mm = MaplexModel()

import csv

def getSQL(type):
    
    if type == "population":
        input_file = input_file_pop
    elif type == "pib":
        input_file = input_file_gdp
    else:
        return ""

    with open(input_file, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        
        sql = ""

        for row in spamreader:
            countryname = row[0] .strip()
            
            if countryname.isdigit():   
                continue

            geoentity = mm.getIdGeoentityByName(countryname,2)
            if not geoentity:
                raise Exception('Not found geoentity for ' + countryname)

            geoentity_id = geoentity[0]["id_geoentity"]
            
            geoentity_names = mm.getGeoentityNames(geoentity_id,1)
            if not geoentity_names:
                raise Exception('Not found geoentity code name for ' + countryname)            

            geoentity_code = geoentity_names[0]["names"][0]

            sql += "DELETE FROM iepg_data_redux.pob_pib WHERE code='%s';\n" % (geoentity_code)

            idx = 1
            for year in const.years:

                value = float(row[idx].replace(",","."))
                value = value*(10**6) if type == "population" else value*(10**9)

                sql += "INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,%s) VALUES ('%s','%s','%s',%f);\n" % \
                            (type,geoentity_code,str(year) + "-01-01",\
                                str(year) + "-12-31",value)

                idx += 1

    return sql


sql = getSQL("population") + getSQL("pib")

print sql