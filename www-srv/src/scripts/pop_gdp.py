input_file_gdp = 'csv/gdp_2019.csv'
input_file_pop = 'csv/pob_2019.csv'

import sys

sys.path.append('..')

from maplex.maplexmodel import MaplexModel
from common import const

mm = MaplexModel()

import csv

data = {}


def countryRightName(countryName):
    if countryName=="Iran (Islamic Republic of)":
        return "Iran"
    elif countryName=="Korea":
        return "South Korea"
    elif countryName=="Russian Federation":
        return "Russia"
    elif countryName=="United Republic of Tanzania":
        return "Tanzania"
    elif countryName=="Venezuela (Bolivarian Republic of)":
        return "Venezuela"
    elif countryName=="Viet Nam":
        return "Vietnam"
    elif countryName=="Bolivia (Plurinational State of)":
        return "Bolivia"
    elif countryName=="Congo (Democratic Republic of the)":
        return "Congo DR"
    elif countryName=="Serbia (Republic of)":
        return "Serbia"
    else:
        return countryName

def parse(type):

    if type == "population":
        input_file = input_file_pop
    elif type == "gdp":
        input_file = input_file_gdp
    else:
        return ""

    with open(input_file, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')

        sql = ""

        for row in spamreader:

            countryname = countryRightName(row[0].strip())
            if countryname.isdigit() or countryname=="":
                continue

            geoentity = mm.getIdGeoentityByName(countryname,2)
            if not geoentity:
                raise Exception('Not found geoentity for ' + countryname)

            geoentity_id = geoentity[0]["id_geoentity"]

            geoentity_names = mm.getGeoentityNames(geoentity_id,1)
            if not geoentity_names:
                raise Exception('Not found geoentity code name for ' + countryname)

            geoentity_code = geoentity_names[0]["names"][0]
            if geoentity_code not in data:
                data[geoentity_code] = {}

            idx = 1
            for year in const.years:

                #value = float(row[idx].replace(",","."))
                #value = float(row[idx].replace(",","."))
                if year not in data[geoentity_code]:
                    data[geoentity_code][year] = {
                        "population" : -1,
                        "gdp" : -1
                    }

                data[geoentity_code][year][type] = float(row[idx]) if row[idx]!="n.d" and row[idx]!="" else None


                idx += 1


parse("population")
parse("gdp")

sql = "DELETE FROM iepg_data_redux.pob_pib; \n"


for countrycode,country in data.iteritems():
    for year,v in country.iteritems():
        # if year==2015 and countrycode=="ES":
        #     print v
        #     print str('%10.2f' % v["gdp"])
        pop = str('%10.2f' % v["population"]) if v["population"] else 'null'
        gdp = str('%10.2f' % v["gdp"]) if v["gdp"] else 'null'
        sql += "INSERT INTO iepg_data_redux.pob_pib (code,date_in,date_out,population,pib) VALUES ('%s','%s','%s',%s,%s);\n" % \
                    (countrycode,str(year) + "-01-01",\
                        str(year) + "-12-31",pop,gdp)

print sql
