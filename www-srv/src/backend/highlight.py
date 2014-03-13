# coding=UTF8

"""

Highlight services

"""
from backend import app
from flask import jsonify,request,session
from model.highlightmodel import HighlightModel
from utils import auth
from werkzeug.utils import secure_filename
import werkzeug
import config
import os
import hashlib
import time


@app.route('/highlight/setorder', methods=['PUT'])
@auth
def setHighlightOrder():
    """Sets the order of published highlights. Receives a JSON in the form:

        {
            "order": [3,1,2,6]
        }
    
    where numbers are the indexes of published highlights."""
    m = HighlightModel()
    return(jsonify({"ordered": m.setHighlightOrder(request.json["order"])}))


@app.route('/highlight/togglepublish/<int:id>', methods=['PUT'])
@auth
def togglePublishHighlight(id):
    """Toggles the published status of a highlight. Uses a parameter:

        id: mandatory, id of the highlight to be toggled
    """
    m = HighlightModel()
    out = m.togglePublishHighlight(id)

    return(jsonify({"new_status": out}))


@app.route('/highlight/active/<string:lang>', methods=['GET'])
@auth
def getActiveHighlight():
    """Returns the list of active highlights. Requires parameters:

        lang: mandatory, en/es
    """
    m = HighlightModel()
    

@app.route('/highlight', methods=['POST'])
@auth
def createHightlight():
    """Creates a new highlight. Recieves a JSON in the form:

    {
        "title_en": "title_en",
        "title_es": "title_es",
        "text_en": "text_en",
        "text_es": "text_es",
        "image_name_en": "image_name_en",
        "image_name_es": "image_name_es",
        "image_hash_en": "image_hash_en",
        "image_hash_es": "image_hash_es",
        "link_en": "link_en",
        "link_es": "link_es",
        "credit_img_en": "credit_img_en",
        "credit_img_es": "credit_img_es"
    }"""
    m = HighlightModel()
    out = m.createHighlight(request.json)

    moveImgFile(request.json["image_hash_en"])
    moveImgFile(request.json["image_hash_es"])

    return(jsonify({"id_highlight": out}))


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
    file = config.cfgBackend["mediaFolder"]+"/"+hash+".jpg"
    os.remove(file)


def moveImgFile(hash):
    origin = config.cfgBackend["tmpFolder"]+"/"+hash+".jpg"
    destination = config.cfgBackend["mediaFolder"]+"/"+hash+".jpg"
    os.rename(origin, destination)


def allowedFileImg(filename):
    """Image file extensions allowed to upload."""
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ["jpg"]


@app.route("/highlight/upload_img",methods=["POST"])
@auth
def uploadImg():
    """Uploads a image."""
    try:
        file = request.files['file']
        if file and allowedFileImg(file.filename):
            filename = secure_filename(file.filename)
            filename, fileExtension = os.path.splitext(filename)
            filename = hashlib.md5(str(time.time())+ session["email"]).hexdigest() + fileExtension
            file.save(os.path.join(config.cfgBackend['tmpFolder'], filename))
            return jsonify(  {"filename": filename} )  
        
        return jsonify(  {"error": -1} )    
    
    except werkzeug.exceptions.UnsupportedMediaType:
        return jsonify(  {"error": -2} )
    
    except werkzeug.exceptions.RequestEntityTooLarge:
        return jsonify(  {"error": -3} )
