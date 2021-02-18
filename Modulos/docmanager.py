
import os

from Modulos.cifrador import *

def renombrararchivo(archivo_a_renombrar, ext1, nuevo, ext2):
	antiguo = archivo_a_renombrar + ext1
	nuevo = nuevo + ext2

	os.rename(antiguo, nuevo) 
	print("Archivo renombrado con exito")

def borrararchivo(archivo_a_borrar, ext):
	eliminar = archivo_a_borrar + ext

	os.remove(eliminar)
	print("Archivo eliminado con exito")

def insertarenarchivo(archivo, ext, texto, direccion = ""):
	archivo = open(direccion + archivo + ext, "w")

	try:
		archivo.write(texto)

	except:
		print("Hubo un error al escibir en el archivo, comprueve que el archivo exista o que ladireccion exista correcta")
		completed = False

	else:
		print("Datos insertados correctamente")
		completed = True

	archivo.close()
	return completed

def propiedades(archivo, ext, modo, direccion = ""):
	archivo = open(direccion + archivo + ext, modo)

	return [archivo.name, archivo.closed, archivo.encoding, archivo.mode]

	archivo.close()

def creararchivo(nombre, ext, modo ="w+", direccion = ""):
	try:
		temp = open(direccion + nombre + ext, modo)

	except:
		print("Hubo un error al crear el archivo")
		completed = False

	else:
		print("Archivo creado con exito")
		completed = True

	temp.close()
	return completed

def leerarchivo(archivo, ext, modo, carcteres_a_leer = "all", direccion = ""): #El modo debe ser de leectura si no dara error

	archivo = open(direccion + archivo + ext, modo)

	if carcteres_a_leer == "all":
		leido = archivo.read()

	else:
		leido = archivo.read(carcteres_a_leer)

	archivo.close()
	print("Texto leido con exito")
	return leido

def cifrar_archivo(archivo, ext, codigo, archivo_cifrado, ext2 , modo = "r", direccion = "", direccion2 = ""):
	
	texto_a_cifrar = open(direccion + archivo + ext, modo)

	archivo_cifrado = open(direccion2 + archivo_cifrado + ext2, "w")

	linea = texto_a_cifrar.readline()

	while linea != "":
		linea = texto_a_cifrar.readline()
		texto_cifrado = cifrartxt(linea, codigo)
		archivo_cifrado.write(texto_cifrado)

	print("Texto cifrado con exito")
	texto_a_cifrar.close()
	archivo_cifrado.close()

def descifrar_archivo(archivo_cifrado, ext, codigo, archivo_descifrado, ext2, modo = "r", direccion = "", direccion2 = ""):
	
	texto_a_descifrar = open(direccion + archivo_cifrado + ext, modo)

	archivo_descifrado = open(direccion2 + archivo_descifrado + ext2, "w")

	linea = texto_a_descifrar.readline()

	while linea != "":
		linea = texto_a_descifrar.readline()
		texto_descifrado = descifrartxt(linea, codigo)
		archivo_descifrado.write(texto_descifrado)

	print("Texto descifrado con exito")
	texto_a_descifrar.close()
	archivo_descifrado.close()

def corregir_descifrado(archivo_descifrado, ext, archivo_corregido, ext2, modo = "r", direccion = "", direccion2 = ""):

	texto_a_corregir = open(direccion + archivo_descifrado + ext, modo)

	archivo_corregido = open(direccion2 + archivo_corregido + ext2, "w")

	linea = "#Texto corregido por corrector y descifrador de textos \n"

	while linea != "":

		texto = texto_a_corregir.readline()

		for caracter in texto:

			if caracter == "":
				archivo_corregido.write(linea + "\n")
				linea = ""

			else:
				linea = linea + str(caracter)

	print("Texto corregido con exito")
	texto_a_corregir.close()
	archivo_corregido.close()
