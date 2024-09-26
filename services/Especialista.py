from flask import Blueprint, request, jsonify
from model.Especialista import tbEspecialista
from utils.db import db

especialistas = Blueprint('especialistas', __name__)

@especialistas.route('/Especialistas/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'AppTrastornoAnsiedad'
    return jsonify(result)

@especialistas.route('/Especialistas/v1/listar', methods=['GET'])
def getEspecialistas():
    result = {}
    Especialistas = tbEspecialista.query.all()
    result["data"] = Especialistas
    result["status_code"] = 200
    result["msg"] = "Se recupero los datos sin incovenientes"
    return jsonify(result), 200

@especialistas.route('/Especialistas/v1/insert', methods=['POST'])
def insert():
    result = {}
    body = request.get_json()
    nombreEspecialista = body.get('nombreEspecialista')
    apellidoEspecialista = body.get('apellidoEspecialista')
    dniEspecialista = body.get('dniEspecialista')
    especialidad = body.get('especialidad')
    celEspecialista = body.get('celEspecialista')
    correoEspecialista = body.get('correoEspecialista')
    contraEspecialista = body.get('contraEspecialista')

    if not nombreEspecialista or not apellidoEspecialista or not dniEspecialista or not especialidad or not celEspecialista or not correoEspecialista or not contraEspecialista:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400

    Especialista = tbEspecialista(nombreEspecialista, apellidoEspecialista, dniEspecialista, especialidad, celEspecialista, correoEspecialista, contraEspecialista)
    db.session.add(Especialista)
    db.session.commit()
    result["data"] = Especialista
    result["status_code"] = 201
    result["msg"] = "Se agrego el especialista"
    return jsonify(result), 201

@especialistas.route('/Especialistas/v1/update', methods=['POST'])  
def update():
    result = {}
    body = request.get_json()
    idEspecialista = body.get('idEspecialista')
    nombreEspecialista = body.get('nombreEspecialista')
    apellidoEspecialista = body.get('apellidoEspecialista')
    dniEspecialista = body.get('dniEspecialista')
    especialidad = body.get('especialidad')
    celEspecialista = body.get('celEspecialista')
    correoEspecialista = body.get('correoEspecialista')
    contraEspecialista = body.get('contraEspecialista')

    if not idEspecialista or not nombreEspecialista or not apellidoEspecialista or not dniEspecialista or not especialidad or not celEspecialista or not correoEspecialista or not contraEspecialista:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400  

    Especialista = tbEspecialista.query.get(idEspecialista)
    if not Especialista:
        result["status_code"] = 400
        result["msg"] = "Especialista no existe"
        return jsonify(result), 400

    Especialista.nombreEspecialista = nombreEspecialista
    Especialista.apellidoEspecialista = apellidoEspecialista
    Especialista.dniEspecialista = dniEspecialista
    Especialista.especialidad = especialidad
    Especialista.celEspecialista = celEspecialista
    Especialista.correoEspecialista = correoEspecialista
    Especialista.contraEspecialista = contraEspecialista
    db.session.commit()

    result["data"] = Especialista
    result["status_code"] = 202
    result["msg"] = "Se modificó el especialista"
    return jsonify(result), 202

@especialistas.route('/Especialistas/v1/delete', methods=['DELETE'])
def delete():
    result={}
    body=request.get_json()
    idEspecialista=body.get('idEspecialista')
    
    if not idEspecialista:
        result["status_code"]=400
        result["msg"]="Debe consignar un id valido"
        return jsonify(result),400
    
    Especialista=tbEspecialista.query.get(idEspecialista)
    if not Especialista:
        result["status_code"]=400
        result["msg"]="Especialista no existe"
        return jsonify(result),400
    
    db.session.delete(Especialista)
    db.session.commit()

    result["data"]=Especialista
    result["status_code"]=200
    result["msg"]="Se eliminó el especialista"
    return jsonify(result),200