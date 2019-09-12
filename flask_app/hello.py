from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello/<int:name>')
def hello_world(name):
    return render_template('hello.html', name=name)  # passing name context to template


@app.route('/index')
def index():
    return render_template('index.html')
