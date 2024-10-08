import datetime
from flask import Blueprint, request, jsonify
from model.resultadoTest import tbResultadoTest
from model.rangosPuntaje import tbRangosPuntaje
from model.respuestasTest import tbRespuestasTest
from datetime import datetime
from utils.db import db

# Definición de blueprint
ResultadoTests = Blueprint('ResultadoTests', __name__)

@ResultadoTests.route('/ResultadoTests/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'AppTrastornoAnsiedad'
    return jsonify(result)

@ResultadoTests.route('/ResultadoTests/v1/listar', methods=['GET'])
def getResultadoTest():
    result = {}
    ResultadoTes = tbResultadoTest.query.all()
    result["data"] = ResultadoTes
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los resultados de los tests sin inconvenientes"
    return jsonify(result), 200

@ResultadoTests.route('/ResultadoTests/v1/insert', methods=['POST'])
def insertResultadoTest():
    result = {}
    body = request.get_json()
    idPaciente = body.get('idPaciente')
    puntajeResultadoTest = body.get('puntajeResultadoTest')
    infoResultado = body.get('infoResultado')
    fechaResultadoTest = body.get('fechaResultadoTest')
    revisadoResultadoTest = body.get('revisadoResultadoTest')
    revisando = body.get('revisando')

    if not idPaciente or not infoResultado or not fechaResultadoTest or puntajeResultadoTest is None:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400

    resultadotest = tbResultadoTest(idPaciente, puntajeResultadoTest, infoResultado, fechaResultadoTest, revisadoResultadoTest, revisando)
    db.session.add(resultadotest)
    db.session.commit()
    result["data"] = resultadotest
    result["status_code"] = 201
    result["msg"] = "Se agregó el resultado del test"
    return jsonify(result), 201

@ResultadoTests.route('/ResultadoTests/v1/update', methods=['POST'])
def updateResultadoTests():
    result = {}
    body = request.get_json()
    idResultadoTest = body.get('idResultadoTest')
    idPaciente = body.get('idPaciente')
    puntajeResultadoTest = body.get('puntajeResultadoTest')
    infoResultado = body.get('infoResultado')
    fechaResultadoTest = body.get('fechaResultadoTest')
    revisadoResultadoTest = body.get('revisadoResultadoTest')
    revisando = body.get('revisando')

    if not idResultadoTest or not idPaciente or not infoResultado or not fechaResultadoTest or puntajeResultadoTest is None:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400

    resultadosTest = tbResultadoTest.query.get(idResultadoTest)
    if not resultadosTest:
        result['status_code'] = 400
        result["msg"] = "El resultado del test no existe"
        return jsonify(result), 400

    resultadosTest.idPaciente = idPaciente
    resultadosTest.puntajeResultadoTest = puntajeResultadoTest
    resultadosTest.infoResultado = infoResultado
    resultadosTest.fechaResultadoTest = fechaResultadoTest
    resultadosTest.revisadoResultadoTest = revisadoResultadoTest
    resultadosTest.revisando = revisando
    db.session.commit()

    result["data"] = resultadosTest
    result["status_code"] = 202
    result["msg"] = "Se modificó el resultado del test"
    return jsonify(result), 202

@ResultadoTests.route('/ResultadoTests/v1/send', methods=['POST'])
def sendResultado():
    body = request.get_json()
    respuestas = list(body.get("respuestas"))
    idTest = int(body.get("idTest"))
    idPaciente = int(body.get("idPaciente"))
    idResultadoTest = tbResultadoTest.query.count() + 1
    puntaje = 0
    tbRespuestas = []
    for respuesta in respuestas:
        tbRespuestas.append(tbRespuestasTest(idResultadoTest = idResultadoTest,
                                             idTest= idTest,
                                             pregunta=respuesta.get("pregunta"),
                                             respuesta=respuesta.get("respuesta"),
                                             valorRespuesta=respuesta.get("valorRespuesta")))
        puntaje += int(respuesta["valorRespuesta"])
    rangoPuntaje = tbRangosPuntaje.query.filter(tbRangosPuntaje.idTest == idTest and tbRangosPuntaje.minimoPuntaje < puntaje and tbRangosPuntaje.maximoPuntaje > puntaje).first()
    interpretacion = rangoPuntaje.interpretacionPuntaje
    resultado = tbResultadoTest(idPaciente=idPaciente,puntajeResultadoTest=puntaje,infoResultado=interpretacion,fechaResultadoTest=datetime.now(),
                                revisando= False,revisadoResultadoTest=False)
    db.session.add(resultado)
    db.session.commit()
    db.session.add_all(tbRespuestas)
    db.session.commit()
    result = {}
    result["data"] = resultado
    return jsonify(result),200

@ResultadoTests.route('/ResultadoTests/v1/delete', methods=['DELETE'])
def deleteResultadoTests():
    result = {}
    body = request.get_json()
    idResultadoTest = body.get('idResultadoTest')
    if not idResultadoTest:
        result["status_code"] = 400
        result["msg"] = "Debe consignar un id válido"
        return jsonify(result), 400

    resultadosTest = tbResultadoTest.query.get(idResultadoTest)
    if not resultadosTest:
        result["status_code"] = 400
        result["msg"] = "El resultado no existe"
        return jsonify(result), 400

    db.session.delete(resultadosTest)
    db.session.commit()

    result["data"] = resultadosTest
    result["status_code"] = 200
    result["msg"] = "Se eliminó el resultado"
    return jsonify(result), 200