from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')

class HabitForm(FlaskForm):
    name = StringField('Habit Name', validators=[DataRequired()])
    frequency = StringField('Frequency', validators=[DataRequired()])
    description = TextAreaField('Description')
    link = StringField('Link')
    submit = SubmitField('Submit')
