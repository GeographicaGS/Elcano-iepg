# coding=UTF8

"""

Explora country services.

"""
from explora import app
from flask import jsonify,request,send_file,make_response
#from model.test import TestModel
from common.helpers import cacheWrapper
import cons
import model.iepgdatamodel
from common.errorhandling import ElcanoApiRestError

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


@app.route('/countries_toremove/<string:lang>', methods=['GET'])
def countries_toremove(lang):
    return jsonify({
        "results" : [{
                "id_country" : "ES",
                "name": "España",
            },
            {
                "id_country" : "FR",
                "name": "France",
            },
            {
                "id_country" : "US",
                "name": "Estados Unidos",
            },
            {
                "id_country" : "AL",
                "name": "Alemania",
            },
            {
                "id_country" : "CH",
                "name": "China",
            },
            {
                "id_country" : "RU",
                "name": "Rusia",
            },
            ]
        })


# Those are the ones

@ app.route('/countryfilter/<string:lang>', methods=['GET'])
def countryFilter(lang):
    m = model.iepgdatamodel.IepgDataModel()
    try:
        return(jsonify({"results": cacheWrapper(m.countryFilter, lang)}))
    except ElcanoApiRestError as e:
        return(jsonify(e.toDict()))
    
