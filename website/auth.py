from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from website.book_search import get_book_search

auth = Blueprint('auth', __name__)

# handles the url routes to the different websites
@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean=True) # you can pass variables to this as well and then use {{}} to put them in html

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        error_exists = False

        if len(email) < 4: 
            flash('Email must be greater than 3 characters', category='error')
            error_exists = True
        elif len(first_name) < 2:
            flash('Name must be greater than 1 character', category='error')
            error_exists = True
        elif password1 != password2:
            flash('Passwords do not match', category='error')
            error_exists = True
        elif len(password1) < 8:
            flash('Password must be at least 8 characters', category='error')
            error_exists = True
        else:
            # add user to database
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account successfully created!', category='success')
            return redirect(url_for('views.home')) # finds the url mapped to home blueprint in views.py
            
        if error_exists:
            return render_template("sign_up.html", first_name=first_name, email=email)
        
    return render_template("sign_up.html")
    

@auth.route('/bookshelf')
def bookshelf():
    return render_template('bookshelf.html')

@auth.route('/search', methods=["GET"])
def search_books():
    query = request.args.get('search_book')
    
    if query:
        book_search_results = get_book_search(query)
        
        print(book_search_results)
        
        return render_template('search_results.html', books=book_search_results, query=query)
    
    return render_template('bookshelf.html')