from flask import Flask
app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='IuwqOl6;a#RF1a',    
)

import user