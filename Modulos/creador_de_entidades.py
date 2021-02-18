import pygame

from Modulos.clasificador import *

def crear_entidad(nombre, posx, posy, list_naves, radio = 0, lado = None, permanecer = False): #list_naves = son los nombres por orden de las naves usadas si es usuada se pone 1 si no lo es se pone 0

	if posx < 0 or posy < 0:
		print("La x o la y son menores a cero")
		return (False, list_naves) #Si se consigue crear correctamente se devuelve la nave si no se devuelve False

	else:
		if nombre == "EBEN1":
			try:
				index_a_poner = list_naves.index(0)
			except:
				print("No quedan espacios para introducir nuevas naves a la partida")
				return (False, list_naves)
			else:
				
				Nave = EBEN1(posx, posy, index_a_poner, radio, lado, permanecer)
				Nave.cargarconimag("EBEN1", ".png")
				list_naves.insert(index_a_poner, 1)
				list_naves.pop()
				return (Nave, list_naves)

		elif nombre == "EBEN2":

			try:
				index_a_poner = list_naves.index(0)

			except:
				print("No quedan espacios para introducir nuevas naves a la partida")
				return (False, list_naves)

			else:
				Nave = EBEN2(posx, posy, index_a_poner, radio, lado, permanecer)
				Nave.cargarconimag("EBEN2", ".png")
				list_naves.insert(index_a_poner, 1)
				list_naves.pop()
				return (Nave, list_naves)

		elif nombre == "EBEN3":

			try:
				index_a_poner = list_naves.index(0)

			except:
				print("No quedan espacios para introducir nuevas naves a la partida")
				return (False, list_naves)

			else:

				Nave = EBEN3(posx, posy, index_a_poner, radio, lado, permanecer)
				Nave.cargarconimag("EBEN3", ".png")
				list_naves.insert(index_a_poner, 1)
				list_naves.pop()
				return (Nave, list_naves)

		elif nombre == "EBEN4":

			try:
				index_a_poner = list_naves.index(0)

			except:
				print("No quedan espacios para introducir nuevas naves a la partida")
				return (False, list_naves)

			else:

				Nave = EBEN4(posx, posy, index_a_poner, radio, lado, permanecer)
				Nave.cargarconimag("EBEN4", ".png")
				list_naves.insert(index_a_poner, 1)
				list_naves.pop()
				return (Nave, list_naves)

		elif nombre == "EBEN5":

			try:
				index_a_poner = list_naves.index(0)

			except:
				print("No quedan espacios para introducir nuevas naves a la partida")
				return (False, list_naves)

			else:

				Nave = EBEN5(posx, posy, index_a_poner, radio, lado, permanecer)
				Nave.cargarconimag("EBEN5", ".png")
				list_naves.insert(index_a_poner, 1)
				list_naves.pop()
				return (Nave, list_naves)

		elif nombre == "EBEN6":

			try:
				index_a_poner = list_naves.index(0)

			except:
				print("No quedan espacios para introducir nuevas naves a la partida")
				return (False, list_naves)

			else:
				
				Nave = EBEN6(posx, posy, index_a_poner, radio, lado, permanecer)
				Nave.cargarconimag("EBEN6", ".png")
				list_naves.insert(index_a_poner, 1)
				list_naves.pop()
				return (Nave, list_naves)

		elif nombre == "EBEN7":

			try:
				index_a_poner = list_naves.index(0)

			except:
				print("No quedan espacios para introducir nuevas naves a la partida")
				return (False, list_naves)

			else:

				Nave = EBEN7(posx, posy)
				Nave.cargarconimag("EBEN7", ".png")
				list_naves.insert(index_a_poner, 1)
				list_naves.pop()
				return (Nave, list_naves)
				
		elif nombre == "EBEN8":

			try:
				index_a_poner = list_naves.index(0)

			except:
				print("No quedan espacios para introducir nuevas naves a la partida")
				return (False, list_naves)

			else:
				
				Nave = EBEN8(posx, posy)
				Nave.cargarconimag("EBEN8", ".png")
				list_naves.insert(index_a_poner, 1)
				list_naves.pop()
				return (Nave, list_naves)

		elif nombre == "EBEN9":

			try:
				index_a_poner = list_naves.index(0)

			except:
				print("No quedan espacios para introducir nuevas naves a la partida")
				return (False, list_naves)

			else:
				
				Nave = EBEN9(posx, posy)
				Nave.cargarconimag("EBEN9", ".png")
				list_naves.insert(index_a_poner, 1)
				list_naves.pop()
				return (Nave, list_naves)

		elif nombre == "EBEN10":
			
			try:
				index_a_poner = list_naves.index(0)

			except:
				print("No quedan espacios para introducir nuevas naves a la partida")
				return (False, list_naves)

			else:

				Nave = EBEN10(posx, posy)
				Nave.cargarconimag("EBEN10", ".png")
				list_naves.insert(index_a_poner, 1)
				list_naves.pop()
				return (Nave, list_naves)

		else:
			print("Ese tipo de sprite a crear no esta definido")