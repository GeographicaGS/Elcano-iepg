from backend import app
from flask import jsonify,request,session
from model.labelmodel import LabelModel
from utils import auth
# import hashlib

@app.route("/label/<string:lang>", methods=["GET"])
@auth
def getLabels(lang):
    """Returns labels."""
    m = LabelModel()
    return jsonify({"results": m.getLabels(lang)})


@app.route("/label/new", methods=["POST"])
@auth
def newLabel():
    """Creates a new label."""
    m = LabelModel()
    return jsonify({"results": \
                    m.insertLabel(request.json["label"]["label"], request.json["label"]["language"])})

