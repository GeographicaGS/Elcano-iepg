# coding=UTF8

"""

Frontend home services.


"""

from frontend import app
from flask import jsonify,request
from werkzeug.utils import secure_filename
import werkzeug
import os
import hashlib
import time
import json
from model.homemodel import HomeModel
import collections
import config


@app.route('/home/document', methods=['GET'])
def getDocument():
    """Gets details of a document. Uses URL arguments:

      iddocument: mandatory, ID of the requested document
      lang: mandatory, language for document's metadata
    """
    m = HomeModel()
    pdf = m.getDocumentPdf(request.args["iddocument"])
    doc = m.getDocument(request.args["iddocument"], request.args["lang"])

    return(jsonify({"details": doc, "pdf": pdf}))


@app.route('/home/documentcatalog', methods=['GET'])
def getDocumentCatalog():
    """Gets a slice of a document list. Uses URL arguments:

      offset: mandatory, page to present
      lang: mandatory, language
      search: optional, search criteria

    """
    m = HomeModel()
    search = request.args["search"] if "search" in request.args else None
    totalSize = m.getDocumentCatalogSize(search=search)
    docs = m.getDocumentCatalog(request.args["offset"], config.cfgFrontend["DocumentListLength"], \
                             request.args["lang"], search=search)

    return(jsonify({"results": docs}))


@app.route('/home/countries', methods=['GET'])
def countries():
    """Returns list of geopolitical blocks and its countries for a
    language and a year. Parameters are:

      lang=en/es: required
      year: required

    Returns a JSON:

    {
      "block":
        {
          "name": "América",
          "ncountries": "2",
          "countries": [
            {"name": "USA"},
            {"name": "Canadá"}
          ]
        },
    }
      
    """
    m = HomeModel()
    a = m.countries(request.args["lang"], request.args["year"])
    blocks=dict()
    countries = dict()
    final = dict()
    
    for r in a:
        if r["block_name"] not in blocks.keys():
            blocks[r["block_name"]]=dict()
            blocks[r["block_name"]]["countries"] = [r["country_name"]]
        else:
            blocks[r["block_name"]]["countries"].append(r["country_name"])

    for key, value in blocks.items():
        value["ncountries"] = len(value["countries"])

    od = collections.OrderedDict(sorted(blocks.items()))

    return(jsonify(od))


@app.route('/home/years', methods=['GET'])
def years():
    """Returns the list of years in IEPG data. JSON is:

    {
      "results": [
        {
          "year": "2012"
        }
      ]
    }

    """
    m = HomeModel()

    a = m.years()

    return(jsonify({"results": a}))
        

@app.route('/home/newstuff', methods=['GET'])
def newStuff():
    """Returns new stuff for the new stuff control. Accepts parameters:

      lang=en/es: mandatory 

      section=Blog/Media/Events/Documents: optional. If absent, sends
      all sections mixed

    Returns a JSON in the form:

    {
        "news":[{
    	    "id": "1",
    	    "user": "Iliana Olivié",
    	    "time": "201401101027",
	    "title": "¿El auge del resto? Apuntes sobre la presencia
	    global de América Latina, Asia y el Magreb y Oriente Medio",
    	    "section": "Blog",
    	    "labels": [
                {"label": "IEPG"},
    	        {"label": "Economía"}]
        }]
    }"""
    m = HomeModel()
    
    if "section" in request.args:
        a = m.newStuff(request.args["lang"], request.args["section"])
    else:
        a = m.newStuff(request.args["lang"])

    return(jsonify({"results": a}))
