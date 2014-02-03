from frontend import app
from flask import jsonify
from model.UserModel import UserModel

@app.route('/', methods = ['GET'])                                            
def alive():
    return jsonify( { "status" : "running"})

