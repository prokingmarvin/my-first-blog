import MySQLdb

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'root'
DB_NAME = 'BaseDatos1'

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
dato = raw_input("Nombre: ")
dato1 = raw_input("Numero: ")
query = "INSERT INTO Tabla1 (Nombre,Numero) VALUES ('%s',%s)" % (dato,dato1)
run_query(query)


#IngresoDato
#datocad = raw_input("Nombre: ")
#datonum = raw_input("Carne: ")
#query = "INSERT INTO Nombre (nombre,carne) VALUES ('%s',%s)" % (datocad,datonum)
#run_query(query)

#ListarDato
#query = "SELECT nombre, carne FROM Nombre ORDER BY carne DESC"
#result = run_query(query)
#print result

#Busqueda
#criterio = raw_input("Nombre: ")
#query = "SELECT nombre,carne FROM Nombre WHERE nombre = '%s'" % criterio
#result = run_query(query)
#print result

#Borrar
#criterio = raw_input("eliminar: ")
#query = "DELETE FROM Nombre WHERE nombre = '%s'" % criterio
#run_query(query)

#Actualizar
b1 = raw_input("Nombre: ")
b2 = raw_input("CarneNuevo: ")
b3 = raw_input("Carne")
query = "UPDATE Nombre SET nombre='%s',carne=%s WHERE carne = %i" % (b1,b2, int(b3))
run_query(query)
