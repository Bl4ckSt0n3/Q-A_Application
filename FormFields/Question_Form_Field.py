from wtforms import SubmitField, TextAreaField, StringField
from flask_wtf import FlaskForm

class QuestionForm(FlaskForm):
    question = StringField("question")
    answer = TextAreaField("answer")
    submit = SubmitField("Submit")