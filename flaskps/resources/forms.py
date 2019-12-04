from wtforms import Form
from wtforms import StringField, TextField, SelectField, IntegerField, ValidationError, DateField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms import validators

#---------------------------------------------------#
#   Inicio de sesión
#---------------------------------------------------#
class Login(Form):
    email = StringField(u'Email', [validators.required(), validators.length(min=1)])
    password = StringField(u'Email', [validators.required(), validators.length(min=1)])

#---------------------------------------------------#
#   Informacion del sitio
#---------------------------------------------------#
    #Cambiar paginacion
class ChangePagination(Form):
    paginacion = IntegerField([validators.DataRequired()])

    #Cambiar información del sitio
class ChangeSiteInfo(Form):
    titulo = StringField(u'Titulo', [validators.required(), validators.length(max=255)])
    descripcion = TextAreaField(u'Descripcion', [validators.required(), validators.length(max=255)])
    email = StringField(u'Email', [validators.required(), validators.length(max=255)])

    #Cambiar estado del sitio
class ChangeSiteStatus(Form):
    estado_sitio = SelectField(u'Estado sitio', choices=[('0', 'Inactivo'), ('1', 'Activo')])

#---------------------------------------------------#
#   ABM Estudiantes
#---------------------------------------------------#
class VerifyStudent(Form):
    apellido = StringField(u'Apellido', [validators.required(), validators.length(max=50)])
    nombre = StringField(u'Nombre', [validators.required(), validators.length(max=50)])
    fecha_nac = DateField('Fecha de nacimiento', [validators.required()], format='%Y-%m-%d')
    localidad_id = IntegerField('Fecha de nacimiento', [validators.required()], min=1)
    nivel_id = IntegerField('Nivel', [validators.required()], min=1)
    domicilio = StringField(u'Apellido', [validators.required(), validators.length(max=100)])
    genero_id = IntegerField('Genero', [validators.required()], min=1)
    escuela_id = IntegerField('Escuela', [validators.required()], min=1)
    tipo_doc_id = IntegerField('Tipo de documento', [validators.required()], min=1)
    numero = IntegerField('Numero de documento', [validators.required()], min=1)
    tel = IntegerField('Telefono', [validators.required()], min=1)
    barrio_id = IntegerField('Barrio', [validators.required()], min=1)

#---------------------------------------------------#
#   Buscar estudiantes
#---------------------------------------------------#
    #Buscar estudiante por nombre
class searchEstudiantesByFirstName(Form):
    solo_nombre = StringField(u'Nombre', [validators.required(), validators.length(max=50)])

class searchEstudiantesByLastName(Form):
    solo_apellido = StringField(u'Apellido', [validators.required(), validators.length(max=50)])

class searchEstudiantesByBoth(Form):
    ambos_nombre = StringField(u'Nombre', [validators.required(), validators.length(max=50)])
    ambos_apellido = StringField(u'Apellido', [validators.required(), validators.length(max=50)])
