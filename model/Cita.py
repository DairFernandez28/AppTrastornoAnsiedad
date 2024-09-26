from utils.db import db
from dataclasses import dataclass
from datetime import date, time

@dataclass
class tbCita(db.Model):
    __tablename__ = 'tbCita'
    idCita: int 
    idPaciente: int
    idRecomendApoyo: int
    fechaCita: date
    horaCita: time
    culminado: bool

    idCita = db.Column(db.Integer, primary_key=True)
    idPaciente = db.Column(db.Integer, db.ForeignKey('tbPaciente.idPaciente'))
    idRecomendApoyo = db.Column(db.Integer, db.ForeignKey('tbRecomendApoyo.idRecomendApoyo'))
    fechaCita = db.Column(db.Date)
    horaCita = db.Column(db.Time)
    culminado = db.Column(db.Boolean)

    def __init__(self, idPaciente, idRecomendApoyo, fechaCita, horaCita, culminado):
        self.idPaciente = idPaciente
        self.idRecomendApoyo = idRecomendApoyo
        self.fechaCita = fechaCita
        self.horaCita = horaCita
        self.culminado = culminado