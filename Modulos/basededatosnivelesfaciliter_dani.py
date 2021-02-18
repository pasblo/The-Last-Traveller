import sqlite3

import os

from Modulos.sqlite3faciliter import *

import shutil

def crearbasededatosniveles(user):

	if (os.path.isdir(os.getcwd() + "\\" + "sqlite3")):

		conexion = sqlite3.connect("sqlite3/%s.sqlite3" %("DataNiveles" + user))

		consulta = conexion.cursor()

	else:

		os.mkdir(os.getcwd() + "\\" + "sqlite3")

		conexion = sqlite3.connect("sqlite3/%s.sqlite3" %("DataNiveles" + user))

		consulta = conexion.cursor()

	sql1 = """
CREATE TABLE IF NOT EXISTS Lv1(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos
	
	sql2 = """
CREATE TABLE IF NOT EXISTS Lv2(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos
	
	sql3 = """
CREATE TABLE IF NOT EXISTS Lv3(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql4 = """
CREATE TABLE IF NOT EXISTS Lv4(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql5 = """
CREATE TABLE IF NOT EXISTS Lv5(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql6 = """
CREATE TABLE IF NOT EXISTS Lv6(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql7 = """
CREATE TABLE IF NOT EXISTS Lv7(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql8 = """
CREATE TABLE IF NOT EXISTS Lv8(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql9 = """
CREATE TABLE IF NOT EXISTS Lv9(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql10 = """
CREATE TABLE IF NOT EXISTS Lv10(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql11 = """
CREATE TABLE IF NOT EXISTS Lv11(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql12 = """
CREATE TABLE IF NOT EXISTS Lv12(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql13 = """
CREATE TABLE IF NOT EXISTS Lv13(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql14 = """
CREATE TABLE IF NOT EXISTS Lv14(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql15 = """
CREATE TABLE IF NOT EXISTS Lv15(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql16 = """
CREATE TABLE IF NOT EXISTS Lv16(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql17 = """
CREATE TABLE IF NOT EXISTS Lv17(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql18 = """
CREATE TABLE IF NOT EXISTS Lv18(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql19 = """
CREATE TABLE IF NOT EXISTS Lv19(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql20= """
CREATE TABLE IF NOT EXISTS Lv20(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql21 = """
CREATE TABLE IF NOT EXISTS Lv21(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql22 = """
CREATE TABLE IF NOT EXISTS Lv22(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql23 = """
CREATE TABLE IF NOT EXISTS Lv23(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql24 = """
CREATE TABLE IF NOT EXISTS Lv24(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql25 = """
CREATE TABLE IF NOT EXISTS Lv25(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql26 = """
CREATE TABLE IF NOT EXISTS Lv26(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql27 = """
CREATE TABLE IF NOT EXISTS Lv27(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql28 = """
CREATE TABLE IF NOT EXISTS Lv28(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos) """ #En segundos

	sql29 = """
CREATE TABLE IF NOT EXISTS Lv29(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos

	sql30 = """
CREATE TABLE IF NOT EXISTS Lv30(
puntuacion INTEGER NOT NULL,
matados INTEGER NOT NULL,
llegado INTEGER NOT NULL,
muertes INTEGER NOT NULL,
tiempo INTEGER NOT NULL,
ident INTEGER PRIMARY KEY AUTOINCREMENT) """ #En segundos

	consulta.execute(sql1)
	conexion.commit()
	consulta.execute(sql2)
	conexion.commit()
	consulta.execute(sql3)
	conexion.commit()
	consulta.execute(sql4)
	conexion.commit()
	consulta.execute(sql5)
	conexion.commit()
	consulta.execute(sql6)
	conexion.commit()
	consulta.execute(sql7)
	conexion.commit()
	consulta.execute(sql8)
	conexion.commit()
	consulta.execute(sql9)
	conexion.commit()
	consulta.execute(sql10)
	conexion.commit()
	consulta.execute(sql11)
	conexion.commit()
	consulta.execute(sql12)
	conexion.commit()
	consulta.execute(sql13)
	conexion.commit()
	consulta.execute(sql14)
	conexion.commit()
	consulta.execute(sql15)
	conexion.commit()
	consulta.execute(sql16)
	conexion.commit()
	consulta.execute(sql17)
	conexion.commit()
	consulta.execute(sql18)
	conexion.commit()
	consulta.execute(sql19)
	conexion.commit()
	consulta.execute(sql20)
	conexion.commit()
	consulta.execute(sql21)
	conexion.commit()
	consulta.execute(sql22)
	conexion.commit()
	consulta.execute(sql23)
	conexion.commit()
	consulta.execute(sql24)
	conexion.commit()
	consulta.execute(sql25)
	conexion.commit()
	consulta.execute(sql26)
	conexion.commit()
	consulta.execute(sql27)
	conexion.commit()
	consulta.execute(sql28)
	conexion.commit()
	consulta.execute(sql29)
	conexion.commit()
	consulta.execute(sql30)

	conexion.commit()

	consulta.close()

	conexion.close()

def insertardatosniveles(datos, user, nivel):

	conexion = sqlite3.connect("sqlite3/%s.sqlite3" %("DataNiveles" + user))

	consulta = conexion.cursor()

	if nivel == 1:
		sql = """
INSERT INTO Lv1(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""
	
	elif nivel == 2:
		sql = """
INSERT INTO Lv2(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 3:
		sql = """
INSERT INTO Lv3(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 4:
		sql = """
INSERT INTO Lv4(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 5:
		sql = """
INSERT INTO Lv5(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 6:
		sql = """
INSERT INTO Lv6(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 7:
		sql = """
INSERT INTO Lv7(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 8:
		sql = """
INSERT INTO Lv8(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 9:
		sql = """
INSERT INTO Lv9(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 10:
		sql = """
INSERT INTO Lv10(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 11:
		sql = """
INSERT INTO Lv11(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 12:
		sql = """
INSERT INTO Lv12(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 13:
		sql = """
INSERT INTO Lv13(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 14:
		sql = """
INSERT INTO Lv14(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 15:
		sql = """
INSERT INTO Lv15(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 16:
		sql = """
INSERT INTO Lv16(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 17:
		sql = """
INSERT INTO Lv17(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 18:
		sql = """
INSERT INTO Lv18(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 19:
		sql = """
INSERT INTO Lv19(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 20:
		sql = """
INSERT INTO Lv20(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 21:
		sql = """
INSERT INTO Lv21(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 22:
		sql = """
INSERT INTO Lv22(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 23:
		sql = """
INSERT INTO Lv23(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 24:
		sql = """
INSERT INTO Lv24(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 25:
		sql = """
INSERT INTO Lv25(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 26:
		sql = """
INSERT INTO Lv26(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 27:
		sql = """
INSERT INTO Lv27(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 28:
		sql = """
INSERT INTO Lv28(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 29:
		sql = """
INSERT INTO Lv29(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""

	elif nivel == 30:
		sql = """
INSERT INTO Lv30(puntuacion, matados, llegado, muertes, tiempo)
VALUES (?, ?, ?, ?, ?)"""
	
	consulta.execute(sql, datos)

	conexion.commit()

	consulta.close()

def extraerdatos(user, nivel, numerodedatos = "all"):

	conexion = sqlite3.connect("sqlite3/%s.sqlite3" %("DataNiveles" + user))

	consulta = conexion.cursor()

	sql = "SELECT * FROM %s" %("Lv" + str(nivel))

	if numerodedatos == "all":

		consulta.execute(sql)

		total = consulta.fetchall()

	conexion.commit()

	consulta.close()

	conexion.close()

	return total

def ordenardbniveles(user, nivel): #Primero el mejor y asi en orden
	
	conexion = sqlite3.connect("sqlite3/%s.sqlite3" %("DataNiveles" + user))

	consulta = conexion.cursor()

	sql = "SELECT * FROM %s" %("Lv" + str(nivel))

	consulta.execute(sql)

	total = consulta.fetchall()

	conjunto = []

	x = []

	for i in total:
		p = i[0]
		t = i[4]

		x.append(2.9*p/(t+(p/10000)))

	print(total)

	for i in total:

		pos = total.index(i)

		conjunto.append((total[pos - 1], x[pos - 1]))
 

	x.sort()
	x.reverse()

	print("Total")
	print(total)
	print("x")
	print(x)
	print("Conjunto")
	print(conjunto)

	LALISTA  = []

	for i in x:
		for o in conjunto:
			if i == o[1]:
				LALISTA.insert(0, o[0])

	LALISTA.reverse()

	print("LALISTA")
	print(LALISTA)

	for i in LALISTA:

		sql= """
		DELETE FROM %s
		WHERE puntuacion = '%s'""" %("Lv" + str(nivel), i[0])

		consulta.execute(sql)

		conexion.commit()

	for i in LALISTA:
		sql = """
		INSERT INTO %s(puntuacion, matados, llegado, muertes, tiempo, ident)
		VALUES (?, ?, ?, ?, ?, ?)""" %("Lv" + str(nivel))

		consulta.execute(sql, i)

		conexion.commit()

	consulta.close()

	conexion.close()


	"""

	sql = SELECT * FROM x" x = tabla de la base de datos                            |
                                                                                    |== Para extraer todos los registros
	x = consulta.fetchall() = Te extrae todos los registros de la tabla introducida |

	sql = "SELECT * FROM x WHERE ident <=> y " x = tabla de la base de datos    y = numero de registro a extraer   |
                                                                                                                   | == Para extraer un solo registro
	x = consulta.fetchone() = Te extrae el registro introducido en la anterior linea                               |

	conexion.commit() = Guarda los cambios en la base de datos ¡¡¡¡Importante hacer esto antes de hacer otro cambio!!!!

	"""

	pass

def calculartotalpuntuacion(user): 

	conexion = sqlite3.connect("sqlite3/%s.sqlite3" %("DataNiveles" + user))

	consulta = conexion.cursor()

	puntuacion = 0

	cont = 1

	while cont < 30:

		sql = "SELECT * FROM %s" %("Lv" + str(cont))

		consulta.execute(sql)

		total = consulta.fetchall()

		try:

			puntuacion = puntuacion + (total[0])[0]

		except:
			pass

		cont += 1

	conexion.commit()

	consulta.close()

	conexion.close()

	return puntuacion

def actualizarpuntuacion(puntuacion, user):

	conexion = sqlite3.connect("sqlite3/Records.sqlite3")

	consulta = conexion.cursor()

	sql = """
UPDATE records SET record = '%s' WHERE usuario = '%s' """ %(puntuacion, user)

	consulta.execute(sql)

	conexion.commit()

	consulta.close()

	conexion.close()

def borardbniveles(user):

	conexion = sqlite3.connect("sqlite3/%s.sqlite3" %("DataNiveles" + user))

	consulta = conexion.cursor()

	cont = 1

	while cont < 31:

		sql = "SELECT * FROM %s" %("Lv" + str(cont))

		consulta.execute(sql)

		total = consulta.fetchall()

		print(total)

		print(len(total))

		extraido = []

		for parte in total:

			extraido.append(parte[5])

		print(extraido)

		for i in extraido:

			print('DELETE FROM %s WHERE ident = %s'%("Lv" + str(cont), i))

			consulta.execute('DELETE FROM %s WHERE ident = %s'%("Lv" + str(cont), i))

			conexion.commit()

		cont += 1

	conexion.commit()

	consulta.close()

	conexion.close()