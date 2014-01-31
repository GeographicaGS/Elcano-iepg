from flask import session
from backend import app

def auth(f):
    """Wraps Authentication"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'id_user' in session:
             return f(*args, **kwargs)
        else:
           return "Not authorized", 401
           
    return decorated_function

def isLogged():
    if 'id_user' in session:
        return True
    else:        
        return False
    