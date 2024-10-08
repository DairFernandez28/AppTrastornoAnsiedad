from flask import Blueprint, request, jsonify
from model.preguntasTest import tbPreguntasTest
from model.opcionesTest import tbOpcionesTest
from utils.db import db

# Definición del blueprint
PreguntasTests = Blueprint('PreguntasTests', __name__)

@PreguntasTests.route('/PreguntasTests/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'AppTrastornoAnsiedad'
    return jsonify(result)

@PreguntasTests.route('/PreguntasTests/v1/listar', methods=['GET'])
def getPreguntasTest():
    result = {}
    preguntaTest = tbPreguntasTest.query.all()
    result["data"] = preguntaTest
    result["status_code"] = 200
    result["msg"] = "Se recuperaron las preguntas del test sin inconvenientes"
    return jsonify(result), 200

@PreguntasTests.route('/PreguntasTests/v1/listarPorIdTest',methods=['GET'])
def getPreguntasTestById():
    params = request.args
    data = []
    preguntaTest = tbPreguntasTest.query.filter(tbPreguntasTest.idTest == int(params["idTest"])).all()
    for p in preguntaTest:
        element = {}
        element["idPreguntaTest"] = p.idPreguntaTest
        element["idTest"] = p.idTest
        element["enunciadoPreguntaTest"] = p.enunciadoPreguntaTest
        element["numPregunta"] = p.numPregunta
        element["opciones"] = tbOpcionesTest.query.filter(tbOpcionesTest.idPreguntaTest == p.idPreguntaTest).all()
        data.append(element)
    result = {}
    result["data"] = data
    result["status_code"] = 200
    result["msg"] = "Se recuperaron las preguntas del test sin inconvenientes"

    return jsonify(result), 200

@PreguntasTests.route('/PreguntasTests/v1/insert', methods=['POST'])
def insertPreguntasTest():
    result = {}
    body = request.get_json()
    idTest = body.get('idTest')
    enunciadoPreguntaTest = body.get('enunciadoPreguntaTest')
    numPregunta = body.get('numPregunta')

    if not idTest or not enunciadoPreguntaTest or not numPregunta:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400

    preguntTest = tbPreguntasTest(idTest=idTest, enunciadoPreguntaTest=enunciadoPreguntaTest, numPregunta=numPregunta)
    db.session.add(preguntTest)
    db.session.commit()
    result["data"] = preguntTest
    result["status_code"] = 201
    result["msg"] = "Se agregó la pregunta del test"
    return jsonify(result), 201

@PreguntasTests.route('/PreguntasTests/v1/update', methods=['POST'])
def updatePreguntasTest():
    result = {}
    body = request.get_json()
    idPreguntaTest = body.get('idPreguntaTest')
    idTest = body.get('idTest')
    enunciadoPreguntaTest = body.get('enunciadoPreguntaTest')
    numPregunta = body.get('numPregunta')

    if not idPreguntaTest or not idTest or not enunciadoPreguntaTest or not numPregunta:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    preguntaTest = tbPreguntasTest.query.get(idPreguntaTest)
    if not preguntaTest:
        result["status_code"] = 400
        result["msg"] = "No existe la pregunta del test"
        return jsonify(result), 400
    
    preguntaTest.idTest = idTest
    preguntaTest.enunciadoPreguntaTest = enunciadoPreguntaTest
    preguntaTest.numPregunta = numPregunta
    db.session.commit()

    result["data"] = preguntaTest
    result["status_code"] = 202
    result["msg"] = "Se modificó la pregunta del test"
    return jsonify(result), 202

@PreguntasTests.route('/PreguntasTests/v1/delete', methods=['DELETE'])
def deletePreguntasTest():
    result = {}
    body = request.get_json()
    idPreguntaTest = body.get('idPreguntaTest')
    if not idPreguntaTest:
        result["status_code"] = 400
        result["msg"] = "Debe consignar un id de la pregunta del test"
        return jsonify(result), 400

    preguntaTest = tbPreguntasTest.query.get(idPreguntaTest)
    if not preguntaTest:
        result["status_code"] = 400
        result["msg"] = "No existe la pregunta del test"
        return jsonify(result), 400
    
    db.session.delete(preguntaTest)
    db.session.commit()

    result["data"] = preguntaTest
    result["status_code"] = 200
    result["msg"] = "Se eliminó la pregunta del test"
    return jsonify(result), 200