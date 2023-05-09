## Imports externos
from flask import Blueprint, flash, render_template, request, redirect, url_for
from models.comment import Comentarios
from utils.db import db

## Imports internos


### Blueprint ###
web = Blueprint('webRoutes',__name__)

## Flask web routes ##
@web.route('/')
def index():
    return render_template('advertencia.html')

@web.route('/edg')
def adviceEDG(): 
    try:
        return redirect(url_for('webRoutes.adminEDG'))
    except:
        flash('No se pudo obtener la pagina web')

@web.route('/color')
def adviceColor():
    try:
        return redirect(url_for('webRoutes.adminColor'))
    except:
        flash('No se pudo obtener la pagina web')


@web.route('/PageColor', methods=['GET', 'POST'])
def adminColor():
    if request.method == 'POST':
        nombre = request.form['txtNombre']
        email = request.form['txtEmail']
        mensaje = request.form['txtMensaje']
        value = {'scroll': "true"}
        if 'cBox' in request.form:
            check = True
        else:
            check = False

        if nombre == ""  or email == "" or mensaje == "":
            flash('Rellena todo lo del formulario')
            return render_template('mod/pagCol.html',value=value)
        else:
            if check == False:
                flash('Acepta los Terminos y condiciones y Politicas de Privacidad Primero')
                return render_template('mod/pagCol.html',value=value)
            else:
                try:
                    newComment = Comentarios(nombre,email,mensaje,"pendiente")
                    db.session.add(newComment)
                    db.session.commit()
                    flash('El comentario se envio correctamente, espera tu respuesta por tu correo :)')
                    return render_template('mod/pagCol.html', value=value)
                except:
                    flash('No se pudo enviar el comentario, lo siento :(')
                    return render_template('mod/pagCol.html', value=value)
    else:
       value = {'scroll': "false"}
       return render_template('mod/pagCol.html', value=value)

@web.route('/PageEDG', methods=['GET', 'POST'])
def adminEDG():
    if request.method == 'POST':
        nombre = request.form['txtNombre']
        email = request.form['txtEmail']
        mensaje = request.form['txtMensaje']
        value = {'scroll': "true"}
        if 'cBox' in request.form:
            check = True
        else:
            check = False

        if nombre == "" or email == "" or mensaje == "":
            flash('Rellena todo lo del formulario')
            return render_template('mod/pagEDG.html', value=value)
        else:
            if check == False:
                flash('Acepta los Terminos y condiciones y Politicas de Privacidad Primero')
                return render_template('mod/pagEDG.html', value=value)
            else:
                try:
                    newComment = Comentarios(nombre,email,mensaje,"inatendido")
                    db.session.add(newComment)
                    db.session.commit()
                    flash('El comentario se envio correctamente, espera tu respuesta por tu correo :)')
                    return render_template('mod/pagEDG.html', value=value)
                except:
                    flash('No se pudo enviar el comentario, lo siento :(')
                    return render_template('mod/pagEDG.html', value=value)
    else:
       value = {'scroll': "false"}
       return render_template('mod/pagEDG.html', value=value)
    

@web.route('/TCPPC')
def TCPPC():
    return render_template('mod/terCol.html')

@web.route('/TCPPE')
def TCPPE():
    return render_template('mod/terEDG.html')

@web.route('/c')
def recEDG():
    return render_template('mod/pagEDG.html')
