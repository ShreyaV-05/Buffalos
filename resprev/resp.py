from flask import request, redirect, url_for
from flask_table import Table, Col
from sqlalchemy import func
from app import app
from resprev.reptable import User, Cuisine, Review
from resprev.init import db

# Declare your Users table
class UserTable(Table):
    UserID = Col('UserID')
    fname = Col('fname')
    lname = Col('lname')

# Declare your  cuisinetable
class CuisineTable(Table):
    User.userid = Col('cuisine')
    cuisine = Col('cuisine')


# Declare your review table
class ReviewTable(Table):
    Cuisine.cuisine_id = Col('cuisine')
    review = Col('review')
    rate = Col('rate')


# connects default URL to a function
@app.route('/')
def databases():
    """convert Users table into a list of dictionary rows"""
    records = []
    user = User.query.all()
    for user in user:
        user_dict = {'id':user.user.userid}
        # filter cuisine
        cuisine = cuisine.query.filter_by(userid=user.userid).first()
        if cuisine:
            user_dict['cuisine'] = cuisine.review
        # filter review
        review = review.query.filter_by(cuisine_id=cuisine.cuisine_id).first()
        if review:
            user_dict['review'] = review.review
        rate = rate.query.filter_by(cuisine_id=cuisine.cuisine_id).first()
        if rate:
            user_dict['rate'] = rate.review
        # append to records
        records.append(user_dict)
    return render_template("resp.db/responserev.html", table=records, menus=menus)

@app.route('/create/', methods=["POST"])
def create():
    if request.form:
        """prepare data for primary table extracting from form"""
        user = User(fname=request.form.get("fname"), lname=request.form.get("lname"))
        """add and commit data to user table"""
        db.session.add(user)
        db.session.commit()
        """prepare data for related tables extracting from form and using new UserID """
        userid = db.session.query(func.max(User.UserID))
        cuisine = Cuisine(cuisine=request.form.get("cuisine"), userid=userid)
        review = Review(review=request.form.get("review"), rate=request.form.get("rate"), cuisine_id=cuisine)
        """cuisine table add and commit"""
        db.session.add(cuisine)
        db.session.commit()
        """review table add and commit"""
        db.session.add(review)
        db.session.commit()
    return redirect(url_for('resprev.init.databases'))
"""
# if email url, show the email table only
@app.route('/cuisine/')
def cuisine(cuisine):
    # fill the table with emails only
    records = []
    cuisine = cuisine.query.all()
    for cuisine in cuisine:
        user_dict = {}
        user_dict['id'] = cuisine.UserID
        user_dict['cuisine'] = cuisine.cuisine
        records.append(user_dict)
    return render_template("app/responserev.html", table=records, menu=menus)


# if phones url, show phones table only
@app.route('/phones/')
def review():
    # fill the table with phone numbers only
    records = []
    review = review.query.all()
    for review in review:
        cuisine_dict = {}
        cuisine_dict['id'] = review.cuisine_id
        cuisine_dict['review'] = review.review
        records.append(cuisine_dict)
    return render_template("app/responserev.html", table=records, menu=menus)
"""