from flask import flask
app = Flask(__name__)

@app.rout('/')
def hello_world():
    return 'Hello, World!'

