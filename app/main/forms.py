from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,SubmitField
from wtforms.validators import Required,Email
from wtforms import ValidationError
from ..models import User,Subscription

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class AddPostForm(FlaskForm):
    title=StringField('Title',validators = [Required()])
    content=TextAreaField('Content',validators = [Required()])
    submit=SubmitField('SUBMIT')

class UpdatePostForm(FlaskForm):
    title=StringField('Title',validators = [Required()])
    content=TextAreaField('Content',validators = [Required()])
    submit=SubmitField('SUBMIT')

class CommentForm(FlaskForm):
   
   username = StringField('Enter your name',validators=[Required()])
   comment = TextAreaField('Your comment Here', validators=[Required()])
   submit = SubmitField('Submit')
class SubscriptionForm(FlaskForm):
    name=StringField('Name',validators =[Required()])
    email=StringField('Email',validators =[Required(),Email()])
    submit = SubmitField('Submit')
    def validate_email(self,data_field):
        if Subscription.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_name(self,data_field):
        if Subscription.query.filter_by(name = data_field.data).first():
            raise ValidationError('That name is taken')

