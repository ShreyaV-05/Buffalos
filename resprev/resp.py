from flask import request, redirect, url_for
from sqlalchemy import func
from app import app
from resprev.reptable import User, Cuisine, Review
from resprev.init import db

# Declare your Users table
class UserTable(Table):
    UserID = Col('UserID')
    username = Col('username')
    password = Col('Password')


# Declare your  emailtable
class EmailTable(Table):
    UserID = Col('UserID')
    email_address = Col('email_address')


# Declare your  phone numbers table
class PNTable(Table):
    UserID = Col('UserID')
    phone_number = Col('phone_number')


# connects default URL to a function
@pythondb_bp.route('/')
def databases():
    """convert Users table into a list of dictionary rows"""
    records = []
    users = Users.query.all()
    for user in users:
        user_dict = {'id': user.UserID, 'name': user.username, 'password': user.password}
        # filter email
        email = Emails.query.filter_by(UserID=user.UserID).first()
        if email:
            user_dict['emails'] = email.email_address
        # filter phone number
        pn = PhoneNumbers.query.filter_by(UserID=user.UserID).first()
        if pn:
            user_dict['phone_numbers'] = pn.phone_number
        # append to records
        records.append(user_dict)
    return render_template("pythondb/index.html", table=records, menus=menus)

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