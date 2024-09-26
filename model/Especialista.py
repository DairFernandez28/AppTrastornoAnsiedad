from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class tbEspecialista(db.Model):
    __tablename__ = 'tbEspecialista' 
    idEspecialista: int
    nombreEspecialista: str
    apellidoEspecialista: str
    dniEspecialista: str
    especialidad: str
    celEspecialista: str
    correoEspecialista: str
    contraEspecialista: str
    
    idEspecialista = db.Column(db.Integer, primary_key=True)
    nombreEspecialista=db.Column(db.String(100))
    apellidoEspecialista=db.Column(db.String(100))
    dniEspecialista=db.Column(db.String(8))
    especialidad=db.Column(db.String(60))
    celEspecialista=db.Column(db.String(9))
    correoEspecialista=db.Column(db.String(100))
    contraEspecialista=db.Column(db.String(30))
    
    def __init__(self, nombreEspecialista, apellidoEspecialista, dniEspecialista, especialidad, celEspecialista, correoEspecialista, contraEspecialista):
        self.nombreEspecialista=nombreEspecialista
        self.apellidoEspecialista=apellidoEspecialista
        self.dniEspecialista=dniEspecialista
        self.especialidad=especialidad
        self.celEspecialista=celEspecialista
        self.correoEspecialista=correoEspecialista
        self.contraEspecialista=contraEspecialista