from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, inspect

app = Flask(__name__)

''' database setup  '''
dbURI = 'sqlite:///resp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)

''' table definitions '''

class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(255), unique=True, nullable=False)
    lname = db.Column(db.String(255), unique=True, nullable=False)


class Cuisine(db.Model):
    cuisine_id = db.Column(db.Integer, primary_key=True)
    cuisine = db.Column(db.String(255), unique=True, nullable=False)
    userid = db.Column(db.Integer, db.ForeignKey('user.userid'))


class Review (db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(255), unique=True, nullable=False)
    rate = db.Column(db.Integer, unique=True, nullable=False)
    cuisine_id = db.Column(db.Integer, db.ForeignKey('cuisine.cuisine_id'))
"""
class rate (db.Model):
    rate_id = db.Column(db.Integer, primary_key=True)
    rate = db.Column(db.String(255), unique=True, nullable=False)
    userid = db.Column(db.Integer, db.ForeignKey('cuisine.cuisine_id'))


    def __repr__(self):
        return '<User %r>' % self.username
"""
''' table creation '''
db.create_all()

''' inspect table '''
engine = create_engine(dbURI)
insp = inspect(engine)
for name in insp.get_table_names():
    print("Table " + str(name))