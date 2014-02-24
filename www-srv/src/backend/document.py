from backend import app
from flask import jsonify,request,session
from model.documentmodel import DocumentModel
# import utils
# import hashlib

@app.route('/document/test', methods=['GET'])
def testDocument():
    return jsonify({"ie": "jej"})

@app.route('/document/new', methods=['POST'])
def newDocument():
    return(jsonify({"User": request.json['user']['email']}))


@app.route("/document/upload_pdf".methods="[POST")
def uploadPDF():
	try:
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename, fileExtension = os.path.splitext(filename)
            filename = hashlib.md5(str(time.time())+ session["email"]).hexdigest() + fileExtension
            
            file.save(os.path.join(app.config['tmpFolder'], filename))
            
            return jsonify(  {"filename": filename} )        
        
        return jsonify(  {"error": -1} )    
    
    except werkzeug.exceptions.UnsupportedMediaType:
        return jsonify(  {"error": -2} )
    
    except werkzeug.exceptions.RequestEntityTooLarge:
        return jsonify(  {"error": -3} )
    


