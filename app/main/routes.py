from flask import render_template, Blueprint, request, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError

from app import db
from app.main.forms import SignupForm
from app.models import User, Forecast

bp_main = Blueprint('main', __name__)

@bp_main.route('/')
def home(): #also called index
    return render_template('index.html')


@bp_main.route('/forecast')
def forecast():
    forecasts = Forecast.query.with_entities(Forecast.comment).all()
    return render_template('forecasts.html', forecasts=forecasts)

@bp_main.route('/signup', methods=['POST', 'GET'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST':
        user = User(username=form.username.data, email=form.email.data)
        try:
            db.session.add (user)
            db.session.commit ()
            flash ('You are now a registered user!')
            return redirect (url_for ('main.home'))
        except IntegrityError:
            db.session.rollback ()
            flash ('ERROR! Unable to register {}. Please check your details are correct and resubmit'.format (form.email.data), 'error')
    return render_template ('signup.html', form=form)


@bp_main.route('/users', methods=['GET'])
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@bp_main.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        term = request.form['search_term']
        if term == "":
            flash("Enter a User to search for")
            return redirect('/')
        results = User.query.filter(User.username.contains(term)).all()
        if not results:
            flash("No users found with that name.")
            return redirect('/')
        return render_template('search_results.html', results=results)
    else:
        return redirect(url_for('main.home'))


