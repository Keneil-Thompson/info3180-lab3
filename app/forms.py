from flask_wtf import FlaskForm
from flask_wtf import csrf
from wtforms import StringField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect

class ContactForm(FlaskForm):
    name = StringField('name',validators=[DataRequired()])
    email = StringField('email',validators=[DataRequired()])
    subject = StringField('subject',validators=[DataRequired()])
    body = TextAreaField('body',validators=[DataRequired()])


