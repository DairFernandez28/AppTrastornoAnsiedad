from utils.db import db
from dataclasses import dataclass
from datetime import datetime, time

@dataclass
class tbHorarioEspecialista(db.Model):
    __tablename__ = 'tbHorarioEspecialista'
    idHorarioEspecialista: int 
    idEspecialista: int
    dia: str
    horaInicio: time
    horaFin: time
    oculto: bool

    idHorarioEspecialista = db.Column(db.Integer, primary_key=True)
    idEspecialista = db.Column(db.Integer, db.ForeignKey('tbEspecialista.idEspecialista'))
    dia = db.Column(db.String(10))
    horaInicio = db.Column(db.Time)
    horaFin = db.Column(db.Time)
    oculto = db.Column(db.Boolean)

    def __init__(self, idEspecialista, dia, horaInicio, horaFin, oculto):
        self.idEspecialista = idEspecialista
        self.dia = dia
        self.horaInicio = horaInicio
        self.horaFin = horaFin
        self.oculto = oculto