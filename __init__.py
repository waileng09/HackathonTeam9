from flask import Flask
from fastapi.templating import Jinja2Templates
import os, shelve

app = Flask(__name__)
BASEDIR = os.getcwd()
basedir = os.path.abspath(os.path.dirname(__file__))

templates = Jinja2Templates(directory=f"{BASEDIR}/templates")

@app.route('/')
def home():
    return 'Hello world!'

if __name__ == '__main__':
    app.debug = True
    app.run()