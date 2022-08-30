from flask import Flask
from fastapi.templating import Jinja2Templates

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello world!'

templates = Jinja2Templates(directory=f"{BASEDIR}/templates")

if __name__ == '__main__':
    app.run()