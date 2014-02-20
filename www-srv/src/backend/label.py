from backend import app
from flask import jsonify,request,session
from model.labelmodel import LabelModel
# import utils
# import hashlib

@app.route('/label/<string:lang>', methods=['GET'])
def getLabels(lang):
    """Returns labels."""
    m = LabelModel()
    return jsonify({'results': m.getLabels(lang)})
