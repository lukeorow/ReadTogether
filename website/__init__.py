from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dqhduicnqowecHSoew'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Bookshelf # or could do just "import .models"
    
    with app.app_context():
        db.create_all()
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME): # checks if the db exists or not
        db.create_all(app=app) # creates the db if it doesn't exist
        print('Database created')