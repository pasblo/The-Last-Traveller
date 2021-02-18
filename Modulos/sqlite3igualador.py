import sqlite3

from Modulos.sqlite3faciliter import *

from Modulos.user import *

from Modulos.cifrador import *

def comprovarigualdad(basededatos1, tabla1, posuser1, basededatos2 = "Datos", tabla2 = "cuentas", posuser2 = 1): #La base de datos 2 va a ser contada SIEMPE como la base de referencia de usuarios

	conexion1 = sqlite3.connect("sqlite3/%s.sqlite3" %(basededatos1))

	consulta1 = conexion1.cursor()

	conexion2 = sqlite3.connect("sqlite3/%s.sqlite3" %(basededatos2))

	consulta2 = conexion2.cursor()

	sql1 = "SELECT * FROM %s" %(tabla1)

	sql2 = "SELECT * FROM %s" %(tabla2)

	consulta1.execute(sql1)

	consulta2.execute(sql2)

	filas1 = consulta1.fetchall()

	filas2 = consulta2.fetchall()

	users1 = []

	users2 = []

	for fila in filas1:

		users1.append(fila[posuser1])

	for fila in filas2:

		users2.append(fila[posuser2])

	if len(users1) > len(users2):
		lenmedia = len(users2)

	else:
		lenmedia = len(users1)

	if len(users1) > 0 and len(users2) > 0:

		ele = 0

		comp = []

		terminar = False

		while terminar != True:

			esta = False

			usuarioacomprovar = users1[ele]

			for usuario in users2:

				if usuario == usuarioacomprovar:
					esta = True

			if esta == True:
				comp.append(1)

			else:
				print("El usuario", usuarioacomprovar, "por ejemplo no esta en las dos listas")

			ele = ele +1

			if ele == lenmedia:
				terminar = True

		erroneos = (len(users2)-len(comp))

		if erroneos == 0:
			print("Todos estan bien")

		else:
			print("En total hay", len(comp),"usuarios bien en las dos listas")

			correctosusers1 = []

			incorrectosusers1 = []

			for comprovar1 in users1:

				if comprovar1 in users2:
					print("El elemento", comprovar1, "esta en las dos listas	CORRECTO")
					correctosusers1.append(comprovar1)

				else:
					print("El elemento", comprovar1, "no esta en la segunda lista    INCORRECTO")
					incorrectosusers1.append(comprovar1)

			correctosusers2 = []

			incorrectosusers2 = []

			for comprovar2 in users2:

				if comprovar2 in users1:

					print("El elemento", comprovar2, "esta en las dos listas    CORRECTO")
					correctosusers2.append(comprovar2)

				else:

					print("El elemento", comprovar2, "no esta en la primera lista    INCORRECTO")
					incorrectosusers2.append(comprovar2)

			if incorrectosusers1 != []:

				for user in incorrectosusers1:

					textinic = cifrartxt("Record sin cuenta user ==", 4)

					cifrated_user = cifrartxt(user, 4)

					print("\nHa ocurrido un ERROR porfavor reportenoslo al siguiente correo:\nnombredeljuego@gmail.com con el mensaje siguiente:\n%¿Error4?%",str(textinic) + cifrated_user,"%¿Error4?%\n")

			if incorrectosusers2 != []:

				for user in incorrectosusers2:

					ultimo = ultimoident("Records", "records")

					datosainsertar = (user, 0, ultimo +1)

					insertardatos("Records", datosainsertar, "Datos insertados correctamente", "Se produjo un error al corregir las bases de datos")

	else:
		print("Aguna/s de las bases de datos no contiene elementos")

	conexion1.commit()

	conexion2.commit()

	consulta1.close()

	consulta2.close()

	conexion1.close()

	conexion2.close()

def ordenarDBrespectoaotraDB(basededatos1, tabla1, poselemento1, basededatos2 = "Datos", tabla2 = "cuentas", poselemento2 = 1): #Siempre se ordenara la segunda DB respecto a la primera

	conexion1 = sqlite3.connect("sqlite3/%s.sqlite3" %(basededatos1))

	consulta1 = conexion1.cursor()

	conexion2 = sqlite3.connect("sqlite3/%s.sqlite3" %(basededatos2))

	consulta2 = conexion2.cursor()

	sql1 = "SELECT * FROM %s" %(tabla1)

	sql2 = "SELECT * FROM %s" %(tabla2)

	consulta1.execute(sql1)

	consulta2.execute(sql2)

	filas1 = consulta1.fetchall()

	filas2 = consulta2.fetchall()

	extractedelements1 = []

	extractedelements2 = []

	for fila in filas1:

		extractedelements1.append(fila)

	for fila in filas2:

		extractedelements2.append(fila)

	if len(extractedelements1) > 0 and len(extractedelements2) > 0:

		if extractedelements1 == extractedelements2:

			print("Las dos bases de datos estan ordenadas correctamente")

		else:
			print("Los elementos no estan bien ordenados\nVamos a proceder a ordenarlos tomando como patron a seguir la base de datos:\n" + basededatos1)

			actordenDB2 = []

			actordenDB2.extend(extractedelements2)

			for user in actordenDB2:

				borrardatos(basededatos2, tabla2, user[poselemento2])

				conexion2.commit()

			for correctuser in extractedelements1:

				error = 0

				for buscaruser in actordenDB2:

					if buscaruser[poselemento2] == correctuser[poselemento1]:

						user = buscaruser[1]

						contraseña = buscaruser[3]

						correo = buscaruser[2]

						nacimiento = buscaruser[4]

						creaccion = buscaruser[5]

						error = error +1

				if error > 1:
					textinic = cifrartxt("En la func ordenarDBrespectoaotraDB hubo dos usuarios iguales")

					usercifrated = cifrartxt(user)
					print("\nHa ocurrido un ERROR porfavor reportenoslo al siguiente correo:\nnombredeljuego@gmail.com con el mensaje siguiente:\n%¿Error5?%",str(textinic) + str(usercifrated), "%¿Error5?%\n")

				ultimoident(basededatos2, tabla2)

				print("Usuario:" + user, "ordenado con exito")

				loggearocrear(False, user, contraseña, "c", nacimiento, correo, creaccion)

				conexion2.commit()

	else:

		print("En alguna de las bases de datos no existe ningun elemento en la columna introducida que sea extraible")

	conexion1.commit()

	conexion2.commit()

	consulta1.close()

	consulta2.close()

	conexion1.close()

	conexion2.close()