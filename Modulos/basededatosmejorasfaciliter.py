import sqlite3

import os

from Modulos.sqlite3faciliter import *

def crearbasededatosmejoras(user):

	if (os.path.isdir(os.getcwd() + "\\" + "sqlite3")):

		conexion = sqlite3.connect("sqlite3/%s.sqlite3" %("DataMejoras" + user))

		consulta = conexion.cursor()

	else:

		os.mkdir(os.getcwd() + "\\" + "sqlite3")

		conexion = sqlite3.connect("sqlite3/%s.sqlite3" %("DataMejoras" + user))

		consulta = conexion.cursor()

	sql1 = """
CREATE TABLE IF NOT EXISTS MejorasNave(
Proteccion INTEGER NOT NULL,
Daño INTEGER NOT NULL,
Velocidad DECIMAL NOT NULL,
Escudo INTEGER NOT NULL,
FrecuenciaDisp INTEGER NOT NULL,
VelocidadDisp INTEGER NOT NULL,
ident INTEGER NOT NULL)""" # 1 == True, 0 == False
	
	consulta.execute(sql1)
	conexion.commit()
	
	sql2 = """
INSERT INTO MejorasNave(Proteccion, Daño, Velocidad, Escudo, FrecuenciaDisp, VelocidadDisp, ident)
VALUES (10, 5, 0.5, 0, 450000, 0.99, 1)"""
	
	consulta.execute(sql2)
	conexion.commit()

	consulta.close()

	conexion.close()

def extraerdatosmejoras(user):

	conexion = sqlite3.connect("sqlite3/%s.sqlite3" %("DataMejoras" + user))

	consulta = conexion.cursor()

	sql = "SELECT * FROM MejorasNave"

	consulta.execute(sql)

	total = consulta.fetchall()

	conexion.commit()

	consulta.close()

	conexion.close()

	return total

def intercambiardatosmejoras(user, datos):

	conexion = sqlite3.connect("sqlite3/%s.sqlite3" %("DataMejoras" + user))

	consulta = conexion.cursor()

	consulta.execute('DELETE FROM MejorasNave WHERE ident = 1')

	conexion.commit()

	sql1 = """
INSERT INTO MejorasNave(Proteccion, Daño, Velocidad, Escudo, FrecuenciaDisp, VelocidadDisp, ident)
VALUES (?, ?, ?, ?, ?, ?, ?)"""
	
	consulta.execute(sql1, datos)
	conexion.commit()

	conexion.commit()

	consulta.close()

	conexion.close()