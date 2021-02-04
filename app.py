from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField
from wtforms.validators import InputRequired,Email,Length
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import projects

import requests
from flask import render_template, request, redirect, url_for
from flask_table import Table, Col
from sqlalchemy import func


app = Flask(__name__)
app.config['SECRET_KEY'] = 'AnimeisGOOD'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(15),unique = True)
    email = db.Column(db.String(50),unique = True)
    password = db.Column(db.String(80))

    def __repr__(self):
        return '<Task %r>' % self.id

class LoginForm(FlaskForm):
    username = StringField('username',validators=[InputRequired(), Length(min=4,max=15)])
    password = PasswordField('password',validators=[InputRequired(), Length(min=8,max=80)])
    remember = BooleanField('remember me')



class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid Email'),Length(max=50)])
    username = StringField('username',validators=[InputRequired(), Length(min=4,max=15)])
    password = PasswordField('password',validators=[InputRequired(), Length(min=8,max=80)])


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

@app.route("/responserev/")
def responserev_route():
    return render_template("responserev.html", projects=projects.setup())

#Create the Login Page
@app.route('/login/',methods = ['GET','POST'])
def login():
    #TODO: Make the form accept the User Value, or somehow update the form
    form = LoginForm()
    #TODO Make The SQL Database work

    if form.validate_on_submit():
        #exists = db.session.query(
        #db.session.query(User).filter_by(username='AndrewZhang').exists()
        #).scalar()
        #if exists == True:
        #return "Exists"
        user = User.query.filter_by(username = form.username.data).first()
        if user:
            if user.password == form.password.data:
                return redirect(url_for('showboard'))

        return '<h1>Invalid username or password</h1>'

    return render_template("login.html", form = form, projects=projects.setup())
"""
#Create the SignUp Page
@app.route('/signup/',methods = ['GET','POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username = form.username.data, email = form.email.data, password = form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home_route'))


    return render_template("auth_user.html", form = form, projects=projects.setup())

@app.route('/dashboard/')
def showboard():
    return render_template("DashBoard.html", projects=projects.setup())
"""


# For Random Cuisine Generator
@app.route('/random/',methods=['GET','POST'])
def random():
    #call to random number web api
    url ='https://csrng.net/csrng/csrng.php?min=0&max=5'
    resp = requests.get(url)

    #formatting variables from return
    random = resp.json()[0]['random']
    print(random)
    return render_template('random.html', random=random)
    return render_template('joke.html', setup=setup, punchline=punchline)

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


if __name__ == "__main__":
    app.run(debug = True, port=8080)