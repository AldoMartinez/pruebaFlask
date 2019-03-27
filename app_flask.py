# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:04:00 2019

@author: AAMARTINEZ
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def Welcome():
    return "Hello World"

@app.route("/nexus/<datosUsuario>")
def nexusApi(datosUsuario):
    claveSplit = "nexusApiAldo"
    # Los datos del alumno vienen en un solo string separados por "nexusApiAldo"
    datos = datosUsuario.split(claveSplit)
    if len(datos) == 2:
        nombreUsuario = datos[0]
        contrasenaUsuario = datos[1]
        return nombreUsuario
    return "Error"

if __name__ == "__main__":
    app.run()
