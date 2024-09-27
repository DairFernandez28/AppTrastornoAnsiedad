from utils.db import db
from dataclasses import dataclass
from datetime import datetime, date, time

@dataclass
class tbCita(db.Model):
    __tablename__ = 'tbCita'
    idCita: int 
    idPaciente: int
    idEspecialista: int
    diagnostico: str
    nivelAnsiedad: str
    fechaCita: date
    fechaDiagnostico: datetime
    horaCita: time
    culminado: bool

    idCita = db.Column(db.Integer, primary_key=True)
    idPaciente = db.Column(db.Integer, db.ForeignKey('tbPaciente.idPaciente'))
    idEspecialista = db.Column(db.Integer, db.ForeignKey('tbEspecialista.idEspecialista'))
    diagnostico = db.Column(db.String(500))
    nivelAnsiedad = db.Column(db.String(255))
    fechaCita = db.Column(db.Date)
    fechaDiagnostico = db.Column(db.DateTime)
    horaCita = db.Column(db.Time)
    culminado = db.Column(db.Boolean)

    def __init__(self, idPaciente, idEspecialista, diagnostico, nivelAnsiedad, fechaCita, fechaDiagnostico, horaCita, culminado):
        self.idPaciente = idPaciente
        self.idEspecialista = idEspecialista
        self.diagnostico = diagnostico
        self.nivelAnsiedad = nivelAnsiedad
        self.fechaCita = fechaCita
        self.fechaDiagnostico = fechaDiagnostico
        self.horaCita = horaCita
        self.culminado = culminado