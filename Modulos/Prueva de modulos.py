from Modulos.user import *

import os

import sqlite3

from Modulos.sqlite3faciliter import *

from Modulos.docmanager import *

from Modulos.cifrador import *

from Modulos.internetacceptor import *

#crear(False)

#crear(False)

#printbasededatos("all", "Datos", "cuentas")

#loggear(False)

#printbasededatos("all", "Datos", "cuentas")

#cambiar("7777", "contraseña", "7654")

#borrardatos("pasblo")

#print(ultimoident("Datos"))

#returned = loggearocrear(False, "pasblo", "7654", "l")

#print(returned)

#printbasededatos("all", "Datos", "cuentas")


sql = """
CREATE TABLE IF NOT EXISTS records(
usuario VARCHAR(50) NOT NULL,
record INTEGER NOT NULL,
ident INTEGER NOT NULL)"""

crearbasededatos(sql, "Records")

printbasededatos("all", "Records", "records")

ultimoidentv = ultimoident("Records")

insertardatos("Records", ("jaja", 10000, ultimoidentv+1), "Los datos fueron insertados correctamente", "Hubo un error al isertar los datos")

ultimoidentv = ultimoident("Records")

insertardatos("Records", ("jojoj", 12345, ultimoidentv+1), "Los datos fueron insertados correctamente", "Hubo un error al isertar los datos")

ultimoidentv = ultimoident("Records")

insertardatos("Records", ("roror", 1, ultimoidentv+1), "Los datos fueron insertados correctamente", "Hubo un error al isertar los datos")

printbasededatos("all", "Records", "records")

#encontrado = obtenerdato("Records", "records", "paulo")

#print(encontrado)

#encontrado = obtenerrecords("Records", "records", 12345, 1)

#print(encontrado)

#indice = encontrarpos("Records", "records", 1, 1, True)

#print(indice)

#borrardatos("Records", "records", "paulo")

#ya = comprovarindice("Records", "records", 2)

#print(ya)

#counter = 0

#while counter < 1000:
    #insertbasededatos("numberone, plusplus", counter+"hola", "Example3", "tab1", "Datos introducidos correctamente", "Error al introducir los datos")
    #counter = counter +1

#resetrecordpersonal("pasblo")

#error = cambiarele("Records", "records", "usuario", "pabo", 0, "olola")

#print(error)

#counter = 1

#print("Prueva HSP")

#while counter < 100:
    #insertardatosHSP("Records", ("pasblo", 1, counter))
    #counter = counter +1

#printbasededatos("all", "Records", "records")

#counter = 1

#print("Prueva NSP")

#while counter < 100:
    #insertardatos("Records", ("paulo", 0, counter), "Los datos fueron insertados correctamente", "Hubo un error al isertar los datos")
    #counter = counter +1

#renombrararchivo("jeje","..ddl", "hiola", ".httml")

#borrararchivo("hiola", ".httml")

#a = creararchivo("pasblo", ".py", "w+")

#print(a)

#pr = propiedades("pasblo", ".py", "w+")

#print(pr)

#txt = """
##Este archivo ha sido creado mediante un programa de python
#print("Hola")"""

#insertarenarchivo("pasblo", ".py", txt)

#archivo_leido = leerarchivo("quijote", ".txt", "r")

#print(archivo_leido)

#cifrar_archivo("quijote", ".txt", 3,"quijote_cifrado", ".txt")

#descifrar_archivo("quijote_cifrado", ".txt", 3, "quijote_descifrado", ".txt")

#corregir_descifrado("quijote_descifrado", ".txt", "quijote_corregido", ".txt")

#cifrada = cifrar_contraseña("2001")

#print(cifrada)

#descifrada = descifrar_contraseña(cifrada, 2)

#print(descifrada)

#printbasededatos("all", "Records", "records")

#abrirpaginaweb("google", ".es")

#abrirbuscador("youtube", "lindsey stirling")

#buscarcualquiercosa("www.google.es")
