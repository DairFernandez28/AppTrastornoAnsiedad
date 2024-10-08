from flask import Blueprint, request, jsonify
from model.Paciente import tbPaciente
from utils.db import db

pacientes = Blueprint('pacientes', __name__)

@pacientes.route('/Pacientes/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'AppTrastornoAnsiedad'
    return jsonify(result)

@pacientes.route('/Pacientes/v1/listar', methods=['GET'])
def getPacientes():
    result = {}
    Pacientes = tbPaciente.query.all()
    result["data"] = Pacientes
    result["status_code"] = 200
    result["msg"] = "Se recupero los datos sin incovenientes"
    return jsonify(result), 200

@pacientes.route('/Pacientes/v1/login', methods=['POST'])
def loginPaciente():
    result = {}
    body = request.get_json()
    Paciente = tbPaciente.query.filter(tbPaciente.correoPaciente == body.get("correoPaciente")).all()
    if len(Paciente) == 0:
        result["data"] = Paciente
        result["status_code"] = 400
        result["msg"] = "Paciente no encontrado"
        return jsonify(result) , 400
    FinalPaciente = list(filter(lambda p: p.contraPaciente == body.get("contraPaciente"),Paciente))
    result["data"] = FinalPaciente
    if len(FinalPaciente) == 0:
        result["status_code"] = 400
        result["msg"] = "Contrasena incorrecta"
        return jsonify(result),400
    result["msg"] = "Login exitoso"
    result["status_code"] = 200

    return jsonify(result),200
 
@pacientes.route('/Paciente/v1/idByDNI',methods=['GET'])
def getIdByDNI():
    dni = request.args["dni"]
    result = {}
    Paciente = tbPaciente.query.filter(tbPaciente.dniPaciente == dni).first()
    if Paciente == None:
        return jsonify(-1),400
    return jsonify(Paciente.idPaciente),200

@pacientes.route('/Pacientes/v1/insert', methods=['POST'])
def insert():
    result = {}
    body = request.get_json()
    nombrePaciente = body.get('nombrePaciente')
    apellidoPaciente = body.get('apellidoPaciente')
    dniPaciente = body.get('dniPaciente')
    distrito = body.get('distrito')
    celPaciente = body.get('celPaciente')
    correoPaciente = body.get('correoPaciente')
    contraPaciente = body.get('contraPaciente')

    if not nombrePaciente or not apellidoPaciente or not dniPaciente or not distrito or not celPaciente or not correoPaciente or not contraPaciente:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400

    Paciente = tbPaciente(nombrePaciente, apellidoPaciente, dniPaciente, distrito, celPaciente, correoPaciente, contraPaciente)
    db.session.add(Paciente)
    db.session.commit()
    result["data"] = Paciente
    result["status_code"] = 201
    result["msg"] = "Se agrego el paciente"
    return jsonify(result), 201

@pacientes.route('/Pacientes/v1/update', methods=['POST'])  
def update():
    result = {}
    body = request.get_json()
    idPaciente = body.get('idPaciente')
    nombrePaciente = body.get('nombrePaciente')
    apellidoPaciente = body.get('apellidoPaciente')
    dniPaciente = body.get('dniPaciente')
    distrito = body.get('distrito')
    celPaciente = body.get('celPaciente')
    correoPaciente = body.get('correoPaciente')
    contraPaciente = body.get('contraPaciente')

    if not idPaciente or not nombrePaciente or not apellidoPaciente or not dniPaciente or not distrito or not celPaciente or not correoPaciente or not contraPaciente:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400  

    Paciente = tbPaciente.query.get(idPaciente)
    if not Paciente:
        result["status_code"] = 400
        result["msg"] = "Paciente no existe"
        return jsonify(result), 400

    Paciente.nombrePaciente = nombrePaciente
    Paciente.apellidoPaciente = apellidoPaciente
    Paciente.dniPaciente = dniPaciente
    Paciente.distrito = distrito
    Paciente.celPaciente = celPaciente
    Paciente.correoPaciente = correoPaciente
    Paciente.contraPaciente = contraPaciente
    db.session.commit()

    result["data"] = Paciente
    result["status_code"] = 202
    result["msg"] = "Se modificó el paciente"
    return jsonify(result), 202

@pacientes.route('/Pacientes/v1/delete', methods=['DELETE'])
def delete():
    result={}
    body=request.get_json()
    idPaciente=body.get('idPaciente')
    
    if not idPaciente:
        result["status_code"]=400
        result["msg"]="Debe consignar un id valido"
        return jsonify(result),400
    
    Paciente=tbPaciente.query.get(idPaciente)
    if not Paciente:
        result["status_code"]=400
        result["msg"]="Paciente no existe"
        return jsonify(result),400
    
    db.session.delete(Paciente)
    db.session.commit()

    result["data"]=Paciente
    result["status_code"]=200
    result["msg"]="Se eliminó el paciente"
    return jsonify(result),200