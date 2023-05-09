from utils.db import db

class Comentarios(db.Model):
    id_comentario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    email = db.Column(db.String(100))
    mensaje = db.Column(db.String(255))
    estado = db.Column(db.String(20))

    def __init__(self,nombre,email,mensaje, estado):
        self.nombre = nombre
        self.email = email
        self.mensaje = mensaje
        self.estado = estado


