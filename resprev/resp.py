from flask import request, redirect, url_for
from sqlalchemy import func
from app import app
from resprev.reptable import User, Cuisine, Review
from resprev.init import db

# Declare your  cuisinetable
class CuisineTable(Table):
    cuisine.cuisine_id = Col('cuisine')
    cuisine = Col('cuisine')


# Declare your review table
class ReviewTable(Table):
    cuisine.cuisine_id = Col('cuisine')
    review = Col('review')
    rate = Col('rate')


# connects default URL to a function
@app.route('/')
def databases():
    """convert Users table into a list of dictionary rows"""
    records = []
    cuisine = cuisine.query.all()
    for cuisine in cuisine:
        cuisine_dict = {'id':cuisine.cuisine_id}
        # filter review
        review = review.query.filter_by(cuisine_id=cuisine.cuisine_id).first()
        if review:
            cuisine_dict['review'] = review.review
        rate = rate.query.filter_by(cuisine_id=cuisine.cuisine_id).first()
        if rate:
            cuisine_dict['rate'] = rate.review
        # append to records
        records.append(cuisine_dict)
    return render_template("resprev/responserev.html", table=records, menus=menus)

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
    return redirect(url_for('pythondb_bp.databases'))