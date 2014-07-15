# coding=UTF8

"""

Download section.


"""
from flask import jsonify, request, send_file
from frontend import app
import common.helpers as chelpers
import common.datacache as dc
from common.config import backend
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
    # if os.path.isfile(fileName):
    #     return(send_file(fileName, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", 
    #                      attachment_filename="Real_Instituto_Elcano-Solicitud_datos_IEPG.xlsx",
    #                      as_attachment=True))

    data = {
        "year": sorted(years.split(",")),
        "variable": variables.split(","),
        "country": countries.split(",")
    }
    translate = dc.isoToEnglish if language=="en" else dc.isoToSpanish

    tabs = ["year", "country", "variable"]
    tabs.remove(columns)
    tabs.remove(rows)
    tabs = tabs[0]

    workbook = xlsxwriter.Workbook(fileName)
    url_format = workbook.add_format({
        "font_color": "blue",
        "underline": 1
    })
    title_format = workbook.add_format({
        "font_color": "white",
        "size": 20,
        "valign": "vcenter",
        "pattern": 1,
        "bg_color": "orange"
    })
    bold_format = workbook.add_format({
        "bold": True
    })
    header_format = workbook.add_format({
        "bg_color": "#08608C",
        "font_color": "white",
        "valign": "vcenter",
        "size": 12
    })
    highlight = workbook.add_format({
        "bg_color": "#eeeeee",
        "valign": "vcenter"
    })
    no_highlight = workbook.add_format({
        "bg_color": "#ffffff",
        "valign": "vcenter"
    })

    print "Config : ",tabs,rows,columns


    allVariables = dict()
    for var in data["variable"]:
        varName, varFamily = var.split("@")
        allVariables[varFamily+"@"+varName] = dc.dataSets[varFamily].variables[varName]
        allVariables = OrderedDict(sorted(allVariables.items(), key=lambda t: 
                                          const.variableNames[t[0].split("@")[0]][t[0].split("@")[1]]["order"]))

    print "All : ", allVariables


    for tabData in data[tabs]:
        print "Tab : ", tabData
        col = 1

        if tabs=="variable":
            varSplitted = tabData.split("@")
            varName = unicode(const.variableNames[varSplitted[1]][varSplitted[0]]["name_"+language])
            if varSplitted[1]=="IEPG":
                familyName = u"Presencia global" if language=="es" else u"Global Presence"
            else:
                familyName = u"Presencia Europea" if language=="es" else u"European Presence"
            tabName = (varName+u" ("+familyName+u")")
            tabTag = tabName if len(tabName)<31 else tabName[0:28]+u"..."

            title = u"Data from Elcano Global Presence Index (Data for "+tabName+")" if language=="en" \
                    else u"Datos del Índice de Presencia Global Elcano (Datos para "+tabName+")"
            variable = allVariables[varSplitted[1]+"@"+varSplitted[0]]

        worksheet = workbook.add_worksheet(tabTag)
        worksheet.set_row(0,30,title_format)
        worksheet.write(0,0,title)

        print data[columns]

        for rowData in data[rows]:
            print "Row : ", rowData
            if rows=="year":
                year=rowData
            if rows=="country":
                country=rowData

            for colData in data[columns]:
                print "Column :",colData
                if columns=="country":
                    country=colData
                if columns=="year":
                    year=colData

                data = chelpers.getData(variable, year=year, code=country)
                print "Data : ",variable,year,country,data
        # for k,v in allVariables.iteritems():

    #     #     print "jd :", k,v

    #     #     data = sorted(chelpers.getData(v, countryList=countries, year=year).values(),
    #     #                   key=lambda t: translate[t["code"]])
    #     #     family,name = k.split("@")
    #     #     worksheet.set_row(1,22,header_format)
    #     #     worksheet.write(1,col,family.upper()+": "+
    #     #                     const.variableNames[family][name]["name_"+language].decode("utf-8"), header_format)
    #     #     row = 2
    #     #     for d in data:
    #     #         if (row-1)%3==0:
    #     #             worksheet.set_row(row,15,highlight)
    #     #         else:
    #     #             worksheet.set_row(row,15,no_highlight)
    #     #         worksheet.write(row, 0, translate[d["code"]].decode("utf-8"))
    #     #         worksheet.set_column(0, 0, 25)
    #     #         worksheet.write(row, col, d["value"])
    #     #         worksheet.set_column(col, col, 15)
    #     #         row+=1
    #     #     col+=1

    #     row = 10

    #     worksheet.write(row+1, 0, "Más información:".decode("utf-8") if language=="es" else 
    #                     "More information:".decode("utf-8"), bold_format)
    #     worksheet.write_url(row+1, 1, "http://www.globalpresence.realinstitutoelcano.org", url_format,
    #                         "http://www.globalpresence.realinstitutoelcano.org")
    workbook.close()

    return(send_file(fileName, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", 
                     attachment_filename="Real_Instituto_Elcano-Solicitud_datos_IEPG.xlsx",
                     as_attachment=True))
