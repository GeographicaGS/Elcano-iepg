from flask import Flask
app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='oN;2R@a-Y&opIY',
    PORT=5001
)

import user
import home
