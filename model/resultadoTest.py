from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class tbResultadoTest(db.Model):
    __tablename__ = 'tbResultadoTest'
    idResultadoTest: int
    idPaciente: int
    puntajeResultadoTest: int
    infoResultado: str
    fechaResultadoTest: datetime
    revisadoResultadoTest: bool
    revisando: bool

    idResultadoTest = db.Column(db.Integer, primary_key=True)
    idPaciente = db.Column(db.Integer, db.ForeignKey('tbPaciente.idPaciente'))
    puntajeResultadoTest = db.Column(db.Integer)
    infoResultado = db.Column(db.String(255))
    fechaResultadoTest = db.Column(db.DateTime)
    revisadoResultadoTest = db.Column(db.Boolean)
    revisando = db.Column(db.Boolean)

    def __init__(self, idPaciente, puntajeResultadoTest, infoResultado, fechaResultadoTest, revisadoResultadoTest, revisando):
        self.idPaciente = idPaciente
        self.puntajeResultadoTest = puntajeResultadoTest
        self.infoResultado = infoResultado
        self.fechaResultadoTest = fechaResultadoTest
        self.revisadoResultadoTest = revisadoResultadoTest
        self.revisando = revisando