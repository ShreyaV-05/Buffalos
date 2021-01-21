from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

app = Flask(__name__)

""" database locations """
dbURI = 'sqlite:///createDB'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)

"""
Sample of table creation and data population
"""

"""DB creation"""
engine = create_engine(dbURI)
session = Session(bind=engine)


"""User table model?"""
class Cuisines(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    type_of_cuisine = db.Column(db.String(255), unique=False, nullable=False)
    name_of_restaurant = db.Column(db.String(255), unique=True, key='name_of_restaurant')
    location = db.Column(db.String(255), unique=False, nullable=False)
    price = db.Column(db.String(255), unique=False, nullable=False)

if __name__ == "__main__":
    """create each table"""
    db.create_all()
    try:
        u1 = Cuisines(type_of_cuisine='Japanese', name_of_restaurant='Akai Hana', location='San Diego', price='$$')
        u2 = Cuisines(type_of_cuisine='Italian', name_of_restaurant='Cotogna', location='San Francisco', price='$$$')
        u3 = Cuisines(type_of_cuisine='Persian', name_of_restaurant='Shamshiri', location='Los Angeles', price='$$')
        u4 = Cuisines(type_of_cuisine='French', name_of_restaurant='Bleu Bohème', location='San Diego', price='$$')
        session.add_all([u1, u2, u3, u4])
        session.commit()
    except:
        print("Records exist")

    print("Table: Cuisines")
    list = Cuisines.query.all()
    for row in list:
        print(row.user_id)
        print(row.type_of_cuisine)
        print(row.name_of_restaurant)
        print(row.location)
        print(row.price)

"""
Test on Terminal from IntelliJ
MacBook-Pro-2:flask-idea-homesiteZ johnmortensen$ cd models
MacBook-Pro-2:models johnmortensen$ sqlite3
SQLite version 3.32.3 2020-06-18 14:16:19
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite> .open createDB
sqlite> .tables
users
sqlite> select * from users;
1|Thomas Edison|Toby|tedison@example.com
2|Nicholas Tesla|Niko|ntesla@example.com
3|Alexander Graham Bell|Lex|agbell@example.com
4|Eli Whitney|Whit|eliw@example.com
"""