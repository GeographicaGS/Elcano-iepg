# coding=UTF8

"""

Maplex services

"""
import model.maplexmodel as maplexmodel
from backend import app
from flask import jsonify, request
from backend.utils import auth
import datetime

@app.route('/maplex/addname', methods=["POST"])
@auth
def addName():
    """Adds a name. Needs a JSON:

    {
    "name": "New name",
    "description": "New description"
    }

    Returns reference ID to the new name."""
    # m = maplexmodel.MaplexModel()
    # j = request.json
    # id = m.newName(j["name"], j["description"])
    # return(jsonify({"id_name": id}))


@app.route('/maplex/getnamefamilies', methods=["GET"])
@auth
def getNameFamilies():
   """Returns name families."""
   # m = maplexmodel.MaplexModel()
   # return(jsonify({"results": m.getNameFamilies()}))


@app.route('/maplex/assigngeoentityname/<int:id_geoentity>/<int:id_name>/<int:id_name_family>', 
           methods=["POST"])
@auth
def assignGeoentityName(id_geoentity, id_name, id_name_family):
    """Assign a name to a geoentity. Request.args:
    date_in: date in in ISO
    date_out: date out in ISO

    TODO: get down to the hour
    """
    # date_in = None
    # date_out = None
    # if "date_in" in request.args:
    #     date_in = request.args["date_in"]
    #     if date_in == "":
    #         date_in = None
    #     else:
    #         date_in = datetime.datetime.strptime(date_in, '%Y-%m-%d')
    # if "date_out" in request.args:
    #     date_out = request.args["date_out"]
    #     if date_out == "":
    #         date_out = None
    #     else:
    #         date_out = datetime.datetime.strptime(date_out, '%Y-%m-%d')
        
    # m = maplexmodel.MaplexModel()
    # id = m.assignGeoentityName(id_geoentity, id_name, id_name_family, date_in=date_in, date_out=date_out)
    # return(jsonify({"id_name": id}))


@app.route('/maplex/getgeoentities', methods=["GET"])
@auth
def getGeoentities():
   """Returns geoentities."""
   # m = maplexmodel.MaplexModel()
   # return(jsonify({"results": m.getGeoentities()}))


@app.route('/maplex/getnames', methods=["GET"])
@auth
def getNames():
   """Returns names."""
   # m = maplexmodel.MaplexModel()
   # return(jsonify({"results": m.getNames()}))
