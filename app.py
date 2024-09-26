from flask import Flask
from utils.db import db

from services.Test import Tests
from services.preguntasTest import PreguntasTests
from services.opcionesTest import OpcionesTests
from services.rangosPuntaje import RangosPuntajes
from services.Paciente import pacientes
from services.Especialista import especialistas
from services.horarioEspecialista import HorariosEspecialistas
from services.resultadoTest import ResultadoTests
from services.respuestasTest import RespuestasTests
from services.recomendApoyo import RecomendacionesApoyos
from services.Cita import Citas

from config import DATABASE_CONNECTION

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION

db.init_app(app)

app.register_blueprint(Tests)
app.register_blueprint(PreguntasTests)
app.register_blueprint(OpcionesTests)
app.register_blueprint(RangosPuntajes)
app.register_blueprint(pacientes)
app.register_blueprint(especialistas)
app.register_blueprint(HorariosEspecialistas)
app.register_blueprint(ResultadoTests)
app.register_blueprint(RespuestasTests)
app.register_blueprint(RecomendacionesApoyos)
app.register_blueprint(Citas)

with app.app_context():
    # Crea todas las tablas definidas en los modelos
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
