from flask import Blueprint, request, jsonify
from model.respuestasTest import tbRespuestasTest
from utils.db import db

# Definición de blueprint
RespuestasTests = Blueprint('RespuestasTests', __name__)

@RespuestasTests.route('/RespuestasTests/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'AppTrastornoAnsiedad'
    return jsonify(result)

@RespuestasTests.route('/RespuestasTests/v1/listar', methods=['GET'])
def getRespuestasTest():
    result = {}
    respuestasTest = tbRespuestasTest.query.all()
    result["data"] = respuestasTest
    result["status_code"] = 200
    result["msg"] = "Se recuperaron las respuestas de los test sin inconvenientes"
    return jsonify(result), 200

@RespuestasTests.route('/RespuestasTests/v1/insert', methods=['POST'])
def insertRespuestasTest():
    result = {}
    body = request.get_json()
    idResultadoTest = body.get('idResultadoTest')
    idTest = body.get('idTest')
    pregunta = body.get('pregunta')
    respuesta = body.get('respuesta')
    valorRespuesta = body.get('valorRespuesta')

    if not idResultadoTest or not idTest or not pregunta or not respuesta or valorRespuesta is None:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400

    respuestaTest = tbRespuestasTest(idResultadoTest=idResultadoTest, idTest=idTest, pregunta=pregunta, respuesta=respuesta, valorRespuesta=valorRespuesta)
    db.session.add(respuestaTest)
    db.session.commit()
    result["data"] = respuestaTest
    result["status_code"] = 201
    result["msg"] = "Se agregó la respuesta del test"
    return jsonify(result), 201

@RespuestasTests.route('/RespuestasTests/v1/delete', methods=['DELETE'])
def deleteRespuestasTests():
    result = {}
    body = request.get_json()
    idRespuestas = body.get('idRespuestas')
    if not idRespuestas:
        result["status_code"] = 400
        result["msg"] = "Debe consignar un id válido"
        return jsonify(result), 400

    respuestasTests = tbRespuestasTest.query.get(idRespuestas)
    if not respuestasTests:
        result["status_code"] = 400
        result["msg"] = "La respuesta no existe"
        return jsonify(result), 400

    db.session.delete(respuestasTests)
    db.session.commit()

    result["data"] = respuestasTests
    result["status_code"] = 200
    result["msg"] = "Se eliminó la respuesta"
    return jsonify(result), 200