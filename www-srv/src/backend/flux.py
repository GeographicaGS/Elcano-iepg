# coding=UTF8

"""

IEPG Calculation Engine service.

"""
from backend import app
from backend.utils import auth
from flask import request, session, send_file
from common.config import backend
import hashlib
import time
import common.arrayops as arrayops
import os
import flux_lib.data.excel_utils as excel_utils, flux_lib.data.core as core
import ast
import numpy as np


@app.route("/iepgengine", methods=["POST"])
@auth
def iepgEngine():
    """Recieves an Excel file and launches the IEPG calculation. Returns
    an Excel with the results."""
    file = request.files["file"]

    if file is not None and file.filename.rsplit(".",1)[1] in ["xlsx","XLSX"]:
        filename = hashlib.md5(str(time.time())+session["email"]).hexdigest()
        file.save(os.path.join(backend["tmpFolder"], filename+".xlsx"))
    else:
        return jsonify({"Error": "Bad file."})

    # Start the calculus
    book = excel_utils.ExcelReader(os.path.join(backend["tmpFolder"], filename+".xlsx"), 
                                   decimalSeparator=",")

    environment = dict()
    variables = dict()
    years = []
    geoentities = []

    # Read metadata
    environmentEx,lastRowEnv = book.rowReader("Metadata", startCell=(1,0), endMark="")
    variablesEx,lastRowVar = book.rowReader("Metadata", startCell=(lastRowEnv+1,0), startMark="Filiation")

    environmentEx.pop(len(environmentEx)-1)
    variablesEx.pop(0)

    # Read configuration variables
    for i in environmentEx:
        environment[i[0].value] = ast.literal_eval(unicode(i[1].value))

    variables = []
    refYear = str(environment["REFERENCE_YEAR"])

    # Read variables
    for i in variablesEx:
        variables.append(core.Variable(i[0].value, 
                                       getattr(core, i[4].value),
                                       getattr(np, i[5].value), 
                                       environment["LANGUAGE_CODES"], 
                                       ast.literal_eval(i[1].value) if i[1].value!="" else None,
                                       ast.literal_eval(i[2].value) if i[2].value!="" else None,
                                       ast.literal_eval(i[3].value) if i[3].value!="" else None,
                                       ast.literal_eval(i[6].value) if i[6].value!="" else None))

    # Process EUROPEAN_UNION environment variable to find missing countries in each year
    totalCountriesEu = []
    [totalCountriesEu.extend(i) for i in environment["EUROPEAN_UNION"].values()]
    totalCountriesEu = list(set(totalCountriesEu))

    missingEuCountries = {}
    for k,v in environment["EUROPEAN_UNION"].iteritems():
        missingEuCountries[k] = arrayops.arraySubstraction(totalCountriesEu, v)

    # Also total years of EU data are encoded from the number of keys of EUROPEAN_UNION
    euDataYears = len(environment["EUROPEAN_UNION"].keys())
    euDataYearsStr = [str(i) for i in missingEuCountries.keys()]
                
    # Prepare variables for IEPG calculus, excluding EU
    # All data for IEPG countries are loaded in data, but
    # not any EU IEPG-specific data
    data = core.GeoVariableArray()
    [data.merge(book.readGeoVariableArray(".".join(x.filiation))) for x
     in variables if x.filiation[0]=="IEPG"]

    # Get indexes of european countries for not to rely on GeoVariableArray indexing, and also european years
    totalCountriesEuIdx = []
    [totalCountriesEuIdx.append(data.geoentity.index(i)) for i in totalCountriesEu]

    euDataYearsIdx = []
    for i in euDataYearsStr:
        for t in data.time:
            if str(t.start.year)==i:
                euDataYearsIdx.append(data.time.index(t))

    missingEuCountriesIdx = {}
    t = 0
    for k,v in missingEuCountries.iteritems():
        missing = []
        [missing.append(data.geoentity.index(i)) for i in v]
        missingEuCountriesIdx[euDataYearsIdx[t]] = missing
        t+=1
        
    # Prepare and add data for EU
    data.addGeoentity(u"Unión Europea")
    # Get the index of the EU for slicing
    euIndex = data.geoentity.index(u"Unión Europea")
    dolarEx = np.array(environment["EURO_DOLAR_ER"])

    # Initial load of EU data
    vectorVar = ["IEPG_EU.Economic.Energy",
                 "IEPG_EU.Economic.FLA",
                 "IEPG_EU.Economic.BVT",
                 "IEPG_EU.Economic.CMI",
                 "IEPG_EU.Economic.AVO",
                 "IEPG_EU.Economic.CHM",
                 "IEPG_EU.Economic.Manufactures",
                 "IEPG_EU.Economic.Machinery",
                 "IEPG_EU.Economic.MMA",
                 "IEPG_EU.Economic.NFM",
                 "IEPG_EU.Economic.PSP",
                 "IEPG_EU.Economic.NMG",
                 "IEPG_EU.Economic.Services",
                 "IEPG_EU.Economic.Investments",
                 "IEPG_EU.Soft.Culture",
                 "IEPG_EU.Soft.Information"]
    tableVar = ["IEPG_EU.Military.Troops",
                "IEPG_EU.Soft.InmigrationTotal",
                "IEPG_EU.Soft.InmigrationIntra",
                "IEPG_EU.Soft.Tourism",
                "IEPG_EU.Soft.TechnologyTotal",
                "IEPG_EU.Soft.TechnologyIntra",
                "IEPG_EU.Soft.EducationTotal",
                "IEPG_EU.Soft.EducationIntra"]
                         
    euVector = core.GeoVariableArray()
    euTable = core.GeoVariableArray()
    [euVector.merge(book.readGeoVariableArray(x)) for x in vectorVar]
    [euTable.merge(book.readGeoVariableArray(x)) for x in tableVar]

    # EU IEPG Energy, loads EU data into "data" for IEPG calculation
    da = euVector.select(0,
                         None,
                         "IEPG_EU.Economic.Energy"
                     )*np.repeat(dolarEx,1,axis=0).reshape(euDataYears,1)/1000
    data[u"Unión Europea",3:,"IEPG.Economic.Energy"]=da[0,:,0]

    # EU IEPG Culture, loads EU data into "data" for IEPG calculation
    da = euVector.select(0, None, ["IEPG_EU.Soft.Culture","IEPG_EU.Economic.Services"])* \
        np.repeat(dolarEx, 1, axis=0).reshape(euDataYears,1)*1000000
    data[u"Unión Europea",3:,"IEPG.Soft.Culture"]=da[0,:,0]
    
    # EU IEPG Services, loads EU data into "data" for IEPG calculation
    da = euVector.select(0, None, "IEPG_EU.Economic.Services")
    data[u"Unión Europea",3:,"IEPG.Economic.Services"]=da[0,:,0]

    # EU IEPG Investments, loads EU data into "data" for IEPG calculation
    da = euVector.select(0,
                         None,
                         [
                          "IEPG_EU.Economic.Investments"]
                     )*np.repeat(dolarEx,1,axis=0).reshape(euDataYears,1)
    
    data[u"Unión Europea",3:,"IEPG.Economic.Investments"]=da[0,:,0]

    # EU IEPG Primary Goods, loads EU data into "data" for IEPG calculation
    primaryG = np.nansum(euVector.select(
        None,
        None,
        ["IEPG_EU.Economic.FLA",
         "IEPG_EU.Economic.BVT",
         "IEPG_EU.Economic.CMI",
         "IEPG_EU.Economic.AVO",
         "IEPG_EU.Economic.NFM",
         "IEPG_EU.Economic.PSP",
         "IEPG_EU.Economic.NMG"]), axis=2)*dolarEx/1000

    data[u"Unión Europea",3:,"IEPG.Economic.PrimaryGoods"]=primaryG

    # EU IEPG Manufactures, loads EU data into "data" for IEPG calculation
    man = np.nansum(euVector.select(None,None,
                                    ["IEPG_EU.Economic.CHM",
                                     "IEPG_EU.Economic.Manufactures",
                                     "IEPG_EU.Economic.Machinery",
                                     "IEPG_EU.Economic.MMA"]), axis=2) - \
        np.nansum(euVector.select(
            None,
            None,
            ["IEPG_EU.Economic.NFM",
             "IEPG_EU.Economic.PSP"]), axis=2)

    man = man*np.array(dolarEx)/1000

    data[u"Unión Europea",3:,"IEPG.Economic.Manufactures"]=man

    # IEPG EU Troops & military equipment, Science, and Cooperation
    data[u"Unión Europea",3:,"IEPG.Military.Troops"] = np.nansum(euTable[:,:,"IEPG_EU.Military.Troops"], axis=0).flatten()

    # europeanIndices = [0,6,8,10,14,17,18,21,22,23,25,27,28,29,30,35,38,42,43,44,46,51,54,55,57,58,59,63]
    # bulgariaIndex = 3
    # croatiaIndex = 5
    # romaniaIndex = 26
    variablesFromGlobal = ["IEPG.Military.Support.AircraftC",
                           "IEPG.Military.Support.Amphibius",
                           "IEPG.Military.Support.Frigates",
                           "IEPG.Military.Support.Destroyer",
                           "IEPG.Military.Support.Cruisers",
                           "IEPG.Military.Support.Submarine",
                           "IEPG.Military.Support.Aeroplane",
                           "IEPG.Military.Support.Airtanker",
                           "IEPG.Soft.Science",
                           "IEPG.Soft.DevelopmentC"]

    for x in variablesFromGlobal:
        da = data.getSubset(totalCountriesEu,euDataYearsStr,x)
        da.sort()
        da = clearMissingEuCountries(da, missingEuCountries)
        da = np.nansum(da.data, axis=0).flatten()
        data[u"Unión Europea",3:,x] = da

    # Inmigration
    data[u"Unión Europea",3:,"IEPG.Soft.Migrations"] = np.nansum(
        (euTable[:,:,"IEPG_EU.Soft.InmigrationTotal"] - \
         euTable[:,:,"IEPG_EU.Soft.InmigrationIntra"]), axis=0).flatten()

    # Tourism
    data[u"Unión Europea",3:,"IEPG.Soft.Tourism"] = np.nansum(
        euTable[:,:,"IEPG_EU.Soft.Tourism"], axis=0).flatten()/1000

    # Information
    data[u"Unión Europea",3:,"IEPG.Soft.Information"] = euVector[0,:,"IEPG_EU.Soft.Information"]

    # Technology
    data[u"Unión Europea",3:,"IEPG.Soft.Technology"] = np.nansum(
        (euTable[:,:,"IEPG_EU.Soft.TechnologyTotal"] - \
         euTable[:,:,"IEPG_EU.Soft.TechnologyIntra"]), axis=0).flatten()

    # Education
    data[u"Unión Europea",3:,"IEPG.Soft.Education"] = np.nansum(
        (euTable[:,:,"IEPG_EU.Soft.EducationTotal"] - \
         euTable[:,:,"IEPG_EU.Soft.EducationIntra"]), axis=0).flatten()

    shape = data.shape

    # Normal calculus
    normal = ["IEPG.Economic.Energy",
              "IEPG.Economic.PrimaryGoods",
              "IEPG.Economic.Manufactures",
              "IEPG.Economic.Services",
              "IEPG.Economic.Investments",
              "IEPG.Military.Troops",
              "IEPG.Soft.Migrations",
              "IEPG.Soft.Tourism",
              "IEPG.Soft.Culture",
              "IEPG.Soft.Information",
              "IEPG.Soft.Technology",
              "IEPG.Soft.Science",
              "IEPG.Soft.Education",
              "IEPG.Soft.DevelopmentC"]

    for i in normal:
        if i+"Est" in data.variable:
            d = np.fmax(data[:,:,i]*1000.0/np.nanmax(data[:euIndex,refYear,i]), 
                        data[:,:,i+"Est"])
        else:
            d = data[:,:,i]*1000.0/np.nanmax(data[:70,refYear,i])

        data.addVariable(i+"_IEPG", data=d)

    # Sports calculus
    # This is the calculus for the sports coefficient
    linearCoef = environment["SPORTS_LINEAR_COEFICIENT"]
    medals_fifa = environment["SPORTS_MEDALS_FIFA_COEFICIENTS"]

    sports = ((medals_fifa[0]/np.repeat( \
                               np.nansum(data[:euIndex,:,"IEPG.Soft.Support.Olimpics"], axis=0).reshape(1,shape[1]), 
                               shape[0], axis=0).reshape(shape[0],shape[1])* \
               10000*data[:,:,"IEPG.Soft.Support.Olimpics"].reshape(shape[0],shape[1]))+ \
              (medals_fifa[1]/np.repeat( \
                            np.nansum(data[:euIndex,:,"IEPG.Soft.Support.FIFAPoints"], axis=0).reshape(1,shape[1]), 
                                         shape[0], axis=0).reshape(shape[0],shape[1])* \
                   10000*data[:,:,"IEPG.Soft.Support.FIFAPoints"].reshape(shape[0],shape[1])))* \
                   np.repeat(np.array(linearCoef).reshape(1,shape[1]), shape[0], axis=0)

    data.addVariable("IEPG.Soft.SportsCoef", data=sports)

    # This is the sum of coeficients for european countries to calculate the EU IEPG
    euIepgSportsCoef = data.getSubset(totalCountriesEu, euDataYearsStr, "IEPG.Soft.SportsCoef")
    euIepgSportsCoef.sort()
    euIepgSportsCoef = clearMissingEuCountries(euIepgSportsCoef, missingEuCountries)
    euIepgSportsCoef = (np.nansum(euIepgSportsCoef.data, axis=0)*.7).flatten()
    data[u"Unión Europea",3:,"IEPG.Soft.SportsCoef"] = euIepgSportsCoef

    # Final IEPG sports calculus
    data.addVariable("IEPG.Soft.Sports_IEPG", data=
                     data[:,:,"IEPG.Soft.SportsCoef"]*1000.0/ \
                     np.nanmax(data[:euIndex,refYear,"IEPG.Soft.SportsCoef"]))

    # Military equipment
    militaryEquipment = ['IEPG.Military.Support.AircraftC',
                         'IEPG.Military.Support.Amphibius',
                         'IEPG.Military.Support.Frigates',
                         'IEPG.Military.Support.Destroyer',
                         'IEPG.Military.Support.Cruisers',
                         'IEPG.Military.Support.Submarine',
                         'IEPG.Military.Support.Aeroplane',
                         'IEPG.Military.Support.Airtanker']

    militaryCoefs = []
    militaryCoefsEquip = []

    for i in militaryEquipment:
        militaryCoefs.append(np.nansum(data[:euIndex,refYear,tuple(militaryEquipment)])/ \
                             np.nansum(data[:euIndex,refYear,i]))

    militaryTotal = np.nansum(np.array(militaryCoefs))

    for i in militaryCoefs:
        militaryCoefsEquip.append(i/militaryTotal*1000)
        
    ae = np.zeros((shape[0],shape[1]))

    for i in range(0, len(militaryCoefsEquip)):
        ae+=militaryCoefsEquip[i]*np.nan_to_num(data[:,:,militaryEquipment[i]].reshape(shape[0],shape[1]))

    data.addVariable("MilitaryPoints", data=ae)    
    data.addVariable("IEPG.Military.MilitaryEquipment_IEPG", data=
                        data[:,:,"MilitaryPoints"]*1000.0/ \
                        np.nanmax(data[:,refYear,"MilitaryPoints"]))

    # Dimensions and Index
    cEconomic = environment["ECONOMIC_COEFICIENTS"]
    vEconomic = ["Energy","PrimaryGoods","Manufactures","Services","Investments"]
    cMilitary = environment["MILITARY_COEFICIENTS"]
    vMilitary = ["Troops", "MilitaryEquipment"]
    cSoft = environment["SOFT_COEFICIENTS"]
    vSoft = ["Migrations", "Tourism", "Sports", "Culture", "Information", "Technology", "Science",
             "Education", "DevelopmentC"]
    cIndex = environment["DIMENSION_COEFICIENTS"]

    a = np.zeros((shape[0],shape[1]))
    for i in range(0, len(cEconomic)):
        a+=data[:,:,"IEPG.Economic."+vEconomic[i]+"_IEPG"].reshape(shape[0],shape[1])*cEconomic[i]
    
    data.addVariable("IEPG.Global.Economic", data=a/100.0)

    a = np.zeros((shape[0],shape[1]))
    for i in range(0, len(cMilitary)):
        a+=data[:,:,"IEPG.Military."+vMilitary[i]+"_IEPG"].reshape(shape[0],shape[1])*cMilitary[i]
    
    data.addVariable("IEPG.Global.Military", data=a/100.0)

    a = np.zeros((shape[0],shape[1]))
    for i in range(0, len(cSoft)):
        a+=data[:,:,"IEPG.Soft."+vSoft[i]+"_IEPG"].reshape(shape[0],shape[1])*cSoft[i]
    
    data.addVariable("IEPG.Global.Soft", data=a/100.0)

    data.addVariable("IEPG.Global.IEPG", data=(data[:,:,"IEPG.Global.Economic"]*cIndex[0]+
                                               data[:,:,"IEPG.Global.Military"]*cIndex[1]+
                                               data[:,:,"IEPG.Global.Soft"]*cIndex[2])/100.0)

    # Quota
    variable = [
        'IEPG.Economic.Energy_IEPG',
        'IEPG.Economic.PrimaryGoods_IEPG',
        'IEPG.Economic.Manufactures_IEPG',
        'IEPG.Economic.Services_IEPG',
        'IEPG.Economic.Investments_IEPG',
        'IEPG.Military.Troops_IEPG',
        'IEPG.Military.MilitaryEquipment_IEPG',
        'IEPG.Soft.Migrations_IEPG',
        'IEPG.Soft.Tourism_IEPG',
        'IEPG.Soft.Culture_IEPG',
        'IEPG.Soft.Information_IEPG',
        'IEPG.Soft.Technology_IEPG',
        'IEPG.Soft.Science_IEPG',
        'IEPG.Soft.Education_IEPG',
        'IEPG.Soft.DevelopmentC_IEPG',
        'IEPG.Soft.Sports_IEPG',
        'IEPG.Global.Economic',
        'IEPG.Global.Military',
        'IEPG.Global.Soft',
        'IEPG.Global.IEPG']

    for i in variable:
        a = data[:,:,i].reshape(shape[0],shape[1])/ \
            (np.repeat(np.nansum(data[:,:,i], axis=0).reshape(1,shape[1]), shape[0], axis=0))

        data.addVariable(i+"_QUOTE", data=a)

    # Contributions
    cPresenceEconomic = []
    cPresenceMilitary = []
    cPresenceSoft = []

    for i in range(0, len(cEconomic)):
        cPresenceEconomic.append(cEconomic[i]*cIndex[0]/10000.0)

    for i in range(0, len(cMilitary)):
        cPresenceMilitary.append(cMilitary[i]*cIndex[1]/10000.0)

    for i in range(0, len(cSoft)):
        cPresenceSoft.append(cSoft[i]*cIndex[2]/10000.0)

    pcdEconomic = 0
    pcdMilitary = 0
    pcdSoft = 0
    for i in range(0, len(vEconomic)):
        pcdEconomic+=np.nansum(data[:,:,"IEPG.Economic."+vEconomic[i]+"_IEPG"])*cPresenceEconomic[i]

    for i in range(0, len(vMilitary)):
        pcdMilitary+=np.nansum(data[:,:,"IEPG.Military."+vMilitary[i]+"_IEPG"])*cPresenceMilitary[i]

    for i in range(0, len(vSoft)):
        pcdSoft+=np.nansum(data[:,:,"IEPG.Soft."+vSoft[i]+"_IEPG"])*cPresenceSoft[i]

    tci = pcdEconomic+pcdMilitary+pcdSoft

    for i in range(0, len(vEconomic)):
        a = data[:,:,"IEPG.Economic."+vEconomic[i]+"_IEPG"]*cEconomic[i]/tci
        data.addVariable("IEPG.Economic."+vEconomic[i]+"_CON", data=a)

    for i in range(0, len(vMilitary)):
        a = data[:,:,"IEPG.Military."+vMilitary[i]+"_IEPG"]*cMilitary[i]/tci
        data.addVariable("IEPG.Military."+vMilitary[i]+"_CON", data=a)

    for i in range(0, len(vSoft)):
        a = data[:,:,"IEPG.Soft."+vSoft[i]+"_IEPG"]*cSoft[i]/tci
        data.addVariable("IEPG.Soft."+vSoft[i]+"_CON", data=a)
        
    outFileName = os.path.join(backend["tmpFolder"],
                               hashlib.md5(str(time.time())+session["email"]+"outputIEPGEngine").hexdigest()+ \
                               ".xlsx")

    data.sort()
    ew = excel_utils.ExcelWriter(outFileName)
    sheets = ew.writeGeoVariableArray(data, variable=['IEPG.Economic.Energy_IEPG',
                                                      'IEPG.Economic.PrimaryGoods_IEPG',
                                                      'IEPG.Economic.Manufactures_IEPG',
                                                      'IEPG.Economic.Services_IEPG',
                                                      'IEPG.Economic.Investments_IEPG',
                                                      'IEPG.Military.Troops_IEPG',
                                                      'IEPG.Military.MilitaryEquipment_IEPG',
                                                      'IEPG.Soft.Migrations_IEPG',
                                                      'IEPG.Soft.Tourism_IEPG',
                                                      'IEPG.Soft.Sports_IEPG',
                                                      'IEPG.Soft.Culture_IEPG',
                                                      'IEPG.Soft.Information_IEPG',
                                                      'IEPG.Soft.Technology_IEPG',
                                                      'IEPG.Soft.Science_IEPG',
                                                      'IEPG.Soft.Education_IEPG',
                                                      'IEPG.Soft.DevelopmentC_IEPG',
                                                      'IEPG.Global.Economic',
                                                      'IEPG.Global.Military',
                                                      'IEPG.Global.Soft',
                                                      'IEPG.Global.IEPG',
                                                      'IEPG.Economic.Energy_IEPG_QUOTE',
                                                      'IEPG.Economic.PrimaryGoods_IEPG_QUOTE',
                                                      'IEPG.Economic.Manufactures_IEPG_QUOTE',
                                                      'IEPG.Economic.Services_IEPG_QUOTE',
                                                      'IEPG.Economic.Investments_IEPG_QUOTE',
                                                      'IEPG.Military.Troops_IEPG_QUOTE',
                                                      'IEPG.Military.MilitaryEquipment_IEPG_QUOTE',
                                                      'IEPG.Soft.Migrations_IEPG_QUOTE',
                                                      'IEPG.Soft.Tourism_IEPG_QUOTE',
                                                      'IEPG.Soft.Sports_IEPG_QUOTE',
                                                      'IEPG.Soft.Culture_IEPG_QUOTE',
                                                      'IEPG.Soft.Information_IEPG_QUOTE',
                                                      'IEPG.Soft.Technology_IEPG_QUOTE',
                                                      'IEPG.Soft.Science_IEPG_QUOTE',
                                                      'IEPG.Soft.Education_IEPG_QUOTE',
                                                      'IEPG.Soft.DevelopmentC_IEPG_QUOTE',
                                                      'IEPG.Global.Economic_QUOTE',
                                                      'IEPG.Global.Military_QUOTE',
                                                      'IEPG.Global.Soft_QUOTE',
                                                      'IEPG.Global.IEPG_QUOTE',
                                                      'IEPG.Economic.Energy_CON',
                                                      'IEPG.Economic.PrimaryGoods_CON',
                                                      'IEPG.Economic.Manufactures_CON',
                                                      'IEPG.Economic.Services_CON',
                                                      'IEPG.Economic.Investments_CON',
                                                      'IEPG.Military.Troops_CON',
                                                      'IEPG.Military.MilitaryEquipment_CON',
                                                      'IEPG.Soft.Migrations_CON',
                                                      'IEPG.Soft.Tourism_CON',
                                                      'IEPG.Soft.Sports_CON',
                                                      'IEPG.Soft.Culture_CON',
                                                      'IEPG.Soft.Information_CON',
                                                      'IEPG.Soft.Technology_CON',
                                                      'IEPG.Soft.Science_CON',
                                                      'IEPG.Soft.Education_CON',
                                                      'IEPG.Soft.DevelopmentC_CON'],
                                      sheetName=['Energy IEPG',
                                                 'Primary Goods IEPG',
                                                 'Manufactures IEPG',
                                                 'Services IEPG',
                                                 'Investments IEPG',
                                                 'Troops IEPG',
                                                 'Military Equipment IEPG',
                                                 'Migrations IEPG',
                                                 'Tourism IEPG',
                                                 'Sports IEPG',
                                                 'Culture IEPG',
                                                 'Information IEPG',
                                                 'Technology IEPG',
                                                 'Science IEPG',
                                                 'Education IEPG',
                                                 'Development Coop. IEPG',
                                                 'Economic IEPG',
                                                 'Military IEPG',
                                                 'Soft IEPG',
                                                 'IEPG',
                                                 'Energy IEPG QUOTE',
                                                 'Primary Goods IEPG QUOTE',
                                                 'Manufactures IEPG QUOTE',
                                                 'Services IEPG QUOTE',
                                                 'Investments IEPG QUOTE',
                                                 'Troops IEPG QUOTE',
                                                 'Military Equipment IEPG QUOTE',
                                                 'Migrations IEPG QUOTE',
                                                 'Tourism IEPG QUOTE',
                                                 'Sports IEPG QUOTE',
                                                 'Culture IEPG QUOTE',
                                                 'Information IEPG QUOTE',
                                                 'Technology IEPG QUOTE',
                                                 'Science IEPG QUOTE',
                                                 'Education IEPG QUOTE',
                                                 'Development Coop. IEPG QUOTE',
                                                 'Economic IEPG QUOTE',
                                                 'Military IEPG QUOTE',
                                                 'Soft IEPG QUOTE',
                                                 'IEPG IEPG QUOTE',
                                                 'Energy IEPG CONTRIBUTION',
                                                 'Primary Goods IEPG CONTRIBUTION',
                                                 'Manufactures IEPG CONTRIBUTION',
                                                 'Services IEPG CONTRIBUTION',
                                                 'Investments IEPG CONTRIBUTION',
                                                 'Troops IEPG CONTRIBUTION',
                                                 'Military E. IEPG CONTRIBUTION',
                                                 'Migrations IEPG CONTRIBUTION',
                                                 'Tourism IEPG CONTRIBUTION',
                                                 'Sports IEPG CONTRIBUTION',
                                                 'Culture IEPG CONTRIBUTION',
                                                 'Information IEPG CONTRIBUTION',
                                                 'Technology IEPG CONTRIBUTION',
                                                 'Science IEPG CONTRIBUTION',
                                                 'Education IEPG CONTRIBUTION',
                                                 'Devel. C. IEPG CONTRIBUTION'])

    ew.addStyle("header", {
        "bg_color": "#08608C",
        "font_color": "white",
        "valign": "vcenter",
        "align": "center",
        "size": 12
    })

    for name,sheet in sheets.iteritems():
        ew.setColumnStyle(sheet, 0, 0, 25)
        ew.setRowStyle(sheet, 0, 20, style="header")



    # IEPE Calculus starts here

    # Keep IEPG data for sports coefficients
    iepgData = data
    
    # Prepare variables for IEPE calculus
    data = core.GeoVariableArray()
    [data.merge(book.readGeoVariableArray(".".join(x.filiation))) for x
    in variables if x.filiation[0]=="IEPE"]
    
    shape = data.shape

    # Previous aggregation
    # Primary goods
    primaryG = np.nansum(data.select(None,None,["IEPE.Economic.FLA","IEPE.Economic.BVT","IEPE.Economic.CMI", \
                                                "IEPE.Economic.AVO","IEPE.Economic.NFM","IEPE.Economic.PSP", \
                                                "IEPE.Economic.NMG"]), axis=2)
    data.addVariable("IEPE.Economic.PrimaryGoods", data=primaryG)
    data = clearMissingEuCountries(data, missingEuCountries, variable="IEPE.Economic.PrimaryGoods")
    
    # Manufactures
    man = np.nansum(data.select(None,None,["IEPE.Economic.CHM", "IEPE.Economic.ManufacturesPre", \
                                           "IEPE.Economic.Machinery", "IEPE.Economic.MMA"]), axis=2) - \
          np.nansum(data.select(None,None,["IEPE.Economic.NFM","IEPE.Economic.PSP"]), axis=2)
    data.addVariable("IEPE.Economic.Manufactures", data=man)
    data = clearMissingEuCountries(data, missingEuCountries, variable="IEPE.Economic.Manufactures")

    # Normal calculus
    normal = ["IEPE.Economic.Energy",
              "IEPE.Economic.PrimaryGoods",
              "IEPE.Economic.Manufactures",
              "IEPE.Economic.Services",
              "IEPE.Economic.Investments",
              "IEPE.Soft.Migrations",
              "IEPE.Soft.Tourism",
              "IEPE.Soft.Culture",
              "IEPE.Soft.Information",
              "IEPE.Soft.Technology",
              "IEPE.Soft.Science",
              "IEPE.Soft.Education"]


    for i in normal:
        d = data[:,:,i]*1000.0/np.nanmax(data[:,refYear,i])
        data.addVariable(i+"_IEPE", data=d)
        data = clearMissingEuCountries(data, missingEuCountries, variable=i+"_IEPE")

    # Dummy zero military equipment, troops, and development cooperation
    zeroes = np.zeros((shape[0],shape[1]))
    data.addVariable("IEPE.Military.Troops_IEPE", data=zeroes)
    data.addVariable("IEPE.Military.MilitaryEquipment_IEPE", data=zeroes)
    data.addVariable("IEPE.Soft.DevelopmentC_IEPE", data=zeroes)

    # IEPE Sports calculus
    euIepgSportsCoef = iepgData.getSubset(totalCountriesEu, euDataYearsStr, "IEPG.Soft.SportsCoef")
    euIepgSportsCoef.sort()
    euIepgSportsCoef = clearMissingEuCountries(euIepgSportsCoef, missingEuCountries)
    euIepgSportsCoef = euIepgSportsCoef.data*1000.0/np.nanmax(euIepgSportsCoef.select(None, refYear, 0))
    data.addVariable("IEPE.Soft.Sports_IEPE", data=euIepgSportsCoef)
    data = clearMissingEuCountries(data, missingEuCountries, variable="IEPE.Soft.Sports_IEPE")
    
    # Dimensions and Index
    cEconomic = environment["ECONOMIC_COEFICIENTS"]
    vEconomic = ["Energy","PrimaryGoods","Manufactures","Services","Investments"]
    cMilitary = environment["MILITARY_COEFICIENTS"]
    vMilitary = ["Troops", "MilitaryEquipment"]
    cSoft = environment["SOFT_COEFICIENTS"]
    vSoft = ["Migrations", "Tourism", "Sports", "Culture", "Information", "Technology", "Science",
             "Education","DevelopmentC"]
    cIndex = environment["DIMENSION_COEFICIENTS"]

    a = np.zeros((shape[0],shape[1]))
    for i in range(0, len(cEconomic)):
        a+=data[:,:,"IEPE.Economic."+vEconomic[i]+"_IEPE"].reshape(shape[0],shape[1])*cEconomic[i]
    
    data.addVariable("IEPE.Global.Economic", data=a/100.0)
    data = clearMissingEuCountries(data, missingEuCountries, variable="IEPE.Global.Economic")

    a = np.zeros((shape[0],shape[1]))
    for i in range(0, len(cMilitary)):
        a+=data[:,:,"IEPE.Military."+vMilitary[i]+"_IEPE"].reshape(shape[0],shape[1])*cMilitary[i]
    
    data.addVariable("IEPE.Global.Military", data=a/100.0)

    a = np.zeros((shape[0],shape[1]))
    for i in range(0, len(cSoft)):
        a+=data[:,:,"IEPE.Soft."+vSoft[i]+"_IEPE"].reshape(shape[0],shape[1])*cSoft[i]
    
    data.addVariable("IEPE.Global.Soft", data=a/100.0)
    data = clearMissingEuCountries(data, missingEuCountries, variable="IEPE.Global.Soft")

    data.addVariable("IEPE.Global.IEPE", data=(data[:,:,"IEPE.Global.Economic"]*cIndex[0]+
                                               data[:,:,"IEPE.Global.Military"]*cIndex[1]+
                                               data[:,:,"IEPE.Global.Soft"]*cIndex[2])/100.0)
    data = clearMissingEuCountries(data, missingEuCountries, variable="IEPE.Global.IEPE")

    # Quota
    variable = [
        'IEPE.Economic.Energy_IEPE',
        'IEPE.Economic.PrimaryGoods_IEPE',
        'IEPE.Economic.Manufactures_IEPE',
        'IEPE.Economic.Services_IEPE',
        'IEPE.Economic.Investments_IEPE',
        'IEPE.Military.Troops_IEPE',
        'IEPE.Military.MilitaryEquipment_IEPE',
        'IEPE.Soft.Migrations_IEPE',
        'IEPE.Soft.Tourism_IEPE',
        'IEPE.Soft.Culture_IEPE',
        'IEPE.Soft.Information_IEPE',
        'IEPE.Soft.Technology_IEPE',
        'IEPE.Soft.Science_IEPE',
        'IEPE.Soft.Education_IEPE',
        'IEPE.Soft.DevelopmentC_IEPE',
        'IEPE.Soft.Sports_IEPE',
        'IEPE.Global.Economic',
        'IEPE.Global.Military',
        'IEPE.Global.Soft',
        'IEPE.Global.IEPE']

    for i in variable:
        a = data[:,:,i].reshape(shape[0],shape[1])/ \
            (np.repeat(np.nansum(data[:,:,i], axis=0).reshape(1,shape[1]), shape[0], axis=0))

        data.addVariable(i+"_QUOTE", data=a)

    # Contributions
    cPresenceEconomic = []
    cPresenceMilitary = []
    cPresenceSoft = []

    for i in range(0, len(cEconomic)):
        cPresenceEconomic.append(cEconomic[i]*cIndex[0]/10000.0)

    for i in range(0, len(cMilitary)):
        cPresenceMilitary.append(cMilitary[i]*cIndex[1]/10000.0)

    for i in range(0, len(cSoft)):
        cPresenceSoft.append(cSoft[i]*cIndex[2]/10000.0)

    pcdEconomic = 0
    pcdMilitary = 0
    pcdSoft = 0
    for i in range(0, len(vEconomic)):
        pcdEconomic+=np.nansum(data[:,:,"IEPE.Economic."+vEconomic[i]+"_IEPE"])*cPresenceEconomic[i]

    for i in range(0, len(vMilitary)):
        pcdMilitary+=np.nansum(data[:,:,"IEPE.Military."+vMilitary[i]+"_IEPE"])*cPresenceMilitary[i]

    for i in range(0, len(vSoft)):
        pcdSoft+=np.nansum(data[:,:,"IEPE.Soft."+vSoft[i]+"_IEPE"])*cPresenceSoft[i]

    tci = pcdEconomic+pcdMilitary+pcdSoft

    for i in range(0, len(vEconomic)):
        a = data[:,:,"IEPE.Economic."+vEconomic[i]+"_IEPE"]*cEconomic[i]/tci
        data.addVariable("IEPE.Economic."+vEconomic[i]+"_CON", data=a)

    for i in range(0, len(vMilitary)):
        a = data[:,:,"IEPE.Military."+vMilitary[i]+"_IEPE"]*cMilitary[i]/tci
        data.addVariable("IEPE.Military."+vMilitary[i]+"_CON", data=a)

    for i in range(0, len(vSoft)):
        a = data[:,:,"IEPE.Soft."+vSoft[i]+"_IEPE"]*cSoft[i]/tci
        data.addVariable("IEPE.Soft."+vSoft[i]+"_CON", data=a)
        
    sheets = ew.writeGeoVariableArray(data, variable=['IEPE.Economic.Energy_IEPE',
                                                      'IEPE.Economic.PrimaryGoods_IEPE',
                                                      'IEPE.Economic.Manufactures_IEPE',
                                                      'IEPE.Economic.Services_IEPE',
                                                      'IEPE.Economic.Investments_IEPE',
                                                      'IEPE.Military.Troops_IEPE',
                                                      'IEPE.Military.MilitaryEquipment_IEPE',
                                                      'IEPE.Soft.Migrations_IEPE',
                                                      'IEPE.Soft.Tourism_IEPE',
                                                      'IEPE.Soft.Sports_IEPE',
                                                      'IEPE.Soft.Culture_IEPE',
                                                      'IEPE.Soft.Information_IEPE',
                                                      'IEPE.Soft.Technology_IEPE',
                                                      'IEPE.Soft.Science_IEPE',
                                                      'IEPE.Soft.Education_IEPE',
                                                      'IEPE.Soft.DevelopmentC_IEPE',
                                                      'IEPE.Global.Economic',
                                                      'IEPE.Global.Military',
                                                      'IEPE.Global.Soft',
                                                      'IEPE.Global.IEPE',
                                                      'IEPE.Economic.Energy_IEPE_QUOTE',
                                                      'IEPE.Economic.PrimaryGoods_IEPE_QUOTE',
                                                      'IEPE.Economic.Manufactures_IEPE_QUOTE',
                                                      'IEPE.Economic.Services_IEPE_QUOTE',
                                                      'IEPE.Economic.Investments_IEPE_QUOTE',
                                                      'IEPE.Military.Troops_IEPE_QUOTE',
                                                      'IEPE.Military.MilitaryEquipment_IEPE_QUOTE',
                                                      'IEPE.Soft.Migrations_IEPE_QUOTE',
                                                      'IEPE.Soft.Tourism_IEPE_QUOTE',
                                                      'IEPE.Soft.Sports_IEPE_QUOTE',
                                                      'IEPE.Soft.Culture_IEPE_QUOTE',
                                                      'IEPE.Soft.Information_IEPE_QUOTE',
                                                      'IEPE.Soft.Technology_IEPE_QUOTE',
                                                      'IEPE.Soft.Science_IEPE_QUOTE',
                                                      'IEPE.Soft.Education_IEPE_QUOTE',
                                                      'IEPE.Soft.DevelopmentC_IEPE_QUOTE',
                                                      'IEPE.Global.Economic_QUOTE',
                                                      'IEPE.Global.Military_QUOTE',
                                                      'IEPE.Global.Soft_QUOTE',
                                                      'IEPE.Global.IEPE_QUOTE',
                                                      'IEPE.Economic.Energy_CON',
                                                      'IEPE.Economic.PrimaryGoods_CON',
                                                      'IEPE.Economic.Manufactures_CON',
                                                      'IEPE.Economic.Services_CON',
                                                      'IEPE.Economic.Investments_CON',
                                                      'IEPE.Military.Troops_CON',
                                                      'IEPE.Military.MilitaryEquipment_CON',
                                                      'IEPE.Soft.Migrations_CON',
                                                      'IEPE.Soft.Tourism_CON',
                                                      'IEPE.Soft.Sports_CON',
                                                      'IEPE.Soft.Culture_CON',
                                                      'IEPE.Soft.Information_CON',
                                                      'IEPE.Soft.Technology_CON',
                                                      'IEPE.Soft.Science_CON',
                                                      'IEPE.Soft.Education_CON',
                                                      'IEPE.Soft.DevelopmentC_CON'],
                                      sheetName=['Energy IEPE',
                                                 'Primary Goods IEPE',
                                                 'Manufactures IEPE',
                                                 'Services IEPE',
                                                 'Investments IEPE',
                                                 'Troops IEPE',
                                                 'Military Equipment IEPE',
                                                 'Migrations IEPE',
                                                 'Tourism IEPE',
                                                 'Sports IEPE',
                                                 'Culture IEPE',
                                                 'Information IEPE',
                                                 'Technology IEPE',
                                                 'Science IEPE',
                                                 'Education IEPE',
                                                 'Development Coop. IEPE',
                                                 'Economic IEPE',
                                                 'Military IEPE',
                                                 'Soft IEPE',
                                                 'IEPE',
                                                 'Energy IEPE QUOTE',
                                                 'Primary Goods IEPE QUOTE',
                                                 'Manufactures IEPE QUOTE',
                                                 'Services IEPE QUOTE',
                                                 'Investments IEPE QUOTE',
                                                 'Troops IEPE QUOTE',
                                                 'Military Equip. IEPE QUOTE',
                                                 'Migrations IEPE QUOTE',
                                                 'Tourism IEPE QUOTE',
                                                 'Sports IEPE QUOTE',
                                                 'Culture IEPE QUOTE',
                                                 'Information IEPE QUOTE',
                                                 'Technology IEPE QUOTE',
                                                 'Science IEPE QUOTE',
                                                 'Education IEPE QUOTE',
                                                 'Development Coop. IEPE QUOTE',
                                                 'Economic IEPE QUOTE',
                                                 'Military IEPE QUOTE',
                                                 'Soft IEPE QUOTE',
                                                 'IEPE IEPE QUOTE',
                                                 'Energy IEPE CONTRIBUTION',
                                                 'Primary Goods IEPE CONTRIBUTION',
                                                 'Manufactures IEPE CONTRIBUTION',
                                                 'Services IEPE CONTRIBUTION',
                                                 'Investments IEPE CONTRIBUTION',
                                                 'Troops IEPE CONTRIBUTION',
                                                 'Military E. IEPE CONTRIBUTION',
                                                 'Migrations IEPE CONTRIBUTION',
                                                 'Tourism IEPE CONTRIBUTION',
                                                 'Sports IEPE CONTRIBUTION',
                                                 'Culture IEPE CONTRIBUTION',
                                                 'Information IEPE CONTRIBUTION',
                                                 'Technology IEPE CONTRIBUTION',
                                                 'Science IEPE CONTRIBUTION',
                                                 'Education IEPE CONTRIBUTION',
                                                 'Devel. C. IEPE CONTRIBUTION'])

    ew.addStyle("header", {
        "bg_color": "#08608C",
        "font_color": "white",
        "valign": "vcenter",
        "align": "center",
        "size": 12
    })

    for name,sheet in sheets.iteritems():
        ew.setColumnStyle(sheet, 0, 0, 25)
        ew.setRowStyle(sheet, 0, 20, style="header")

    ew.closeWorkbook()

    return(send_file(outFileName, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", 
                     attachment_filename="Real_Instituto_Elcano-Calculo_IEPG.xlsx",
                     as_attachment=True))


# Clears data for non present countries in EU for certain years 
def clearMissingEuCountries(array, missingEuCountries, variable=0):
    for k,v in missingEuCountries.iteritems():
        for i in v:
            array[i, str(k), variable] = np.nan

    return array
