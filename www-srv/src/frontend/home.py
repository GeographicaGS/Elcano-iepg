# coding=UTF8

"""

Frontend home services.


"""
from frontend import app
from flask import jsonify,request
from model.homemodel import HomeModel
from model.iepgdatamodel import IepgDataModel
from model.highlightmodel import HighlightModel
from model.labelmodel import LabelModel
import helpers
import collections
import config
import cons
from model.helpers import ElcanoError, ElcanoErrorBadNewsSection, ElcanoErrorBadLanguage

@app.route('/home/slider/<string:lang>', methods=['GET'])
def getSliderFrontend(lang):
    """Gets the slider's data."""
    m = HighlightModel()
    
    try:
        out = m.getSliderFrontend(lang)
        return(jsonify({"results": out}))
    except ElcanoErrorBadLanguage as e:
        return(jsonify(e.dict()))


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
      section= 1=Blog/2=Media/3=Events/4=Documents/5=Twitter: optional. If absent, sends
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
    l = LabelModel()
    lang = request.args["lang"]
    section = int(request.args["section"]) if "section" in request.args else None

    try:
        labels = l.getLabels(lang)
        if section:
            if section in [1,2,3]:
                stuff = m.newStuffSections(lang, section)
            elif section==4:
                stuff = m.newStuffDocuments(lang)
            elif section==5:
                timeline = helpers.twitterGetLatestTweets()
                stuff = []
                for tweet in timeline:
                    stuff.append({
                        "id" : tweet.id,
                        "time" : tweet.created_at,
                        "title" : tweet.text,
                        "section" : "Twitter",
                        "labels" :[],
                        "wwwuser" : "@rielcano"
                    })
            else:
                e = ElcanoErrorBadNewsSection(section)
                return(jsonify(e.dict()))
        else:
            stuff = m.newStuffAll(lang)
    except ElcanoError as e:
        return(jsonify(e.dict()))

    for s in stuff:
        lab = []
        if s["labels"]!=[None]:
            for l in s["labels"]:
                for a in labels:
                    if str(a["id"])==str(l):
                        lab.append(a)

        s["labels"] = lab

    return(jsonify({"results": stuff}))
