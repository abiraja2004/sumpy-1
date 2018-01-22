
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello World!"

@app.route('/hello/')
@app.route('/hello/<name>')
def hi(name=None):
        return render_template('index.html', name=name)







