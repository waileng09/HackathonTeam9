from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello world!'

if __name___ == '__main__':
    app.run()