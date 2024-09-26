from flask import Blueprint, request, jsonify
from model.recomendApoyo import tbRecomendApoyo
from utils.db import db

RecomendacionesApoyos = Blueprint('RecomendacionesApoyos', __name__)

@RecomendacionesApoyos.route('/RecomendacionesApoyos/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'AppTrastornoAnsiedad'
    return jsonify(result)

@RecomendacionesApoyos.route('/RecomendacionesApoyos/v1/listar', methods=['GET'])
def getRecomendacionesApoyos():
    result = {}
    recomendacionesApoyos = tbRecomendApoyo.query.all()
    result["data"] = recomendacionesApoyos
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los datos sin inconvenientes"
    return jsonify(result), 200

@RecomendacionesApoyos.route('/RecomendacionesApoyos/v1/insert', methods=['POST'])
def insertRecomendacionesApoyos():
    result = {}
    body = request.get_json()
    idEspecialista = body.get('idEspecialista')
    idResultadoTest = body.get('idResultadoTest')
    descripRecomendApoyo = body.get('descripRecomendApoyo')
    fechaRecomendApoyo = body.get('fechaRecomendApoyo')
    nivelAnsiedadRevision = body.get('nivelAnsiedadRevision')
    citaAgendada = body.get('citaAgendada')

    if not idEspecialista or not idResultadoTest or not descripRecomendApoyo or not fechaRecomendApoyo or not nivelAnsiedadRevision:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    RecomendacionApoyo = tbRecomendApoyo(idEspecialista, idResultadoTest, descripRecomendApoyo, fechaRecomendApoyo, nivelAnsiedadRevision, citaAgendada)
    db.session.add(RecomendacionApoyo)
    db.session.commit()
    result["data"] = RecomendacionApoyo
    result["status_code"] = 201
    result["msg"] = "Se agregó la recomendación o el tratamiento"
    return jsonify(result), 201

@RecomendacionesApoyos.route('/RecomendacionesApoyos/v1/update', methods=['POST'])
def updateRecomendacionesApoyos():
    result = {}
    body = request.get_json()
    idRecomendApoyo = body.get('idRecomendApoyo')
    idEspecialista = body.get('idEspecialista')
    idResultadoTest = body.get('idResultadoTest')
    descripRecomendApoyo = body.get('descripRecomendApoyo')
    fechaRecomendApoyo = body.get('fechaRecomendApoyo')
    nivelAnsiedadRevision = body.get('nivelAnsiedadRevision')
    citaAgendada = body.get('citaAgendada')

    if not idRecomendApoyo or not idEspecialista or not idResultadoTest or not descripRecomendApoyo or not fechaRecomendApoyo or not nivelAnsiedadRevision:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    RecomendacionApoyo = tbRecomendApoyo.query.get(idRecomendApoyo)
    if not RecomendacionApoyo:
        result['status_code'] = 400
        result["msg"] = "La recomendacion o el tratamiento no existe"
        return jsonify(result), 400
    
    RecomendacionApoyo.idEspecialista = idEspecialista
    RecomendacionApoyo.idResultadoTest = idResultadoTest
    RecomendacionApoyo.descripRecomendApoyo = descripRecomendApoyo
    RecomendacionApoyo.fechaRecomendApoyo = fechaRecomendApoyo
    RecomendacionApoyo.nivelAnsiedadRevision = nivelAnsiedadRevision
    RecomendacionApoyo.citaAgendada = citaAgendada
    db.session.commit()

    result["data"] = RecomendacionApoyo
    result["status_code"] = 202
    result["msg"] = "Se modificó la recomendacion o el tratamiento"
    return jsonify(result), 202

@RecomendacionesApoyos.route('/RecomendacionesApoyos/v1/delete', methods=['DELETE'])
def deleteRecomendacionesApoyos():
    result = {}
    body = request.get_json()
    idRecomendApoyo = body.get('idRecomendApoyo')
    if not idRecomendApoyo:
        result['status_code'] = 400
        result["msg"] = "Debe consignar un id valido"
        return jsonify(result), 400
    
    RecomendacionApoyo = tbRecomendApoyo.query.get(idRecomendApoyo)
    if not RecomendacionApoyo:
        result["status_code"] = 400
        result["msg"] = "La recomendacion o el tratamiento no existe"
        return jsonify(result), 400
    
    db.session.delete(RecomendacionApoyo)
    db.session.commit()

    result["data"] = RecomendacionApoyo
    result['status_code'] = 200
    result["msg"] = "Se eliminó la recomendacion o el tratamiento"
    return jsonify(result), 200