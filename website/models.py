from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Bookshelf(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    author_name = db.Column(db.String(300))
    date_added = db.Column(db.DateTime(timezone=True), default=func.now())
    rating = db.Column(db.Float)
    review = db.Column(db.String(3000))
    completed = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
     

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    Bookshelf = db.relationship('Bookshelf')
