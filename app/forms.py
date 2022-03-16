from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length

from app.models import User


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('是否保存')
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    password2 = PasswordField('再一次输入', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('注册')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('用户名已经被注册')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('邮箱已经被注册')


class EditProfileForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    about_me = TextAreaField('个人介绍', validators=[Length(min=0, max=140)])
    submit = SubmitField('提交')


'''
    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
'''


def validate_username(self, username):
    if username.data != self.original_username:
        user = User.query.filter_by(username=self.username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')


class PostForm(FlaskForm):
    post = TextAreaField('回复', validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('提交')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    submit = SubmitField('提交')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('密码', validators=[DataRequired()])
    password2 = PasswordField('再一次输入密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('提交')


class PostForm(FlaskForm):
    post = TextAreaField('回复', validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('提交')
