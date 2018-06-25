from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import ValidationError


class UpdateProfile(FlaskForm):
    bio = TextAreaField('About you', validators=[Required()])
    profile_pic_path = TextAreaField('Profile Picture URL', validators=[Required()])
    submit = SubmitField('Submit')


class ChallengeForm(FlaskForm):
    content = TextAreaField('YOUR PITCH')
    submit = SubmitField('SUBMIT')


class CommentForm(FlaskForm):
    comment_id = TextAreaField('WRITE COMMENT')
    submit = SubmitField('SUBMIT')