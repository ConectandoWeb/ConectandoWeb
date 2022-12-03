from utils.db import db

class Comentarios(db.Model):
    id_comentario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    telefono = db.Column(db.String(12))
    email = db.Column(db.String(100))
    mensaje = db.Column(db.String(255))

    def __init__(self,nombre,telefono,email,mensaje):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.mensaje = mensaje
