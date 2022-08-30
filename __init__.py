from flask import Flask, render_template
from fastapi.templating import Jinja2Templates
import os, shelve

app = Flask(__name__)
BASEDIR = os.getcwd()
basedir = os.path.abspath(os.path.dirname(__file__))

templates = Jinja2Templates(directory=f"{BASEDIR}/templates")

@app.route('/')
def customer_home():
    return render_template('customer_home.html')

if __name__ == '__main__':
    app.debug = True
    app.run()