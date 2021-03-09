from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import projects
import view
import requests
from flask import render_template, request, redirect, url_for
from flask_table import Table, Col
from sqlalchemy import func

"""
app = Flask(__name__)
app.config['SECRET_KEY'] = 'AnimeisGOOD'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
"""




# Andrea Coming Soon Page
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Food'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foods.db'  # telling program where to put the database
db = SQLAlchemy(app)  # db defined here
Bootstrap(app)
records = []


# class defines database -- what rows you want in database
class Cuisines(db.Model):
    cuisine = db.Column('item_id', db.String(50), primary_key=True)
    restaurant = db.Column(db.String(100))
    location = db.Column(db.String(50))
    price = db.Column(db.Float(200))


# constructor that initializes the database
def __init__(self, location, restaurant, cuisine, price):
    self.restaurant = restaurant
    self.location = location
    self.cuisine = cuisine
    self.price = price

class reviewed(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    cuisine = db.Column(db.String(100))
    review = db.Column(db.String(500))
    location = db.Column(db.String(10))

    # constructor that initializes the database
    def __init__(self, cuisine, review, location):
        self.cuisine = cuisine
        self.review = review
        self.location = location



"Create Database"
db.create_all()  # creates food.db file


class FoodForm(FlaskForm):
    cuisine = StringField('cuisine', validators=[InputRequired(), Length(min=1, max=15)])
    restaurant = StringField('restaurant', validators=[InputRequired(), Length(min=1, max=80)])
    price = StringField('price', validators=[InputRequired()])
    location = StringField('location', validators=[InputRequired()])


@app.route('/')
def home_route():
    return render_template("home.html", projects=projects.setup())


@app.route("/sandiego/")
def sandiego_route():
    return render_template("sandiego.html", projects=projects.setup())


@app.route("/losangeles/")
def losangeles_route():
    return render_template("losangeles.html", projects=projects.setup())


@app.route("/sanfrancisco/")
def sanfrancisco_route():
    return render_template("sanfrancisco.html", projects=projects.setup())


@app.route("/responserev/", methods=['GET', 'POST'])
def responserev_route():
    if request.method == 'POST':
        cuisine= request.form['cuisine']
        review = request.form['review']


        #  adding user into the all_user database
        new_review = reviewed(cuisine = cuisine,review = review)
        db.session.add(new_review)
        db.session.commit()

        return render_template("responserev.html", projects=projects.setup())

    return render_template("responserev.html", projects=projects.setup())

rate_rev = []
sd_rev = []
sf_rev = []
def review_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste
    database = reviewed.query.all()
    for review in database:
        review_dict = {'id': review.id, 'cuisine': review.cuisine, 'review': review.review, 'location':review.location}
        rate_rev.append(review_dict)

        #getting the value that corresponds with the key 'location'
        location = review_dict['location']

        #if it is SD
        if location == 'SD':
            #append to sd_review
            sd_rev.append(review_dict)

        if location == 'SF':
            #append to sd_review
            sf_rev.append(review_dict)

review_map()
print('reviews in database:')
print(rate_rev)
print('sd_review')
print(sd_rev)
#this is where reviews end up
@app.route("/SDREV/")
def rating_route():
    return render_template("SDREV.html", projects=projects.setup(), reviews_table=sd_rev, location='San Diego', image='https://i0.wp.com/hollywoodsign.org/wp-content/uploads/2018/05/HS_HeaderPhoto2.jpg?fit=1500%2C642&ssl=1')

@app.route("/SFREV/")
def rating_route_1():
    return render_template("SDREV.html", projects=projects.setup(), reviews_table=sf_rev, location='San Fran')

@app.route("/easteregg/")
def easteregg_route():
    return render_template("easteregg.html", projects=projects.setup())



@app.route('/dashboard/')
def showboard():
    return render_template("dashBoard.html", projects=projects.setup())



@app.route('/tictactoe/')
def tictactoe_route():
    return render_template("tictactoe.html", projects=projects.setup())


# For Random Cuisine Generator
@app.route('/random/', methods=['GET', 'POST'])
def random():
    # call to random number web api
    url = 'https://csrng.net/csrng/csrng.php?min=1&max=5'
    resp = requests.get(url)

    # formatting variables from return
    random = resp.json()[0]['random']
    print(random)
    return render_template('random.html', random=random)


"""
# For Recommend Page
# Declare user ID, type of cuisine, and name of restaurant table
class UserTable(Table):
    UserID = Col('UserID')
    cuisine = Col('Cuisine')
    restaurant = Col('Restaurant')


# Declare location table
class LocationTable(Table):
    UserID = Col('UserID')
    location = Col('location')


# Declare prices table
class PriceTable(Table):
    UserID = Col('UserID')
    price = Col('price')


# connects default URL to a function
@app.route('/recommend/')
def databases():
    # convert Users table into a list of dictionary rows
    records = []
    users = users.query.all()
    for user in users:
        user_dict = {'id': user.UserID, 'name': user.cusine, 'password': user.restaurant}
        # filter location
        location = location.query.filter_by(UserID=user.UserID).first()
        if location:
            user_dict['emails'] = location.email_address
        # filter price
        price = price.query.filter_by(UserID=user.UserID).first()
        if price:
            user_dict['price'] = price.phone_number
        # append to records
        records.append(user_dict)
    return render_template("recommend.html", table=records, menus=menus)


# create/add a new record to the table
@app.route('/create/', methods=["POST"])
def create():
    if request.form:
        # prepare data for primary table extracting from form
        user = UserTable(username=request.form.get("username"), password=request.form.get("password"))
        # add and commit data to user table
        db.session.add(user)
        db.session.commit()
        # prepare data for related tables extracting from form and using new UserID
        userid = db.session.query(func.max(UserTable.UserID))
        location = LocationTable(location=request.form.get("location"), UserID=userid)
        price = PriceTable(price=request.form.get("price"), UserID=userid)
        # email table add and commit
        db.session.add(location)
        db.session.commit()
        # phone number table add and commit
        db.session.add(price)
        db.session.commit()
    return redirect(url_for('pythondb_bp.databases'))

"""


# Continue Andrea Coming Soon Page


# shows what is in the database even if you reload the program (preserving the existence of the items in the database)
# showing old items in the table
def list_map():  # mapping the front end to  backend, put in the function so we don't have to copy paste all the time
    food = Cuisines.query.all()
    for food in food:
        user_dict = {'cuisine': food.cuisine, 'location': food.location, 'restaurant': food.restaurant,
                     'price': food.price}
        records.append(user_dict)
        # records is a list initiated at top of code, showcases all the items appending to the database


# calling the method list_map()
list_map()
@app.route("/soon/", methods=['GET', "POST"])
def soon_route():
    form = FoodForm()
    if form.validate_on_submit():  # adding in all
        new_food = Cuisines(cuisine=form.cuisine.data, restaurant=form.restaurant.data, price=form.price.data,
                            location=form.location.data)
        db.session.add(new_food)
        db.session.commit()
        user_dict = {'restaurant': new_food.restaurant, 'location': new_food.location, 'cuisine': new_food.cuisine,
                     'price': new_food.price}
        records.append(user_dict)  # adding a new item to the table
    return render_template("coming_soon.html", form=form, table=records)


import flask
from flask import request, redirect
from auth_user import newuser
import requests
from view import updatepswd, delete,checkLogin

username = "Shreya"
password = "FoodYum"

@app.route('/login/', methods = ["GET","POST"])
def login():
    if request.method == 'POST':
        form_username = request.form['user_name']
        form_password = request.form['user_pswd']
        if form_username == "Shreya":
            if form_password == "FoodYum":
                return render_template("sandiego.html")
        else:
            return '<h1>Invalid username or password</h1>'


    return flask.render_template("login.html")


@app.route('/signup/')
def auth_user():
    return flask.render_template("auth_user.html")

@app.route('/signup', methods=['POST'])
def signup(): return newuser(request)




@app.route('/changepwd', methods=['POST'])
def changepwd():
    return flask.render_template("profile.html", error=updatepswd(request))

@app.route('/deleteAccount', methods=['POST'])
def deleteAccount():
    return flask.render_template("profile.html", error=delete(request))

if __name__ == "__main__":
    app.run(debug=True, port=' 5002', host='127.0.0.1')