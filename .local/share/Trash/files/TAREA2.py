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

descri2 = descri1
keywi2 = keywi1
print descri2
print keywi2
query2 = "INSERT INTO Webs (idWebs, Links, Descripcion, Key) VALUES (%s, '%s', '%s', '%s')" % (datonum, datozelda, descri2, keywi2)

run_query(query2)
