#!/usr/bin/python3

import sqlite3

import os

def crearbasededatos(sqlinic, basededatos, cant = 1, sqlinic2 = None):

	if (os.path.isdir(os.getcwd() + "\\" + "sqlite3")):
            
		conexion = sqlite3.connect("sqlite3/%s.sqlite3" %(basededatos))
        
		consulta = conexion.cursor()

	else:

		os.mkdir(os.getcwd() + "\\" + "sqlite3")
        
		conexion = sqlite3.connect("sqlite3/%s.sqlite3" %(basededatos))
        
		consulta = conexion.cursor()

	if sqlinic2 != None:
		sqls = [sqlinic, sqlinic2]

	else:
		sqls = [sqlinic]

	for l in range(cant):

		if(consulta.execute(sqls[l - 1])):
			pass

		else:
			print("Ha ocurrido un error al crear la base de datos")
			loggeado = False

	conexion.commit()

	consulta.close()

	conexion.close()

def identde(basededatos, tabla, usuario, posicion):

	conexion = sqlite3.connect("sqlite3/%s.sqlite3" %(basededatos))

	consulta = conexion.cursor()

	sql = "SELECT * FROM %s" %(tabla)

	consulta.execute(sql)

	filas = consulta.fetchall()

	for fila in filas:

		if fila[posicion] == usuario:
			ident = fila[2]

	return ident

	conexion.commit()

	consulta.close()

	conexion.close()

def ultimoident(basededatos, tabla, ident = 0): #Para esta func es necesario haber definido con antelacion el parametro ident en la base de datos introducida

    conexion = sqlite3.connect("sqlite3/%s.sqlite3" %(basededatos))

    consulta = conexion.cursor()

    encontrado = False

    while encontrado != True:

        sql = "SELECT * FROM %s WHERE ident>%d " %(tabla, ident)

        consulta.execute(sql)

        act = consulta.fetchone()

        if act != None:
            encontrado = False
            ident = ident + 1

        else:
            encontrado = True

    return ident

    conexion.commit()

    consulta.close()

    conexion.close()

def printbasededatos(cuantos = "all", basededatos = "Datos", tabla = "cuentas"):

    conexion = sqlite3.connect("sqlite3/%s.sqlite3" %(basededatos))

    consulta = conexion.cursor()

    sql = "SELECT * FROM %s" %(tabla)

    if cuantos == "all":

        consulta.execute(sql)

        total = consulta.fetchall()

        print(total)

    conexion.commit()

    consulta.close()

    conexion.close()

def insertardatos(basededatos, datosainsertar, mensajetrue, mensajefalse, tabla = "records", restar = False):

	conexion = sqlite3.connect("sqlite3/%s.sqlite3" %(basededatos))

	consulta = conexion.cursor() 

	if basededatos == "Records" and tabla == "records":
		sql = "SELECT * FROM records"

		if consulta.execute(sql):
			vale = True
			filas = consulta.fetchall()
			q = 0

			for fila in filas:

				if fila[0] == datosainsertar[0]:
					q = "igual"
					vale = False
					lugar = fila[2]

				elif len(datosainsertar[0]) < 1:
					q = "nada"
					vale = False
			if vale:

				sql = """
INSERT INTO records(usuario, record, ident)
VALUES (?, ?, ?)"""

				if (consulta.execute(sql, datosainsertar)):
					print(mensajetrue)
					conexion.commit()

				else:
					print(mensajefalse)

			else:

				if q == "igual":
					cuenta = filas[lugar-1]

					if datosainsertar[1] > cuenta[1]:

						sql = """
UPDATE records SET record = '%s' WHERE ident = %d """ %(datosainsertar[1], lugar)

						if consulta.execute(sql):
							print(mensajetrue)

						else:
							print(mensajefalse)
					else:
						print("El dato existente es mayor o igual")

				else:
					print("Escribe algo")
					return False

	if basededatos == "Records" and tabla == "monedas":
		sql = "SELECT * FROM monedas"

		if consulta.execute(sql):
			filas = consulta.fetchall()
			existe = False
			
			for fila in filas:

				if fila[0] == datosainsertar[0]:
					trabajarcon = fila
					
					existe = True
					
			if existe == False:
				sql = """
INSERT INTO monedas(usuario, monedas, ident)
VALUES (?, ?, ?)"""
				
				consulta.execute(sql, datosainsertar)
				conexion.commit()

			else:
				if restar == True:
					sql = """
UPDATE monedas SET monedas = '%s' WHERE usuario = '%s' """ %(trabajarcon[1] - datosainsertar[1], trabajarcon[0])
				
				else:
					sql = """
UPDATE monedas SET monedas = '%s' WHERE usuario = '%s' """ %(datosainsertar[1] + trabajarcon[1], trabajarcon[0])
				
				consulta.execute(sql)
				conexion.commit()

	conexion.commit()

	consulta.close()

	conexion.close()

def encontrarpos(basededatos, tabla, elemento, pos, integer = False):

	conexion = sqlite3.connect("sqlite3/%s.sqlite3" %(basededatos))

	consulta = conexion.cursor()

	sql = "SELECT * FROM %s" %(tabla)

	if integer:

		if (consulta.execute(sql)):
			indx = 1
			filas = consulta.fetchall()
			cuenta = ""  

			for fila in filas:

				if fila[pos] == int(elemento):
					cuenta = fila
					return indx

				indx = indx +1
		else:
 			print("Ha ocurrido un error al abrir el archivo necesario para este programa")
	else:

		if (consulta.execute(sql)):
			indx = 1
			filas = consulta.fetchall()
			cuenta = ""  

			for fila in filas:

				if fila[pos] == elemento:
					cuenta = fila
					return indx

				indx = indx +1
		else:
			print("Ha ocurrido un error al abrir el archivo necesario para este programa")

	conexion.commit()

	consulta.close()

	conexion.close()

def comprovarindice(basededatos, tabla, pos = 0): #Para esta func tiene que existir la columna index en la base de datos introducida
	
	conexion = sqlite3.connect("sqlite3/%s.sqlite3" %(basededatos))

	consulta = conexion.cursor()

	sql = "SELECT * FROM %s" %(tabla)

	if (consulta.execute(sql)):

		filas = consulta.fetchall()

		control = []

		cont = 0

		errores = 0

		for fila in filas:

			cont = cont +1

			if fila[pos] == cont:
				print("Correcto")
				control.extend(str(cont))

			else:
				errores = errores +1

		if errores == 0:
			return True

		else:

			print("Las listas no estann bien ordenadas")
			print("Vamos a proceder a ordenarlas...")

			cont = 0

			for fila in filas:

				cont = cont +1

				if fila[pos] == cont:
					pass

				else:
					sql = """
UPDATE %s SET ident = '%d' WHERE ident = '%d' """ %(tabla, cont, fila[pos])
					
					if (consulta.execute(sql)):
						print("Usuario ",cont," arreglado")
						conexion.commit()

					else:
						print("Error")

	else:
		print("Ha ocurrido un error al abrir el archivo necesario para este programa")

	conexion.commit()

	consulta.close()

	conexion.close()

def resetrecordpersonal(usuario, nuevo = 0):

	conexion = sqlite3.connect("sqlite3/Records.sqlite3" )

	consulta = conexion.cursor()

	sql = "UPDATE records SET record = '%d' WHERE usuario = '%s' " %(nuevo, usuario)

	if (consulta.execute(sql)):
		print("Record fijado a:",nuevo)
		conexion.commit()
	else:
		print("El record no se pudo resetear")

	conexion.commit()

	consulta.close()

def borrardatos(basededatos, tabla, usuario):

	conexion = sqlite3.connect("sqlite3/%s.sqlite3" %(basededatos))

	consulta = conexion.cursor()

	sql= """
DELETE FROM %s
WHERE usuario = '%s'""" %(tabla, usuario)
	
	try:
		consulta.execute(sql)

	except:

		print("Hubo un error al borrar el usuario puede ser que ese usuario no exista o que se hayan borrado los datos necesarios del programa")

	else:

		print("Usuario borrado con exito")

	conexion.commit()

	consulta.close()

	conexion.close()

def cambiarele(basededatos, tabla, columna, datoacambiar, ident, user = None):

	conexion = sqlite3.connect("sqlite3/%s.sqlite3" %(basededatos))

	consulta = conexion.cursor()

	error = False

	sql = "SELECT * FROM %s" %(tabla)

	if consulta.execute(sql):
		vale = True
		filas = consulta.fetchall()
		q = 0

		for fila in filas:

			if fila[int(ident)] == user:
				q = "igual"
				vale = False

			elif len(user) < 1:
				q = "nada"
				vale = False

		if vale != True:

			consulta.execute(sql)

			filas = consulta.fetchall()

			founded = False

			if user != None:

				for fila in filas:
					
					if fila[int(ident)] == user:

						founded = True

						sql = "UPDATE %s SET %s = '%s' WHERE usuario = '%s' " %(tabla, columna, datoacambiar, fila[int(ident)])

						try:
							consulta.execute(sql)

							conexion.commit()

						except:

							print("Hubo un error al cambiar el dato", datoacambiar)

				if founded:
					print("El dato ha sido cambiado")

				else:
					print("Ese usuario no existe")
					error = True

		else:
			if q == "igual":
				print("Ese usuario no existe")
				error = True

			else:
				print("Escribe algo")
				error = True

	return error

	conexion.commit()

	consulta.close()

	conexion.close()

def insertardatosHSP(basededatos, datosainsertar):

	conexion = sqlite3.connect("sqlite3/%s.sqlite3" %(basededatos))

	consulta = conexion.cursor()

	if basededatos == "Records":

		sql = """
INSERT INTO records(usuario, record, ident)
VALUES (?, ?, ?)"""
		
		try:
			consulta.execute(sql, datosainsertar)
			conexion.commit()


		except:
			pass

		else:
			pass

	conexion.commit()

	consulta.close()

	conexion.close()

def obtenerdato(basededatos, tabla, usuario, pos = 1):

	conexion = sqlite3.connect("sqlite3/%s.sqlite3" %(basededatos))

	consulta = conexion.cursor()

	try:

		sql = "SELECT * FROM %s" %(tabla)

		encontrado = False

		if (consulta.execute(sql)):

			filas = consulta.fetchall()

			for fila in filas:

				if fila[pos] == usuario:

					aextraer = fila

					encontrado = True

	except:
		encontrado = False

	if encontrado:

		return aextraer

	else:
		print("Ese usurio no existe")

		return encontrado

	conexion.commit()

	consulta.close()

	conexion.close()

def obtenerrecords(basededatos, tabla, record, pos, cant = "all"):

	conexion = sqlite3.connect("sqlite3/%s.sqlite3" %(basededatos))

	consulta = conexion.cursor()

	sql = "SELECT * FROM %s" %(tabla)

	if cant == "all":

		encontrado = False

		aextraer = []

		if (consulta.execute(sql)):

			filas = consulta.fetchall()

			for fila in filas:

				if fila[pos] == record:

					aextraer.append(fila)

					encontrado = True

			if encontrado:

				return aextraer

			else:
				print("Ese record no existe")

				return encontrado

	conexion.commit()

	consulta.close()

	conexion.close()

def ordenarrecords(maxima_puntuacion, banned_users):

	def borrardatos(basededatos, tabla, usuario):

		conexion = sqlite3.connect("sqlite3/%s.sqlite3" %(basededatos))

		consulta = conexion.cursor()

		sql= """
	DELETE FROM %s
	WHERE usuario = '%s'""" %(tabla, usuario)

		try:
			consulta.execute(sql)

		except:
			pass

		else:
			conexion.commit()


	conexion = sqlite3.connect("sqlite3/Records.sqlite3")

	consulta = conexion.cursor()

	sql = "SELECT * FROM records"

	consulta.execute(sql)

	filas = consulta.fetchall()

	guard = filas

	record_actual = 0

	record_anterior = maxima_puntuacion

	records_ordenados = []

	ordenado = False

	print("#Si mas de un usurio tiene el mismo record, el primer puesto se dara al ultimo \nque lo hizo")

	while ordenado != True:
		banned = False

		for fila in filas:
			if fila[1] >= record_actual and fila[1] <= record_anterior:
				record_actual = fila[1]
				user = fila[0]

			elif maxima_puntuacion < fila[1]:
				print("Sobrepasaste la puntuacion maxima,\nEs malo ser haker,\nLo siento pero vamos a proceder a borrar tu cuenta \ny a impedir que puedas volver a entrar.\nSi crees que esta accion es inapropiada \nporfavor reportanosla a este correo junto al nombre de de tu usuario\nNombredeljuego@gmail.com")
				banned_users.append(fila[0])
				banned = True
				user = fila[0]
				record_actual = fila[1]

		records_ordenados.append((record_actual, user))
		record_anterior = record_actual
		record_actual = 0

		borrardatos("Records", "records", user)
		sql = "SELECT * FROM records"
		consulta.execute(sql)
		filas = consulta.fetchall()

		if len(records_ordenados) == len(guard):
			ordenado = True

	sql = """
INSERT INTO records(usuario, record, ident)
VALUES (?, ?, ?)"""
	
	pos = 1

	for line in records_ordenados:
		act = records_ordenados[pos -1]
		datosainsertar = (act[1], int(act[0]), pos)
		consulta.execute(sql, datosainsertar)
		pos = pos +1

	conexion.commit()

	consulta.close()

	conexion.close()

	return banned_users

def obtener_record():

	conexion = sqlite3.connect("sqlite3/Records.sqlite3")

	consulta = conexion.cursor()

	sql = "SELECT * FROM records"

	consulta.execute(sql)

	filas = consulta.fetchall()

	record_act = 0

	for fila in filas:

		if fila[1] > record_act:

			record_act = fila[1]

	conexion.commit()

	consulta.close()

	conexion.close()

	return record_act