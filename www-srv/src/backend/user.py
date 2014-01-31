from backend import app
from flask import jsonify,request,session
from model.UserModel import UserModel
import utils
import hashlib

@app.route('/user', methods = ['GET'])                                            
def user():
   
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

def sess_logout():
    session.pop('email', None)
    session.pop('id_user', None)
    session.pop('profile', None)
    session.pop('username', None)    
    
@app.route('/user/login',methods=['POST'])
def login():
    
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
            session["id_user"] = u["id_user"]
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