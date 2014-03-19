# coding=UTF8

"""

Frontend home services.


"""
from frontend import app
from flask import jsonify,request
from model.homemodel import HomeModel
from model.iepgdatamodel import IepgDataModel
from model.highlightmodel import HighlightModel
import helpers
import collections
import config
import cons


@app.route('/home/slider/<string:lang>', methods=['GET'])
def getSliderFrontend(lang):
    """Gets the slider's data."""
    if lang not in cons.lang:
        return(jsonify(cons.errors["-1"]))

    m = HighlightModel()
    out = m.getSliderFrontend(lang)
    return(jsonify({"results": out}))


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
    m = IepgDataModel()
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
    m = IepgDataModel()
    a = m.years()

    return(jsonify({"results": a}))
        

@app.route('/home/newstuff', methods=['GET'])
def newStuff():
    """Returns new stuff for the new stuff control. Accepts request.args:

      lang=en/es: mandatory 

      section=Blog/Media/Events/Documents/Twitter: optional. If absent, sends
      all sections mixed

    Returns a JSON in the form:

    {
        "news":[{
    	    "id": "1",
    	    "wwwuser": "Iliana Olivié",
    	    "time": "201401101027",
	    "title": "¿El auge del resto? Apuntes sobre la presencia
	    global de América Latina, Asia y el Magreb y Oriente Medio",
    	    "section": "Blog",
    	    "labels": [
                {"id": "1", "label": "IEPG"},
    	        {"id": "2", "label": "Economía"}]
        }]
    }
    """
    m = HomeModel()

    if request.args["lang"] not in cons.lang:
        return(jsonify(cons.errors["-1"]))

    if "section" in request.args:
        if request.args["section"] not in cons.newsSections:
            return(jsonify(cons.errors["-2"]))

    labels = m.getLabels(request.args["lang"])

    if "section" in request.args:
        if request.args["section"] in ["Blog", "Media", "Events"]:
            stuff = m.newStuffSections(request.args["lang"], request.args["section"])
        elif request.args["section"]=="Documents":
            stuff = m.newStuffDocuments(request.args["lang"])
        elif request.args["section"]=="Twitter":

            import ipdb
            ipdb.set_trace()

            stuff = helpers.twitterGetLatestTweets()
            return(jsonify({"results": stuff}))
    else:
        stuff = m.newStuffAll(request.args["lang"])

    for s in stuff:
        lab = []
        if s["label"]!=[None]:
            for l in s["label"]:
                for a in labels:
                    if str(a["id"])==str(l):
                        lab.append(a)

        s["label"] = lab

    return(jsonify({"results": stuff}))
