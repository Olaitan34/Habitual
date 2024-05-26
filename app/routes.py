from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():
    print("Index route accessed")
    return render_template('index.html', title='Home')

@main.route('/user/<username>')
def user_profile(username):
    print(f"User profile route accessed for {username}")
    user = {'username': username, 'email': f'{username}@example.com'}  # Mock user for demonstration
    return render_template('user.html', user=user)

@main.route('/habit/<int:id>')
def habit_detail(id):
    print(f"Habit detail route accessed for ID {id}")
    habit = {'name': 'Sample Habit', 'description': 'A sample habit', 'frequency': 'daily', 'link': 'http://example.com'}  # Mock habit for demonstration
    return render_template('habit.html', habit=habit)
