## Imports externos
from flask import Blueprint, flash, render_template, request, redirect, url_for

## Imports internos

### Blueprint ###
web = Blueprint('WebRoutes',__name__)

## Flask web routes ##
@web.route('/')
def index():
    return render_template('pagInformativa.html')