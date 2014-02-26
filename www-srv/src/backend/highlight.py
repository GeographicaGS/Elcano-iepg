# coding=UTF8

"""

Highlight services

"""

from backend import app
from flask import jsonify,request,session
from model.highlightmodel import HighlightModel
from utils import auth
import config

@app.route('/highlight', methods=['POST'])
@auth
def createHightlight():
    """Creates a new highlight."""
    m = HighlightModel()
    out = m.createHighlight(request.json)

    moveImgFile(request.json["image_hash_en"])
    moveImgFile(request.json["image_hash_es"])

    return(jsonify({"result": {"id_highlight": out}}))


@app.route('/highlight', methods=['PUT'])
@auth
def editHightlight():
    """Edits a highlight."""
    m = HighlightModel()
    oldHighlight = m.getHighlight(request.json["id_highlight"])

    if oldHighlight["image_hash_en"]!=request.json["new_image_hash_en"]:
        deleteImgFile(oldHighlight["image_hash_en"])
        moveImgFile(request.json["new_image_hash_en"])        

    if oldHighlight["image_hash_es"]!=request.json["new_image_hash_es"]:
        deleteImgFile(oldHighlight["image_hash_es"])
        moveImgFile(request.json["new_image_hash_es"])

    out = m.editHighlight(request.json)
    return(jsonify({"result": {"id_highlight": out}}))


def deleteImgFile(hash):
    file = config.cfgBackend["mediaFolder"]+"/"+hash+".png"
    print("Remove: ", file)
    # os.remove(file)


def moveImgFile(hash):
    origin = config.cfgBackend["tmpFolder"]+"/"+hash+".png"
    destination = config.cfgBackend["mediaFolder"]+"/"+hash+".png"
    # os.rename(origin, destination)
    print("Move: ", origin, destination)
