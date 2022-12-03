from flask_login import UserMixin
from utils.db import db
from utils.log import login_manager
from werkzeug.security import check_password_hash

@login_manager.user_loader
def load_user(id):
    return Usuarios.query.get(int(id))

class Usuarios(UserMixin,db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45))
    password = db.Column(db.String(102))

    def get_id(self):
        return (self.id_usuario)
    
    def __init__(self, id_usuario, username, password):
        self.id_usuario = id_usuario
        self.username = username
        self.password = password

class ModelUser():

    @classmethod
    def check_password(self,hashed_password, password):
        return check_password_hash(hashed_password, password)
    
    @classmethod
    def comprobacion_login(self,user):
        try:
            result = Usuarios.query.filter_by(username=user.username).first()
            if result != None:
                try_user = Usuarios(result.id_usuario,result.username,ModelUser.check_password(result.password,user.password))
                return try_user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)