from flask import Blueprint, request, jsonify
from model.Cita import tbCita
from utils.db import db

Citas = Blueprint('Citas', __name__)

@Citas.route('/Citas/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'AppTrastornoAnsiedad'
    return jsonify(result)

@Citas.route('/Citas/v1/listar', methods=['GET'])
def getCitas():
    result = {}
    citas = tbCita.query.all()
    result["data"] = citas
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los datos sin inconvenientes"
    return jsonify(result), 200

@Citas.route('/Citas/v1/insert', methods=['POST'])
def insertCitas():
    result = {}
    body = request.get_json()
    idPaciente = body.get('idPaciente')
    idEspecialista = body.get('idEspecialista')
    diagnostico = body.get('diagnostico')
    nivelAnsiedad = body.get('nivelAnsiedad')
    fechaCita = body.get('fechaCita')
    fechaDiagnostico = body.get('fechaDiagnostico')
    horaCita = body.get('horaCita')
    culminado = body.get('culminado')

    if not idPaciente or not idEspecialista or not diagnostico or not nivelAnsiedad or not fechaCita or not fechaDiagnostico or not horaCita:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    Cita = tbCita(idPaciente, idEspecialista, diagnostico, nivelAnsiedad, fechaCita, fechaDiagnostico, horaCita, culminado)
    db.session.add(Cita)
    db.session.commit()
    result["data"] = Cita
    result["status_code"] = 201
    result["msg"] = "Se agregó la cita"
    return jsonify(result), 201

@Citas.route('/Citas/v1/update', methods=['POST'])
def updateCitas():
    result = {}
    body = request.get_json()
    idCita = body.get('idCita')
    idPaciente = body.get('idPaciente')
    idEspecialista = body.get('idEspecialista')
    diagnostico = body.get('diagnostico')
    nivelAnsiedad = body.get('nivelAnsiedad')
    fechaCita = body.get('fechaCita')
    fechaDiagnostico = body.get('fechaDiagnostico')
    horaCita = body.get('horaCita')
    culminado = body.get('culminado')

    if not idCita or not idPaciente or not idEspecialista or not diagnostico or not nivelAnsiedad or not fechaCita or not fechaDiagnostico or not horaCita:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    Cita = tbCita.query.get(idCita)
    if not Cita:
        result['status_code'] = 400
        result["msg"] = "La cita no existe"
        return jsonify(result), 400
    
    Cita.idPaciente = idPaciente
    Cita.idEspecialista = idEspecialista
    Cita.diagnostico = diagnostico
    Cita.nivelAnsiedad = nivelAnsiedad
    Cita.fechaCita = fechaCita
    Cita.fechaDiagnostico = fechaDiagnostico
    Cita.horaCita = horaCita
    Cita.culminado = culminado
    db.session.commit()

    result["data"] = Cita
    result["status_code"] = 202
    result["msg"] = "Se modificó la cita"
    return jsonify(result), 202

@Citas.route('/Citas/v1/delete', methods=['DELETE'])
def deleteCitas():
    result = {}
    body = request.get_json()
    idCita = body.get('idCita')
    if not idCita:
        result['status_code'] = 400
        result["msg"] = "Debe consignar un id valido"
        return jsonify(result), 400
    
    Cita = tbCita.query.get(idCita)
    if not Cita:
        result["status_code"] = 400
        result["msg"] = "La cita no existe"
        return jsonify(result), 400
    
    db.session.delete(Cita)
    db.session.commit()

    result["data"] = Cita
    result['status_code'] = 200
    result["msg"] = "Se eliminó la cita"
    return jsonify(result), 200