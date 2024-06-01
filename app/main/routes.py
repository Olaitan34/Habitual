from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from app import db
from app.models import User, Habit
from . import main

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main.route('/add_habit', methods=['POST'])
@login_required
def add_habit():
    name = request.form['name']
    frequency = request.form['frequency']
    description = request.form.get('description')
    link = request.form.get('link')
    habit = Habit(user_id=current_user.id, name=name, frequency=frequency, description=description, link=link)
    db.session.add(habit)
    db.session.commit()
    return redirect(url_for('main.dashboard'))

