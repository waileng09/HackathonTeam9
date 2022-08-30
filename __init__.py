from flask import Flask
from fastapi.templating import Jinja2Templates
import os,shelve
from datetime import datetime, timedelta,date

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello world!'


BASEDIR = os.getcwd()
basedir = os.path.abspath(os.path.dirname(__file__))

templates = Jinja2Templates(directory=f"{BASEDIR}/templates")

if __name__ == '__main__':
    app.debug = True
    app.run()