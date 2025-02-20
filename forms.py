from wtforms import Form, SelectField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, RadioField, IntegerField, EmailField
from wtforms import validators

class ZodiacoForm(Form):
    nombre = StringField('Nombre', [
        validators.DataRequired(message='El campo es requerido'),
    ])
    apellidoPa = StringField('Apellido Paterno', [
        validators.DataRequired(message='El campo es requerido')
    ])
    apellidoMa = StringField('Apellido Materno', [
        validators.DataRequired(message='El campo es requerido')
    ])
    dia = IntegerField('Día', [
        validators.DataRequired(message='El campo es requerido'),
        validators.NumberRange(min=1, max=31, message='El día debe estar entre 1 y 31.')
    ])
    mes = IntegerField('Mes', [
        validators.DataRequired(message='El campo es requerido'),
        validators.NumberRange(min=1, max=12, message='El mes debe estar entre 1 y 12.')
        
    ])
    anio = IntegerField('Año', [
        validators.DataRequired(message='El campo es requerido'),
        validators.NumberRange(min=1900, max=2025, message='El año debe estar entre 1900 y 2025.')
    ])
    genero = SelectField('Género', choices=[
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino')
    ])

class UserForm(Form):
    matricula = StringField('Matricula',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=3,max=10,message='El campo debe tener entre 3 y 10 caracteres')
    ])
    nombre = StringField('Nombre',[
        validators.DataRequired(message='El campo es requerido')
    ])
    apellido = StringField('Apellido',[
        validators.DataRequired(message='El campo es requerido')
    ])
    email = EmailField('Correo',[
        validators.Email(message='Ingrese un correo valido')
    ])