import sqlite3
from app import app
from flask import flask
from flask import redirect, render_template
from view import checkLogin
"""
@app.route('/login')
def login():
    return flask.render_template("login.html")


@app.route('/Sign Up')
def auth_user():
    return flask.render_template("auth_user.html")
"""


def validate(request):
    if checkLogin(request) == 1:
        return redirect('/')
    else:
        return render_template("login.html", error='UserId or password Incorrect')