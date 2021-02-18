import sqlite3

import os

from Modulos.sqlite3faciliter import *

def añadirdato(dato):

	conexion = sqlite3.connect("sqlite3/DatosVariados.sqlite3")

	consulta = conexion.cursor()

	conexion.commit()

	sql = """

INSERT INTO records(dato)
VALUES (?)"""
	
	consulta.execute(sql, dato)

	conexion.commit()

	consulta.close()

	conexion.close()

def borrardato(datoanterior):

	conexion = sqlite3.connect("sqlite3/DatosVariados.sqlite3")

	consulta = conexion.cursor()

	conexion.commit()

	sql= """
DELETE FROM datosvariados
WHERE dato = '%s'""" %(datoanterior)