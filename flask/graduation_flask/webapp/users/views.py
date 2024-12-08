from flask import Blueprint
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user, login_required

from .forms import RegistrationForm, LoginForm, EditProfileForm
from .models import User

from webapp import db


# Create BP for user views
blueprint = Blueprint('users', __name__, url_prefix='/users')


@blueprint.route('/registration', methods=['GET', 'POST'])
def registration():
    """
    Renders the page with registration form
    """
    title = 'Registration'
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    return render_template('user/registration.html', title=title, form=form)


@blueprint.route('/process-registration', methods=['POST'])
def process_registration():
    """
    Validates and processes the registration form
    If the form is valid, creates a new User object and adds it to the database
    If the form is not valid, re-renders the registration page with the form errors
    """
    title = 'Registration'
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            firstname=form.firstname.data,
            lastname=form.lastname.data
        )
        new_user.visible_name = new_user.username
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('user/registration.html', title=title, form=form)


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    """
    Renders the page with login form
    """
    title = 'Sign In'
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    return render_template('user/login.html', title=title, form=form)


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    """
    Validates and processes the login form
    If the form is valid, logs the user in and redirects to the index page
    If the form is not valid, re-renders the login page with the form errors
    """
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('users.login'))

    flash('Wrong username or password')
    return redirect(url_for('users.login'))


@blueprint.route('/<username>', methods=['GET', 'POST'])
@login_required
def profile(username):
    """
    Shows user's profile page
    """
    if username != current_user.username:
        return redirect(url_for('index'))
    user = User.query.filter_by(username=username).first()

    if user:
        return render_template('user/users.html', user=user)
    else:
        flash('User does not exist')
        return redirect(url_for('index'))


@blueprint.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    """
    Allows user to edit their profile
    """
    title = 'Edit profile'
    form = EditProfileForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            current_user.visible_name = form.visible_name.data
            current_user.firstname = form.firstname.data
            current_user.lastname = form.lastname.data
            db.session.commit()
            flash('Profile has been changed')
            return redirect(url_for('users.profile', username=current_user.username))

    elif request.method == 'GET':
        form.visible_name.data = current_user.visible_name
        form.firstname.data = current_user.firstname
        form.lastname.data = current_user.lastname

    return render_template('user/edit_profile.html', title=title, form=form)


@blueprint.route('/logout')
def logout():
    """
    Logs the user out and redirects to the login page
    """
    flash('You have been logged out')
    logout_user()
    return redirect(url_for('users.login'))
