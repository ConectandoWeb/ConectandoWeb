## Imports externos
from flask import Blueprint, flash, render_template, request, redirect, url_for

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
        return render_template('mod/pagEDG.html')
    except:
        flash('No se pudieron obtener los alumnos')

