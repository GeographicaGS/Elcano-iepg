from flask import Flask
import home
import documentcatalog
import document


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='oN;2R@a-Y&opIY',
    PORT=5001
)


@app.route('/', methods = ['GET'])                                            
def alive():
    return jsonify( { "status" : "running"})
