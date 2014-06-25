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


@app.route('/download/<string:language>/<string:years>/<string:variables>/<string:countries>', methods=["GET"])
def getDownloadData(language, years, variables, countries):
    """Gets download data. Call examples:

    /download/es/1990,1995,2000,2005/energy@iepg,soft@iepg,military@iepg,soft@iepe,energy@iepg/EN,ES,US,GB,FR
    
    /download/en/1990,2000/energy@iepg,energy@iepe,iepg,iepe,military_presence@iepg,military_presence@iepe/EN,ES,US
    """
    fileName = os.path.join(backend["tmpFolder"], 
                            hashlib.sha256(request.url.strip(request.url_root)).hexdigest()+".xlsx")
    if os.path.isfile(fileName):
        return(send_file(fileName, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", 
                         attachment_filename="Real_Instituto_Elcano-Solicitud_datos_IEPG.xlsx",
                         as_attachment=True))

    years = sorted(years.split(","))
    variables = variables.split(",")
    countries = countries.split(",")
    translate = dc.isoToEnglish if language=="en" else dc.isoToSpanish
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

    allVariables = dict()
    for var in variables:
        varSplitted = var.split("@")
        if len(varSplitted)==1:
            varFamily = varSplitted[0]
            varName = None
        else:
            varName, varFamily = varSplitted
        if varName:
            allVariables = dict(allVariables.items()+{varFamily+"@"+dc.dataSets[varFamily].variables[varName].id:
                                                      dc.dataSets[varFamily].variables[varName]}.items())
        else:
            allVariables = dict(allVariables.items()+{varFamily+"@"+k: v for (k,v)
                                                      in dc.dataSets[varFamily].variables.iteritems()}.items())


        allVariables = OrderedDict(sorted(allVariables.items(), key=lambda t: 
                                          const.variableNames[t[0].split("@")[0]][t[0].split("@")[1]]["order"]))

    for year in years:
        col = 1
        worksheet = workbook.add_worksheet(('Datos año '+str(year)).decode("utf-8"))
        title = "Data from Elcano Global Presence Index (year "+str(year)+")" if language=="en" else \
                "Datos del Índice de Presencia Global Elcano (año "+str(year)+")"
        worksheet.set_row(0,30,title_format)
        worksheet.write(0,0,title.decode("utf-8"))
        for k,v in allVariables.iteritems():
            data = sorted(chelpers.getData(v, countryList=countries, year=year).values(),
                          key=lambda t: translate[t["code"]])
            family,name = k.split("@")
            worksheet.set_row(1,22,header_format)
            worksheet.write(1,col,family.upper()+": "+
                            const.variableNames[family][name]["name_"+language].decode("utf-8"), header_format)
            row = 2
            for d in data:
                if (row-1)%3==0:
                    worksheet.set_row(row,15,highlight)
                else:
                    worksheet.set_row(row,15,no_highlight)
                worksheet.write(row, 0, translate[d["code"]].decode("utf-8"))
                worksheet.set_column(0, 0, 25)
                worksheet.write(row, col, d["value"])
                worksheet.set_column(col, col, 15)
                row+=1
            col+=1

        worksheet.write(row+1, 0, "Más información:".decode("utf-8") if language=="es" else 
                        "More information:".decode("utf-8"), bold_format)
        worksheet.write_url(row+1, 1, "http://www.globalpresence.realinstitutoelcano.org", url_format,
                            "http://www.globalpresence.realinstitutoelcano.org")
    workbook.close()

    return(send_file(fileName, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", 
                     attachment_filename="Real_Instituto_Elcano-Solicitud_datos_IEPG.xlsx",
                     as_attachment=True))