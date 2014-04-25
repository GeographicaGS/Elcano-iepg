# coding=UTF8

"""

Explora country services.

"""
from explora import app
from flask import jsonify,request,send_file,make_response
from common.helpers import cacheWrapper
import cons
import model.iepgdatamodel
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
    m = model.iepgdatamodel.IepgDataModel()
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
    m = model.iepgdatamodel.IepgDataModel()
    filter = None
    if "filter" in request.args:
        filter=request.args["filter"].split(",")
    try:
        data = dict()
        for year in years:
            y = dict()
            iepg_var = dict()
            for var,item in iepg_variables.items():
                if filter:
                    iepg_var[item["name_en"]]=cacheWrapper(m.ranking, lang, countryCode, 
                                                           var, year, filter=filter)
                else:
                    iepg_var[item["name_en"]]=cacheWrapper(m.ranking, lang, countryCode, var, year)
            context_var = dict()
            for var,item in context_variables.items():
                if filter:
                    context_var[item["name_en"]]=cacheWrapper(m.ranking, lang, countryCode, 
                                                              var, year, filter=filter)
                else:
                    context_var[item["name_en"]]=cacheWrapper(m.ranking, lang, countryCode, var, year)
            y["iepg_variables"] = iepg_var
            y["context_var"] = context_var
            y["comment"]=cacheWrapper(m.getIepgComment, lang, countryCode, year)
            data[year]=y
        return(jsonify({"results": data}))
    except ElcanoApiRestError as e:
        return(jsonify(e.toDict()))
