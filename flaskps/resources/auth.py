from flask import redirect, render_template, request, url_for, abort, session, flash, jsonify
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.resources import forms

#Forms & validation
from wtforms import Form
import wtforms_json
wtforms_json.init()

#Autentica el usuario
def authenticate():
    if request.method == 'POST':
        #Obtención de información
        post_data = request.get_json()
        #Validacion de formulario
        form = forms.ValidateLogin.from_json(post_data, skip_unknown_keys=False)
        if form.validate():
            #Busco usuario
            User.db = get_db()
            user = User.find_by_email_and_pass(post_data['email'], post_data['password'])
            #Usuario no existe
            if not user:
                response_object = {'status': 'warning', 'message': 'Email o contraseña incorrectos', 'success': False}
            #Usuario no activo
            elif not user['activo']:
                response_object = {'status': 'warning', 'message': 'Usuario inactivo', 'success': False}
            #Inicio de sesión
            else:
                response_object = {'status': 'success', 'message': 'Inicio exitoso', 'success': True}
                #Variable de sesion
                login(user)
        #Inputs invalidos
        else:
            response_object = {'status': 'warning', 'message': 'Ingrese email y contraseña', 'success': False}

    return jsonify(response_object)

#Inicia la sesión
def login(user):
    #Variables de sesion
    session['id'] = user['id']
    session['user'] = user['username']
    session['email'] = user['email']
    session['nombre'] = user['first_name']
    session['apellido'] = user['last_name']
    return True

def authenticated():
    response_object = {'authenticated': False}
    if 'id' in session:
        response_object = {'authenticated': True}
    return jsonify(response_object)

def unauthenticate():
    session.clear()
    response_object = {'success': True}
    return jsonify(response_object)
