# -*- coding: utf-8 -*-

from sys import path
path.append('/home/proking/python-web/app')

from sitioweb import contacto, ejemplos, form


def application(environ, start_response):
    peticion = environ['REQUEST_URI']
    parametros = environ['QUERY_STRING']

    if peticion.startswith('/contacto'):
        output = contacto.saludo()
    elif peticion.startswith('/ejemplos'):
        output = ejemplos.variable()
    elif peticion.startswith('/tabla'): 
        output = ejemplos.tabla()
    elif peticion.startswith('/form'):
        output = form.envia()
    elif peticion.startswith ('/recibe'):
        output = form.recibe(environ)
    else:
        output = "No se a dónde acceder!!"


    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return output
