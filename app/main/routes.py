from flask import render_template, Blueprint
from app.models import User, Habit

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
