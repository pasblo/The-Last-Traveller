import sqlite3

import os

from Modulos.sqlite3faciliter import *

def crearbasededatosajustes(datospredefinidos = False):

	print(datospredefinidos)
	
	sql = """
CREATE TABLE IF NOT EXISTS ajustes(
nombre_de_ajuste VARCHAR(50) NOT NULL,
ajuste VARCHAR(50) NOT NULL)"""

	crearbasededatos(sql, "_data_aj")

	conexion = sqlite3.connect("sqlite3/_data_aj.sqlite3")

	consulta = conexion.cursor() 

	conexion.commit()

	sql = """
INSERT INTO ajustes(nombre_de_ajuste, ajuste)
VALUES (?, ?)"""

	if datospredefinidos != False:

		for i in datospredefinidos:

			print(i)

			consulta.execute(sql, i)

			conexion.commit()

	consulta.close()

def extraer_ajustes(cuantos = "all", nombre_de_ajuste = None):

    conexion = sqlite3.connect("sqlite3/_data_aj.sqlite3")

    consulta = conexion.cursor()

    sql = "SELECT * FROM ajustes"

    if cuantos == "all":

        consulta.execute(sql)

        total = consulta.fetchall()

        #print(total)

        extracted = []

        for ajuste in total:

        	extracted.append(ajuste[1])

       	return extracted

    conexion.commit()

    consulta.close()

def comprovarexistencia():

	try:

		conexion = sqlite3.connect("sqlite3/_data_aj.sqlite3")

		consulta = conexion.cursor()

		sql = "SELECT * FROM ajustes"

		consulta.execute(sql)

		total = consulta.fetchall()

		conexion.commit()

		consulta.close()

	except:

		conexion.commit()

		consulta.close()

		return False

	else:
		if len(total) > 0:

			return True

		else:
			return False

def actualizar_dato(nombre_de_ajuste, ajuste):

	conexion = sqlite3.connect("sqlite3/_data_aj.sqlite3")

	consulta = conexion.cursor()

	sql = """
UPDATE ajustes SET ajuste = '%s' WHERE nombre_de_ajuste = '%s' """ %(ajuste, nombre_de_ajuste)
	
	try:
		print("Ajuste realizado correctamente")

		consulta.execute(sql)

		conexion.commit()

		consulta.close()

	except:

		conexion.commit()

		consulta.close()

		return False

	else:
		return True

	