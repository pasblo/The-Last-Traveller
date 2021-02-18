import pygame

import sys

import sqlite3

from Modulos.sqlite3faciliter import *

from Modulos.basededatosajustesfaciliter import *

from pygame.locals import *

import time

def print_pantalla(texto, posx, posy, tamaño, color = (0, 0, 0), fuente = "Default", color_de_fondo = None):

	try:
		if fuente != "Default":
			miFuente = pygame.font.SysFont(fuente, tamaño)

		else:
			miFuente = pygame.font.Font(None, tamaño)

		if color_de_fondo != None:

			miTexto = miFuente.render(texto, 0, color, color_de_fondo)

		else:
			miTexto = miFuente.render(texto, 0, color)

	except:
		print("Ocurrio un error al generar el texto")

	else:
		return (miTexto, (posx, posy))

def dibujar_recuadro_introductor(ventana, texto, colortxt, fuente, tamaño, posx1, posy1, posx2, posy2, pulsado = False, color_recuadro = (255, 255, 255), color_de_fondo = None):

	if pulsado == False:

		print(posx1, posy1, posx2, posy2)

		rectangulo = pygame.draw.rect(ventana, color_recuadro, (posx1, posy1, posx2 -  posx1, posy2 - posy1))

		try:
			if fuente != "Default":
				miFuente = pygame.font.SysFont(fuente, int(tamaño))

			else:
				miFuente = pygame.font.Font(None, int(tamaño))

			if color_de_fondo != None:

				miTexto = miFuente.render(texto, 0, colortxt, color_de_fondo)

			else:
				miTexto = miFuente.render(texto, 0, colortxt)

		except:
			print("Ocurrio un error al generar el texto")

	else:
		rectangulo = pygame.draw.rect(ventana, color_recuadro, (posx1, posy1, posx2 -  posx1, posy2 - posy1))

		miTexto = ""

	return (miTexto, (posx1 + 3, posy1 + 3), rectangulo, (posx1, posy1, posx2, posy2))

def print_txt_comp(texto, posxinic, posyinic, maxchar, colortxt = (0, 0, 0), fuente = "Deafault", color_de_fondo = None):

	ajustes = extraer_ajustes()

	ancho = int(ajustes[0])
	alto = int(ajustes[1])

	miFuente = pygame.font.SysFont(fuente, round(0.0234375 * ancho))

	def calcularx(letras, ancho):

		longit = 0

		for letraact in letras:
			print(letraact)

			if letraact == "l" or letraact == "i" or letraact == "." or letraact == "," or letraact == ";" or letraact == ":" or letraact == "I" or letraact == "'" or letraact == "¡" or letraact == "!" or letraact == "·" or letraact == "|":
				longit = longit + round(0.0046875 * ancho)

			elif letraact == "j" or letraact == "(" or letraact == "[" or letraact == "{" or letraact == "/" or letraact == "\\" or letraact == "¨" or letraact == "´"  or letraact == "`"  or letraact == '"':
				longit = longit + round(0.00625 * ancho)

			elif letraact == "r"  or letraact == "f" or letraact == "t" or letraact == ")" or letraact == "]" or letraact == "}":
				longit = longit + round(0.00703125 * ancho)

			elif letraact == "-" or letraact == "º" or letraact == "ª":
				longit = longit + round(0.0078125 * ancho)

			elif letraact == "*":
				longit = longit + round(0.00859375 * ancho)

			elif letraact == "J" or letraact == "^":
				longit = longit + round(0.009375 * ancho)

			elif letraact == "s":
				longit = longit + round(0.010105625 * ancho)

			elif letraact == "o" or letraact == "A" or letraact == "B" or letraact == "E" or letraact == "P" or letraact == "S" or letraact == "Y" or letraact == "_":
				longit = longit + round(0.01171875 * ancho)

			elif letraact == "P" or letraact == "D" or letraact == "H" or letraact == "V" or letraact == "+" or letraact == "#":
				longit = longit + round(0.0125 * ancho)

			elif letraact == "C" or letraact == "N" or letraact == "Ñ" or letraact == "X":
				longit = longit + round(0.01328125 * ancho)

			elif letraact == "Q" or letraact == "U" or letraact == "Ç":
				longit = longit + round(0.0140625 * ancho)

			elif letraact == "M" or letraact == "O" or letraact == "R":
				longit = longit + round(0.01484375 * ancho)

			elif letraact == "G":
				longit = longit + round(0.015625 * ancho)

			elif letraact == "m" or letraact == "w" or letraact == "%":
				longit = longit + round(0.01640625 * ancho)

			elif letraact == "W":
				longit = longit + round(0.01875 * ancho)

			elif letraact == "@":
				longit = longit + round(0.01953125 * ancho)

			else:
				longit = longit + round(0.0109375 * ancho)

		return longit

	txt_list = []

	txt_list.extend(texto)

	print(txt_list)

	if len(txt_list) <= maxchar:

		print("Texto introducido igual o mas corto que una linea")

		miTexto = miFuente.render(texto, 0, colortxt, color_de_fondo)
		return (miTexto, (posxinic, posyinic))

	else:
		
		print("Texto introducido mas largo que una linea")

		maximo = False

		letrasact = ""

		conjtxt = []

		eleact = 0

		a_corregir = []

		while maximo != True:
			
			for i in txt_list:

				if i == " ":
					letrasact = letrasact + str(i)

					if len(letrasact) < 1:
						pass

					elif len(letrasact) <= maxchar:
						pass

					else:
						a_corregir.extend(letrasact)
						a_corregir.reverse()
						newlist = a_corregir
						total = len(a_corregir)
						terminado = False
						eliminados = []
						nº = 0
						print(a_corregir)

						while nº < total:
							print(a_corregir[nº])

							if a_corregir[nº] != " ":
								eliminados.extend(a_corregir[nº])
								print(eliminados)

							nº = nº + 1

						letrasact = ""

				else:
					letrasact = letrasact + str(i)

				eleact = eleact + 1

			maximo = True


def crear_boton(texto, posx, posy, posx2, posy2, tamaño, ventana, color = (0, 0, 0), fuente = "Deafault", color_boton = (255, 255, 255)):

	if fuente != "Deafault":
		fuente_txt = pygame.font.SysFont(fuente, tamaño)
		miTexto = fuente_txt.render(texto, 0, color)
		rectangulo2 = pygame.draw.rect(ventana, color, (posx - 3, posy - 3, posx2 - posx - 3, posy2 - posy - 3))
		rectangulo = pygame.draw.rect(ventana, color_boton, (posx, posy, posx2 - posx, posy2 - posy))
		return(miTexto, (rectangulo, (posx + 8, posy), (posx2, posy2)), rectangulo2)

	else:
		fuente_txt = pygame.font.Font(None, tamaño)
		miTexto = fuente_txt.render(texto, 0, color)
		rectangulo2 = pygame.draw.rect(ventana, color, (posx - 3, posy - 3, posx2 - posx - 3, posy2 - posy - 3))
		rectangulo = pygame.draw.rect(ventana, color_boton, (posx, posy, posx2 - posx, posy2 - posy))
		return(miTexto, (rectangulo, (posx + 8, posy), (posx2, posy2)), rectangulo2)

def crear_boton2(ventana, posx, posy, posx2, posy2, texto, tamaño, color = (0, 0, 0), fuente = "Deafault", color_boton = (255, 255, 255)):
	if fuente != "Deafault":
		fuente_txt = pygame.font.SysFont(fuente, tamaño)
		miTexto = fuente_txt.render(texto, 0, color)
		rectangulo = pygame.draw.rect(ventana, color_boton, (posx, posy, posx2 - posx, posy2 - posy))
		return(miTexto, (rectangulo, (posx + 8, posy), (posx2, posy2)))

	else:
		fuente_txt = pygame.font.Font(None, tamaño)
		miTexto = fuente_txt.render(texto, 0, color)
		rectangulo = pygame.draw.rect(ventana, color_boton, (posx, posy, posx2 - posx, posy2 - posy))
		return(miTexto, (rectangulo, (posx + 8, posy), (posx2, posy2)))

def crear_boton3(ventana, posx, posy, posx2, posy2, texto, tamaño, tamañoline, error = 0, color = (0, 0, 0), fuente = "Deafault", color_boton = (255, 255, 255)):
	if fuente != "Deafault":
		fuente_txt = pygame.font.SysFont(fuente, tamaño)
		miTexto = fuente_txt.render(texto, 0, color)
		#rectangulo = pygame.draw.rect(ventana, color_boton, (posx, posy, posx2 - posx, posy2 - posy))
		pygame.draw.line(ventana, color_boton, (posx + 8 - error, posy - error), (posx2, posy - error), tamañoline)
		pygame.draw.line(ventana, color_boton, (posx + 8 - error, posy - error), (posx + 8 - error, posy2), tamañoline)
		pygame.draw.line(ventana, color_boton, (posx + 8 - error, posy2), (posx2, posy2), tamañoline)
		pygame.draw.line(ventana, color_boton, (posx2, posy2), (posx2, posy - error), tamañoline)
		return(miTexto, ((posx + 8, posy), (posx2, posy2)))

	else:
		fuente_txt = pygame.font.Font(None, tamaño)
		miTexto = fuente_txt.render(texto, 0, color)
		#rectangulo = pygame.draw.rect(ventana, color_boton, (posx, posy, posx2 - posx, posy2 - posy))
		pygame.draw.line(ventana, color_boton, (posx + 8 - error, posy - error), (posx2, posy - error), tamañoline)
		pygame.draw.line(ventana, color_boton, (posx + 8 - error, posy - error), (posx + 8 - error, posy2), tamañoline)
		pygame.draw.line(ventana, color_boton, (posx + 8 - error, posy2), (posx2, posy2), tamañoline)
		pygame.draw.line(ventana, color_boton, (posx2, posy2), (posx2, posy - error), tamañoline)
		return(miTexto, ((posx + 8, posy), (posx2, posy2)))

def record_user(tamaño, color):

	fuente = pygame.font.Font(None, tamaño)

	record = obtener_record()

	miTexto = fuente.render(str(record), 0, color)

	return miTexto

def escribir_en_terminal(texto, tipodeletra, nº, ventana, ancho, alto):

	tamañotxtgeneral = round(0.0234375 * ancho)
	distelin = round(0.01953125 * ancho)

	blanco = (255, 255, 255)

	miFuente = pygame.font.SysFont(tipodeletra, tamañotxtgeneral)

	miTexto = miFuente.render(texto, 0, blanco)

	ventana.blit(miTexto, (0, (nº * distelin)*2 + distelin))

	pygame.display.update()

def preguntar(letras, tipodeletra, pregunta, nº, ventana, posytxt, maxword, conjpant, minword = 0, modo_seguro = False):

	alto = conjpant[0]

	ancho = conjpant[1]

	intro = False

	blanco = (255, 255, 255)

	negro = (0, 0, 0)

	rojo = (255, 0, 0)

	letraslist = []

	tamañotxtgeneral = round(0.0234375 * ancho)
	distprinc = round(0.023075 * ancho) #Distancia desde el principio de las x
	distelin = round(0.01953125 * ancho) #Distancia entre lineado

	if nº == 0:
		miFuente = pygame.font.SysFont(tipodeletra, tamañotxtgeneral)

		miTexto = miFuente.render("#Escriba /Exit para salir de la terminal", 0, blanco)

		ventana.blit(miTexto, (0, 0))

		pygame.display.update()

	miFuente = pygame.font.SysFont(tipodeletra, tamañotxtgeneral)

	miTexto = miFuente.render(pregunta, 0, blanco)

	ventana.blit(miTexto, (0, (nº * distelin)*2 + distelin))

	pygame.display.update()

	miFuente = pygame.font.SysFont(tipodeletra, tamañotxtgeneral)

	miTexto = miFuente.render(">>", 0, blanco)

	ventana.blit(miTexto, (0, (nº * distelin)*2 + distelin*2))

	pygame.display.update()

	def calcularx(letras, ancho, modo_seguro = False):

		longit = 0

		for letraact in letras:

			if modo_seguro == True:
				letraact = "*"

			if letraact == "l" or letraact == "i" or letraact == "." or letraact == "," or letraact == ";" or letraact == ":" or letraact == "I" or letraact == "'" or letraact == "¡" or letraact == "!" or letraact == "·" or letraact == "|":
				longit = longit + round(0.0046875 * ancho)

			elif letraact == "j" or letraact == "(" or letraact == "[" or letraact == "{" or letraact == "/" or letraact == "\\" or letraact == "¨" or letraact == "´"  or letraact == "`"  or letraact == '"':
				longit = longit + round(0.00625 * ancho)

			elif letraact == "r"  or letraact == "f" or letraact == "t" or letraact == ")" or letraact == "]" or letraact == "}":
				longit = longit + round(0.00703125 * ancho)

			elif letraact == "-" or letraact == "º" or letraact == "ª":
				longit = longit + round(0.0078125 * ancho)

			elif letraact == "*":
				longit = longit + round(0.00859375 * ancho)

			elif letraact == "J" or letraact == "^":
				longit = longit + round(0.009375 * ancho)

			elif letraact == "s":
				longit = longit + round(0.010105625 * ancho)

			elif letraact == "o" or letraact == "A" or letraact == "B" or letraact == "E" or letraact == "P" or letraact == "S" or letraact == "Y" or letraact == "_":
				longit = longit + round(0.01171875 * ancho)

			elif letraact == "P" or letraact == "D" or letraact == "H" or letraact == "V" or letraact == "+" or letraact == "#":
				longit = longit + round(0.0125 * ancho)

			elif letraact == "C" or letraact == "N" or letraact == "Ñ" or letraact == "X":
				longit = longit + round(0.01328125 * ancho)

			elif letraact == "Q" or letraact == "U" or letraact == "Ç":
				longit = longit + round(0.0140625 * ancho)

			elif letraact == "M" or letraact == "O" or letraact == "R":
				longit = longit + round(0.01484375 * ancho)

			elif letraact == "G":
				longit = longit + round(0.015625 * ancho)

			elif letraact == "m" or letraact == "w" or letraact == "%":
				longit = longit + round(0.01640625 * ancho)

			elif letraact == "W":
				longit = longit + round(0.01875 * ancho)

			elif letraact == "@":
				longit = longit + round(0.01953125 * ancho)

			else:
				longit = longit + round(0.0109375 * ancho)

		return longit

	def escribir(letra, letras, ventana, color, posytxt, maxword, ancho, modo_seguro):


		miFuente = pygame.font.SysFont(tipodeletra, tamañotxtgeneral)

		if modo_seguro == True:
			miTexto = miFuente.render("*", 0, color)

		else:
			miTexto = miFuente.render(letra, 0, color)

		longitudx = calcularx(letras, ancho, modo_seguro)
		ventana.blit(miTexto, (longitudx + distprinc, posytxt))
		letras = letras + letra
		pygame.display.update()
		return letras

	for evento in pygame.event.get():

		if evento.type == QUIT:
			print("Juego terminado")
			pygame.quit()
			sys.exit()

		if evento.type == KEYDOWN:

			if evento.key == 285:
				print("Juego terminado")
				pygame.quit()
				sys.exit()

			elif evento.key == 292: #Presiona F11

				pantalla_comp = True
				pygame.display.set_mode((ancho, alto), pygame.FULLSCREEN)
				actualizar_dato("pantcomp", pantalla_comp)

			elif evento.key == 27: #Presiona ESC

				pantalla_comp = False
				pygame.display.set_mode((ancho, alto))
				actualizar_dato("pantcomp", pantalla_comp)

			elif len(letras) > maxword and not evento.key == 8 and not evento.key == 13 and not evento.key == 127:
				miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneral)
				miTexto2 = miFuente2.render("Max " + str(maxword) + " char", 0, rojo)
				posxtgo = calcularx(letras, ancho, modo_seguro)
				ventana.blit(miTexto2, (posxtgo + distprinc, posytxt + distelin))
				pygame.display.update()
				time.sleep(1)
				miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneral)
				miTexto2 = miFuente2.render("Max " + str(maxword) + " char", 0, negro)
				ventana.blit(miTexto2, (posxtgo + distprinc, posytxt + distelin))
				pygame.display.update()

			else:
				if evento.key == 8 or evento.key == 127:
					letraslist.extend(letras)
					letraslist.reverse()

					try:
						letraborrar = letraslist[0]

					except:
						miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneral)
						miTexto2 = miFuente2.render("Nada para borrar", 0, rojo)
						posxtgo = calcularx(letras, ancho)
						ventana.blit(miTexto2, (posxtgo + distprinc, posytxt + distelin))
						pygame.display.update()
						time.sleep(1)
						miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneral)
						miTexto2 = miFuente2.render("Nada para borrar", 0, negro)
						ventana.blit(miTexto2, (posxtgo + distprinc, posytxt + distelin))
						pygame.display.update()

					else:
						letraslist.reverse()
						letraslist.pop()
						letras = ""

						for letra in letraslist:
							letras = letras + letra

						letras = escribir(letraborrar, letras, ventana, negro, posytxt + distelin, maxword, ancho, modo_seguro)
						letraslist = []
						letraslist.extend(letras)
						letraslist.pop()
						letras = ""

						for letra in letraslist:
							letras = letras + letra

				elif evento.key == 13:

					if len(letras) < minword:
						miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneral)
						miTexto2 = miFuente2.render("Min " + str(minword) + " char", 0, rojo)
						posxtgo = calcularx(letras, ancho, modo_seguro)
						ventana.blit(miTexto2, (posxtgo + distprinc, posytxt + distelin))
						pygame.display.update()
						time.sleep(1)
						miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneral)
						miTexto2 = miFuente2.render("Min " + str(minword) + " char", 0, negro)
						ventana.blit(miTexto2, (posxtgo + distprinc, posytxt + distelin))
						pygame.display.update()

					else:
						print("Texto introducido correctamente")
						intro = True

				else:

					try:

						letras = escribir(evento.unicode, letras, ventana, blanco, posytxt + distelin, maxword, ancho, modo_seguro)

					except:
						print("Esa tecla no esta predefinida")
						miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneral)
						miTexto2 = miFuente2.render("Ese comando no es válido", 0, rojo)
						posxtgo = calcularx(letras, ancho, modo_seguro)
						ventana.blit(miTexto2, (posxtgo + distprinc, posytxt + distelin))
						pygame.display.update()
						time.sleep(1)
						miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneral)
						miTexto2 = miFuente2.render("Ese comando no es válido", 0, negro)
						ventana.blit(miTexto2, (posxtgo + distprinc, posytxt + distelin))
						pygame.display.update()

	return (intro, letras)