
"""_init_.py is used to define app and all blueprints"""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
dbURI = 'sqlite:///models/resp.db'

""" database setup to support db examples """
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)

""" blue print to move db to its own folder  ASK FOR HELP NEXT WEEK
from resprev import resprev_bp
app.register_blueprint(resprev_bp, url_prefix='/resprevdb')
 """
"""__init.py__ has responsibility of defining interfaces for blueprint"""
from flask import Blueprint
resprev_bp = Blueprint(
    'resprev_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)
