from backend import app
from flask import jsonify,request,session
from model.documentmodel import DocumentModel
from utils import auth

@app.route('/highlight', methods=['POST'])
@auth
def 
