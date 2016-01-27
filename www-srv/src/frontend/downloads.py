# coding=UTF8

"""

Download section.


"""
from flask import jsonify, request, send_file
from frontend import app
import common.helpers as chelpers
import common.datacache as dc
from common.config import backend, basePath
import xlsxwriter
import common.const as const
from collections import OrderedDict
import hashlib
import os.path


@app.route('/download/<string:language>/<string:years>/<string:variables>/<string:countries>/<string:rows>/<string:columns>', methods=["GET"])
def getDownloadData(language, years, variables, countries, rows, columns):
    """Gets download data. Call examples:

    /download/es/1990,1995,2000,2005/energy@iepg,soft@iepg,military@iepg,soft@iepe,energy@iepg/EN,ES,US,GB,FR/year/variable
    
    /download/en/1990,2000/energy@iepg,energy@iepe,iepg,iepe,military_presence@iepg,military_presence@iepe/EN,ES,US/country/variable

    Both columns and rows can have the following values: year, country, variable
    """
    fileName = os.path.join(backend["tmpFolder"], 
                            hashlib.sha256(request.url.strip(request.url_root)).hexdigest()+".xlsx")

    # # Try to get file from cache
    # if os.path.isfile(fileName):
    #     return(send_file(fileName, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", 
    #                      attachment_filename="Real_Instituto_Elcano-Solicitud_datos_IEPG.xlsx",
    #                      as_attachment=True))

    translate = dc.isoToEnglish if language=="en" else dc.isoToSpanish
    years = sorted(years.split(","))
    variables = variables.split(",")
    countryList = countries.split(",")
    countries = sorted([{k: v} for (k,v) in translate.iteritems() if k in countryList], 
                       key=lambda t: t.values()[0])

    tabs = ["year", "country", "variable"]
    tabs.remove(columns)
    tabs.remove(rows)
    tabs = tabs[0]

    workbook = xlsxwriter.Workbook(fileName)

    url_format = workbook.add_format({
        "font_color": "blue",
        "underline": 1,
        "bg_color": "white",
        "size": 10
    })

    title_format = workbook.add_format({
        "font_color": "white",
        "size": 20,
        "valign": "vcenter",
        "pattern": 1,
        "bg_color": "#A6192E",
    })

    bold_format = workbook.add_format({
        "bold": True
    })

    header_format = workbook.add_format({
        "bg_color": "#FFCD33",
        "text_wrap": "True",
        "valign": "vcenter",
        "align": "center",
        "size": 12
    })

    highlight = workbook.add_format({
        "bg_color": "#eeeeee",
        "valign": "vcenter",
        "num_format": "0.00",
        "text_wrap": "True",
        "align": "center",
        "size": 10
    })

    no_highlight = workbook.add_format({
        "bg_color": "#ffffff",
        "valign": "vcenter",
        "num_format": "0.00",
        "text_wrap": "True",
        "align": "center",
        "size": 10
    })

    highlightL = workbook.add_format({
        "bg_color": "#eeeeee",
        "valign": "vcenter",
        "num_format": "0.00",
        "text_wrap": "True",
        "align": "left",
        "size": 10
    })

    no_highlightL = workbook.add_format({
        "bg_color": "#ffffff",
        "valign": "vcenter",
        "num_format": "0.00",
        "text_wrap": "True",
        "align": "left",
        "size": 10
    })

    normalC = workbook.add_format({
        "text_wrap": "True",
        "valign": "vcenter",
        "align": "center",
        "size": 10
    })

    normalL = workbook.add_format({
        "text_wrap": "True",
        "valign": "vcenter",
        "size": 10,
        
    })

    info = workbook.add_format({
        "valign": "vcenter",
        "size": 10
    })

    note = workbook.add_format({
        "text_wrap": "True",
        "valign": "top",
        "align": "left",
        "size": 11
    })

    allVariables = dict()
    for var in variables:
        varName, varFamily = var.split("@")
        allVariables[varFamily+"@"+varName] = dc.dataSets[varFamily].variables[varName]
        allVariables = OrderedDict(sorted(allVariables.items(), key=lambda t: 
                                          const.variableNames[t[0].split("@")[0]][t[0].split("@")[1]]["order"]))

    metaDataSheetName = u"Nota" if language=="es" else u"Note"
    metaDataNote = const.excelExportNoteES if language=="es" else const.excelExportNoteEN
    worksheet = workbook.add_worksheet(metaDataSheetName)
    worksheet.insert_image(0,0, basePath+ \
                           "cdn/Real_instituto_elcano_logotipo.jpg", {"x_scale": 0.95, "y_scale": 1})

    worksheet.write("A7", metaDataNote, note)
    worksheet.set_row(6,100,note)
    worksheet.set_column(0,0,100,note)

    worksheet.write(8, 0, "Más información:".decode("utf-8") if language=="es" else 
                    "More information:".decode("utf-8"), info)
    worksheet.write_url(9, 0, "http://www.globalpresence.realinstitutoelcano.org", url_format,
                        "http://www.globalpresence.realinstitutoelcano.org")

    if tabs=="variable":
        varTagNum = 1
        for var in variables:
            varSplitted = var.split("@")
            varName = unicode(const.variableNames[varSplitted[1]][varSplitted[0]]["name_"+language])
            if varSplitted[1]=="iepg":
                familyName = u"(Índice de Presencia Global)" if language=="es" else \
                             u"(Global Presence Index)"
            else:
                familyName = u"(Índice de Presencia Europea)" if language=="es" else \
                             u"(European Presence Index)"
            tabName = varName+" "+familyName
            tabTag = u"Datos "+str(varTagNum) if language=="es" else u"Data "+str(varTagNum)

            title = tabName if language=="en" \
                    else tabName
            variable = allVariables[varSplitted[1]+"@"+varSplitted[0]]

            worksheet = workbook.add_worksheet(tabTag)
            worksheet.set_row(0,30, title_format)
            worksheet.set_row(1,30)
            worksheet.write(0,0,title)
            varTagNum+=1

            row = 2
            if rows=="year":
                for year in years:
                    worksheet.set_column(0,0,8)
                    if (row+2)%3==0:
                        worksheet.write(row,0,year,highlight)
                    else:
                        worksheet.write(row,0,year,no_highlight)
                    col = 1
                    for country in countries:
                        worksheet.write(1,col, unicode(country.values()[0].decode("utf-8")),header_format)
                        worksheet.set_column(col,col,15)
                        data = chelpers.getData(variable, year=year, code=country.keys()[0])
                        val = data.values()[0]["value"]
                        fval = round(float(val),2) if val!=None else None
                        worksheet.set_row(row,18)
                        if (row+2)%3==0:
                            worksheet.write(row,col,fval,highlight)
                        else:
                            worksheet.write(row,col,fval,no_highlight)
                        col+=1
                    row+=1
            else:
                for country in countries:
                    worksheet.set_column(0,0,30)
                    if (row+2)%3==0:
                        worksheet.write(row,0,unicode(country.values()[0].decode("utf-8")),highlight)
                    else:
                        worksheet.write(row,0,unicode(country.values()[0].decode("utf-8")),no_highlight)
                    col = 1
                    for year in years:
                        worksheet.write(1,col,year, header_format)
                        worksheet.set_column(col,col,8)
                        data = chelpers.getData(variable, year=year, code=country.keys()[0])
                        val = data.values()[0]["value"]
                        fval = round(float(val),2) if val!=None else None
                        worksheet.set_row(row,18)
                        if (row+2)%3==0:
                            worksheet.write(row,col,fval,highlight)
                        else:
                            worksheet.write(row,col,fval,no_highlight)
                        col+=1
                    row+=1
            
            row+=2
            worksheet.write(row, 0, "Más información:".decode("utf-8") if language=="es" else 
                            "More information:".decode("utf-8"), info)
            worksheet.write_url(row+1, 0, "http://www.globalpresence.realinstitutoelcano.org", url_format,
                                "http://www.globalpresence.realinstitutoelcano.org")

    if tabs=="year":
        for year in years:
            tabTag = u"Año "+str(year) if language=="es" else u"Year "+str(year)
            title = u"Data from Elcano Global Presence Index (Data for year "+str(year)+")" if language=="en" \
                    else u"Datos del Índice de Presencia Global Elcano (Datos para el año "+str(year)+")"

            worksheet = workbook.add_worksheet(tabTag)
            worksheet.set_row(0,30, title_format)
            worksheet.set_row(1,30)
            worksheet.write(0,0,title)

            row = 2
            if rows=="variable":
                for var in variables:
                    varSplitted = var.split("@")
                    varName = unicode(const.variableNames[varSplitted[1]][varSplitted[0]]["name_"+language])
                    if varSplitted[1]=="iepg":
                        familyName = u"global" if language=="es" else u"global"
                    else:
                        familyName = u"europea" if language=="es" else u"european"
                    colName = (varName+u" ("+familyName+u")")
                    variable = allVariables[varSplitted[1]+"@"+varSplitted[0]]
                    worksheet.set_column(0,0,30)
                    if (row+2)%3==0:
                        worksheet.write(row,0,colName,highlight)
                    else:
                        worksheet.write(row,0,colName,no_highlight)
                    col = 1
                    for country in countries:
                        worksheet.write(1,col, unicode(country.values()[0].decode("utf-8")), header_format)
                        worksheet.set_column(col,col,15)
                        data = chelpers.getData(variable, year=year, code=country.keys()[0])
                        val = data.values()[0]["value"]
                        fval = round(float(val),2) if val!=None else None
                        worksheet.set_row(row,25)
                        if (row+2)%3==0:
                            worksheet.write(row,col,fval,highlight)
                        else:
                            worksheet.write(row,col,fval,no_highlight)

                        col+=1
                    row+=1
            else:
                for country in countries:
                    worksheet.set_column(0,0,15)
                    if (row+2)%3==0:
                        worksheet.write(row,0,unicode(country.values()[0].decode("utf-8")),highlight)
                    else:
                        worksheet.write(row,0,unicode(country.values()[0].decode("utf-8")),no_highlight)
                    col = 1
                    for var in variables:
                        varSplitted = var.split("@")
                        varName = unicode(const.variableNames[varSplitted[1]][varSplitted[0]]["name_"+language])
                        if varSplitted[1]=="iepg":
                            familyName = u"global" if language=="es" else u"global"
                        else:
                            familyName = u"europea" if language=="es" else u"european"
                        colName = (varName+u" ("+familyName+u")")
                        variable = allVariables[varSplitted[1]+"@"+varSplitted[0]]
                        worksheet.write(1,col, colName,header_format)
                        worksheet.set_column(col,col,20)
                        data = chelpers.getData(variable, year=year, code=country.keys()[0])
                        val = data.values()[0]["value"]
                        fval = round(float(val),2) if val!=None else None
                        worksheet.set_row(row,25)
                        if (row+2)%3==0:
                            worksheet.write(row,col,fval,highlight)
                        else:
                            worksheet.write(row,col,fval,no_highlight)
                        col+=1
                    row+=1
            
            row+=2
            worksheet.write(row, 0, "Más información:".decode("utf-8") if language=="es" else 
                            "More information:".decode("utf-8"), info)
            worksheet.write_url(row+1, 0, "http://www.globalpresence.realinstitutoelcano.org", url_format,
                                "http://www.globalpresence.realinstitutoelcano.org")

    if tabs=="country":
        for country in countries:
            tabTag = unicode(country.values()[0].decode("utf-8"))
            title = u"Data from Elcano Global Presence Index (Data for "+tabTag+")" if language=="en" \
                    else u"Datos del Índice de Presencia Global Elcano (Datos para "+tabTag+")"

            worksheet = workbook.add_worksheet(tabTag)
            
            worksheet.set_row(0,30, title_format)
            worksheet.set_row(1,30)
            worksheet.write(0,0,title)

            row = 2
            if rows=="variable":
                for var in variables:
                    varSplitted = var.split("@")
                    varName = unicode(const.variableNames[varSplitted[1]][varSplitted[0]]["name_"+language])
                    if varSplitted[1]=="iepg":
                        familyName = u"global" if language=="es" else u"global"
                    else:
                        familyName = u"europea" if language=="es" else u"european"
                    colName = (varName+u" ("+familyName+u")")
                    variable = allVariables[varSplitted[1]+"@"+varSplitted[0]]
                    worksheet.set_column(0,0,30)
                    if (row+2)%3==0:
                        worksheet.write(row,0,colName,highlight)
                    else:
                        worksheet.write(row,0,colName,no_highlight)
                    col = 1
                    for year in years:
                        worksheet.write(1,col, year, header_format)
                        worksheet.set_column(col,col,15)
                        data = chelpers.getData(variable, year=year, code=country.keys()[0])
                        val = data.values()[0]["value"]
                        fval = round(float(val),2) if val!=None else None
                        worksheet.set_row(row,30)
                        if (row+2)%3==0:
                            worksheet.write(row,col,fval,highlight)
                        else:
                            worksheet.write(row,col,fval,no_highlight)
                        col+=1
                    row+=1
            else:
                for year in years:
                    worksheet.set_column(0,0,8)
                    if (row+2)%3==0:
                        worksheet.write(row,0,year,highlight)
                    else:
                        worksheet.write(row,0,year,no_highlight)
                    col = 1
                    for var in variables:
                        varSplitted = var.split("@")
                        varName = unicode(const.variableNames[varSplitted[1]][varSplitted[0]]["name_"+language])
                        if varSplitted[1]=="iepg":
                            familyName = u"global" if language=="es" else u"global"
                        else:
                            familyName = u"europea" if language=="es" else u"european"
                        colName = (varName+u" ("+familyName+u")")
                        variable = allVariables[varSplitted[1]+"@"+varSplitted[0]]
                        worksheet.write(1,col,colName,header_format)
                        worksheet.set_column(col,col,25)
                        data = chelpers.getData(variable, year=year, code=country.keys()[0])
                        val = data.values()[0]["value"]
                        fval = round(float(val),2) if val!=None else None
                        worksheet.write(row,col,fval,normalL)
                        worksheet.set_row(row,18)
                        if (row+2)%3==0:
                            worksheet.write(row,col,fval,highlight)
                        else:
                            worksheet.write(row,col,fval,no_highlight)
                        col+=1
                    row+=1
            
            row+=2
            worksheet.write(row, 0, "Más información:".decode("utf-8") if language=="es" else 
                            "More information:".decode("utf-8"), info)
            worksheet.write_url(row+1, 0, "http://www.globalpresence.realinstitutoelcano.org", url_format,
                                "http://www.globalpresence.realinstitutoelcano.org")

    workbook.close()

    attachName = "Real_Instituto_Elcano-Solicitud_datos_Presencia_Global.xlsx" if language=="es" else \
                 "Elcano_Royal_Institute-Global_Presence_Requested_Data.xlsx"

    return(send_file(fileName, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", 
                     attachment_filename=attachName, as_attachment=True))
