from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class tbPaciente(db.Model):
    __tablename__ = 'tbPaciente' 
    idPaciente: int
    nombrePaciente: str
    apellidoPaciente: str
    dniPaciente: str
    distrito: str
    celPaciente: str
    correoPaciente: str
    contraPaciente: str
    
    idPaciente = db.Column(db.Integer, primary_key=True)
    nombrePaciente=db.Column(db.String(100))
    apellidoPaciente=db.Column(db.String(100))
    dniPaciente=db.Column(db.String(8))
    distrito=db.Column(db.String(60))
    celPaciente=db.Column(db.String(9))
    correoPaciente=db.Column(db.String(100))
    contraPaciente=db.Column(db.String(30))
    
    def __init__(self, nombrePaciente, apellidoPaciente, dniPaciente, distrito, celPaciente, correoPaciente, contraPaciente):
        self.nombrePaciente=nombrePaciente
        self.apellidoPaciente=apellidoPaciente
        self.dniPaciente=dniPaciente
        self.distrito=distrito
        self.celPaciente=celPaciente
        self.correoPaciente=correoPaciente
        self.contraPaciente=contraPaciente