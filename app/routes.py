from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import User, Habit
from app.forms import UserForm, HabitForm

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html', title='Home')

@main.route('/user/<username>')
def user_profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)

@main.route('/habit/<int:id>')
def habit_detail(id):
    habit = Habit.query.get_or_404(id)
    return render_template('habit.html', habit=habit)

@main.route('/create_user', methods=['GET', 'POST'])
def create_user():
    form = UserForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'User {form.username.data} created successfully!')
        return redirect(url_for('main.index'))
    return render_template('create_user.html', title='Create User', form=form)

@main.route('/create_habit', methods=['GET', 'POST'])
@login_required
def create_habit():
    form = HabitForm()
    if form.validate_on_submit():
        habit = Habit(name=form.name.data, frequency=form.frequency.data, description=form.description.data, link=form.link.data, user_id=current_user.id)
        db.session.add(habit)
        db.session.commit()
        flash(f'Habit {form.name.data} created successfully!')
        return redirect(url_for('main.index'))
    return render_template('create_habit.html', title='Create Habit', form=form)

