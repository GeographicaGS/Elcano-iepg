from backend import app
from flask import jsonify,request,session
from model.labelmodel import LabelModel
from utils import auth

# There is no delete method, remember that labels are deleted by a
# trigger

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
