from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def customer_home():
    return render_template('customer_home.html')

if __name__ == '__main__':
    app.debug = True
    app.run()