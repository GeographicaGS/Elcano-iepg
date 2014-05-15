# coding=UTF8

"""

User backend.

"""
from backend import app
from flask import jsonify,request,session
from model.usermodel import UserModel
import utils
import hashlib


@app.route('/user', methods = ['GET'])                                            
def user():
    """Gets logged in user info."""
    if not utils.isLogged():        
        return jsonify( { "id" : None})
    else:
        return jsonify({
            'id':session["id_user"],
            'email':session["email"],
            "username":session["username"],
            "name":session["name"],
            "surname":session["surname"],
            "language":session["language"]
        })


@app.route('/user', methods=['POST'])
@utils.auth
def newUser():
    """
    
    Creates a new user. JSON:

      {
        "name": "Iliana",
        "surname": "Olivié",
        "password": "eac9e8dd8575f4c7831f1f6a72607126",
        "email": "iolivie@rielcano.org",
        "admin": "true",
        "username": "iolivie",
        "language": "es",
        "status": "1"
      }

    """
    m = UserModel()
    return(jsonify(m.newUser(request.json)))


def sess_logout():
    session.pop('email', None)
    session.pop('id_user', None)
    session.pop('profile', None)
    session.pop('username', None)    

    
@app.route('/user/login',methods=['POST'])
def login():
    """
    
    Logs in a user. The JSON is:

      {
        "email": "jpalcantara@geographica.gs",
        "password": "jderj"
      }
   
    Password is sent in plain.

    """
    if not request.json  or not "email" in request.json or not "password" in request.json:        
        return jsonify({"Login": False})
    
    if "id_user" in session :        
        return jsonify({"Login": True})
    
    else:
        # login procedure
        # get user input
        email = request.json['email']
        password = request.json['password']
         # do password hash
        password = hashlib.md5(password).hexdigest()
        # compare password against database        
        u = UserModel().getUserLogin(email=email)
        if u and u['password']==password:
            session["id_user"] = u["id_wwwuser"]
            session['email'] = email
            session["username"] = u["username"]
            session["name"] = u["name"]
            session["surname"] = u["surname"]
            session["language"] = u["language"]
            return jsonify({"Login": True})
        
        return jsonify({"Login": False})

@app.route('/user/logout')
def logout():
    sess_logout()
    return jsonify({'logout':True})
