from flask import session
from backend import app
from functools import wraps
import cgi

def auth(f):
    """Wraps Authentication"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if app.config["autoAuth"]==True:
            return f(*args, **kwargs)

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
    

def prettyNumber(number):
    if number<10:
        return "0"+str(number)
    else:
        return str(number)


def renameKeyDict(dict,oldKeyName,newKeyName):
    dict[newKeyName]=dict.pop(oldKeyName)
    return dict;


def hsc(s):
    """Just an alias."""
    return htmlspecialchars(s)


def htmlspecialchars(s):
    if s:
        return cgi.escape(s)
    else:
        return None
