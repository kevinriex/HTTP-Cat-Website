'''Docstring'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def main():
    '''Docstring'''
    return {"Message": "It Works!"}


@app.route("/<code>")
def code(code):
    '''Docstring'''
    return render_template("code.html", code=code)


app.run()
