# coding=UTF8

# This module reads IEPG data from Excel
# ASSUMPTIONS: Data are ordered by code and years are also ordered

import data.excel_utils as excel_utils, data.core as core, ast, numpy as np
reload(excel_utils)
reload(core)

book = excel_utils.ExcelReader("Prototipo hoja de datos.xlsx", decimalSeparator=",")

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
    environment[i[0].value] = ast.literal_eval(i[1].value)

data = core.GeoVariableArray()

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
        d = np.fmax(np.round(data[:,:,i]*1000.0/np.nanmax(data[:,"2010",i])), data[:,:,i+"Est"])
    else:
        d = np.round(data[:,:,i]*1000.0/np.nanmax(data[:,"2010",i]))

    data.addVariable(i+"_IEPG", data=d)

# Sports calculus
linearCoef = [0.48,0.56,0.58,0.82,1,1,1,1]

sports = ((75.0/np.repeat( \
        np.nansum(data[:,:,"IEPG.Soft.Support.Olimpics"], axis=0).reshape(1,8), 70, axis=0).reshape(70,8)* \
              10000*data[:,:,"IEPG.Soft.Support.Olimpics"])+ \
              (25.0/np.repeat( \
        np.nansum(data[:,:,"IEPG.Soft.Support.FIFAPoints"], axis=0).reshape(1,8), 70, axis=0).reshape(70,8)* \
                   10000*data[:,:,"IEPG.Soft.Support.FIFAPoints"]))* \
                   np.repeat(np.array(linearCoef).reshape(1,8), 70, axis=0)

data.addVariable("IEPG.Soft.SportsCoef", data=sports)
data.addVariable("IEPG.Soft.Sports_IEPG", data=
                 np.round(data[:,:,"IEPG.Soft.SportsCoef"]*1000.0/ \
                              np.nanmax(data[:,"2010","IEPG.Soft.SportsCoef"])))

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
    militaryCoefs.append(np.nansum(data[:,"2010",militaryEquipment])/np.nansum(data[:,"2010",i]))

militaryTotal = np.nansum(np.array(militaryCoefs))

for i in militaryCoefs:
    militaryCoefsEquip.append(i/militaryTotal)

ae = np.zeros((70,8))

for i in range(0, len(militaryCoefsEquip)):
    ae+=militaryCoefsEquip[i]*np.nan_to_num(data[:,:,militaryEquipment[i]])

data.addVariable("MilitaryPoints", data=ae)    

data.addVariable("IEPG.Military.MilitaryEquipment_IEPG", data=
                 np.round(data[:,:,"MilitaryPoints"]*1000.0/ \
                              np.nanmax(data[:,"2010","MilitaryPoints"])))

# Dimensions and Index
cEconomic = [18,13,20,23,26]
vEconomic = ["Energy","PrimaryGoods","Manufactures","Services","Investments"]
cMilitary = [51,49]
vMilitary = ["Troops", "MilitaryEquipment"]
cSoft = [9,9,7,15,13,13,12,12,10]
vSoft = ["Migrations", "Tourism", "Sports", "Culture", "Information", "Technology", "Science",
         "Education", "DevelopmentC"]
cIndex = [38,16,46]

a = np.zeros((70,8))
for i in range(0, len(cEconomic)):
    a+=data[:,:,"IEPG.Economic."+vEconomic[i]+"_IEPG"]*cEconomic[i]
    
data.addVariable("IEPG.Global.Economic", data=a/100.0)

a = np.zeros((70,8))
for i in range(0, len(cMilitary)):
    a+=data[:,:,"IEPG.Military."+vMilitary[i]+"_IEPG"]*cMilitary[i]
    
data.addVariable("IEPG.Global.Military", data=a/100.0)

a = np.zeros((70,8))
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
        (np.repeat(np.nansum(data[:,:,i], axis=0).reshape(1,8), 70, axis=0))

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


