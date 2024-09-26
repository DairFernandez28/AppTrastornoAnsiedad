from utils.db import db
from dataclasses import dataclass

@dataclass
class tbRespuestasTest(db.Model):
    __tablename__ = 'tbRespuestasTest'
    idRespuestas: int
    idResultadoTest: int
    idTest: int
    pregunta: str
    respuesta: str
    valorRespuesta: int

    idRespuestas = db.Column(db.Integer, primary_key=True)
    idResultadoTest = db.Column(db.Integer, db.ForeignKey('tbResultadoTest.idResultadoTest'))
    idTest = db.Column(db.Integer, db.ForeignKey('tbTest.idTest'))
    pregunta = db.Column(db.String(255))
    respuesta = db.Column(db.String(255))
    valorRespuesta = db.Column(db.Integer)