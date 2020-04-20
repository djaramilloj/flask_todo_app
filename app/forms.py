from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('passowrd', validators=[DataRequired()])
    submit = SubmitField('enviar')


class TodoForm(FlaskForm):
    descripcion= StringField('descripcion', validators=[DataRequired()])
    submit = SubmitField('crear')


class DeleteTodoForm(FlaskForm):
    submit = SubmitField('Borrar')


class UpdateTodoForm(FlaskForm):
    submit = SubmitField('Actualizar')