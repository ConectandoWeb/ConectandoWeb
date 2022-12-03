## Imports externos
from flask import Flask, redirect, url_for

## Imports internos
from routes.routesWeb import web
from utils.config import Config

app = Flask(__name__)

###Developer Configs###
app.config.from_object(Config)

###BluePrints para routes###
app.register_blueprint(web)

### Errores ###
def status_401(error):
    return redirect(url_for('WebRoutes.index'))
def status_404(error):
    return '<h1>ERROR 404: Pagina no encontrada</h1>'

app.register_error_handler(401,status_401)
app.register_error_handler(404,status_404)


if __name__ == '__main__':
    app.run(debug=True)