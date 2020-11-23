import os
from flask import Flask, render_template, request, session, flash, redirect, url_for
from socket import socket, AF_INET, SOCK_STREAM
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def homepage():
    return render_template("toolbox.html")

@app.route("/spyder/", methods=["GET", "POST"])
def spyder():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('spyder', 7070))
    return render_template("toolbox.html")


@app.route("/tensorflow/", methods=["GET", "POST"])
def tensorflow():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('tensorflow', 7575))
    return render_template("toolbox.html")

@app.route("/git/", methods=["GET", "POST"])
def git():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('git', 9191))
    return render_template("toolbox.html")

@app.route("/spark/", methods=["GET", "POST"])
def spark():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('spark', 5151))
    return render_template("toolbox.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
