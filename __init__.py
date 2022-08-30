from flask import Flask, render_template, request, redirect, url_for, session, current_app, flash
from fastapi.templating import Jinja2Templates
import os, shelve

app = Flask(__name__)
BASEDIR = os.getcwd()
basedir = os.path.abspath(os.path.dirname(__file__))

templates = Jinja2Templates(directory=f"{BASEDIR}/templates")


@app.route('/')
def customer_home():
    return render_template('customer page/customer_home.html')


@app.route('/recyclingpage')
def recyclingform():
    return render_template('customer page/recycling_page.html')


if __name__ == '__main__':
    app.debug = True
    app.run()