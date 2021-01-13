from flask import render_template, request, redirect, url_for
from flask_table import Table, Col
from sqlalchemy import func
from pythondb import pythondb_bp
from pythondb.model import Users, Emails, PhoneNumbers
from __init__ import db
from models.lessons import menus

@pythondb_bp.route('/create/', methods=["POST"])
def create():
    if request.form:
        """prepare data for primary table extracting from form"""
        user = Users(fname=request.form.get("fname"), lname=request.form.get("lname"))
        """add and commit data to user table"""
        db.session.add(user)
        db.session.commit()
        """prepare data for related tables extracting from form and using new UserID """
        userid = db.session.query(func.max(Users.UserID))
        restaurant = restaurant(restaurant=request.form.get("restuarants"), UserID=userid)
        review = review(review=request.form.get("review"), UserID=userid)
        rate = rate(rate=request.form.get("rate"), UserID=userid)
        """restaurant table add and commit"""
        db.session.add(restaurant)
        db.session.commit()
        """review table add and commit"""
        db.session.add(review)
        db.session.commit()
        """rate table add and commit"""
        db.session.add(rate)
        db.session.commit()
    return redirect(url_for('pythondb_bp.databases'))