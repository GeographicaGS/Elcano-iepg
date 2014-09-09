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
import os
import flux_lib.data.excel_utils as excel_utils, flux_lib.data.core as core
import ast
import numpy as np
import datetime as dt

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
        environment[i[0].value] = ast.literal_eval(str(i[1].value))

    data = core.GeoVariableArray()
    refYear = str(environment["REFERENCE_YEAR"])

    # Read variables
    for i in variablesEx:
        var = core.Variable(i[0].value, 
                            getattr(core, i[4].value),
                            getattr(np, i[5].value), 
                            environment["LANGUAGE_CODES"], 
                            ast.literal_eval(i[1].value) if i[1].value!="" else None,
                            ast.literal_eval(i[2].value) if i[2].value!="" else None,
                            ast.literal_eval(i[3].value) if i[3].value!="" else None,
                            ast.literal_eval(i[6].value) if i[6].value!="" else None)

        data.merge(book.readGeoVariableArray(".".join(var.filiation)))

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
            d = np.fmax(np.round(data[:,:,i]*1000.0/np.nanmax(data[:,refYear,i])), 
                        data[:,:,i+"Est"])
        else:
            d = np.round(data[:,:,i]*1000.0/np.nanmax(data[:,refYear,i]))

        data.addVariable(i+"_IEPG", data=d)

    # Sports calculus
    linearCoef = environment["SPORTS_LINEAR_COEFICIENT"]
    medals_fifa = environment["SPORTS_MEDALS_FIFA_COEFICIENTS"]

    sports = ((medals_fifa[0]/np.repeat( \
                               np.nansum(data[:,:,"IEPG.Soft.Support.Olimpics"], axis=0).reshape(1,shape[1]), 
                               shape[0], axis=0).reshape(shape[0],shape[1])* \
              10000*data[:,:,"IEPG.Soft.Support.Olimpics"])+ \
              (medals_fifa[1]/np.repeat( \
                            np.nansum(data[:,:,"IEPG.Soft.Support.FIFAPoints"], axis=0).reshape(1,shape[1]), 
                                         shape[0], axis=0).reshape(shape[0],shape[1])* \
                   10000*data[:,:,"IEPG.Soft.Support.FIFAPoints"]))* \
                   np.repeat(np.array(linearCoef).reshape(1,shape[1]), shape[0], axis=0)

    data.addVariable("IEPG.Soft.SportsCoef", data=sports)
    data.addVariable("IEPG.Soft.Sports_IEPG", data=
                     np.round(data[:,:,"IEPG.Soft.SportsCoef"]*1000.0/ \
                              np.nanmax(data[:,refYear,"IEPG.Soft.SportsCoef"])))

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
        militaryCoefs.append(np.nansum(data[:,refYear,militaryEquipment])/np.nansum(data[:,refYear,i]))

    militaryTotal = np.nansum(np.array(militaryCoefs))

    for i in militaryCoefs:
        militaryCoefsEquip.append(i/militaryTotal)

    ae = np.zeros((shape[0],shape[1]))

    for i in range(0, len(militaryCoefsEquip)):
        ae+=militaryCoefsEquip[i]*np.nan_to_num(data[:,:,militaryEquipment[i]])

    data.addVariable("MilitaryPoints", data=ae)    

    data.addVariable("IEPG.Military.MilitaryEquipment_IEPG", data=
                     np.round(data[:,:,"MilitaryPoints"]*1000.0/ \
                              np.nanmax(data[:,refYear,"MilitaryPoints"])))

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
        a+=data[:,:,"IEPG.Economic."+vEconomic[i]+"_IEPG"]*cEconomic[i]
    
    data.addVariable("IEPG.Global.Economic", data=a/100.0)

    a = np.zeros((shape[0],shape[1]))
    for i in range(0, len(cMilitary)):
        a+=data[:,:,"IEPG.Military."+vMilitary[i]+"_IEPG"]*cMilitary[i]
    
    data.addVariable("IEPG.Global.Military", data=a/100.0)

    a = np.zeros((shape[0],shape[1]))
    for i in range(0, len(cSoft)):
        a+=data[:,:,"IEPG.Soft."+vSoft[i]+"_IEPG"]*cSoft[i]
    
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
        a = data[:,:,i]/ \
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
                                                 'Energy QUOTE',
                                                 'Primary Goods QUOTE',
                                                 'Manufactures QUOTE',
                                                 'Services QUOTE',
                                                 'Investments QUOTE',
                                                 'Troops QUOTE',
                                                 'Military Equipment QUOTE',
                                                 'Migrations QUOTE',
                                                 'Tourism QUOTE',
                                                 'Sports QUOTE',
                                                 'Culture QUOTE',
                                                 'Information QUOTE',
                                                 'Technology QUOTE',
                                                 'Science QUOTE',
                                                 'Education QUOTE',
                                                 'Development Coop. QUOTE',
                                                 'Economic QUOTE',
                                                 'Military QUOTE',
                                                 'Soft QUOTE',
                                                 'IEPG QUOTE',
                                                 'Energy CONTRIBUTION',
                                                 'Primary Goods CONTRIBUTION',
                                                 'Manufactures CONTRIBUTION',
                                                 'Services CONTRIBUTION',
                                                 'Investments CONTRIBUTION',
                                                 'Troops CONTRIBUTION',
                                                 'Military Equipment CONTRIBUTION',
                                                 'Migrations CONTRIBUTION',
                                                 'Tourism CONTRIBUTION',
                                                 'Sports CONTRIBUTION',
                                                 'Culture CONTRIBUTION',
                                                 'Information CONTRIBUTION',
                                                 'Technology CONTRIBUTION',
                                                 'Science CONTRIBUTION',
                                                 'Education CONTRIBUTION',
                                                 'Development Coop. CONTRIBUTION'])

    ew.addStyle("header", {
        "bg_color": "#08608C",
        "font_color": "white",
        "valign": "vcenter",
        "align": "center",
        "size": 12
    })

    for name,sheet in sheets.iteritems():
        print name, sheet
        ew.setColumnStyle(sheet, 0, 0, 25)
        ew.setRowStyle(sheet, 0, 20, style="header")

        

    ew.closeWorkbook()

    return(send_file(outFileName, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", 
                     attachment_filename="Real_Instituto_Elcano-Calculo_IEPG.xlsx",
                     as_attachment=True))

