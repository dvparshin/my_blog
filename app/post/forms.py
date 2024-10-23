from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class PostForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    body = StringField('Содержание', validators=[DataRequired()], widget=TextArea())
    author = StringField('Автор', validators=[DataRequired()])
    submit = SubmitField('Отправить')