# coding=UTF8

"""

Highlight services for the administration backend.

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
import cons


@app.route('/highlight/<int:idHighlight>', methods=['DELETE'])
@auth
def deleteHighlight(idHighlight):
    """Deletes a highlight by ID passed in the URL."""
    m = HighlightModel()

    return(jsonify({"deleted": m.deleteHighlight(idHighlight)}))


@app.route('/highlight/<int:idHighlight>', methods=['GET'])
@auth
def getHighlight(idHighlight):
    """Gets a highlight by ID in the URL."""
    m = HighlightModel()

    return(jsonify(m.getHighlight(idHighlight)))


@app.route('/highlight/publishedcatalog', methods=['GET'])
@auth
def getPublishedHighlightCatalog():
    """Gets the highlight's published catalog."""
    return __getHighlightCatalog(True)

@app.route('/highlight/unpublishedcatalog', methods=['GET'])
@auth
def getUnpublishedHighlightCatalog():
    """Gets the unpublished highlight catalog. request.args:

      page: page to show, mandatory
      search: search criteria, optional

    """
    page = request.args["page"] if "page" in request.args else None
    search = request.args["search"] if "search" in request.args else None
    
    return __getHighlightCatalog(False, page=page, search=search)
        

def __getHighlightCatalog(published, page=None, search=None):
    """Gets the highlight's catalog."""
    m = HighlightModel()

    if page!=None:
        listSize = config.cfgBackend["UnpublishedHighlightCatalogBackendListLength"]
    else:
        listSize = None

    total, results = m.getHighlightCatalogBackend(published,page=page,listSize=listSize,search=search) 
    out = []

    for r in results:
        h = {}

        if r["title_en"]!=None and r["text_en"]!=None and r["image_hash_en"]!=None:
            h["english"] = True
        else:
            h["english"] = False

        if r["title_es"]!=None and r["text_es"]!=None and r["image_hash_es"]!=None:
            h["spanish"] = True
        else:
            h["spanish"] = False

        h["id"] = r["id_highlight"]
        h["title"] = r["title"]
        h["text"] = r["text"]
        h["edit"] = r["last_edit_time"]
        # No need of the following links
        #h["link_en"] = r["link_en"]
        #h["link_es"] = r["link_es"]
        out.append(h)

    return(jsonify({"listSize": total, "results": out}))


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
    
    try:
        moveImgFile(request.json["image_hash_en"])
        moveImgFile(request.json["image_hash_es"])

        out = m.createHighlight(request.json)
        return(jsonify({"id": out}))
    except:
        return(jsonify(cons.errors["-1"]))


@app.route('/highlight/<int:id_highlight>', methods=['PUT'])
@auth
def editHightlight(id_highlight):
    """Edits a highlight. Gets a JSON in the form:

    {
        "title_en": "title_en",
        "title_es": "title_es",
        "text_en": "text_en",
        "text_es": "text_es",
        "new_image_name_en": "new_image_name_en",
        "new_image_name_es": "new_image_name_es",
        "new_image_hash_en": "new_image_hash_en",
        "new_image_hash_es": "new_image_hash_es",
        "link_en": "link_en",
        "link_es": "link_es",
        "credit_img_en": "credit_img_en",
        "credit_img_es": "credit_img_es",
    }"""
    m = HighlightModel()
    oldHighlight = m.getHighlight(id_highlight)
    app.logger.info(oldHighlight)

    #try:
    if oldHighlight["image_hash_en"]!=request.json["image_hash_en"]:
        app.logger.info("here");
        deleteImgFile(oldHighlight["image_hash_en"])
        moveImgFile(request.json["image_hash_en"])        

    if oldHighlight["image_hash_es"]!=request.json["image_hash_es"]:
        app.logger.info("here2");
        deleteImgFile(oldHighlight["image_hash_es"])
        moveImgFile(request.json["image_hash_es"])

    out = m.editHighlight(request.json)
    return(jsonify({"result": {"id_highlight": out}}))
    #except:
    #    return(jsonify(cons.errors["-1"]))


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
            filename = hashlib.md5(str(time.time())+ session["email"]).hexdigest() 
            file.save(os.path.join(config.cfgBackend['tmpFolder'], filename + fileExtension))
            return jsonify(  {"filename": filename} )  
        
        return jsonify(  {"error": -1} )    
    
    except werkzeug.exceptions.UnsupportedMediaType:
        return jsonify(  {"error": -2} )
    
    except werkzeug.exceptions.RequestEntityTooLarge:
        return jsonify(  {"error": -3} )
