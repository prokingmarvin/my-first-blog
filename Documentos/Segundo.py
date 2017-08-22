import re
import urllib2

def leehtml():
    response = urllib2.urlopen('http://python.org/')
    html= response.read()
    print html
    return (html)

def digitos(texto):
    patrondigito = re.compile("[0-9]")
    print patrondigito.findall(texto)
    print len(patrondigito.findall(texto))

digitos(leehtml())




def funcion(a,b):
    if (a > b):
        return("Mayor")
    else:
        return(-1)

def otra():
    c = 10
    print "Otra funcion"


funcion(20,10)
