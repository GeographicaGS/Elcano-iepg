# coding=UTF8

"""

Variable engine services.

"""
from backend import app
import varengine.varenginemodel as enginemodel
from backend.utils import auth
from flask import jsonify, request
import datetime


@app.route('/engine/addvariable', methods=["POST"])
@auth
def addVariable():
    """Adds a variable. Gets a JSON:
    {
    "name_en": "name_en",
    "name_es": "name_es",
    "description_en": "description_en",
    "description_es": "description_es",
    "continuous": true,
    "id_family": 1,
    "var_table": "var_table",
    "var_column": "var_column"
    }
    """
    m = enginemodel.EngineModel()
    descriptionEn = None
    descriptionEs = None
    j = request.json
    if j["description_en"]<>"":
        descriptionEn = j["description_en"]
    if j["description_es"]<>"":
        descriptionEs = j["description_es"]
    return(jsonify({"id_variable": m.addVariable(j["name_en"], j["name_es"], j["continuous"],
                                                 j["id_family"], j["var_table"], j["var_column"],
                                                 descriptionEn=descriptionEn, 
                                                 descriptionEs=descriptionEs)}))


@app.route('/engine/getvariables', methods=["GET"])
@auth
def getVariables():
    """Returns variables."""
    pass
    # m = enginemodel.EngineModel()
    # return(jsonify({"results": m.getVariables()}))


@app.route('/engine/getvariable/<int:idVariable>', methods=["GET"])
@auth
def getVariable(idVariable):
    """Returns variable with ID idVariable."""
    pass
    # m = enginemodel.EngineModel()
    # return(jsonify(m.getVariable(idVariable)))


@app.route('/engine/getvariablecodes/<int:idVariable>', methods=["GET"])
@auth
def getVariableCodes(idVariable):
    """Returns available codes for variable idVariable. Request.args:
    date_in: date in in ISO
    date_out: date out in ISO

    TODO: get down to the hour
    """
    pass
    # m = enginemodel.EngineModel()
    # dateIn = None
    # dateOut = None
    # if "date_in" in request.args:
    #     dateIn = request.args["date_in"]
    #     if dateIn == "":
    #         dateIn = None
    #     else:
    #         dateIn = datetime.datetime.strptime(dateIn, '%Y-%m-%d')
    # if "date_out" in request.args:
    #     dateOut = request.args["date_out"]
    #     if dateOut == "":
    #         dateOut = None
    #     else:
    #         dateOut = datetime.datetime.strptime(dateOut, '%Y-%m-%d')

    # variable = m.getVariable(idVariable)
    # return(jsonify({"results": m.getVariableCodes(variable["var_table"], dateIn=dateIn, dateOut=dateOut)}))


@app.route('/engine/addfamily', methods=["POST"])
@auth
def addFamily():
    """Adds a variable family. Gets a JSON:
    {
    "name_en": "name_en",
    "name_es": "name_es",
    "description_en": "description_en",
    "description_es": "description_es"
    }
    """
    m = enginemodel.EngineModel()
    descriptionEn = None
    descriptionEs = None
    j = request.json
    if j["description_en"]<>"":
        descriptionEn = j["description_en"]
    if j["description_es"]<>"":
        descriptionEs = j["description_es"]
    return(jsonify({"id_family": m.addFamily(j["name_en"], j["name_es"],
                                               descriptionEn=descriptionEn, 
                                               descriptionEs=descriptionEs)}))


@app.route('/engine/getfamilies', methods=["GET"])
@auth
def getFamilies():
    """Returns families."""
    m = enginemodel.EngineModel()
    return(jsonify({"results": m.getFamilies()}))


# @app.route('
