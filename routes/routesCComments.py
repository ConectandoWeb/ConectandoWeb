## Imports externos
from flask import Blueprint, flash, render_template, request, redirect, url_for
from utils.email import mail
from flask_login import login_required
import logging
from flask_mail import Message
from models.comment import Comentarios
from utils.db import db

### Blueprint ###
ccomments = Blueprint('ccomentsRoutes',__name__)

@ccomments.route('/homeComments')
@login_required
def homeComments():
    try:
        e = Comentarios.query.filter(Comentarios.estado == "pendiente").all()
        return render_template('mod/pendientes.html', e=e)
    except:
        flash('No se pudieron obtener los alumnos')
        return render_template('mod/pendientes.html')

@ccomments.route('/deleteComment/<id>')
@login_required
def deleteComment(id):
    try:
        comm = Comentarios.query.get(int(id))
        db.session.delete(comm)
        db.session.commit()
        return redirect(url_for('ccomentsRoutes.homeComments'))
    except:
        flash('No se puede eliminar el usuario, lo siento :(')
        return redirect(url_for('ccomentsRoutes.homeComments'))
    
@ccomments.route('/curseComments')
@login_required
def curseComments():
    try:
        e = Comentarios.query.filter(Comentarios.estado == "en curso").all()
        return render_template('mod/curso.html', e=e)
    except:
        flash('No se pudieron obtener los alumnos')
        return render_template('mod/curso.html')
    
@ccomments.route('/completeComments')
@login_required
def completeComments():
    try:
        e = Comentarios.query.filter(Comentarios.estado == "completado").all()
        return render_template('mod/completados.html', e=e)
    except:
        flash('No se pudieron obtener los alumnos')
        return render_template('mod/completados.html')
    
@ccomments.route('/regretComment/<id>')
@login_required
def regretComment(id):
    try:
        comm = Comentarios.query.get(int(id))
        comm.estado = "en curso"
        db.session.commit()
        return redirect(url_for('ccomentsRoutes.completeComments'))
    except:
        flash('No se puedo actualizar el estado del comentario, lo siento :(')
        return redirect(url_for('ccomentsRoutes.completeComments'))
    
@ccomments.route('/terminateComment/<id>')
@login_required
def terminateComment(id):
    try:
        comm = Comentarios.query.get(int(id))
        comm.estado = "completado"
        db.session.commit()
        return redirect(url_for('ccomentsRoutes.curseComments'))
    except:
        flash('No se puedo actualizar el estado del comentario, lo siento :(')
        return redirect(url_for('ccomentsRoutes.curseComments'))
    
@ccomments.route('/sendEmail/<id>', methods=['GET', 'POST'])
@login_required

def sendEmail(id):
    comm = Comentarios.query.get(int(id))
    if request.method == 'POST':
        asunto = request.form['txtAsunto']
        contenido = request.form['txtMensajeEmail']
        if asunto != "" and contenido != "":
            try:
                msg = Message(asunto, sender='conectando.infor@gmail.com', recipients=[comm.email])
                msg.body = contenido    
                mail.send(msg)
                comm = comm.estado = "en curso"
                db.session.commit()
                return redirect(url_for('ccomentsRoutes.homeComments'))
            except:
                logging.error("Error al enviar el correo electrónico: %s", str(e))
                flash('No se puedo actualizar el estado del comentario, lo siento :(')
                return redirect(url_for('ccomentsRoutes.homeComments'))
        else:
            flash('Rellena todos los campos')
            return render_template('mod/sendEmail.html', comm=comm)
    else:
        return render_template('mod/sendEmail.html', comm=comm)
    