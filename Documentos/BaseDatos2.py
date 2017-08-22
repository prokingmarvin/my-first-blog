import MySQLdb
import re
import urllib2

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'root'
DB_NAME = 'URLS'

def run_query(query=''):
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

    conn = MySQLdb.connect(*datos) # Conectar a la base de datos
    cursor = conn.cursor()         # Crear un cursor
    cursor.execute(query)          # Ejecutar una consulta

    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()   # Traer los resultados de un select
    else:
        conn.commit()              # Hacer efectiva la escritura de datos
        data = None

    cursor.close()                 # Cerrar el cursor
    conn.close()

    return data


datonum = raw_input("Numero: ")
datozelda = raw_input("Link: ")

html = urllib2.urlopen(datozelda).read()

descri1 = re.findall('"description" content="(.*?)"',html)
keywi1 = re.findall('"keywords" content="(.*?)"',html)

print hreff
print descri1
print keywi1

descri = raw_input("Ingrese Descripcion anterior: ")
keywi = raw_input("Ingrese Keyword anterior: ")

query2 = "INSERT INTO Paginas (idPaginas, webs, titulos, keys) VALUES (%s, '%s', '%s', '%s')" % (datonum, datozelda, descri, keywi)
run_query(query2)

query3 = "SELECT idPaginas, webs, titulos, keys FROM Paginas ORDER BY idPaginas"
result = run_query(query3)
print result
