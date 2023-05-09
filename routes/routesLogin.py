####Imports Externos####
from flask_login import login_user, logout_user, current_user, login_required, LoginManager
from flask import Blueprint, flash, render_template, request, redirect, url_for
###Imports Internos###
from models.user import Usuarios, ModelUser
from utils.log import login_manager
from utils.db import db

### Blueprint ###
login = Blueprint('LoginRoutes',__name__)

@login.route('/sign-in')
def sign():
    return redirect(url_for('LoginRoutes.log_in'))

### Flask login routes ###
@login_manager.user_loader
def load_user(user_id):
    return Usuarios.query.get(int(user_id))

@login.route('/login', methods=['GET', 'POST'])
def log_in():
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == '' or password == '':
            flash('Rellena todos los campos')
            return render_template('login.html')
        else:    
            user = Usuarios(0,username,password)
            logged_user = ModelUser.comprobacion_login(user)
            if logged_user != None:
                if logged_user.password:
                    login_user(logged_user)
                    return redirect(url_for('ccomentsRoutes.homeComments'))
                else:
                    flash('Usuario o contraseña incorrecta')
                    return render_template('login.html')
            else:
                flash('Usuario o contraseña incorrecta')
                return render_template('login.html')
    else:
        return render_template('login.html')


@login.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('LoginRoutes.sign'))