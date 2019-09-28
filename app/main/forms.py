from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,SubmitField
from wtforms.validators import Required
from ..models import User

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class AddPostForm(FlaskForm):
    title=StringField('Title',validators = [Required()])
    content=TextAreaField('Content',validators = [Required()])
    image=StringField('Image url',validators = [Required()])
    submit=SubmitField('SUBMIT')

class UpdatePostForm(FlaskForm):
    title=StringField('Title',validators = [Required()])
    content=TextAreaField('Content',validators = [Required()])
    submit=SubmitField('SUBMIT')

class CommentForm(FlaskForm):
   
   username = StringField('Enter your name',validators=[Required()])
   comment = TextAreaField('Your comment Here', validators=[Required()])
   submit = SubmitField('Submit')

