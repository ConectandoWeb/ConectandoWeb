## Imports externos
from flask import Flask, redirect, url_for

## Imports internos
from routes.routesWeb import web
from routes.routesLogin import login
from routes.routesCComments import ccomments
from utils.log import login_manager
from flask_mail import Mail
from utils.config import Config
##from utils.email import mail
from utils.db import db

app = Flask(__name__)

###Developer Configs###
app.config.from_object(Config)

###BluePrints para routes###
app.register_blueprint(web)
app.register_blueprint(login)
app.register_blueprint(ccomments)

###Base de Datos###
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://conect_user:passwd@localhost/conectando'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

###Login Flask###
login_manager.init_app(app)

### Email Flask ###
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'conectando.infor@gmail.com' 
app.config['MAIL_PASSWORD'] = 'kvzbauyahfouylto'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

### Errores ###
def status_401(error):
    return redirect(url_for('WebRoutes.index'))
def status_404(error):
    return '<h1>ERROR 404: Pagina no encontrada</h1>'

app.register_error_handler(401,status_401)
app.register_error_handler(404,status_404)

if __name__ == '__main__':
    app.run(debug=True)