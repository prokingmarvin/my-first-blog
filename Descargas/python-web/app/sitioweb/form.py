# -*- coding: utf-8 -*-
import re
import urllib2
import MySQLdb
import cgi

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'manu.uver'
DB_NAME = 'Web'


def run_query(query=''):
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

    conn = MySQLdb.connect(*datos)
    cursor = conn.cursor()
    cursor.execute(query)

    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()
    else:
        conn.commit()
        data = None

    cursor.close()
    conn.close()

    return data

def envia():
    texto = "<form action=\"http://python-web/recibe\" method=\"get\">\
            <p>Ingresar Busqueda: <input type=\"text\" name=\"nombre\" value=\"\"/></p>\
            <p><input type=\"submit\" value=\"Buscar\"/></p>\
            </form>"
    return texto

def recibe(parametros):
    texto = parametros['QUERY_STRING']
    texto = texto[7:len(texto)]
    query="SELECT * FROM Pagina WHERE link LIKE '%"+texto+"%' OR keywords LIKE '%"+texto+"%' OR datos LIKE '%"+texto+"%'"
    resultado = run_query(query)
    tabla = "<table style=\"width:100%\"> "
    for fila in resultado:
        dato1 = str(fila[0])
        dato2 = str(fila[1])
        dato3 = str(fila[2])

        tabla += "<table> \
                        <tr>\
                        <td></td>\
                        <td><a href="+dato1+" >"+ dato1+"</a></td>\
                        </tr>\
                        <tr>\
                        <td></td>\
                        <td><a>"+ dato2 + "</a></td>\
                        </tr>\
                        <tr>\
                        <td></td>\
                        <td><a>"+ dato3 + "</a></td>\
                        </tr>\
                        "
    tabla += " </table>"
    return tabla
