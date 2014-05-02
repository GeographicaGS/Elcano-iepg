# coding=UTF8

"""

Explora country services.

"""
from explora import app
from flask import jsonify,request,send_file,make_response
from common.helpers import cacheWrapper, baseMapData
import cons
import json
from model import iepgdatamodel, basemap
from common.errorhandling import ElcanoApiRestError
from common.const import context_variables, iepg_variables, years

@app.route('/country/<string:country>/<int:year>/<int:variable>/<string:lang>', methods=['GET'])
def country(country,year,variable,lang):
    return jsonify({
        "id_country" : country,
        "name": "España",
        "year" : year,
        "lang" : lang,
        "variable" : variable,
        "summary" : "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"
    })


# Those are the ones

@app.route('/countryfilter/<string:lang>', methods=['GET'])
def countryFilter(lang):
    m = iepgdatamodel.IepgDataModel()
    try:
        return(jsonify({"results": cacheWrapper(m.countryFilter, lang)}))
    except ElcanoApiRestError as e:
        return(jsonify(e.toDict()))


@app.route('/countrysheet/<string:lang>/<string:countryCode>', methods=['GET'])
def countrySheet(lang, countryCode):
    """Retrieves all the data, for all years, and for a single country, to render the country sheet.
    Service call:

    /countrysheet/es/US?filter=US,DK,ES
    
    """
    m = iepgdatamodel.IepgDataModel()
    filter = None
    if "filter" in request.args:
        filter=(None if request.args["filter"].split(",")[0]=="" else request.args["filter"].split(","))
    try:
        data = dict()
        for year in years:
            y = dict()
            iepg_var = dict()
            for var,item in iepg_variables.items():
                if filter:
                    rankData = cacheWrapper(m.ranking, lang, countryCode, 
                                                           var, year, filter=filter)
                else:
                    rankData = cacheWrapper(m.ranking, lang, countryCode, var, year)
                    
                iepg_var[var] = rankData[0]

            context_var = dict()
            for var,item in context_variables.items():
                if filter:
                    rankData = cacheWrapper(m.ranking, lang, countryCode, 
                                                              var, year, filter=filter)
                else:
                    rankData = cacheWrapper(m.ranking, lang, countryCode, var, year)

                context_var[var] = rankData[0]

            y["iepg_variables"] = iepg_var
            y["context_var"] = context_var
            y["comment"] = cacheWrapper(m.getIepgComment, lang, countryCode, year)[0]
            data[year]=y
        return(jsonify({"results": data}))
    except ElcanoApiRestError as e:
        return(jsonify(e.toDict()))


@app.route('/mapdata/<string:variable>/<int:year>', methods=['GET'])
def mapData(variable, year):
    """Retrieves map data. Service call:
    
    /mapdata/es/economic_presence/2013?filter=US,DK,ES&toolfilter=US,DK

    """
    filter = None
    if "filter" in request.args:
        filter=(None if request.args["filter"].split(",")[0]=="" else request.args["filter"].split(","))
    toolFilter = None
    if "toolfilter" in request.args:
        toolFilter=(None if request.args["toolfilter"].split(",")[0]=="" else \
                    request.args["toolfilter"].split(","))
    m = iepgdatamodel.IepgDataModel()

    try:
        varData = cacheWrapper(m.variableData, variable, year, filter=filter, toolFilter=toolFilter)
    except ElcanoApiRestError as e:
        return(jsonify(e.toDict()))    

    return(jsonify({"results": varData}))


@app.route('/mapgeojson', methods=['GET'])
def mapGeoJson():
    """Returns the map GeoJSON."""
    m = basemap.GeometryData()
    data = cacheWrapper(m.geometryData)
    out = dict()
    out["type"] = "FeatureCollection"
    
    features = []
    for d in data:
        print(d)
        f = dict()
        f["type"] = "Feature"
        f["geometry"] = json.loads(d["geojson"])
        fp = dict()
        fp["code"] = d["iso_3166_1_2_code"]
        fp["name_en"] = d["name_en"]
        fp["name_es"] = d["name_es"]
        f["properties"] = fp
        features.append(f)

    out["features"] = features

    return(jsonify(out))
