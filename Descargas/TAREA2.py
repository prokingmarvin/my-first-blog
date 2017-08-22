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
for d in descri1:
    d = d.replace("'['"," ")
    descri1 = d
for e in descri1:
    e = e.replace("']'"," ")
for f in keywi1:
    f = f.replace("'['"," ")
    keywi1 = f
for g in keywi1:
    g = g.replace("']'"," ")
descri2 = descri1
keywi2 = keywi1
print descri2
print keywi2
query2 = "INSERT INTO Webs (idWebs, Links, Descripcion, Key) VALUES (%s, '%s', '%s', '%s')" % (datonum, datozelda, descri2, keywi2)
#print query2
run_query(query2)

#query3 = "SELECT idURL, LINK, Description, KeyWords FROM URL ORDER BY idURL"
#result = run_query(query3)
#print result
