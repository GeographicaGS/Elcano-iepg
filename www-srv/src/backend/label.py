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


@app.route("/label/<string:lang>", methods=["POST"])
@auth
def newLabel(lang):
    """Creates a new label."""
    m = LabelModel()
    
    return jsonify({"id": \
                    m.insertLabel(request.json["label"], lang)})

