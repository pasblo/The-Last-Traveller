import pygame

import sys

import sqlite3

from Modulos.objetos_de_pantalla import *

from pygame.locals import *

from Modulos.user import *

from Modulos.cifrador import *

from Modulos.sqlite3faciliter import *

from Modulos.sqlite3igualador import *

from Modulos.basededatosajustesfaciliter import *

from Modulos.clasificador import SoundObj, BGMObj

import time

def Ejecutarajustes(ventana, user_act, ancho, alto, debug_vent = "Pantalla", debug_font = "Calibri"):

	def calcularx(letras, ancho):

		longit = 0

		for letraact in letras:

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

		return longit + 4

	negro = (0, 0, 0)

	blanco = (255, 255, 255)

	rojo = (255, 0, 0)

	azul = (0, 0, 255)

	posxtxt1 = round(0.0078125 * ancho) #Caracteristicas de texto superior
	posytxt1 = round(0.0078125 * alto)
	tamañotxt1 = round(0.03906 * ancho)

	tamañoline = round(0.00190625 * ancho) #Caracteristicas generales de las lineas

	posyline1 = round(0.08333333 * alto) #Caracteristicas de linea 1

	posxline2 = round(0.6265625 * ancho) #Caracteristicas de la linea 2
	posyline2 = round(0.08333333 * alto)

	posxline3 = round(0.6265625 * ancho) #Caracteristicas de la linea 3
	posyline3 = round(0.138888888 * alto)

	posxline4 = round(0.6265625 * ancho) #Caracteristicas de la linea 4
	posyline4 = round(0.41666666 * alto) #300 if y == 720

	posxline5 = round(0.6265625 * ancho) #Caracteristicas de la linea 5
	posyline5 = round(0.4722222 * alto) #340 if y == 720

	posxfinishlines = round(0.6265625 * ancho)

	posyline6 = round(0.2083333 * alto) #150 == 720
	posyline7 = round(0.2638888 * alto) #190 == 720
	posyline8 = round(0.3194444 * alto) #230 == 720
	posyline9 = round(0.375 * alto) # 270 == 720

	bytesperenterline = 100 #For nothing

	posy1polygon = round(0.08333333 * alto) #Caracteristicas de los botones principales
	posy2polygon = round(0.138888888 * alto)
	posx3polygon = round(0.19625 * ancho)
	posy3polygon = round(0.138888888 * alto)
	posx4polygon = round(0.2353125 * ancho)
	posy4polygon = round(0.08333333 * alto)
	tamañopolygon = round(0.00190625 * ancho)
	tamañotxtpolygon = round(0.02734375 * ancho)
	tamañotxtat = round(0.0234375 * ancho)
	posx1botat = round(0.015625 * ancho)
	posy1botat = round(0.9305555 * alto)
	posx2botat = round(0.234375 * ancho)
	posy2botat = round(0.9722222 * alto)
	errordebotat = round(0.00390625 * ancho)
	textoinfox = round(0.25 * ancho)
	textoinfoy = round(0.944444444 * alto)
	tamañotextoinfo = round(0.0140625 * ancho)

	caracteristicaspolygons = [posy1polygon, posy2polygon, posx3polygon, posy3polygon, posx4polygon, posy4polygon, tamañopolygon, tamañotxtpolygon, tamañotxtat, posx1botat, posy1botat, posx2botat, posy2botat, errordebotat, textoinfox, textoinfoy, tamañotextoinfo]

	posxcircle1 = round(0.015625 * ancho) #Caracteristicas de la seleccion de ajustes
	posycircle1 = round(0.180555 * alto)
	posxtxt = round(0.021875 * ancho)
	posytxt = round(0.1625 * alto)
	tamañotxtajustes = round(0.0234375 * ancho)
	ydeinterlineado = round(0.0555555 * alto)

	caracteristicastxtajustes = [posxcircle1, posycircle1, posxtxt, posytxt, tamañotxtajustes, ydeinterlineado]

	#posx1bot1 = 805
	#posy1bot1 = 116
	#posx2bot1 = 1033
	#posy2bot1 = 145
	#tamañobot1 = 30

	posxtxtgen = round(0.63046875 * ancho) #Caracteristicas de las especificaciones de los ajustes
	posytxt1_es = round(0.166666 * alto)
	posytxt2_es = round(0.208333 * alto)
	posytxt3_es = round(0.25 * alto)
	posytxt4_es = round(0.291666 * alto)
	posytxt5_es = round(0.33333333333 * alto)
	posytxt6_es = round(0.375 * alto)
	tamañotxtgen = round(0.015625 * ancho)

	posytxt10 = round(0.48611111 * alto)

	posytxt11 = round(0.52777777 * alto)

	caracteristicas_especifico = [posxtxtgen, posytxt1_es, posytxt2_es, posytxt3_es, posytxt4_es, posytxt5_es, posytxt6_es, tamañotxtgen, posytxt10, posytxt11, tamañopolygon]

	posxtxt8y9 = round(0.671875 * ancho) #Caracteristicas de textos enunciados 1 y 2
	posytxt8 = round(0.09028 * alto)
	posytxt9 = round(0.423611 * alto)

	posx1bot7 = round(0.78125 * ancho) #botones: play/stop # =                 1000
	posy1bot7 = round(0.90277777 * alto)#Ant = (0.944444 * alto) # =           680
	posx2bot7 = round(0.8203125 * ancho) #Ant = round(0.796875 * ancho) # =    1050
	posy2bot7 = round(0.972222 * alto) # =                                     700

	posx1txt21 = round(0.44140625 * ancho)
	posy1txt21 = round(0.01111111111111111111111111111111 * alto)

	posx2txt21 = round(0.875 * ancho)
	posy2txt21 = round(0.01111111111111111111111111111111 * alto)

	posx1bot9 = round(0.015625 * ancho)
	posy1bot9 = round(0.423611 * alto)
	posx2bot9 = round(0.29296875 * ancho)
	posy2bot9 = round(0.45833333333333333333333333333333 * alto)

	posxtxt232425 = round(0.296875 * ancho)
	posytxt23 = round(0.40694444444444444444444444444444 * alto)
	posytxt24 = round(0.43472222222222222222222222222222 * alto)
	posytxt25 = round(0.4625 * alto)
	posytxt26 = round(0.47222222222222222222222222222222 * alto)

	#Loggeo de pantalla por primera vez:

	ventana.fill(negro)

	txt1, posxytxt1 = print_pantalla("Ajustes de " + debug_vent + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

	vent_act = debug_vent

	def set_botones(caracteristicas, ventana, debug_vent): #Terminado

		posy1polygon = caracteristicas[0]
		posy2polygon = caracteristicas[1]
		posx3polygon = caracteristicas[2]
		posy3polygon = caracteristicas[3]
		posx4polygon = caracteristicas[4]
		posy4polygon = caracteristicas[5]
		tamañopolygon = caracteristicas[6]
		tamañotxtpolygon = caracteristicas[7]
		tamañotxtat = caracteristicas[8]
		posx1botat = caracteristicas[9]
		posy1botat = caracteristicas[10]
		posx2botat = caracteristicas[11]
		posy2botat = caracteristicas[12]
		errordebotat = caracteristicas[13]
		textoinfox = caracteristicas[14]
		textoinfoy = caracteristicas[15]
		tamañotextoinfo = caracteristicas[16]

		ajustes = extraer_ajustes()

		vol_general = ajustes[4]
		vol_musica = ajustes[6]

		if debug_vent == "Pantalla":

			pygame.draw.polygon(ventana, blanco, ((0, posy1polygon), (0, posy2polygon), (posx3polygon, posy3polygon), (posx4polygon, posy4polygon)))

			pygame.draw.polygon(ventana, blanco, ((posx4polygon, posy1polygon), (posx3polygon, posy2polygon), (posx3polygon * 2, posy3polygon), (posx4polygon * 2 - (posx4polygon - posx3polygon), posy4polygon)), tamañopolygon)

			pygame.draw.polygon(ventana, blanco, ((posx4polygon * 2 - (posx4polygon - posx3polygon), posy1polygon), (posx3polygon * 2, posy2polygon), (posx3polygon * 3, posy3polygon), (posx4polygon * 3 - (posx4polygon - posx3polygon) * 2, posy4polygon)), tamañopolygon)

			txt2, posxytxt2 = print_pantalla("Pantalla", tamañopolygon * 4, posy1polygon + tamañopolygon, tamañotxtpolygon + tamañopolygon * 2, negro, debug_font)

			txt3, posxytxt3 = print_pantalla("Sonido", posx4polygon + tamañopolygon * 4, posy1polygon + tamañopolygon * 2, tamañotxtpolygon, blanco, debug_font)

			txt4, posxytxt4 = print_pantalla("Animaciones", posx4polygon * 2 - (posx4polygon - posx3polygon) + tamañopolygon * 4, posy1polygon + tamañopolygon * 2, tamañotxtpolygon, blanco, debug_font)

		elif debug_vent == "Sonido":

			pygame.draw.polygon(ventana, blanco, ((0, posy1polygon), (0, posy2polygon), (posx3polygon, posy3polygon), (posx4polygon, posy4polygon)), tamañopolygon)

			pygame.draw.polygon(ventana, blanco, ((posx4polygon, posy1polygon), (posx3polygon, posy2polygon), (posx3polygon * 2, posy3polygon), (posx4polygon * 2 - (posx4polygon - posx3polygon), posy4polygon)))

			pygame.draw.polygon(ventana, blanco, ((posx4polygon * 2 - (posx4polygon - posx3polygon), posy1polygon), (posx3polygon * 2, posy2polygon), (posx3polygon * 3, posy3polygon), (posx4polygon * 3 - (posx4polygon - posx3polygon) * 2, posy4polygon)), tamañopolygon)

			txt2, posxytxt2 = print_pantalla("Pantalla", tamañopolygon * 4, posy1polygon + tamañopolygon, tamañotxtpolygon + tamañopolygon * 2, blanco, debug_font)

			txt3, posxytxt3 = print_pantalla("Sonido", posx4polygon + tamañopolygon * 4, posy1polygon + tamañopolygon * 2, tamañotxtpolygon, negro, debug_font)

			txt4, posxytxt4 = print_pantalla("Animaciones", posx4polygon * 2 - (posx4polygon - posx3polygon) + tamañopolygon * 4, posy1polygon + tamañopolygon * 2, tamañotxtpolygon, blanco, debug_font)

		elif debug_vent == "Animaciones":

			pygame.draw.polygon(ventana, blanco, ((0, posy1polygon), (0, posy2polygon), (posx3polygon, posy3polygon), (posx4polygon, posy4polygon)), tamañopolygon)

			pygame.draw.polygon(ventana, blanco, ((posx4polygon, posy1polygon), (posx3polygon, posy2polygon), (posx3polygon * 2, posy3polygon), (posx4polygon * 2 - (posx4polygon - posx3polygon), posy4polygon)), tamañopolygon)

			pygame.draw.polygon(ventana, blanco, ((posx4polygon * 2 - (posx4polygon - posx3polygon), posy1polygon), (posx3polygon * 2, posy2polygon), (posx3polygon * 3, posy3polygon), (posx4polygon * 3 - (posx4polygon - posx3polygon) * 2, posy4polygon)))

			txt2, posxytxt2 = print_pantalla("Pantalla", tamañopolygon * 4, posy1polygon + tamañopolygon, tamañotxtpolygon + tamañopolygon * 2, blanco, debug_font)

			txt3, posxytxt3 = print_pantalla("Sonido", posx4polygon + tamañopolygon * 4, posy1polygon + tamañopolygon * 2, tamañotxtpolygon, blanco, debug_font)

			txt4, posxytxt4 = print_pantalla("Animaciones", posx4polygon * 2 - (posx4polygon - posx3polygon) + tamañopolygon * 4, posy1polygon + tamañopolygon * 2, tamañotxtpolygon, negro, debug_font)

		bot1 = crear_boton3(ventana, posx1botat, posy1botat, posx2botat, posy2botat, "<-- Pantalla anterior", tamañotxtat, tamañopolygon, errordebotat, blanco, debug_font, blanco)

		txt19, posxytxt19 = print_pantalla("* Estos ajustes se guardaran para todos los usuarios por igual", textoinfox, textoinfoy, tamañotextoinfo, blanco, debug_font)

		posesxybot1, posesxy2bot1 = bot1[1]

		return ((txt2, posxytxt2), (txt3, posxytxt3), (txt4, posxytxt4), (posesxybot1, posesxy2bot1, bot1[0]), (txt19, posxytxt19))

	def set_ajustes(caracteristicas, ventana, vent, ajuste):

		posxcircle1 = caracteristicas[0]
		posycircle1 = caracteristicas[1]
		posxtxt = caracteristicas[2]
		posytxt = caracteristicas[3]
		tamañotxtajustes = caracteristicas[4]
		ydeinterlineado = caracteristicas[5]

		ajustes = extraer_ajustes()

		ancho_ext = int(ajustes[0])
		alto_ext = int(ajustes[1])
		pantalla_comp_ext = ajustes[2]
		font_ext = ajustes[3]

		vol_general = ajustes[4]
		vol_efectos = ajustes[5]
		vol_musica = ajustes[6]

		Effectyanimations = ajustes[7]
		Scroll = ajustes[8]
		MaxFPS = ajustes[9]
		VSync = ajustes[10]

		if vent == "Pantalla":

			if ajuste == "TamañoPant":

				pygame.draw.circle(ventana, rojo, (posxcircle1, posycircle1), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado * 2), round(0.00390625 * ancho_ext))

			elif ajuste == "PantComp":

				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, rojo, (posxcircle1, posycircle1 + ydeinterlineado), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado * 2), round(0.00390625 * ancho_ext))

			elif ajuste == "Fuente":

				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, rojo, (posxcircle1, posycircle1 + ydeinterlineado * 2), round(0.00390625 * ancho_ext))

			else:

				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado * 2), round(0.00390625 * ancho_ext))

			txt5, posxytxt5 = print_pantalla("Tamaño de pantalla: " + str(ancho_ext) + " X " + str(alto_ext), posxtxt, posytxt, tamañotxtajustes, blanco, debug_font)

			txt6, posxytxt6 = print_pantalla("Pantalla completa: " + str(pantalla_comp_ext), posxtxt, posytxt + ydeinterlineado, tamañotxtajustes, blanco, debug_font)

			txt7, posxytxt7 = print_pantalla("Fuente de letra: " + str(font_ext), posxtxt, posytxt + ydeinterlineado * 2, tamañotxtajustes, blanco, debug_font)

			pygame.draw.line(ventana, blanco, (0, posyline6), (posxfinishlines, posyline6), tamañoline)

			pygame.draw.line(ventana, blanco, (0, posyline7), (posxfinishlines, posyline7), tamañoline)

			pygame.draw.line(ventana, blanco, (0, posyline8), (posxfinishlines, posyline8), tamañoline)

			#Sin utilizar:

			txt18, posxytxt18 = print_pantalla("", posxtxt, posytxt + ydeinterlineado * 3, tamañotxtajustes, blanco, debug_font)


		elif vent == "Sonido":

			if ajuste == "VolGen":

				pygame.draw.circle(ventana, rojo, (posxcircle1, posycircle1), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado * 2), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado * 3), round(0.00390625 * ancho_ext))

			elif ajuste == "VolEffect":

				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, rojo, (posxcircle1, posycircle1 + ydeinterlineado), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado * 2), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado * 3), round(0.00390625 * ancho_ext))

			elif ajuste == "VolFondo":

				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, rojo, (posxcircle1, posycircle1 + ydeinterlineado * 2), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado * 3), round(0.00390625 * ancho_ext))

			elif ajuste == "AddCancion":

				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado * 2), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, rojo, (posxcircle1, posycircle1 + ydeinterlineado * 3), round(0.00390625 * ancho_ext))

			else:

				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado * 2), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado * 3), round(0.00390625 * ancho_ext))

			txt5, posxytxt5 = print_pantalla("Volumen general: " + str(vol_general) + "%", posxtxt, posytxt, tamañotxtajustes, blanco, debug_font)

			txt6, posxytxt6 = print_pantalla("Volumen efectos de sonido: " + str(vol_efectos) + "%", posxtxt, posytxt + ydeinterlineado, tamañotxtajustes, blanco, debug_font)

			txt7, posxytxt7 = print_pantalla("Volumen musica de fondo: " + str(vol_musica) + "%", posxtxt, posytxt + ydeinterlineado * 2, tamañotxtajustes, blanco, debug_font)

			txt18, posxytxt18 = print_pantalla("Añadir musica de fondo", posxtxt, posytxt + ydeinterlineado * 3, tamañotxtajustes, blanco, debug_font)

			pygame.draw.line(ventana, blanco, (0, posyline6), (posxfinishlines, posyline6), tamañoline)

			pygame.draw.line(ventana, blanco, (0, posyline7), (posxfinishlines, posyline7), tamañoline)

			pygame.draw.line(ventana, blanco, (0, posyline8), (posxfinishlines, posyline8), tamañoline)

			pygame.draw.line(ventana, blanco, (0, posyline9), (posxfinishlines, posyline9), tamañoline)


		elif vent == "Animaciones":

			if ajuste == "Effectyanimations":

				pygame.draw.circle(ventana, rojo, (posxcircle1, posycircle1), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado * 2), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado * 3), round(0.00390625 * ancho_ext))

			elif ajuste == "Scroll":

				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, rojo, (posxcircle1, posycircle1 + ydeinterlineado), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado * 2), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado * 3), round(0.00390625 * ancho_ext))

			elif ajuste == "MaxFPS":

				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, rojo, (posxcircle1, posycircle1 + ydeinterlineado * 2), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado * 3), round(0.00390625 * ancho_ext))

			elif ajuste == "VSync":

				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado * 2), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, rojo, (posxcircle1, posycircle1 + ydeinterlineado * 3), round(0.00390625 * ancho_ext))

			else:

				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado * 2), round(0.00390625 * ancho_ext))
				pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + ydeinterlineado * 3), round(0.00390625 * ancho_ext))

			txt5, posxytxt5 = print_pantalla("Efectos y animaciones: " + Effectyanimations, posxtxt, posytxt, tamañotxtajustes, blanco, debug_font)

			txt6, posxytxt6 = print_pantalla("Scroll del fondo: " + Scroll, posxtxt, posytxt + ydeinterlineado, tamañotxtajustes, blanco, debug_font)

			if int(MaxFPS) > 500:

				txt7, posxytxt7 = print_pantalla("FPS aproximados: Infinitos", posxtxt, posytxt + ydeinterlineado * 2, tamañotxtajustes, blanco, debug_font)

			else:

				txt7, posxytxt7 = print_pantalla("FPS aproximados: " + MaxFPS, posxtxt, posytxt + ydeinterlineado * 2, tamañotxtajustes, blanco, debug_font)

			txt18, posxytxt18 = print_pantalla("Activar VSync: " + VSync, posxtxt, posytxt + ydeinterlineado * 3, tamañotxtajustes, blanco, debug_font)

			pygame.draw.line(ventana, blanco, (0, posyline6), (posxfinishlines, posyline6), tamañoline)

			pygame.draw.line(ventana, blanco, (0, posyline7), (posxfinishlines, posyline7), tamañoline)

			pygame.draw.line(ventana, blanco, (0, posyline8), (posxfinishlines, posyline8), tamañoline)

			pygame.draw.line(ventana, blanco, (0, posyline9), (posxfinishlines, posyline9), tamañoline)

		return((txt5, posxytxt5), (txt6, posxytxt6), (txt7, posxytxt7), (txt18, posxytxt18))

	def set_parte_especifica(caracteristicas, ventana, ajuste = None):

		posxtxtgen = caracteristicas[0]
		posytxt1 = caracteristicas[1]
		posytxt2 = caracteristicas[2]
		posytxt3 = caracteristicas[3]
		posytxt4 = caracteristicas[4]
		posytxt5 = caracteristicas[5]
		posytxt6 = caracteristicas[6]

		tamañotxtgen = caracteristicas[7]

		posytxt10 = caracteristicas[8]
		posytxt11 = caracteristicas[9]
		tamañopolygon = caracteristicas[10]

		ajustes = extraer_ajustes()

		ancho_ext = ajustes[0]
		alto_ext = ajustes[1]
		pantalla_comp_ext = ajustes[2]
		font_ext = ajustes[3]

		vol_general = ajustes[4]
		vol_efectos = ajustes[5]
		vol_musica = ajustes[6]

		Effectyanimations = ajustes[7]
		Scroll = ajustes[8]
		MaxFPS = ajustes[9]
		VSync = ajustes[10]

		if ajuste == None:

			#Definicion del apartado de caracteristicas

			dts1 = print_pantalla("", posxtxtgen, posytxt1, tamañotxtgen, blanco, debug_font)

			dts2 = print_pantalla("", posxtxtgen, posytxt2, tamañotxtgen, blanco, debug_font)

			dts3 = print_pantalla("", posxtxtgen, posytxt3, tamañotxtgen, blanco, debug_font)

			dts4 = print_pantalla("", posxtxtgen, posytxt4, tamañotxtgen, blanco, debug_font)

			dts5 = print_pantalla("", posxtxtgen, posytxt5, tamañotxtgen, blanco, debug_font)

			dts6 = print_pantalla("", posxtxtgen, posytxt6, tamañotxtgen, blanco, debug_font)

			#Definicion del apartado de ajustes

			txt_debajo1 = print_pantalla("", posxtxtgen, posytxt10, tamañotxtgen, blanco, debug_font)

			txt_debajo2 = print_pantalla("", posxtxtgen, posytxt11, tamañotxtgen, blanco, debug_font)

			recint =  ["", ("", ""), "", ("", "", "", "")]

			bot2 = ["", ""]

			posesxybot2, posesxy2bot2 = [("", ""), ("", "")]

			txt_acomp1 = ["", ""]

			bot3 = ["", ""]

			posesxybot3, posesxy2bot3 = [("", ""), ("", "")]

			bot4 = ["", ""]

			posesxybot4, posesxy2bot4 = [("", ""), ("", "")]

			bot5 = ["", ""]

			posesxybot5, posesxy2bot5 = [("", ""), ("", "")]

			bot6 = ["", ""]

			posesxybot6, posesxy2bot6 = [("", ""), ("", "")]

		elif ajuste == "TamañoPant":

			#Definicion del apartado de caracteristicas

			dts1 = print_pantalla("Esta opción te permite cambiar el tamaño de la pantalla", posxtxtgen, posytxt1, tamañotxtgen, blanco, debug_font)

			dts2 = print_pantalla("del juego. Para elegir correctamente, escoge la opción", posxtxtgen, posytxt2, tamañotxtgen, blanco, debug_font)

			dts3 = print_pantalla("cuyo ancho sea igual al del tamaño de la pantalla de tu", posxtxtgen, posytxt3, tamañotxtgen, blanco, debug_font)

			dts4 = print_pantalla("ordenador. Para restablecer las condiciones iniciales", posxtxtgen, posytxt4, tamañotxtgen, blanco, debug_font)

			dts5 = print_pantalla("del tamaño de tu pantalla (1280 x 720) pulse F1", posxtxtgen, posytxt5, tamañotxtgen, blanco, debug_font)

			dts6 = print_pantalla("", posxtxtgen, posytxt6, tamañotxtgen, blanco, debug_font)

			#Definicion del apartado de ajustes

			txt_debajo1 = print_pantalla("El tamaño minimo es: (640 X 360)", posxtxtgen, posytxt10, tamañotxtgen, blanco, debug_font)

			txt_debajo2 = print_pantalla("El tamaño maximo es: (1920 X 1080)", posxtxtgen, posytxt11, tamañotxtgen, blanco, debug_font)

			recint =  ["", ("", ""), "", ("", "", "", "")]

			bot2 = crear_boton3(ventana, round(0.6484375 * ancho), round(0.6041666 * alto), round(0.72109375 * ancho), round(0.63888 * alto), "Anterior", round(0.01875 * ancho), round(0.0015625 * ancho), errordebotat, blanco, debug_font, blanco)

			posesxybot2, posesxy2bot2 = bot2[1]

			txt_acomp1 = print_pantalla(ancho_ext + " X " + alto_ext, round(0.725 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), blanco, debug_font)

			bot3 = crear_boton3(ventana, round(0.8203125 * ancho), round(0.6041666 * alto), round(0.8984375 * ancho), round(0.63888 * alto), "Siguiente", round(0.01875 * ancho), round(0.0015625 * ancho), errordebotat, blanco, debug_font, blanco)

			posesxybot3, posesxy2bot3 = bot3[1]

			bot4 = ["", ""]

			posesxybot4, posesxy2bot4 = [("", ""), ("", "")]

			bot5 = ["", ""]

			posesxybot5, posesxy2bot5 = [("", ""), ("", "")]

			bot6 = ["", ""]

			posesxybot6, posesxy2bot6 = [("", ""), ("", "")]

		elif ajuste == "PantComp":

			#Definicion del apartado de caracteristicas

			dts1 = print_pantalla("Decide si quieres jugar en pantalla completa o no.", posxtxtgen, posytxt1, tamañotxtgen, blanco, debug_font)

			dts2 = print_pantalla("Recuerda que para poner en pantalla completa puedes", posxtxtgen, posytxt2, tamañotxtgen, blanco, debug_font)

			dts3 = print_pantalla("usar F11 y, para quitarla, Esc. Si juegas en pantalla", posxtxtgen, posytxt3, tamañotxtgen, blanco, debug_font)

			dts4 = print_pantalla("completa, ajusta la calidad de la pantalla en la opción", posxtxtgen, posytxt4, tamañotxtgen, blanco, debug_font)

			dts5 = print_pantalla("anterior.", posxtxtgen, posytxt5, tamañotxtgen, blanco, debug_font)

			dts6 = print_pantalla("", posxtxtgen, posytxt6, tamañotxtgen, blanco, debug_font)

			#Definicion del apartado de ajustes

			txt_debajo1 = print_pantalla("Pulsa el botón para cambiar de True a False o viceversa." , posxtxtgen, posytxt10, tamañotxtgen, blanco, debug_font)

			txt_debajo2 = print_pantalla("", posxtxtgen, posytxt11, tamañotxtgen, blanco, debug_font)

			recint =  ["", ("", ""), "", ("", "", "", "")]

			bot2 = crear_boton3(ventana, round(0.6484375 * ancho), round(0.6041666 * alto), round(0.72109375 * ancho), round(0.63888 * alto), "Cambiar", round(0.01875 * ancho), round(0.0015625 * ancho), errordebotat, blanco, debug_font, blanco)

			posesxybot2, posesxy2bot2 = bot2[1]

			txt_acomp1 = ["", ""]

			bot3 = ["", ""]

			posesxybot3, posesxy2bot3 = [("", ""), ("", "")]

			bot4 = ["", ""]

			posesxybot4, posesxy2bot4 = [("", ""), ("", "")]

			bot5 = ["", ""]

			posesxybot5, posesxy2bot5 = [("", ""), ("", "")]

			bot6 = ["", ""]

			posesxybot6, posesxy2bot6 = [("", ""), ("", "")]

		elif ajuste == "Fuente":

			#Definicion del apartado de caracteristicas

			dts1 = print_pantalla("Usa esta opción para cambiar la fuente de letra. Es la", posxtxtgen, posytxt1, tamañotxtgen, blanco, debug_font)

			dts2 = print_pantalla("fuente que va a aparecer en todos los menús del juego,", posxtxtgen, posytxt2, tamañotxtgen, blanco, debug_font)

			dts3 = print_pantalla("por lo que escoge una que te guste.", posxtxtgen, posytxt3, tamañotxtgen, blanco, debug_font)

			dts4 = print_pantalla("", posxtxtgen, posytxt4, tamañotxtgen, blanco, debug_font)

			dts5 = print_pantalla("", posxtxtgen, posytxt5, tamañotxtgen, blanco, debug_font)

			dts6 = print_pantalla("", posxtxtgen, posytxt6, tamañotxtgen, blanco, debug_font)

			#Definicion del apartado de ajustes

			txt_debajo1 = print_pantalla("Esta función está actualmente desactivada. Para más", posxtxtgen, posytxt10, tamañotxtgen, blanco, debug_font)

			txt_debajo2 = print_pantalla("información, visite nuestra web:", posxtxtgen, posytxt11, tamañotxtgen, blanco, debug_font)

			recint =  ["", ("", ""), "", ("", "", "", "")]

			bot2 = ["", ""]

			posesxybot2, posesxy2bot2 = [("", ""), ("", "")]

			txt_acomp1 = ["", ""]

			bot3 = ["", ""]

			posesxybot3, posesxy2bot3 = [("", ""), ("", "")]

			bot4 = ["", ""]

			posesxybot4, posesxy2bot4 = [("", ""), ("", "")]

			bot5 = ["", ""]

			posesxybot5, posesxy2bot5 = [("", ""), ("", "")]

			bot6 = ["", ""]

			posesxybot6, posesxy2bot6 = [("", ""), ("", "")]


		elif ajuste == "VolGen":

			#Definicion del apartado de caracteristicas

			dts1 = print_pantalla("Con esta opción puedes modificar el volumen de todos", posxtxtgen, posytxt1, tamañotxtgen, blanco, debug_font)

			dts2 = print_pantalla("los sonidos del juego, independientemente de si es", posxtxtgen, posytxt2, tamañotxtgen, blanco, debug_font)

			dts3 = print_pantalla("música o sonidos de efecto. Es como si regulases el", posxtxtgen, posytxt3, tamañotxtgen, blanco, debug_font)

			dts4 = print_pantalla("volumen de unos altavoces externos, lo cual afecta al", posxtxtgen, posytxt4, tamañotxtgen, blanco, debug_font)

			dts5 = print_pantalla("volumen del ordenador.", posxtxtgen, posytxt5, tamañotxtgen, blanco, debug_font)

			dts6 = print_pantalla("", posxtxtgen, posytxt6, tamañotxtgen, blanco, debug_font)

			#Definicion del apartado de ajustes

			txt_debajo1 = print_pantalla('Usa "+/-" y Play para probar el volumen. Dale a actuali-', posxtxtgen, posytxt10, tamañotxtgen, blanco, debug_font)

			txt_debajo2 = print_pantalla("zar para guardarlo. Presione shift para ir de 10 en 10.", posxtxtgen, posytxt11, tamañotxtgen, blanco, debug_font)

			recint =  ["", ("", ""), "", ("", "", "", "")]

			bot2 =  crear_boton3(ventana, round(0.6484375 * ancho), round(0.6041666 * alto), round(0.66609375 * ancho), round(0.63888 * alto), "-", round(0.01875 * ancho), round(0.0015625 * ancho), errordebotat, blanco, debug_font, blanco)

			posesxybot2, posesxy2bot2 = bot2[1]

			txt_acomp1 = print_pantalla(vol_general + "%", round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), blanco, debug_font)

			bot3 = crear_boton3(ventana, round(0.713125 * ancho), round(0.6041666 * alto), round(0.7324375 * ancho), round(0.63888 * alto), "+", round(0.01875 * ancho), round(0.0015625 * ancho), errordebotat, blanco, debug_font, blanco)

			posesxybot3, posesxy2bot3 = bot3[1]

			bot4 = crear_boton3(ventana, round(0.87890625 * ancho), round(0.944444 * alto), round(0.98828125 * ancho), round(0.972222 * alto), "Actualizar Vol", round(0.01875 * ancho), round(0.0015625 * ancho), errordebotat, blanco, debug_font, blanco)

			posesxybot4, posesxy2bot4 = bot4[1]

			bot5 = ["", ""]

			posesxybot5, posesxy2bot5 = [("", ""), ("", "")]

			bot6 = ["", ""]

			posesxybot6, posesxy2bot6 = [("", ""), ("", "")]

		elif ajuste == "VolEffect":

			#Definicion del apartado de caracteristicas

			dts1 = print_pantalla("Usa este ajuste para regular el volumen de los sonidos", posxtxtgen, posytxt1, tamañotxtgen, blanco, debug_font)

			dts2 = print_pantalla("de efecto. Por ejemplo, la destrucción de una nave", posxtxtgen, posytxt2, tamañotxtgen, blanco, debug_font)

			dts3 = print_pantalla("enemiga o un disparo.", posxtxtgen, posytxt3, tamañotxtgen, blanco, debug_font)

			dts4 = print_pantalla("", posxtxtgen, posytxt4, tamañotxtgen, blanco, debug_font)

			dts5 = print_pantalla("", posxtxtgen, posytxt5, tamañotxtgen, blanco, debug_font)

			dts6 = print_pantalla("", posxtxtgen, posytxt6, tamañotxtgen, blanco, debug_font)

			#Definicion del apartado de ajustes

			txt_debajo1 = print_pantalla('Usa "+/-" y Play para probar el volumen. Dale a actuali-', posxtxtgen, posytxt10, tamañotxtgen, blanco, debug_font)

			txt_debajo2 = print_pantalla('zar para guardarlo. Presione shift para ir de 10 en 10.', posxtxtgen, posytxt11, tamañotxtgen, blanco, debug_font)

			recint =  ["", ("", ""), "", ("", "", "", "")]

			bot2 =  crear_boton3(ventana, round(0.6484375 * ancho), round(0.6041666 * alto), round(0.66609375 * ancho), round(0.63888 * alto), "-", round(0.01875 * ancho), round(0.0015625 * ancho), errordebotat, blanco, debug_font, blanco)

			posesxybot2, posesxy2bot2 = bot2[1]

			txt_acomp1 = print_pantalla(vol_efectos + "%", round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), blanco, debug_font)

			bot3 = crear_boton3(ventana, round(0.713125 * ancho), round(0.6041666 * alto), round(0.7324375 * ancho), round(0.63888 * alto), "+", round(0.01875 * ancho), round(0.0015625 * ancho), errordebotat, blanco, debug_font, blanco)

			posesxybot3, posesxy2bot3 = bot3[1]

			bot4 = crear_boton3(ventana, round(0.87890625 * ancho), round(0.944444 * alto), round(0.98828125 * ancho), round(0.972222 * alto), "Actualizar Vol", round(0.01875 * ancho), round(0.0015625 * ancho), errordebotat, blanco, debug_font, blanco)

			posesxybot4, posesxy2bot4 = bot4[1]

			bot5 = ["", ""]

			posesxybot5, posesxy2bot5 = [("", ""), ("", "")]

			bot6 = ["", ""]

			posesxybot6, posesxy2bot6 = [("", ""), ("", "")]

		elif ajuste == "VolFondo":

			#Definicion del apartado de caracteristicas

			dts1 = print_pantalla("Regula el volumen de la música de fondo (menú,", posxtxtgen, posytxt1, tamañotxtgen, blanco, debug_font)

			dts2 = print_pantalla("niveles...).", posxtxtgen, posytxt2, tamañotxtgen, blanco, debug_font)

			dts3 = print_pantalla("", posxtxtgen, posytxt3, tamañotxtgen, blanco, debug_font)

			dts4 = print_pantalla("", posxtxtgen, posytxt4, tamañotxtgen, blanco, debug_font)

			dts5 = print_pantalla("", posxtxtgen, posytxt5, tamañotxtgen, blanco, debug_font)

			dts6 = print_pantalla("", posxtxtgen, posytxt6, tamañotxtgen, blanco, debug_font)

			#Definicion del apartado de ajustes

			txt_debajo1 = print_pantalla('Usa "+/-" y Play para probar el volumen. Dale a actuali-', posxtxtgen, posytxt10, tamañotxtgen, blanco, debug_font)

			txt_debajo2 = print_pantalla('zar para guardarlo. Presione shift para ir de 10 en 10.', posxtxtgen, posytxt11, tamañotxtgen, blanco, debug_font)

			recint =  ["", ("", ""), "", ("", "", "", "")]

			bot2 =  crear_boton3(ventana, round(0.6484375 * ancho), round(0.6041666 * alto), round(0.66609375 * ancho), round(0.63888 * alto), "-", round(0.01875 * ancho), round(0.0015625 * ancho), errordebotat, blanco, debug_font, blanco)

			posesxybot2, posesxy2bot2 = bot2[1]

			txt_acomp1 = print_pantalla(vol_musica + "%", round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), blanco, debug_font)

			bot3 = crear_boton3(ventana, round(0.713125 * ancho), round(0.6041666 * alto), round(0.7324375 * ancho), round(0.63888 * alto), "+", round(0.01875 * ancho), round(0.0015625 * ancho), errordebotat, blanco, debug_font, blanco)

			posesxybot3, posesxy2bot3 = bot3[1]

			bot4 = crear_boton3(ventana, round(0.87890625 * ancho), round(0.944444 * alto), round(0.98828125 * ancho), round(0.972222 * alto), "Actualizar Vol", round(0.01875 * ancho), round(0.0015625 * ancho), errordebotat, blanco, debug_font, blanco)

			posesxybot4, posesxy2bot4 = bot4[1]

			bot5 = ["", ""]

			posesxybot5, posesxy2bot5 = [("", ""), ("", "")]

			bot6 = ["", ""]

			posesxybot6, posesxy2bot6 = [("", ""), ("", "")]

		elif ajuste == "AddCancion":

			#Definicion del apartado de caracteristicas

			dts1 = print_pantalla("Utiliza este ajuste para cambiar la música de fondo.", posxtxtgen, posytxt1, tamañotxtgen, blanco, debug_font)

			dts2 = print_pantalla("", posxtxtgen, posytxt2, tamañotxtgen, blanco, debug_font)

			dts3 = print_pantalla("", posxtxtgen, posytxt3, tamañotxtgen, blanco, debug_font)

			dts4 = print_pantalla("", posxtxtgen, posytxt4, tamañotxtgen, blanco, debug_font)

			dts5 = print_pantalla("", posxtxtgen, posytxt5, tamañotxtgen, blanco, debug_font)

			dts6 = print_pantalla("", posxtxtgen, posytxt6, tamañotxtgen, blanco, debug_font)

			#Definicion del apartado de ajustes

			txt_debajo1 = print_pantalla("Esta función está actualmente desactivada. Para más", posxtxtgen, posytxt10, tamañotxtgen, blanco, debug_font) # 830, 435

			txt_debajo2 = print_pantalla("información, visite nuesta web:", posxtxtgen, posytxt11, tamañotxtgen, blanco, debug_font)

			recint = ["", ("", ""), "", ("", "", "", "")] #dibujar_recuadro_introductor(ventana, "Introduce aqui la cancion", (40, 40, 40), debug_font, 16, round(0.6484375 * ancho), 435, 930, 455)

			bot2 =  ["", ""] #crear_boton3(ventana, round(0.6484375 * ancho), round(0.6041666 * alto), round(0.72109375 * ancho), round(0.63888 * alto), "Añadir", round(0.01875 * ancho), round(0.0015625 * ancho), errordebotat, blanco, debug_font, blanco)

			posesxybot2, posesxy2bot2 = [("", ""), ("", "")] #bot2[1]

			txt_acomp1 = ["", ""]

			bot3 = ["", ""]

			posesxybot3, posesxy2bot3 = [("", ""), ("", "")]

			bot4 = ["", ""]

			posesxybot4, posesxy2bot4 = [("", ""), ("", "")]

			bot5 = ["", ""]

			posesxybot5, posesxy2bot5 = [("", ""), ("", "")]

			bot6 = ["", ""]

			posesxybot6, posesxy2bot6 = [("", ""), ("", "")]

		elif ajuste == "Effectyanimations":

			#Definicion del apartado de caracteristicas

			dts1 = print_pantalla("Utiliza este ajuste para elegir si quieres desactivar", posxtxtgen, posytxt1, tamañotxtgen, blanco, debug_font)

			dts2 = print_pantalla("algunos efectos y animaciones, como explosiones,", posxtxtgen, posytxt2, tamañotxtgen, blanco, debug_font)

			dts3 = print_pantalla("partículas... Si tienes un ordenador lento, se", posxtxtgen, posytxt3, tamañotxtgen, blanco, debug_font)

			dts4 = print_pantalla("recomienda que tengas esta opción en False.", posxtxtgen, posytxt4, tamañotxtgen, blanco, debug_font)

			dts5 = print_pantalla("", posxtxtgen, posytxt5, tamañotxtgen, blanco, debug_font)

			dts6 = print_pantalla("", posxtxtgen, posytxt6, tamañotxtgen, blanco, debug_font)

			#Definicion del apartado de ajustes

			txt_debajo1 = print_pantalla("Pulsa el botón para cambiar de True a False o viceversa.", posxtxtgen, posytxt10, tamañotxtgen, blanco, debug_font)

			txt_debajo2 = print_pantalla("", posxtxtgen, posytxt11, tamañotxtgen, blanco, debug_font)

			recint =  ["", ("", ""), "", ("", "", "", "")]

			bot2 = crear_boton3(ventana, round(0.6484375 * ancho), round(0.6041666 * alto), round(0.72109375 * ancho), round(0.63888 * alto), "Cambiar", round(0.01875 * ancho), round(0.0015625 * ancho), errordebotat, blanco, debug_font, blanco)

			posesxybot2, posesxy2bot2 = bot2[1]

			txt_acomp1 = ["", ""]

			bot3 = ["", ""]

			posesxybot3, posesxy2bot3 = [("", ""), ("", "")]

			bot4 = ["", ""]

			posesxybot4, posesxy2bot4 = [("", ""), ("", "")]

			bot5 = ["", ""]

			posesxybot5, posesxy2bot5 = [("", ""), ("", "")]

			bot6 = ["", ""]

			posesxybot6, posesxy2bot6 = [("", ""), ("", "")]

		elif ajuste == "Scroll":

			#Definicion del apartado de caracteristicas

			dts1 = print_pantalla("Usa este ajuste para elegir si quieres que el fondo", posxtxtgen, posytxt1, tamañotxtgen, blanco, debug_font)

			dts2 = print_pantalla("de la pantalla durante el juego se mueva o sea fija.", posxtxtgen, posytxt2, tamañotxtgen, blanco, debug_font)

			dts3 = print_pantalla("Si tienes un ordenador lento, se recomienda que tengas", posxtxtgen, posytxt3, tamañotxtgen, blanco, debug_font)

			dts4 = print_pantalla("esta opción en False.", posxtxtgen, posytxt4, tamañotxtgen, blanco, debug_font)

			dts5 = print_pantalla("", posxtxtgen, posytxt5, tamañotxtgen, blanco, debug_font)

			dts6 = print_pantalla("", posxtxtgen, posytxt6, tamañotxtgen, blanco, debug_font)

			#Definicion del apartado de ajustes

			txt_debajo1 = print_pantalla("Pulsa el botón para cambiar de True a False o viceversa.", posxtxtgen, posytxt10, tamañotxtgen, blanco, debug_font)

			txt_debajo2 = print_pantalla("", posxtxtgen, posytxt11, tamañotxtgen, blanco, debug_font)

			recint =  ["", ("", ""), "", ("", "", "", "")]

			bot2 = crear_boton3(ventana, round(0.6484375 * ancho), round(0.6041666 * alto), round(0.72109375 * ancho), round(0.63888 * alto), "Cambiar", round(0.01875 * ancho), round(0.0015625 * ancho), errordebotat, blanco, debug_font, blanco)

			posesxybot2, posesxy2bot2 = bot2[1]

			txt_acomp1 = ["", ""]

			bot3 = ["", ""]

			posesxybot3, posesxy2bot3 = [("", ""), ("", "")]

			bot4 = ["", ""]

			posesxybot4, posesxy2bot4 = [("", ""), ("", "")]

			bot5 = ["", ""]

			posesxybot5, posesxy2bot5 = [("", ""), ("", "")]

			bot6 = ["", ""]

			posesxybot6, posesxy2bot6 = [("", ""), ("", "")]

		elif ajuste == "MaxFPS":

			#Definicion del apartado de caracteristicas

			dts1 = print_pantalla("Esta función te permite regular el número aproximado", posxtxtgen, posytxt1, tamañotxtgen, blanco, debug_font)

			dts2 = print_pantalla("de FPS. A partir de 500 FPS , se consideran infinitos.", posxtxtgen, posytxt2, tamañotxtgen, blanco, debug_font)

			dts3 = print_pantalla("Los FPS (Frames per second) son el número de", posxtxtgen, posytxt3, tamañotxtgen, blanco, debug_font)

			dts4 = print_pantalla("fotogramas que muestra la pantalla por segundo.", posxtxtgen, posytxt4, tamañotxtgen, blanco, debug_font)

			dts5 = print_pantalla("", posxtxtgen, posytxt5, tamañotxtgen, blanco, debug_font)

			dts6 = print_pantalla("", posxtxtgen, posytxt6, tamañotxtgen, blanco, debug_font)

			#Definicion del apartado de ajustes

			txt_debajo1 = print_pantalla("Presione mas y menos para variar los FPS, presione", posxtxtgen, posytxt10, tamañotxtgen, blanco, debug_font)

			txt_debajo2 = print_pantalla("actualizar para guardarlos, y shift para ir de 10 en 10.", posxtxtgen, posytxt11, tamañotxtgen, blanco, debug_font)

			recint =  ["", ("", ""), "", ("", "", "", "")]

			bot2 =  crear_boton3(ventana, round(0.6484375 * ancho), round(0.6041666 * alto), round(0.66609375 * ancho), round(0.63888 * alto), "-", round(0.01875 * ancho), round(0.0015625 * ancho), errordebotat, blanco, debug_font, blanco)

			posesxybot2, posesxy2bot2 = bot2[1]

			if int(MaxFPS) > 500:

				txt_acomp1 = print_pantalla("Infinitos", round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), blanco, debug_font)

			else:

				txt_acomp1 = print_pantalla("FPS: " + str(MaxFPS), round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), blanco, debug_font)

			bot3 = crear_boton3(ventana, round(0.783125 * ancho), round(0.6041666 * alto), round(0.8024375 * ancho), round(0.63888 * alto), "+", round(0.01875 * ancho), round(0.0015625 * ancho), errordebotat, blanco, debug_font, blanco)

			posesxybot3, posesxy2bot3 = bot3[1]

			bot4 = crear_boton3(ventana, round(0.87890625 * ancho), round(0.944444 * alto), round(0.98828125 * ancho), round(0.972222 * alto), "Actualizar FPS", round(0.01875 * ancho), round(0.0015625 * ancho), errordebotat, blanco, debug_font, blanco)

			posesxybot4, posesxy2bot4 = bot4[1]

			bot5 = ["", ""]

			posesxybot5, posesxy2bot5 = [("", ""), ("", "")]

			bot6 = ["", ""]

			posesxybot6, posesxy2bot6 = [("", ""), ("", "")]

		elif ajuste == "VSync":

			#Definicion del apartado de caracteristicas

			dts1 = print_pantalla("Utiliza esta opción para elegir si quieres tener activado", posxtxtgen, posytxt1, tamañotxtgen, blanco, debug_font)

			dts2 = print_pantalla("el VSync o no. El VSync reduce el intervalo de FPS", posxtxtgen, posytxt2, tamañotxtgen, blanco, debug_font)

			dts3 = print_pantalla("(Fotogramas por segundo), aumentando el número de", posxtxtgen, posytxt3, tamañotxtgen, blanco, debug_font)

			dts4 = print_pantalla("FPS menor del intervalo y reduciendo el mayor.", posxtxtgen, posytxt4, tamañotxtgen, blanco, debug_font)

			dts5 = print_pantalla("", posxtxtgen, posytxt5, tamañotxtgen, blanco, debug_font)

			dts6 = print_pantalla("", posxtxtgen, posytxt6, tamañotxtgen, blanco, debug_font)

			#Definicion del apartado de ajustes

			txt_debajo1 = print_pantalla("Pulsa el botón para cambiar de True a False o viceversa.", posxtxtgen, posytxt10, tamañotxtgen, blanco, debug_font)

			txt_debajo2 = print_pantalla("", posxtxtgen, posytxt11, tamañotxtgen, blanco, debug_font)

			recint =  ["", ("", ""), "", ("", "", "", "")]

			bot2 = crear_boton3(ventana, round(0.6484375 * ancho), round(0.6041666 * alto), round(0.72109375 * ancho), round(0.63888 * alto), "Cambiar", round(0.01875 * ancho), round(0.0015625 * ancho), errordebotat, blanco, debug_font, blanco)

			posesxybot2, posesxy2bot2 = bot2[1]

			txt_acomp1 = ["", ""]

			bot3 = ["", ""]

			posesxybot3, posesxy2bot3 = [("", ""), ("", "")]

			bot4 = ["", ""]

			posesxybot4, posesxy2bot4 = [("", ""), ("", "")]

			bot5 = ["", ""]

			posesxybot5, posesxy2bot5 = [("", ""), ("", "")]

			bot6 = ["", ""]

			posesxybot6, posesxy2bot6 = [("", ""), ("", "")]

		dts = [dts1, dts2, dts3, dts4, dts5, dts6, txt_debajo1, txt_debajo2, txt_acomp1, (posesxybot2, posesxy2bot2, bot2[0]), (posesxybot3, posesxy2bot3, bot3[0]), (posesxybot4, posesxy2bot4, bot4[0]), (posesxybot5, posesxy2bot5, bot5[0]), (posesxybot6, posesxy2bot6, bot6[0]), recint]

		return dts

	Exit_presionado = False

	sucedio_accion = False

	ajuste_act = None

	ultimoevento = None

	pause_play = "play"

	musicapulsed = False

	shiftpressed = False

	ajustes = extraer_ajustes()

	ancho_ext = ajustes[0]
	alto_ext = ajustes[1]
	pantalla_comp_ext = ajustes[2]
	font_ext = ajustes[3]

	vol_general = ajustes[4]
	vol_efectos = ajustes[5]
	vol_musica = ajustes[6]

	Effectyanimations = ajustes[7]
	Scroll = ajustes[8]
	MaxFPS = ajustes[9]
	VSync = ajustes[10]

	Usuario = ajustes[11]

	volgenact = int(vol_general)

	voleffectact = int(vol_efectos)

	volmusicact = int(vol_musica)

	MaxFPSact = int(MaxFPS)

	pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

	pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

	pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

	pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

	pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

	todas = set_botones(caracteristicaspolygons, ventana, debug_vent)

	txt2, posxytxt2 = todas[0]

	txt3, posxytxt3 = todas[1]

	txt4, posxytxt4 = todas[2]

	posesxybot1, posesxy2bot1, botonreturn = todas[3]

	txt19, posxytxt19 = todas[4]

	todas = set_ajustes(caracteristicastxtajustes, ventana, debug_vent, ajuste_act)

	txt5, posxytxt5 = todas[0]

	txt6, posxytxt6 = todas[1]

	txt7, posxytxt7 = todas[2]

	txt18, posxytxt18 = todas[3]

	if Usuario == "None":
		guardado = False

	else:
		guardado = True

	txt8, posxytxt8 = print_pantalla("Carcteristicas de ajuste:", posxtxt8y9, posytxt8, tamañotxtpolygon, (255, 255, 255), debug_font)

	txt9, posxytxt9 = print_pantalla("Opciones de ajuste:", posxtxt8y9, posytxt9, tamañotxtpolygon, (255, 255, 255), debug_font)

	if user_act[1] != "None":
		txt26 = print_pantalla("Usuario actual guardado: " + Usuario, posx1bot9, posytxt26, tamañotxtgen, (255, 255, 255), debug_font)
		bot9 =  crear_boton3(ventana, posx1bot9, posy1bot9, posx2bot9, posy2bot9, "Guardar usuario actual: " + str(guardado), tamañotxtat, round(0.0015625 * ancho), errordebotat + 6, blanco, debug_font, blanco)
		txt23 = print_pantalla("Esta funcion sirve para que el usuario actualmente", posxtxt232425, posytxt23, tamañotxtgen, (255, 255, 255), debug_font)
		txt24 = print_pantalla("en uso se quede guardado y la próxima vez que este", posxtxt232425, posytxt24, tamañotxtgen, (255, 255, 255), debug_font)
		txt25 = print_pantalla("juego se abra, aparecera ya logeado.", posxtxt232425, posytxt25, tamañotxtgen, (255, 255, 255), debug_font)

	else:
		txt26 = ["", ""]
		bot9 = ["", ""]
		txt23 = ["", ""]
		txt24 = ["", ""]
		txt25 = ["", ""]
	
	if user_act[0]:

		txt21, posxytxt21 = print_pantalla("Usuario actual: " + user_act[1], posx1txt21, posy1txt21, tamañotxtpolygon, (255, 255, 255), debug_font)

	else:

		txt21, posxytxt21 = print_pantalla("No logeado", posx2txt21, posy2txt21, tamañotxtpolygon, (255, 255, 255), debug_font)

	dts = set_parte_especifica(caracteristicas_especifico, ventana)

	if dts != None:

		if dts[0] != None: txt10, posxytxt10 = dts[0]

		if dts[1] != None: txt11, posxytxt11 = dts[1]

		if dts[2] != None: txt12, posxytxt12 = dts[2]

		if dts[3] != None: txt13, posxytxt13 = dts[3]

		if dts[4] != None: txt14, posxytxt14 = dts[4]

		if dts[5] != None: txt15, posxytxt15 = dts[5]

		if dts[6] != None: txt16, posxytxt16 = dts[6]

		if dts[7] != None: txt17, posxytxt17 = dts[7]

		if dts[8] != None: txt20, posxytxt20 = dts[8]

		if dts[9] != None: posesxybot2, posesxy2bot2, bot2 = dts[9]

		if dts[10] != None: posesxybot3, posesxy2bot3, bot3 = dts[10]

		if dts[11] != None: posesxybot4, posesxy2bot4, bot4 = dts[11]

		if dts[12] != None: posesxybot5, posesxy2bot5, bot5 = dts[12]

		if dts[13] != None: posesxybot6, posesxy2bot6, bot6 = dts[13]

		if dts[14] != None: txt22, posxytxt22, bot8, posesxybot8 = dts[14]

	else: txt8 = None4

	bot7_alpha = pygame.image.load("Imagenes/play.png")

	bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

	posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

	while Exit_presionado == False:

		sucedio_accion = False

		for evento in pygame.event.get():

			ultimoevento = evento.type

			sucedio_accion = False

			ratonx, ratony = pygame.mouse.get_pos()

			conjdrect = ratonx - posx3polygon
			conjdrect2 = ratony - posy1polygon

			if evento.type == QUIT:
				print("Juego terminado")
				pygame.quit()
				raise KeyError

			elif evento.type == KEYUP:

				if evento.key == 304:

					shiftpressed = False

			elif evento.type == KEYDOWN:

				if evento.key == 304:

					shiftpressed = True

				elif evento.key == 282: #Cambiar a tamaño default

					actualizar_dato("ancho", 1280)
					actualizar_dato("alto", 720)

					ajustes = extraer_ajustes()

					ancho = int(ajustes[0])

					alto = int(ajustes[1])

					pantalla_comp = ajustes[2]

					if pantalla_comp == "True":
						try:
							pygame.display.set_mode((ancho, alto), pygame.FULLSCREEN)
						except:
							pass

					else:
						try:
							pygame.display.set_mode((ancho, alto))
						except:
							pass

					posxtxt1 = round(0.0078125 * ancho) #Caracteristicas de texto superior
					posytxt1 = round(0.0078125 * alto)
					tamañotxt1 = round(0.03906 * ancho)

					tamañoline = round(0.00190625 * ancho) #Caracteristicas generales de las lineas

					posyline1 = round(0.08333333 * alto) #Caracteristicas de linea 1

					posxline2 = round(0.6265625 * ancho) #Caracteristicas de la linea 2
					posyline2 = round(0.08333333 * alto)

					posxline3 = round(0.6265625 * ancho) #Caracteristicas de la linea 3
					posyline3 = round(0.138888888 * alto)

					posxline4 = round(0.6265625 * ancho) #Caracteristicas de la linea 4
					posyline4 = round(0.41666666 * alto) #300 if y == 720

					posxline5 = round(0.6265625 * ancho) #Caracteristicas de la linea 5
					posyline5 = round(0.4722222 * alto) #340 if y == 720

					posxfinishlines = round(0.6265625 * ancho)

					posyline6 = round(0.2083333 * alto) #150 == 720
					posyline7 = round(0.2638888 * alto) #190 == 720
					posyline8 = round(0.3194444 * alto) #230 == 720
					posyline9 = round(0.375 * alto) # 270 == 720

					bytesperenterline = 100 #For nothing

					posy1polygon = round(0.08333333 * alto) #Caracteristicas de los botones principales
					posy2polygon = round(0.138888888 * alto)
					posx3polygon = round(0.19625 * ancho)
					posy3polygon = round(0.138888888 * alto)
					posx4polygon = round(0.2353125 * ancho)
					posy4polygon = round(0.08333333 * alto)
					tamañopolygon = round(0.00190625 * ancho)
					tamañotxtpolygon = round(0.02734375 * ancho)
					tamañotxtat = round(0.0234375 * ancho)
					posx1botat = round(0.015625 * ancho)
					posy1botat = round(0.9305555 * alto)
					posx2botat = round(0.234375 * ancho)
					posy2botat = round(0.9722222 * alto)
					errordebotat = round(0.00390625 * ancho)
					textoinfox = round(0.25 * ancho)
					textoinfoy = round(0.944444444 * alto)
					tamañotextoinfo = round(0.0140625 * ancho)

					caracteristicaspolygons = [posy1polygon, posy2polygon, posx3polygon, posy3polygon, posx4polygon, posy4polygon, tamañopolygon, tamañotxtpolygon, tamañotxtat, posx1botat, posy1botat, posx2botat, posy2botat, errordebotat, textoinfox, textoinfoy, tamañotextoinfo]

					posxcircle1 = round(0.015625 * ancho) #Caracteristicas de la seleccion de ajustes
					posycircle1 = round(0.180555 * alto)
					posxtxt = round(0.021875 * ancho)
					posytxt = round(0.1625 * alto)
					tamañotxtajustes = round(0.0234375 * ancho)
					ydeinterlineado = round(0.0555555 * alto)

					caracteristicastxtajustes = [posxcircle1, posycircle1, posxtxt, posytxt, tamañotxtajustes, ydeinterlineado]

					#posx1bot1 = 805
					#posy1bot1 = 116
					#posx2bot1 = 1033
					#posy2bot1 = 145
					#tamañobot1 = 30

					posxtxtgen = round(0.63046875 * ancho) #Caracteristicas de las especificaciones de los ajustes
					posytxt1_es = round(0.166666 * alto)
					posytxt2_es = round(0.208333 * alto)
					posytxt3_es = round(0.25 * alto)
					posytxt4_es = round(0.291666 * alto)
					posytxt5_es = round(0.33333333333 * alto)
					posytxt6_es = round(0.375 * alto)
					tamañotxtgen = round(0.015625 * ancho)

					posytxt10 = round(0.48611111 * alto)

					posytxt11 = round(0.52777777 * alto)

					caracteristicas_especifico = [posxtxtgen, posytxt1_es, posytxt2_es, posytxt3_es, posytxt4_es, posytxt5_es, posytxt6_es, tamañotxtgen, posytxt10, posytxt11, tamañopolygon]

					posxtxt8y9 = round(0.671875 * ancho) #Caracteristicas de textos enunciados 1 y 2
					posytxt8 = round(0.09028 * alto)
					posytxt9 = round(0.423611 * alto)

					posx1bot7 = round(0.78125 * ancho) #botones: play/stop # =                 1000
					posy1bot7 = round(0.90277777 * alto)#Ant = (0.944444 * alto) # =           680
					posx2bot7 = round(0.8203125 * ancho) #Ant = round(0.796875 * ancho) # =    1050
					posy2bot7 = round(0.972222 * alto) # =

					posx1txt21 = round(0.44140625 * ancho)
					posy1txt21 = round(0.01111111111111111111111111111111 * alto)

					posx2txt21 = round(0.875 * ancho)
					posy2txt21 = round(0.01111111111111111111111111111111 * alto)

					posx1bot9 = round(0.015625 * ancho)
					posy1bot9 = round(0.423611 * alto)
					posx2bot9 = round(0.29296875 * ancho)
					posy2bot9 = round(0.45833333333333333333333333333333 * alto)

					posxtxt232425 = round(0.296875 * ancho)
					posytxt23 = round(0.40694444444444444444444444444444 * alto)
					posytxt24 = round(0.43472222222222222222222222222222 * alto)
					posytxt25 = round(0.4625 * alto)
					posytxt26 = round(0.47222222222222222222222222222222 * alto)

					txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

					pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

					todas = set_botones(caracteristicaspolygons, ventana, vent_act)

					txt2, posxytxt2 = todas[0]
								
					txt3, posxytxt3 = todas[1]

					txt4, posxytxt4 = todas[2]

					posesxybot1, posesxy2bot1, botonreturn = todas[3]

					txt19, posxytxt19 = todas[4]

					todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act, ajuste_act)

					txt5, posxytxt5 = todas[0]

					txt6, posxytxt6 = todas[1]

					txt7, posxytxt7 = todas[2]

					txt18, posxytxt18 = todas[3]

					txt8, posxytxt8 = print_pantalla("Carcteristicas de ajuste:", posxtxt8y9, posytxt8, tamañotxtpolygon, (255, 255, 255), debug_font)

					txt9, posxytxt9 = print_pantalla("Opciones de ajuste:", posxtxt8y9, posytxt9, tamañotxtpolygon, (255, 255, 255), debug_font)

					if user_act[1] != "None":
						txt26 = print_pantalla("Usuario actual guardado: " + Usuario, posx1bot9, posytxt26, tamañotxtgen, (255, 255, 255), debug_font)
						bot9 =  crear_boton3(ventana, posx1bot9, posy1bot9, posx2bot9, posy2bot9, "Guardar usuario actual: " + str(guardado), tamañotxtat, round(0.0015625 * ancho), errordebotat + 6, blanco, debug_font, blanco)
						txt23 = print_pantalla("Esta funcion sirve para que el usuario actualmente", posxtxt232425, posytxt23, tamañotxtgen, (255, 255, 255), debug_font)
						txt24 = print_pantalla("en uso se quede guardado y la próxima vez que este", posxtxt232425, posytxt24, tamañotxtgen, (255, 255, 255), debug_font)
						txt25 = print_pantalla("juego se abra, aparecera ya logeado.", posxtxt232425, posytxt25, tamañotxtgen, (255, 255, 255), debug_font)

					else:
						txt26 = ["", ""]
						bot9 = ["", ""]
						txt23 = ["", ""]
						txt24 = ["", ""]
						txt25 = ["", ""]
					if user_act[0]:

						txt21, posxytxt21 = print_pantalla("Usuario actual: " + user_act[1], posx1txt21, posy1txt21, tamañotxtpolygon, (255, 255, 255), debug_font)

					else:

						txt21, posxytxt21 = print_pantalla("No logeado", posx2txt21, posy2txt21, tamañotxtpolygon, (255, 255, 255), debug_font)

					dts = set_parte_especifica(caracteristicas_especifico, ventana, ajuste_act)

					if dts != None:

						if dts[0] != None: txt10, posxytxt10 = dts[0]

						if dts[1] != None: txt11, posxytxt11 = dts[1]

						if dts[2] != None: txt12, posxytxt12 = dts[2]

						if dts[3] != None: txt13, posxytxt13 = dts[3]

						if dts[4] != None: txt14, posxytxt14 = dts[4]

						if dts[5] != None: txt15, posxytxt15 = dts[5]

						if dts[6] != None: txt16, posxytxt16 = dts[6]

						if dts[7] != None: txt17, posxytxt17 = dts[7]

						if dts[8] != None: txt20, posxytxt20 = dts[8]

						if dts[9] != None: posesxybot2, posesxy2bot2, bot2 = dts[9]

						if dts[10] != None: posesxybot3, posesxy2bot3, bot3 = dts[10]

						if dts[11] != None: posesxybot4, posesxy2bot4, bot4 = dts[11]

						if dts[12] != None: posesxybot5, posesxy2bot5, bot5 = dts[12]

						if dts[13] != None: posesxybot6, posesxy2bot6, bot6 = dts[13]

						if dts[14] != None: txt22, posxytxt22, bot8, posesxybot8 = dts[14]

					if pause_play == "play":

						bot7_alpha = pygame.image.load("Imagenes/play.png")

						bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

						posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

					else: 

						bot7_alpha = pygame.image.load("Imagenes/pause.png")

						bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

						posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

				elif evento.key == 285: # F4
					print("Juego terminado")
					pygame.quit()
					raise KeyError

				elif evento.key == 27: # Esc

					pantalla_comp = False

					try:

						pygame.display.set_mode((ancho, alto))

						actualizar_dato("pantcomp", pantalla_comp)

						pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

						pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

						pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

						pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

						pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

						if user_act[1] != "None":
							txt26 = print_pantalla("Usuario actual guardado: " + Usuario, posx1bot9, posytxt26, tamañotxtgen, (255, 255, 255), debug_font)
							bot9 =  crear_boton3(ventana, posx1bot9, posy1bot9, posx2bot9, posy2bot9, "Guardar usuario actual: " + str(guardado), tamañotxtat, round(0.0015625 * ancho), errordebotat + 6, blanco, debug_font, blanco)
							txt23 = print_pantalla("Esta funcion sirve para que el usuario actualmente", posxtxt232425, posytxt23, tamañotxtgen, (255, 255, 255), debug_font)
							txt24 = print_pantalla("en uso se quede guardado y la próxima vez que este", posxtxt232425, posytxt24, tamañotxtgen, (255, 255, 255), debug_font)
							txt25 = print_pantalla("juego se abra, aparecera ya logeado.", posxtxt232425, posytxt25, tamañotxtgen, (255, 255, 255), debug_font)

						else:
							txt26 = ["", ""]
							bot9 = ["", ""]
							txt23 = ["", ""]
							txt24 = ["", ""]
							txt25 = ["", ""]

						todas = set_botones(caracteristicaspolygons, ventana, vent_act)

						txt2, posxytxt2 = todas[0]

						txt3, posxytxt3 = todas[1]

						txt4, posxytxt4 = todas[2]

						txt19, posxytxt19 = todas[4]

						todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act, ajuste_act)

						txt5, posxytxt5 = todas[0]

						txt6, posxytxt6 = todas[1]

						txt7, posxytxt7 = todas[2]

						txt18, posxytxt18 = todas[3]

						dts = set_parte_especifica(caracteristicas_especifico, ventana, ajuste_act)

						if dts != None:

							if dts[0] != None: txt10, posxytxt10 = dts[0]

							if dts[1] != None: txt11, posxytxt11 = dts[1]

							if dts[2] != None: txt12, posxytxt12 = dts[2]

							if dts[3] != None: txt13, posxytxt13 = dts[3]

							if dts[4] != None: txt14, posxytxt14 = dts[4]

							if dts[5] != None: txt15, posxytxt15 = dts[5]

							if dts[6] != None: txt16, posxytxt16 = dts[6]

							if dts[7] != None: txt17, posxytxt17 = dts[7]

							if dts[8] != None: txt20, posxytxt20 = dts[8]

							if dts[9] != None: posesxybot2, posesxy2bot2, bot2 = dts[9]

							if dts[10] != None: posesxybot3, posesxy2bot3, bot3 = dts[10]

							if dts[11] != None: posesxybot4, posesxy2bot4, bot4 = dts[11]

							if dts[12] != None: posesxybot5, posesxy2bot5, bot5 = dts[12]

							if dts[13] != None: posesxybot6, posesxy2bot6, bot6 = dts[13]

							if dts[14] != None: txt22, posxytxt22, bot8, posesxybot8 = dts[14]

						if pause_play == "play":

							bot7_alpha = pygame.image.load("Imagenes/play.png")

							bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

							posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

						else: 

							bot7_alpha = pygame.image.load("Imagenes/pause.png")

							bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

							posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

					except:
						print("Pantalla demasido grande o demasiado pequeña")

				elif evento.key == 292: # F11

					pantalla_comp = True

					try:

						pygame.display.set_mode((ancho, alto), pygame.FULLSCREEN)

						actualizar_dato("pantcomp", pantalla_comp)

						pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

						pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

						pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

						pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

						pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

						if user_act[1] != "None":
							txt26 = print_pantalla("Usuario actual guardado: " + Usuario, posx1bot9, posytxt26, tamañotxtgen, (255, 255, 255), debug_font)
							bot9 =  crear_boton3(ventana, posx1bot9, posy1bot9, posx2bot9, posy2bot9, "Guardar usuario actual: " + str(guardado), tamañotxtat, round(0.0015625 * ancho), errordebotat + 6, blanco, debug_font, blanco)
							txt23 = print_pantalla("Esta funcion sirve para que el usuario actualmente", posxtxt232425, posytxt23, tamañotxtgen, (255, 255, 255), debug_font)
							txt24 = print_pantalla("en uso se quede guardado y la próxima vez que este", posxtxt232425, posytxt24, tamañotxtgen, (255, 255, 255), debug_font)
							txt25 = print_pantalla("juego se abra, aparecera ya logeado.", posxtxt232425, posytxt25, tamañotxtgen, (255, 255, 255), debug_font)

						else:
							txt26 = ["", ""]
							bot9 = ["", ""]
							txt23 = ["", ""]
							txt24 = ["", ""]
							txt25 = ["", ""]

						todas = set_botones(caracteristicaspolygons, ventana, vent_act)

						txt2, posxytxt2 = todas[0]

						txt3, posxytxt3 = todas[1]

						txt4, posxytxt4 = todas[2]

						txt19, posxytxt19 = todas[4]

						todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act, ajuste_act)

						txt5, posxytxt5 = todas[0]

						txt6, posxytxt6 = todas[1]

						txt7, posxytxt7 = todas[2]

						txt18, posxytxt18 = todas[3]

						dts = set_parte_especifica(caracteristicas_especifico, ventana, ajuste_act)

						if dts != None:

							if dts[0] != None: txt10, posxytxt10 = dts[0]

							if dts[1] != None: txt11, posxytxt11 = dts[1]

							if dts[2] != None: txt12, posxytxt12 = dts[2]

							if dts[3] != None: txt13, posxytxt13 = dts[3]

							if dts[4] != None: txt14, posxytxt14 = dts[4]

							if dts[5] != None: txt15, posxytxt15 = dts[5]

							if dts[6] != None: txt16, posxytxt16 = dts[6]

							if dts[7] != None: txt17, posxytxt17 = dts[7]

							if dts[8] != None: txt20, posxytxt20 = dts[8]

							if dts[9] != None: posesxybot2, posesxy2bot2, bot2 = dts[9]

							if dts[10] != None: posesxybot3, posesxy2bot3, bot3 = dts[10]

							if dts[11] != None: posesxybot4, posesxy2bot4, bot4 = dts[11]

							if dts[12] != None: posesxybot5, posesxy2bot5, bot5 = dts[12]

							if dts[13] != None: posesxybot6, posesxy2bot6, bot6 = dts[13]

							if dts[14] != None: txt22, posxytxt22, bot8, posesxybot8 = dts[14]

						if pause_play == "play":

							bot7_alpha = pygame.image.load("Imagenes/play.png")

							bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

							posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

						else: 

							bot7_alpha = pygame.image.load("Imagenes/pause.png")

							bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

							posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

					except:
						print("Pantalla demasiado grande o demasido pequeña")

			if ratonx > 0 and ratony > posy1polygon and (ratony - posy1polygon)*(ratonx - posx3polygon) < 550 and ratony < posy2polygon and ratonx < posx4polygon:

				if evento.type == MOUSEBUTTONDOWN:

					try:

						musicadeprueva.stop()

					except:
						pass

					vent_act = "Pantalla"

					print("Boton 1 pulsado, cambiando a ajustes de la pantalla")

					ventana.fill(negro)

					txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

					pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

					if user_act[1] != "None":
						bot9 =  crear_boton3(ventana, posx1bot9, posy1bot9, posx2bot9, posy2bot9, "Guardar usuario actual: " + str(guardado), tamañotxtat, round(0.0015625 * ancho), errordebotat + 6, blanco, debug_font, blanco)

					else:
						bot9 = ["", ""]

					todas = set_botones(caracteristicaspolygons, ventana, vent_act)

					txt2, posxytxt2 = todas[0]

					txt3, posxytxt3 = todas[1]

					txt4, posxytxt4 = todas[2]

					txt19, posxytxt19 = todas[4]

					todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act, ajuste_act)

					txt5, posxytxt5 = todas[0]

					txt6, posxytxt6 = todas[1]

					txt7, posxytxt7 = todas[2]

					txt18, posxytxt18 = todas[3]

					dts = set_parte_especifica(caracteristicas_especifico, ventana)

					if dts != None:

						if dts[0] != None: txt10, posxytxt10 = dts[0]

						if dts[1] != None: txt11, posxytxt11 = dts[1]

						if dts[2] != None: txt12, posxytxt12 = dts[2]

						if dts[3] != None: txt13, posxytxt13 = dts[3]

						if dts[4] != None: txt14, posxytxt14 = dts[4]

						if dts[5] != None: txt15, posxytxt15 = dts[5]

						if dts[6] != None: txt16, posxytxt16 = dts[6]

						if dts[7] != None: txt17, posxytxt17 = dts[7]

						if dts[8] != None: txt20, posxytxt20 = dts[8]

						if dts[9] != None: posesxybot2, posesxy2bot2, bot2 = dts[9]

						if dts[10] != None: posesxybot3, posesxy2bot3, bot3 = dts[10]

						if dts[11] != None: posesxybot4, posesxy2bot4, bot4 = dts[11]

						if dts[12] != None: posesxybot5, posesxy2bot5, bot5 = dts[12]

						if dts[13] != None: posesxybot6, posesxy2bot6, bot6 = dts[13]

						if dts[14] != None: txt22, posxytxt22, bot8, posesxybot8 = dts[14]

					bot7_alpha = pygame.image.load("Imagenes/play.png")

					bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

					posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

			elif ratonx > 0 and ratony > posy1polygon and (ratony - posy1polygon)*(ratonx - posx3polygon * 2) < 550 and ratony < posy2polygon and ratonx < (posx4polygon * 2 - (posx4polygon - posx3polygon)):

				if evento.type == MOUSEBUTTONDOWN:

					try:

						musicadeprueva.stop()

					except:
						pass

					vent_act = "Sonido"

					print("Boton 2 pulsado, cambiando a ajustes del sonido")

					ajuste_act = None

					ventana.fill(negro)

					txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

					pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

					if user_act[1] != "None":
						bot9 =  crear_boton3(ventana, posx1bot9, posy1bot9, posx2bot9, posy2bot9, "Guardar usuario actual: " + str(guardado), tamañotxtat, round(0.0015625 * ancho), errordebotat + 6, blanco, debug_font, blanco)

					else:
						bot9 = ["", ""]

					todas = set_botones(caracteristicaspolygons, ventana, vent_act)

					txt2, posxytxt2 = todas[0]

					txt3, posxytxt3 = todas[1]

					txt4, posxytxt4 = todas[2]

					txt19, posxytxt19 = todas[4]

					todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act, ajuste_act)

					txt5, posxytxt5 = todas[0]

					txt6, posxytxt6 = todas[1]

					txt7, posxytxt7 = todas[2]

					txt18, posxytxt18 = todas[3]

					dts = set_parte_especifica(caracteristicas_especifico, ventana)

					if dts != None:

						if dts[0] != None: txt10, posxytxt10 = dts[0]

						if dts[1] != None: txt11, posxytxt11 = dts[1]

						if dts[2] != None: txt12, posxytxt12 = dts[2]

						if dts[3] != None: txt13, posxytxt13 = dts[3]

						if dts[4] != None: txt14, posxytxt14 = dts[4]

						if dts[5] != None: txt15, posxytxt15 = dts[5]

						if dts[6] != None: txt16, posxytxt16 = dts[6]

						if dts[7] != None: txt17, posxytxt17 = dts[7]

						if dts[8] != None: txt20, posxytxt20 = dts[8]

						if dts[9] != None: posesxybot2, posesxy2bot2, bot2 = dts[9]

						if dts[10] != None: posesxybot3, posesxy2bot3, bot3 = dts[10]

						if dts[11] != None: posesxybot4, posesxy2bot4, bot4 = dts[11]

						if dts[12] != None: posesxybot5, posesxy2bot5, bot5 = dts[12]

						if dts[13] != None: posesxybot6, posesxy2bot6, bot6 = dts[13]

						if dts[14] != None: txt22, posxytxt22, bot8, posesxybot8 = dts[14]

					bot7_alpha = pygame.image.load("Imagenes/play.png")

					bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

					posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

			elif ratonx > 0 and ratony > posy1polygon and (ratony - posy1polygon)*(ratonx - posx3polygon * 3) < 550 and ratony < posy2polygon and ratonx < (posx4polygon * 3 - (posx4polygon - posx3polygon) * 2):

				if evento.type == MOUSEBUTTONDOWN:

					try:

						musicadeprueva.stop()

					except:
						pass

					vent_act = "Animaciones"

					print("Boton 3 pulsado, cambiando a ajustes de las animaciones")

					ventana.fill(negro)

					txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

					pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

					if user_act[1] != "None":
						bot9 =  crear_boton3(ventana, posx1bot9, posy1bot9, posx2bot9, posy2bot9, "Guardar usuario actual: " + str(guardado), tamañotxtat, round(0.0015625 * ancho), errordebotat + 6, blanco, debug_font, blanco)

					else:
						bot9 = ["", ""]

					todas = set_botones(caracteristicaspolygons, ventana, vent_act)

					txt2, posxytxt2 = todas[0]

					txt3, posxytxt3 = todas[1]

					txt4, posxytxt4 = todas[2]

					txt19, posxytxt19 = todas[4]

					todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act, ajuste_act)

					txt5, posxytxt5 = todas[0]

					txt6, posxytxt6 = todas[1]

					txt7, posxytxt7 = todas[2]

					txt18, posxytxt18 = todas[3]

					dts = set_parte_especifica(caracteristicas_especifico, ventana)

					if dts != None:

						if dts[0] != None: txt10, posxytxt10 = dts[0]

						if dts[1] != None: txt11, posxytxt11 = dts[1]

						if dts[2] != None: txt12, posxytxt12 = dts[2]

						if dts[3] != None: txt13, posxytxt13 = dts[3]

						if dts[4] != None: txt14, posxytxt14 = dts[4]

						if dts[5] != None: txt15, posxytxt15 = dts[5]

						if dts[6] != None: txt16, posxytxt16 = dts[6]

						if dts[7] != None: txt17, posxytxt17 = dts[7]

						if dts[8] != None: txt20, posxytxt20 = dts[8]

						if dts[9] != None: posesxybot2, posesxy2bot2, bot2 = dts[9]

						if dts[10] != None: posesxybot3, posesxy2bot3, bot3 = dts[10]

						if dts[11] != None: posesxybot4, posesxy2bot4, bot4 = dts[11]

						if dts[12] != None: posesxybot5, posesxy2bot5, bot5 = dts[12]

						if dts[13] != None: posesxybot6, posesxy2bot6, bot6 = dts[13]

						if dts[14] != None: txt22, posxytxt22, bot8, posesxybot8 = dts[14]

					bot7_alpha = pygame.image.load("Imagenes/play.png")

					bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

					posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

			elif ratonx > 0 and ratony > posy2polygon and ratonx < posxfinishlines and ratony < posyline6:

				if evento.type == MOUSEBUTTONDOWN:

					ajustes = extraer_ajustes()

					vol_general_a_actualizar = int(ajustes[4])

					try:

						musicadeprueva.stop()

					except:
						pass

					if vent_act == "Pantalla":
						ajuste_act = "TamañoPant"

					elif vent_act == "Sonido":
						ajuste_act = "VolGen"
						volgenact = vol_general_a_actualizar

					elif vent_act == "Animaciones":
						ajuste_act = "Effectyanimations"

					print("Boton 4 pulsado, cambiando a ajuste " + ajuste_act)

					ventana.fill(negro)

					txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

					pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

					if user_act[1] != "None":
						bot9 =  crear_boton3(ventana, posx1bot9, posy1bot9, posx2bot9, posy2bot9, "Guardar usuario actual: " + str(guardado), tamañotxtat, round(0.0015625 * ancho), errordebotat + 6, blanco, debug_font, blanco)

					else:
						bot9 = ["", ""]

					todas = set_botones(caracteristicaspolygons, ventana, vent_act)

					txt2, posxytxt2 = todas[0]
						
					txt3, posxytxt3 = todas[1]

					txt4, posxytxt4 = todas[2]

					txt19, posxytxt19 = todas[4]

					todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act, ajuste_act)

					txt5, posxytxt5 = todas[0]

					txt6, posxytxt6 = todas[1]

					txt7, posxytxt7 = todas[2]

					txt18, posxytxt18 = todas[3]

					dts = set_parte_especifica(caracteristicas_especifico, ventana, ajuste_act)

					if dts != None:

						if dts[0] != None: txt10, posxytxt10 = dts[0]

						if dts[1] != None: txt11, posxytxt11 = dts[1]

						if dts[2] != None: txt12, posxytxt12 = dts[2]

						if dts[3] != None: txt13, posxytxt13 = dts[3]

						if dts[4] != None: txt14, posxytxt14 = dts[4]

						if dts[5] != None: txt15, posxytxt15 = dts[5]

						if dts[6] != None: txt16, posxytxt16 = dts[6]

						if dts[7] != None: txt17, posxytxt17 = dts[7]

						if dts[8] != None: txt20, posxytxt20 = dts[8]

						if dts[9] != None: posesxybot2, posesxy2bot2, bot2 = dts[9]

						if dts[10] != None: posesxybot3, posesxy2bot3, bot3 = dts[10]

						if dts[11] != None: posesxybot4, posesxy2bot4, bot4 = dts[11]

						if dts[12] != None: posesxybot5, posesxy2bot5, bot5 = dts[12]

						if dts[13] != None: posesxybot6, posesxy2bot6, bot6 = dts[13]

						if dts[14] != None: txt22, posxytxt22, bot8, posesxybot8 = dts[14]

					bot7_alpha = pygame.image.load("Imagenes/play.png")

					bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

					posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

			elif ratonx > 0 and ratony > posyline6 and ratonx < posxfinishlines and ratony < posyline7:

				if evento.type == MOUSEBUTTONDOWN:

					ajustes = extraer_ajustes()

					vol_efectos_a_actualizar = int(ajustes[5])

					try:

						musicadeprueva.stop()

					except:
						pass

					if vent_act == "Pantalla":
						ajuste_act = "PantComp"

					elif vent_act == "Sonido":
						ajuste_act = "VolEffect"
						voleffectact = vol_efectos_a_actualizar

					elif vent_act == "Animaciones":
						ajuste_act = "Scroll"

					print("Boton 5 pulsado, cambiando a ajuste " + ajuste_act)

					ventana.fill(negro)

					txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

					pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

					if user_act[1] != "None":
						bot9 =  crear_boton3(ventana, posx1bot9, posy1bot9, posx2bot9, posy2bot9, "Guardar usuario actual: " + str(guardado), tamañotxtat, round(0.0015625 * ancho), errordebotat + 6, blanco, debug_font, blanco)

					else:
						bot9 = ["", ""]

					todas = set_botones(caracteristicaspolygons, ventana, vent_act)

					txt2, posxytxt2 = todas[0]
						
					txt3, posxytxt3 = todas[1]

					txt4, posxytxt4 = todas[2]

					txt19, posxytxt19 = todas[4]

					todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act, ajuste_act)

					txt5, posxytxt5 = todas[0]

					txt6, posxytxt6 = todas[1]

					txt7, posxytxt7 = todas[2]

					txt18, posxytxt18 = todas[3]

					dts = set_parte_especifica(caracteristicas_especifico, ventana, ajuste_act)

					if dts != None:

						if dts[0] != None: txt10, posxytxt10 = dts[0]

						if dts[1] != None: txt11, posxytxt11 = dts[1]

						if dts[2] != None: txt12, posxytxt12 = dts[2]

						if dts[3] != None: txt13, posxytxt13 = dts[3]

						if dts[4] != None: txt14, posxytxt14 = dts[4]

						if dts[5] != None: txt15, posxytxt15 = dts[5]

						if dts[6] != None: txt16, posxytxt16 = dts[6]

						if dts[7] != None: txt17, posxytxt17 = dts[7]

						if dts[8] != None: txt20, posxytxt20 = dts[8]

						if dts[9] != None: posesxybot2, posesxy2bot2, bot2 = dts[9]

						if dts[10] != None: posesxybot3, posesxy2bot3, bot3 = dts[10]

						if dts[11] != None: posesxybot4, posesxy2bot4, bot4 = dts[11]

						if dts[12] != None: posesxybot5, posesxy2bot5, bot5 = dts[12]

						if dts[13] != None: posesxybot6, posesxy2bot6, bot6 = dts[13]

						if dts[14] != None: txt22, posxytxt22, bot8, posesxybot8 = dts[14]

					bot7_alpha = pygame.image.load("Imagenes/play.png")

					bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

					posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

			elif ratonx > 0 and ratony > posyline7 and ratonx < posxfinishlines and ratony < posyline8:

				if evento.type == MOUSEBUTTONDOWN:

					ajustes = extraer_ajustes()

					vol_musica_a_actualizar = int(ajustes[6])

					try:

						musicadeprueva.stop()

					except:
						pass

					if vent_act == "Pantalla":
						ajuste_act = "Fuente"

					elif vent_act == "Sonido":
						ajuste_act = "VolFondo"
						volmusicact = vol_musica_a_actualizar

					elif vent_act == "Animaciones":
						ajuste_act = "MaxFPS"
						MaxFPSact = int(ajustes[9])

					print("Boton 6 pulsado, cambiando a ajuste " + ajuste_act)

					ventana.fill(negro)

					txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

					pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

					if user_act[1] != "None":
						bot9 =  crear_boton3(ventana, posx1bot9, posy1bot9, posx2bot9, posy2bot9, "Guardar usuario actual: " + str(guardado), tamañotxtat, round(0.0015625 * ancho), errordebotat + 6, blanco, debug_font, blanco)

					else:
						bot9 = ["", ""]

					todas = set_botones(caracteristicaspolygons, ventana, vent_act)

					txt2, posxytxt2 = todas[0]
						
					txt3, posxytxt3 = todas[1]

					txt4, posxytxt4 = todas[2]

					txt19, posxytxt19 = todas[4]

					todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act, ajuste_act)

					txt5, posxytxt5 = todas[0]

					txt6, posxytxt6 = todas[1]

					txt7, posxytxt7 = todas[2]

					txt18, posxytxt18 = todas[3]

					dts = set_parte_especifica(caracteristicas_especifico, ventana, ajuste_act)

					if dts != None:

						if dts[0] != None: txt10, posxytxt10 = dts[0]

						if dts[1] != None: txt11, posxytxt11 = dts[1]

						if dts[2] != None: txt12, posxytxt12 = dts[2]

						if dts[3] != None: txt13, posxytxt13 = dts[3]

						if dts[4] != None: txt14, posxytxt14 = dts[4]

						if dts[5] != None: txt15, posxytxt15 = dts[5]

						if dts[6] != None: txt16, posxytxt16 = dts[6]

						if dts[7] != None: txt17, posxytxt17 = dts[7]

						if dts[8] != None: txt20, posxytxt20 = dts[8]

						if dts[9] != None: posesxybot2, posesxy2bot2, bot2 = dts[9]

						if dts[10] != None: posesxybot3, posesxy2bot3, bot3 = dts[10]

						if dts[11] != None: posesxybot4, posesxy2bot4, bot4 = dts[11]

						if dts[12] != None: posesxybot5, posesxy2bot5, bot5 = dts[12]

						if dts[13] != None: posesxybot6, posesxy2bot6, bot6 = dts[13]

						if dts[14] != None: txt22, posxytxt22, bot8, posesxybot8 = dts[14]

					bot7_alpha = pygame.image.load("Imagenes/play.png")

					bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

					posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

			elif ratonx > 0 and ratony > posyline8 and ratonx < posxfinishlines and ratony < posyline9 and vent_act != "Pantalla":

				if evento.type == MOUSEBUTTONDOWN:

					try:

						musicadeprueva.stop()

					except:
						pass

					if vent_act == "Pantalla":
						ajuste_act = None

					elif vent_act == "Sonido":
						ajuste_act = "AddCancion"

						print("Boton 7 pulsado, cambiando a ajuste " + ajuste_act)

					elif vent_act == "Animaciones":
						ajuste_act = "VSync"

						print("Boton 7 pulsado, cambiando a ajuste " + ajuste_act)

					ventana.fill(negro)

					txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

					pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

					if user_act[1] != "None":
						bot9 =  crear_boton3(ventana, posx1bot9, posy1bot9, posx2bot9, posy2bot9, "Guardar usuario actual: " + str(guardado), tamañotxtat, round(0.0015625 * ancho), errordebotat + 6, blanco, debug_font, blanco)

					else:
						bot9 = ["", ""]

					todas = set_botones(caracteristicaspolygons, ventana, vent_act)

					txt2, posxytxt2 = todas[0]
						
					txt3, posxytxt3 = todas[1]

					txt4, posxytxt4 = todas[2]

					txt19, posxytxt19 = todas[4]

					todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act, ajuste_act)

					txt5, posxytxt5 = todas[0]

					txt6, posxytxt6 = todas[1]

					txt7, posxytxt7 = todas[2]

					txt18, posxytxt18 = todas[3]

					dts = set_parte_especifica(caracteristicas_especifico, ventana, ajuste_act)

					if dts != None:

						if dts[0] != None: txt10, posxytxt10 = dts[0]

						if dts[1] != None: txt11, posxytxt11 = dts[1]

						if dts[2] != None: txt12, posxytxt12 = dts[2]

						if dts[3] != None: txt13, posxytxt13 = dts[3]

						if dts[4] != None: txt14, posxytxt14 = dts[4]

						if dts[5] != None: txt15, posxytxt15 = dts[5]

						if dts[6] != None: txt16, posxytxt16 = dts[6]

						if dts[7] != None: txt17, posxytxt17 = dts[7]

						if dts[8] != None: txt20, posxytxt20 = dts[8]

						if dts[9] != None: posesxybot2, posesxy2bot2, bot2 = dts[9]

						if dts[10] != None: posesxybot3, posesxy2bot3, bot3 = dts[10]

						if dts[11] != None: posesxybot4, posesxy2bot4, bot4 = dts[11]

						if dts[12] != None: posesxybot5, posesxy2bot5, bot5 = dts[12]

						if dts[13] != None: posesxybot6, posesxy2bot6, bot6 = dts[13]

						if dts[14] != None: txt22, posxytxt22, bot8, posesxybot8 = dts[14]

					bot7_alpha = pygame.image.load("Imagenes/play.png")

					bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

					posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

			elif vent_act == "Pantalla":

				if ajuste_act == "TamañoPant":

					if bot2 != "" and ratonx > posesxybot2[0] and ratony > posesxybot2[1] and ratonx < posesxy2bot2[0] and ratony < posesxy2bot2[1]: #Tamaño de pantalla/Anterior

						if evento.type == MOUSEBUTTONDOWN and ancho != 640:

							tamaños = [(640, 360), (800, 450), (960, 540), (1120, 630), (1280, 720), (1440, 810), (1600, 900), (1760, 990), (1920, 1080)]

							ajustes = extraer_ajustes()

							ancho_ext = ajustes[0]
							alto_ext = ajustes[1]
							pantalla_comp_ext = ajustes[2]

							ya = False

							for i in tamaños:

								if str(i[0]) == str(ancho_ext) and str(i[1]) == str(alto_ext):

									try:
										anterior = anterior_beta

									except:
										anterior = i

								anterior_beta = i

							if pantalla_comp_ext == "True":
								try:
									pygame.display.set_mode((int(anterior[0]), int(anterior[1])), pygame.FULLSCREEN)

								except:
									print("Ese tamaño es muy pequeño para tu ordenador")

								else:
									actualizar_dato("ancho", anterior[0])
									actualizar_dato("alto", anterior[1])

							else:
								try:
									pygame.display.set_mode((int(anterior[0]), int(anterior[1])))

								except:
									print("Ese tamaño es muy pequeño para tu ordenador")

								else:
									actualizar_dato("ancho", anterior[0])
									actualizar_dato("alto", anterior[1])

							ventana.fill(negro)

							ajustes = extraer_ajustes()

							ancho = int(ajustes[0])

							alto = int(ajustes[1])

							posxtxt1 = round(0.0078125 * ancho) #Caracteristicas de texto superior
							posytxt1 = round(0.0078125 * alto)
							tamañotxt1 = round(0.03906 * ancho)

							tamañoline = round(0.00190625 * ancho) #Caracteristicas generales de las lineas

							posyline1 = round(0.08333333 * alto) #Caracteristicas de linea 1

							posxline2 = round(0.6265625 * ancho) #Caracteristicas de la linea 2
							posyline2 = round(0.08333333 * alto)

							posxline3 = round(0.6265625 * ancho) #Caracteristicas de la linea 3
							posyline3 = round(0.138888888 * alto)

							posxline4 = round(0.6265625 * ancho) #Caracteristicas de la linea 4
							posyline4 = round(0.41666666 * alto) #300 if y == 720

							posxline5 = round(0.6265625 * ancho) #Caracteristicas de la linea 5
							posyline5 = round(0.4722222 * alto) #340 if y == 720

							posxfinishlines = round(0.6265625 * ancho)

							posyline6 = round(0.2083333 * alto) #150 == 720
							posyline7 = round(0.2638888 * alto) #190 == 720
							posyline8 = round(0.3194444 * alto) #230 == 720
							posyline9 = round(0.375 * alto) # 270 == 720

							bytesperenterline = 100 #For nothing

							posy1polygon = round(0.08333333 * alto) #Caracteristicas de los botones principales
							posy2polygon = round(0.138888888 * alto)
							posx3polygon = round(0.19625 * ancho)
							posy3polygon = round(0.138888888 * alto)
							posx4polygon = round(0.2353125 * ancho)
							posy4polygon = round(0.08333333 * alto)
							tamañopolygon = round(0.00190625 * ancho)
							tamañotxtpolygon = round(0.02734375 * ancho)
							tamañotxtat = round(0.0234375 * ancho)
							posx1botat = round(0.015625 * ancho)
							posy1botat = round(0.9305555 * alto)
							posx2botat = round(0.234375 * ancho)
							posy2botat = round(0.9722222 * alto)
							errordebotat = round(0.00390625 * ancho)
							textoinfox = round(0.25 * ancho)
							textoinfoy = round(0.944444444 * alto)
							tamañotextoinfo = round(0.0140625 * ancho)

							caracteristicaspolygons = [posy1polygon, posy2polygon, posx3polygon, posy3polygon, posx4polygon, posy4polygon, tamañopolygon, tamañotxtpolygon, tamañotxtat, posx1botat, posy1botat, posx2botat, posy2botat, errordebotat, textoinfox, textoinfoy, tamañotextoinfo]

							posxcircle1 = round(0.015625 * ancho) #Caracteristicas de la seleccion de ajustes
							posycircle1 = round(0.180555 * alto)
							posxtxt = round(0.021875 * ancho)
							posytxt = round(0.1625 * alto)
							tamañotxtajustes = round(0.0234375 * ancho)
							ydeinterlineado = round(0.0555555 * alto)

							caracteristicastxtajustes = [posxcircle1, posycircle1, posxtxt, posytxt, tamañotxtajustes, ydeinterlineado]

							#posx1bot1 = 805
							#posy1bot1 = 116
							#posx2bot1 = 1033
							#posy2bot1 = 145
							#tamañobot1 = 30

							posxtxtgen = round(0.63046875 * ancho) #Caracteristicas de las especificaciones de los ajustes
							posytxt1_es = round(0.166666 * alto)
							posytxt2_es = round(0.208333 * alto)
							posytxt3_es = round(0.25 * alto)
							posytxt4_es = round(0.291666 * alto)
							posytxt5_es = round(0.33333333333 * alto)
							posytxt6_es = round(0.375 * alto)
							tamañotxtgen = round(0.015625 * ancho)

							posytxt10 = round(0.48611111 * alto)

							posytxt11 = round(0.52777777 * alto)

							caracteristicas_especifico = [posxtxtgen, posytxt1_es, posytxt2_es, posytxt3_es, posytxt4_es, posytxt5_es, posytxt6_es, tamañotxtgen, posytxt10, posytxt11, tamañopolygon]

							posxtxt8y9 = round(0.671875 * ancho) #Caracteristicas de textos enunciados 1 y 2
							posytxt8 = round(0.09028 * alto)
							posytxt9 = round(0.423611 * alto)

							posx1bot7 = round(0.78125 * ancho) #botones: play/stop # =                 1000
							posy1bot7 = round(0.90277777 * alto)#Ant = (0.944444 * alto) # =           680
							posx2bot7 = round(0.8203125 * ancho) #Ant = round(0.796875 * ancho) # =    1050
							posy2bot7 = round(0.972222 * alto) # =

							posx1txt21 = round(0.44140625 * ancho)
							posy1txt21 = round(0.01111111111111111111111111111111 * alto)

							posx2txt21 = round(0.875 * ancho)
							posy2txt21 = round(0.01111111111111111111111111111111 * alto)

							posx1bot9 = round(0.015625 * ancho)
							posy1bot9 = round(0.423611 * alto)
							posx2bot9 = round(0.29296875 * ancho)
							posy2bot9 = round(0.45833333333333333333333333333333 * alto)

							posxtxt232425 = round(0.296875 * ancho)
							posytxt23 = round(0.40694444444444444444444444444444 * alto)
							posytxt24 = round(0.43472222222222222222222222222222 * alto)
							posytxt25 = round(0.4625 * alto)
							posytxt26 = round(0.47222222222222222222222222222222 * alto)

							txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

							pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

							todas = set_botones(caracteristicaspolygons, ventana, vent_act)

							txt2, posxytxt2 = todas[0]
								
							txt3, posxytxt3 = todas[1]

							txt4, posxytxt4 = todas[2]

							posesxybot1, posesxy2bot1, botonreturn = todas[3]

							txt19, posxytxt19 = todas[4]

							todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act, ajuste_act)

							txt5, posxytxt5 = todas[0]

							txt6, posxytxt6 = todas[1]

							txt7, posxytxt7 = todas[2]

							txt18, posxytxt18 = todas[3]

							txt8, posxytxt8 = print_pantalla("Carcteristicas de ajuste:", posxtxt8y9, posytxt8, tamañotxtpolygon, (255, 255, 255), debug_font)

							txt9, posxytxt9 = print_pantalla("Opciones de ajuste:", posxtxt8y9, posytxt9, tamañotxtpolygon, (255, 255, 255), debug_font)

							if user_act[1] != "None":
								txt26 = print_pantalla("Usuario actual guardado: " + Usuario, posx1bot9, posytxt26, tamañotxtgen, (255, 255, 255), debug_font)
								bot9 =  crear_boton3(ventana, posx1bot9, posy1bot9, posx2bot9, posy2bot9, "Guardar usuario actual: " + str(guardado), tamañotxtat, round(0.0015625 * ancho), errordebotat + 6, blanco, debug_font, blanco)
								txt23 = print_pantalla("Esta funcion sirve para que el usuario actualmente", posxtxt232425, posytxt23, tamañotxtgen, (255, 255, 255), debug_font)
								txt24 = print_pantalla("en uso se quede guardado y la próxima vez que este", posxtxt232425, posytxt24, tamañotxtgen, (255, 255, 255), debug_font)
								txt25 = print_pantalla("juego se abra, aparecera ya logeado.", posxtxt232425, posytxt25, tamañotxtgen, (255, 255, 255), debug_font)

							else:
								txt26 = ["", ""]
								bot9 = ["", ""]
								txt23 = ["", ""]
								txt24 = ["", ""]
								txt25 = ["", ""]

							if user_act[0]:

								txt21, posxytxt21 = print_pantalla("Usuario actual: " + user_act[1], posx1txt21, posy1txt21, tamañotxtpolygon, (255, 255, 255), debug_font)

							else:

								txt21, posxytxt21 = print_pantalla("No logeado", posx2txt21, posy2txt21, tamañotxtpolygon, (255, 255, 255), debug_font)

							dts = set_parte_especifica(caracteristicas_especifico, ventana, ajuste_act)

							if dts != None:

								if dts[0] != None: txt10, posxytxt10 = dts[0]

								if dts[1] != None: txt11, posxytxt11 = dts[1]

								if dts[2] != None: txt12, posxytxt12 = dts[2]

								if dts[3] != None: txt13, posxytxt13 = dts[3]

								if dts[4] != None: txt14, posxytxt14 = dts[4]

								if dts[5] != None: txt15, posxytxt15 = dts[5]

								if dts[6] != None: txt16, posxytxt16 = dts[6]

								if dts[7] != None: txt17, posxytxt17 = dts[7]

								if dts[8] != None: txt20, posxytxt20 = dts[8]

								if dts[9] != None: posesxybot2, posesxy2bot2, bot2 = dts[9]

								if dts[10] != None: posesxybot3, posesxy2bot3, bot3 = dts[10]

								if dts[11] != None: posesxybot4, posesxy2bot4, bot4 = dts[11]

								if dts[12] != None: posesxybot5, posesxy2bot5, bot5 = dts[12]

								if dts[13] != None: posesxybot6, posesxy2bot6, bot6 = dts[13]

								if dts[14] != None: txt22, posxytxt22, bot8, posesxybot8 = dts[14]

							bot7_alpha = pygame.image.load("Imagenes/play.png")

							bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

							posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

					elif bot3 != "" and ratonx > posesxybot3[0] and ratony > posesxybot3[1] and ratonx < posesxy2bot3[0] and ratony < posesxy2bot3[1]: #Tamaño de pantalla/Siguiente

						if evento.type == MOUSEBUTTONDOWN:

							tamaños = [(640, 360), (800, 450), (960, 540), (1120, 630), (1280, 720), (1440, 810), (1600, 900), (1760, 990), (1920, 1080)]

							ajustes = extraer_ajustes()

							ancho_ext = ajustes[0]
							alto_ext = ajustes[1]

							ya = False

							for i in tamaños:

								if ya == True:

									siguientesxy = i

									ya = False

								if str(i[0]) == str(ancho_ext) and str(i[1]) == str(alto_ext):

									ya = True

							if pantalla_comp_ext == "True":
								try:
									pygame.display.set_mode((int(siguientesxy[0]), int(siguientesxy[1])), pygame.FULLSCREEN)

								except:
									print("Ese tamaño es mas grande que tu ordenador")

								else:
									actualizar_dato("ancho", siguientesxy[0])
									actualizar_dato("alto", siguientesxy[1])

							else:
								try:
									pygame.display.set_mode((int(siguientesxy[0]), int(siguientesxy[1])))

								except:
									print("Ese tamaño es mas grande que tu ordenador")

								else:
									actualizar_dato("ancho", siguientesxy[0])
									actualizar_dato("alto", siguientesxy[1])

							ventana.fill(negro)

							ajustes = extraer_ajustes()

							ancho = int(ajustes[0])

							alto = int(ajustes[1])

							posxtxt1 = round(0.0078125 * ancho) #Caracteristicas de texto superior
							posytxt1 = round(0.0078125 * alto)
							tamañotxt1 = round(0.03906 * ancho)

							tamañoline = round(0.00190625 * ancho) #Caracteristicas generales de las lineas

							posyline1 = round(0.08333333 * alto) #Caracteristicas de linea 1

							posxline2 = round(0.6265625 * ancho) #Caracteristicas de la linea 2
							posyline2 = round(0.08333333 * alto)

							posxline3 = round(0.6265625 * ancho) #Caracteristicas de la linea 3
							posyline3 = round(0.138888888 * alto)

							posxline4 = round(0.6265625 * ancho) #Caracteristicas de la linea 4
							posyline4 = round(0.41666666 * alto) #300 if y == 720

							posxline5 = round(0.6265625 * ancho) #Caracteristicas de la linea 5
							posyline5 = round(0.4722222 * alto) #340 if y == 720

							posxfinishlines = round(0.6265625 * ancho)

							posyline6 = round(0.2083333 * alto) #150 == 720
							posyline7 = round(0.2638888 * alto) #190 == 720
							posyline8 = round(0.3194444 * alto) #230 == 720
							posyline9 = round(0.375 * alto) # 270 == 720

							bytesperenterline = 100 #For nothing

							posy1polygon = round(0.08333333 * alto) #Caracteristicas de los botones principales
							posy2polygon = round(0.138888888 * alto)
							posx3polygon = round(0.19625 * ancho)
							posy3polygon = round(0.138888888 * alto)
							posx4polygon = round(0.2353125 * ancho)
							posy4polygon = round(0.08333333 * alto)
							tamañopolygon = round(0.00190625 * ancho)
							tamañotxtpolygon = round(0.02734375 * ancho)
							tamañotxtat = round(0.0234375 * ancho)
							posx1botat = round(0.015625 * ancho)
							posy1botat = round(0.9305555 * alto)
							posx2botat = round(0.234375 * ancho)
							posy2botat = round(0.9722222 * alto)
							errordebotat = round(0.00390625 * ancho)
							textoinfox = round(0.25 * ancho)
							textoinfoy = round(0.944444444 * alto)
							tamañotextoinfo = round(0.0140625 * ancho)

							caracteristicaspolygons = [posy1polygon, posy2polygon, posx3polygon, posy3polygon, posx4polygon, posy4polygon, tamañopolygon, tamañotxtpolygon, tamañotxtat, posx1botat, posy1botat, posx2botat, posy2botat, errordebotat, textoinfox, textoinfoy, tamañotextoinfo]

							posxcircle1 = round(0.015625 * ancho) #Caracteristicas de la seleccion de ajustes
							posycircle1 = round(0.180555 * alto)
							posxtxt = round(0.021875 * ancho)
							posytxt = round(0.1625 * alto)
							tamañotxtajustes = round(0.0234375 * ancho)
							ydeinterlineado = round(0.0555555 * alto)

							caracteristicastxtajustes = [posxcircle1, posycircle1, posxtxt, posytxt, tamañotxtajustes, ydeinterlineado]

							#posx1bot1 = 805
							#posy1bot1 = 116
							#posx2bot1 = 1033
							#posy2bot1 = 145
							#tamañobot1 = 30

							posxtxtgen = round(0.63046875 * ancho) #Caracteristicas de las especificaciones de los ajustes
							posytxt1_es = round(0.166666 * alto)
							posytxt2_es = round(0.208333 * alto)
							posytxt3_es = round(0.25 * alto)
							posytxt4_es = round(0.291666 * alto)
							posytxt5_es = round(0.33333333333 * alto)
							posytxt6_es = round(0.375 * alto)
							tamañotxtgen = round(0.015625 * ancho)

							posytxt10 = round(0.48611111 * alto)

							posytxt11 = round(0.52777777 * alto)

							caracteristicas_especifico = [posxtxtgen, posytxt1_es, posytxt2_es, posytxt3_es, posytxt4_es, posytxt5_es, posytxt6_es, tamañotxtgen, posytxt10, posytxt11, tamañopolygon]

							posxtxt8y9 = round(0.671875 * ancho) #Caracteristicas de textos enunciados 1 y 2
							posytxt8 = round(0.09028 * alto)
							posytxt9 = round(0.423611 * alto)

							posx1bot7 = round(0.78125 * ancho) #botones: play/stop # =                 1000
							posy1bot7 = round(0.90277777 * alto)#Ant = (0.944444 * alto) # =           680
							posx2bot7 = round(0.8203125 * ancho) #Ant = round(0.796875 * ancho) # =    1050
							posy2bot7 = round(0.972222 * alto) # =

							posx1txt21 = round(0.44140625 * ancho)
							posy1txt21 = round(0.01111111111111111111111111111111 * alto)

							posx2txt21 = round(0.875 * ancho)
							posy2txt21 = round(0.01111111111111111111111111111111 * alto)

							posx1bot9 = round(0.015625 * ancho)
							posy1bot9 = round(0.423611 * alto)
							posx2bot9 = round(0.29296875 * ancho)
							posy2bot9 = round(0.45833333333333333333333333333333 * alto)

							posxtxt232425 = round(0.296875 * ancho)
							posytxt23 = round(0.40694444444444444444444444444444 * alto)
							posytxt24 = round(0.43472222222222222222222222222222 * alto)
							posytxt25 = round(0.4625 * alto)
							posytxt26 = round(0.47222222222222222222222222222222 * alto)

							txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

							pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

							todas = set_botones(caracteristicaspolygons, ventana, vent_act)

							txt2, posxytxt2 = todas[0]
								
							txt3, posxytxt3 = todas[1]

							txt4, posxytxt4 = todas[2]

							posesxybot1, posesxy2bot1, botonreturn = todas[3]

							txt19, posxytxt19 = todas[4]

							todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act, ajuste_act)

							txt5, posxytxt5 = todas[0]

							txt6, posxytxt6 = todas[1]

							txt7, posxytxt7 = todas[2]

							txt18, posxytxt18 = todas[3]

							txt8, posxytxt8 = print_pantalla("Carcteristicas de ajuste:", posxtxt8y9, posytxt8, tamañotxtpolygon, (255, 255, 255), debug_font)

							txt9, posxytxt9 = print_pantalla("Opciones de ajuste:", posxtxt8y9, posytxt9, tamañotxtpolygon, (255, 255, 255), debug_font)

							if user_act[1] != "None":
								txt26 = print_pantalla("Usuario actual guardado: " + Usuario, posx1bot9, posytxt26, tamañotxtgen, (255, 255, 255), debug_font)
								bot9 =  crear_boton3(ventana, posx1bot9, posy1bot9, posx2bot9, posy2bot9, "Guardar usuario actual: " + str(guardado), tamañotxtat, round(0.0015625 * ancho), errordebotat + 6, blanco, debug_font, blanco)
								txt23 = print_pantalla("Esta funcion sirve para que el usuario actualmente", posxtxt232425, posytxt23, tamañotxtgen, (255, 255, 255), debug_font)
								txt24 = print_pantalla("en uso se quede guardado y la próxima vez que este", posxtxt232425, posytxt24, tamañotxtgen, (255, 255, 255), debug_font)
								txt25 = print_pantalla("juego se abra, aparecera ya logeado.", posxtxt232425, posytxt25, tamañotxtgen, (255, 255, 255), debug_font)

							else:
								txt26 = ["", ""]
								bot9 = ["", ""]
								txt23 = ["", ""]
								txt24 = ["", ""]
								txt25 = ["", ""]

							if user_act[0]:

								txt21, posxytxt21 = print_pantalla("Usuario actual: " + user_act[1], posx1txt21, posy1txt21, tamañotxtpolygon, (255, 255, 255), debug_font)

							else:

								txt21, posxytxt21 = print_pantalla("No logeado", posx2txt21, posy2txt21, tamañotxtpolygon, (255, 255, 255), debug_font)

							dts = set_parte_especifica(caracteristicas_especifico, ventana, ajuste_act)

							if dts != None:

								if dts[0] != None: txt10, posxytxt10 = dts[0]

								if dts[1] != None: txt11, posxytxt11 = dts[1]

								if dts[2] != None: txt12, posxytxt12 = dts[2]

								if dts[3] != None: txt13, posxytxt13 = dts[3]

								if dts[4] != None: txt14, posxytxt14 = dts[4]

								if dts[5] != None: txt15, posxytxt15 = dts[5]

								if dts[6] != None: txt16, posxytxt16 = dts[6]

								if dts[7] != None: txt17, posxytxt17 = dts[7]

								if dts[8] != None: txt20, posxytxt20 = dts[8]

								if dts[9] != None: posesxybot2, posesxy2bot2, bot2 = dts[9]

								if dts[10] != None: posesxybot3, posesxy2bot3, bot3 = dts[10]

								if dts[11] != None: posesxybot4, posesxy2bot4, bot4 = dts[11]

								if dts[12] != None: posesxybot5, posesxy2bot5, bot5 = dts[12]

								if dts[13] != None: posesxybot6, posesxy2bot6, bot6 = dts[13]

								if dts[14] != None: txt22, posxytxt22, bot8, posesxybot8 = dts[14]

							bot7_alpha = pygame.image.load("Imagenes/play.png")

							bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

							posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

				elif ajuste_act == "PantComp":

					if bot2 != "" and ratonx > posesxybot2[0] and ratony > posesxybot2[1] and ratonx < posesxy2bot2[0] and ratony < posesxy2bot2[1]: #Tamaño de pantalla/Anterior

						if evento.type == MOUSEBUTTONDOWN:

							ajustes = extraer_ajustes()

							pantalla_comp_ext = ajustes[2]

							if pantalla_comp_ext == "True":
								actualizar_dato("pantcomp", "False")
								try:
									pygame.display.set_mode((int(ancho), int(alto)))
								except:
									pass

							else:
								actualizar_dato("pantcomp", "True")
								try:
									pygame.display.set_mode((int(ancho), int(alto)), pygame.FULLSCREEN)
								except:
									pass

							txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

							pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

							todas = set_botones(caracteristicaspolygons, ventana, vent_act)

							txt2, posxytxt2 = todas[0]
								
							txt3, posxytxt3 = todas[1]

							txt4, posxytxt4 = todas[2]

							posesxybot1, posesxy2bot1, botonreturn = todas[3]

							txt19, posxytxt19 = todas[4]

							todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act, ajuste_act)

							txt5, posxytxt5 = todas[0]

							txt6, posxytxt6 = todas[1]

							txt7, posxytxt7 = todas[2]

							txt18, posxytxt18 = todas[3]

							txt8, posxytxt8 = print_pantalla("Carcteristicas de ajuste:", posxtxt8y9, posytxt8, tamañotxtpolygon, (255, 255, 255), debug_font)

							txt9, posxytxt9 = print_pantalla("Opciones de ajuste:", posxtxt8y9, posytxt9, tamañotxtpolygon, (255, 255, 255), debug_font)

							if user_act[1] != "None":
								bot9 =  crear_boton3(ventana, posx1bot9, posy1bot9, posx2bot9, posy2bot9, "Guardar usuario actual: " + str(guardado), tamañotxtat, round(0.0015625 * ancho), errordebotat + 6, blanco, debug_font, blanco)

							else:
								bot9 = ["", ""]

							dts = set_parte_especifica(caracteristicas_especifico, ventana, ajuste_act)

							if dts != None:

								if dts[0] != None: txt10, posxytxt10 = dts[0]

								if dts[1] != None: txt11, posxytxt11 = dts[1]

								if dts[2] != None: txt12, posxytxt12 = dts[2]

								if dts[3] != None: txt13, posxytxt13 = dts[3]

								if dts[4] != None: txt14, posxytxt14 = dts[4]

								if dts[5] != None: txt15, posxytxt15 = dts[5]

								if dts[6] != None: txt16, posxytxt16 = dts[6]

								if dts[7] != None: txt17, posxytxt17 = dts[7]

								if dts[8] != None: txt20, posxytxt20 = dts[8]

								if dts[9] != None: posesxybot2, posesxy2bot2, bot2 = dts[9]

								if dts[10] != None: posesxybot3, posesxy2bot3, bot3 = dts[10]

								if dts[11] != None: posesxybot4, posesxy2bot4, bot4 = dts[11]

								if dts[12] != None: posesxybot5, posesxy2bot5, bot5 = dts[12]

								if dts[13] != None: posesxybot6, posesxy2bot6, bot6 = dts[13]

								if dts[14] != None: txt22, posxytxt22, bot8, posesxybot8 = dts[14]

							bot7_alpha = pygame.image.load("Imagenes/play.png")

							bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

							posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

			elif vent_act == "Sonido":

				if ajuste_act == "VolGen":

					if evento.type == MOUSEBUTTONDOWN:

						if bot7 != "" and ratonx > posesxybot7[0] and ratony > posesxybot7[1] and ratonx < posesxy2bot7[0] and ratony < posesxy2bot7[1]:

							if pause_play == "play":

								bot7_alpha = pygame.image.load("Imagenes/pause.png")

								bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

								posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

								pause_play = "pause"

								try:

									musicadeprueva.stop()

								except:
									pass
								
								musicadeprueva = SoundObj("Musica_prueva")

								musicadeprueva.setVol(volgenact/5)

								musicadeprueva.play()

								musicapulsed = True

							else:

								bot7_alpha = pygame.image.load("Imagenes/play.png")

								bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

								posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

								pause_play = "play"

								musicapulsed = False

								try:

									musicadeprueva.stop()

								except:
									pass

						elif bot4 != "" and ratonx > posesxybot4[0] and ratony > posesxybot4[1] and ratonx < posesxy2bot4[0] and ratony < posesxy2bot4[1]:

							actualizar_dato("Volgen", str(volgenact))

							ventana.fill(negro)

							txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

							pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

							if user_act[1] != "None":
								bot9 =  crear_boton3(ventana, posx1bot9, posy1bot9, posx2bot9, posy2bot9, "Guardar usuario actual: " + str(guardado), tamañotxtat, round(0.0015625 * ancho), errordebotat + 6, blanco, debug_font, blanco)

							else:
								bot9 = ["", ""]

							todas = set_botones(caracteristicaspolygons, ventana, vent_act)

							txt2, posxytxt2 = todas[0]
								
							txt3, posxytxt3 = todas[1]

							txt4, posxytxt4 = todas[2]

							posesxybot1, posesxy2bot1, botonreturn = todas[3]

							txt19, posxytxt19 = todas[4]

							todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act, ajuste_act)

							txt5, posxytxt5 = todas[0]

							txt6, posxytxt6 = todas[1]

							txt7, posxytxt7 = todas[2]

							txt18, posxytxt18 = todas[3]

							txt8, posxytxt8 = print_pantalla("Carcteristicas de ajuste:", posxtxt8y9, posytxt8, tamañotxtpolygon, (255, 255, 255), debug_font)

							txt9, posxytxt9 = print_pantalla("Opciones de ajuste:", posxtxt8y9, posytxt9, tamañotxtpolygon, (255, 255, 255), debug_font)

							dts = set_parte_especifica(caracteristicas_especifico, ventana, ajuste_act)

							if dts != None:

								if dts[0] != None: txt10, posxytxt10 = dts[0]

								if dts[1] != None: txt11, posxytxt11 = dts[1]

								if dts[2] != None: txt12, posxytxt12 = dts[2]

								if dts[3] != None: txt13, posxytxt13 = dts[3]

								if dts[4] != None: txt14, posxytxt14 = dts[4]

								if dts[5] != None: txt15, posxytxt15 = dts[5]

								if dts[6] != None: txt16, posxytxt16 = dts[6]

								if dts[7] != None: txt17, posxytxt17 = dts[7]

								if dts[8] != None: txt20, posxytxt20 = dts[8]

								if dts[9] != None: posesxybot2, posesxy2bot2, bot2 = dts[9]

								if dts[10] != None: posesxybot3, posesxy2bot3, bot3 = dts[10]

								if dts[11] != None: posesxybot4, posesxy2bot4, bot4 = dts[11]

								if dts[12] != None: posesxybot5, posesxy2bot5, bot5 = dts[12]

								if dts[13] != None: posesxybot6, posesxy2bot6, bot6 = dts[13]

								if dts[14] != None: txt22, posxytxt22, bot8, posesxybot8 = dts[14]

							if pause_play == "play":

								bot7_alpha = pygame.image.load("Imagenes/play.png")

								bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

								posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

							else: 

								bot7_alpha = pygame.image.load("Imagenes/pause.png")

								bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

								posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

				elif ajuste_act == "VolEffect":

					if evento.type == MOUSEBUTTONDOWN:

						if bot7 != "" and ratonx > posesxybot7[0] and ratony > posesxybot7[1] and ratonx < posesxy2bot7[0] and ratony < posesxy2bot7[1]:

							if pause_play == "play":

								bot7_alpha = pygame.image.load("Imagenes/pause.png")

								bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

								posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

								pause_play = "pause"

								try:

									musicadeprueva.stop()

								except:
									pass
								
								musicadeprueva = SoundObj("Sonido_prueva")

								musicadeprueva.setVol((voleffectact * volgenact)/500)

								musicadeprueva.play()

								musicapulsed = True

							else:

								bot7_alpha = pygame.image.load("Imagenes/play.png")

								bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

								posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

								pause_play = "play"

								musicapulsed = False

								try:

									musicadeprueva.stop()

								except:
									pass

						elif bot4 != "" and ratonx > posesxybot4[0] and ratony > posesxybot4[1] and ratonx < posesxy2bot4[0] and ratony < posesxy2bot4[1]:

							actualizar_dato("Volefect", str(voleffectact))

							ventana.fill(negro)

							txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

							pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

							if user_act[1] != "None":
								bot9 =  crear_boton3(ventana, posx1bot9, posy1bot9, posx2bot9, posy2bot9, "Guardar usuario actual: " + str(guardado), tamañotxtat, round(0.0015625 * ancho), errordebotat + 6, blanco, debug_font, blanco)

							else:
								bot9 = ["", ""]

							todas = set_botones(caracteristicaspolygons, ventana, vent_act)

							txt2, posxytxt2 = todas[0]
								
							txt3, posxytxt3 = todas[1]

							txt4, posxytxt4 = todas[2]

							posesxybot1, posesxy2bot1, botonreturn = todas[3]

							txt19, posxytxt19 = todas[4]

							todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act, ajuste_act)

							txt5, posxytxt5 = todas[0]

							txt6, posxytxt6 = todas[1]

							txt7, posxytxt7 = todas[2]

							txt18, posxytxt18 = todas[3]

							txt8, posxytxt8 = print_pantalla("Carcteristicas de ajuste:", posxtxt8y9, posytxt8, tamañotxtpolygon, (255, 255, 255), debug_font)

							txt9, posxytxt9 = print_pantalla("Opciones de ajuste:", posxtxt8y9, posytxt9, tamañotxtpolygon, (255, 255, 255), debug_font)

							dts = set_parte_especifica(caracteristicas_especifico, ventana, ajuste_act)

							if dts != None:

								if dts[0] != None: txt10, posxytxt10 = dts[0]

								if dts[1] != None: txt11, posxytxt11 = dts[1]

								if dts[2] != None: txt12, posxytxt12 = dts[2]

								if dts[3] != None: txt13, posxytxt13 = dts[3]

								if dts[4] != None: txt14, posxytxt14 = dts[4]

								if dts[5] != None: txt15, posxytxt15 = dts[5]

								if dts[6] != None: txt16, posxytxt16 = dts[6]

								if dts[7] != None: txt17, posxytxt17 = dts[7]

								if dts[8] != None: txt20, posxytxt20 = dts[8]

								if dts[9] != None: posesxybot2, posesxy2bot2, bot2 = dts[9]

								if dts[10] != None: posesxybot3, posesxy2bot3, bot3 = dts[10]

								if dts[11] != None: posesxybot4, posesxy2bot4, bot4 = dts[11]

								if dts[12] != None: posesxybot5, posesxy2bot5, bot5 = dts[12]

								if dts[13] != None: posesxybot6, posesxy2bot6, bot6 = dts[13]

								if dts[14] != None: txt22, posxytxt22, bot8, posesxybot8 = dts[14]

							if pause_play == "play":

								bot7_alpha = pygame.image.load("Imagenes/play.png")

								bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

								posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

							else: 

								bot7_alpha = pygame.image.load("Imagenes/pause.png")

								bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

								posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

				elif ajuste_act == "VolFondo":

					if evento.type == MOUSEBUTTONDOWN:

						if bot7 != "" and ratonx > posesxybot7[0] and ratony > posesxybot7[1] and ratonx < posesxy2bot7[0] and ratony < posesxy2bot7[1]:

							if pause_play == "play":

								bot7_alpha = pygame.image.load("Imagenes/pause.png")

								bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

								posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

								pause_play = "pause"

								try:

									musicadeprueva.stop()

								except:
									pass
								
								musicadeprueva = SoundObj("Musica_prueva")

								musicadeprueva.setVol((volmusicact * volgenact)/500)

								musicadeprueva.play()

								musicapulsed = True

							else:

								bot7_alpha = pygame.image.load("Imagenes/play.png")

								bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

								posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

								pause_play = "play"

								musicapulsed = False

								try:

									musicadeprueva.stop()

								except:
									pass

						elif bot4 != "" and ratonx > posesxybot4[0] and ratony > posesxybot4[1] and ratonx < posesxy2bot4[0] and ratony < posesxy2bot4[1]:

							actualizar_dato("Volmusic", str(volmusicact))

							ventana.fill(negro)

							txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

							pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

							if user_act[1] != "None":
								bot9 =  crear_boton3(ventana, posx1bot9, posy1bot9, posx2bot9, posy2bot9, "Guardar usuario actual: " + str(guardado), tamañotxtat, round(0.0015625 * ancho), errordebotat + 6, blanco, debug_font, blanco)

							else:
								bot9 = ["", ""]

							todas = set_botones(caracteristicaspolygons, ventana, vent_act)

							txt2, posxytxt2 = todas[0]
								
							txt3, posxytxt3 = todas[1]

							txt4, posxytxt4 = todas[2]

							posesxybot1, posesxy2bot1, botonreturn = todas[3]

							txt19, posxytxt19 = todas[4]

							todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act, ajuste_act)

							txt5, posxytxt5 = todas[0]

							txt6, posxytxt6 = todas[1]

							txt7, posxytxt7 = todas[2]

							txt18, posxytxt18 = todas[3]

							txt8, posxytxt8 = print_pantalla("Carcteristicas de ajuste:", posxtxt8y9, posytxt8, tamañotxtpolygon, (255, 255, 255), debug_font)

							txt9, posxytxt9 = print_pantalla("Opciones de ajuste:", posxtxt8y9, posytxt9, tamañotxtpolygon, (255, 255, 255), debug_font)

							dts = set_parte_especifica(caracteristicas_especifico, ventana, ajuste_act)

							if dts != None:

								if dts[0] != None: txt10, posxytxt10 = dts[0]

								if dts[1] != None: txt11, posxytxt11 = dts[1]

								if dts[2] != None: txt12, posxytxt12 = dts[2]

								if dts[3] != None: txt13, posxytxt13 = dts[3]

								if dts[4] != None: txt14, posxytxt14 = dts[4]

								if dts[5] != None: txt15, posxytxt15 = dts[5]

								if dts[6] != None: txt16, posxytxt16 = dts[6]

								if dts[7] != None: txt17, posxytxt17 = dts[7]

								if dts[8] != None: txt20, posxytxt20 = dts[8]

								if dts[9] != None: posesxybot2, posesxy2bot2, bot2 = dts[9]

								if dts[10] != None: posesxybot3, posesxy2bot3, bot3 = dts[10]

								if dts[11] != None: posesxybot4, posesxy2bot4, bot4 = dts[11]

								if dts[12] != None: posesxybot5, posesxy2bot5, bot5 = dts[12]

								if dts[13] != None: posesxybot6, posesxy2bot6, bot6 = dts[13]

								if dts[14] != None: txt22, posxytxt22, bot8, posesxybot8 = dts[14]

							if pause_play == "play":

								bot7_alpha = pygame.image.load("Imagenes/play.png")

								bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

								posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

							else: 

								bot7_alpha = pygame.image.load("Imagenes/pause.png")

								bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

								posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))
				elif ajuste_act == "AddCancion":

					if evento.type == MOUSEBUTTONDOWN:

						if bot8 != "" and ratonx > posesxybot8[0] and ratony > posesxybot8[1] and ratonx < posesxybot8[2] and ratony < posesxybot8[3]:
							pass

							recint = dibujar_recuadro_introductor(ventana, "Introduce aqui la cancion", (40, 40, 40), debug_font, 16, round(0.6484375 * ancho), 435, 930, 455, True)

							txt22, posxytxt22, bot8, posesxybot8 = recint

							while terminado == False:
								pass

			elif vent_act == "Animaciones":
				if ajuste_act == "Effectyanimations":

					if evento.type == MOUSEBUTTONDOWN:

						if bot2 != "" and ratonx > posesxybot2[0] and ratony > posesxybot2[1] and ratonx < posesxy2bot2[0] and ratony < posesxy2bot2[1]:

							ajustes = extraer_ajustes()

							Effectyanimations = ajustes[7]

							if Effectyanimations == "True":
								actualizar_dato("Effectyanimations", "False")

							else:
								actualizar_dato("Effectyanimations", "True")

							ventana.fill(negro)

							txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

							pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

							if user_act[1] != "None":
								bot9 =  crear_boton3(ventana, posx1bot9, posy1bot9, posx2bot9, posy2bot9, "Guardar usuario actual: " + str(guardado), tamañotxtat, round(0.0015625 * ancho), errordebotat + 6, blanco, debug_font, blanco)

							else:
								bot9 = ["", ""]

							todas = set_botones(caracteristicaspolygons, ventana, vent_act)

							txt2, posxytxt2 = todas[0]
								
							txt3, posxytxt3 = todas[1]

							txt4, posxytxt4 = todas[2]

							posesxybot1, posesxy2bot1, botonreturn = todas[3]

							txt19, posxytxt19 = todas[4]

							todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act, ajuste_act)

							txt5, posxytxt5 = todas[0]

							txt6, posxytxt6 = todas[1]

							txt7, posxytxt7 = todas[2]

							txt18, posxytxt18 = todas[3]

							txt8, posxytxt8 = print_pantalla("Carcteristicas de ajuste:", posxtxt8y9, posytxt8, tamañotxtpolygon, (255, 255, 255), debug_font)

							txt9, posxytxt9 = print_pantalla("Opciones de ajuste:", posxtxt8y9, posytxt9, tamañotxtpolygon, (255, 255, 255), debug_font)

							dts = set_parte_especifica(caracteristicas_especifico, ventana, ajuste_act)

							if dts != None:

								if dts[0] != None: txt10, posxytxt10 = dts[0]

								if dts[1] != None: txt11, posxytxt11 = dts[1]

								if dts[2] != None: txt12, posxytxt12 = dts[2]

								if dts[3] != None: txt13, posxytxt13 = dts[3]

								if dts[4] != None: txt14, posxytxt14 = dts[4]

								if dts[5] != None: txt15, posxytxt15 = dts[5]

								if dts[6] != None: txt16, posxytxt16 = dts[6]

								if dts[7] != None: txt17, posxytxt17 = dts[7]

								if dts[8] != None: txt20, posxytxt20 = dts[8]

								if dts[9] != None: posesxybot2, posesxy2bot2, bot2 = dts[9]

								if dts[10] != None: posesxybot3, posesxy2bot3, bot3 = dts[10]

								if dts[11] != None: posesxybot4, posesxy2bot4, bot4 = dts[11]

								if dts[12] != None: posesxybot5, posesxy2bot5, bot5 = dts[12]

								if dts[13] != None: posesxybot6, posesxy2bot6, bot6 = dts[13]

								if dts[14] != None: txt22, posxytxt22, bot8, posesxybot8 = dts[14]

							bot7_alpha = pygame.image.load("Imagenes/play.png")

							bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

							posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

				elif ajuste_act == "Scroll":

					if evento.type == MOUSEBUTTONDOWN:

						if bot2 != "" and ratonx > posesxybot2[0] and ratony > posesxybot2[1] and ratonx < posesxy2bot2[0] and ratony < posesxy2bot2[1]:

							ajustes = extraer_ajustes()

							Scroll = ajustes[8]

							if Scroll == "True":
								actualizar_dato("Scroll", "False")

							else:
								actualizar_dato("Scroll", "True")

							ventana.fill(negro)

							txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

							pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

							if user_act[1] != "None":
								bot9 =  crear_boton3(ventana, posx1bot9, posy1bot9, posx2bot9, posy2bot9, "Guardar usuario actual: " + str(guardado), tamañotxtat, round(0.0015625 * ancho), errordebotat + 6, blanco, debug_font, blanco)

							else:
								bot9 = ["", ""]

							todas = set_botones(caracteristicaspolygons, ventana, vent_act)

							txt2, posxytxt2 = todas[0]
								
							txt3, posxytxt3 = todas[1]

							txt4, posxytxt4 = todas[2]

							posesxybot1, posesxy2bot1, botonreturn = todas[3]

							txt19, posxytxt19 = todas[4]

							todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act, ajuste_act)

							txt5, posxytxt5 = todas[0]

							txt6, posxytxt6 = todas[1]

							txt7, posxytxt7 = todas[2]

							txt18, posxytxt18 = todas[3]

							txt8, posxytxt8 = print_pantalla("Carcteristicas de ajuste:", posxtxt8y9, posytxt8, tamañotxtpolygon, (255, 255, 255), debug_font)

							txt9, posxytxt9 = print_pantalla("Opciones de ajuste:", posxtxt8y9, posytxt9, tamañotxtpolygon, (255, 255, 255), debug_font)

							dts = set_parte_especifica(caracteristicas_especifico, ventana, ajuste_act)

							if dts != None:

								if dts[0] != None: txt10, posxytxt10 = dts[0]

								if dts[1] != None: txt11, posxytxt11 = dts[1]

								if dts[2] != None: txt12, posxytxt12 = dts[2]

								if dts[3] != None: txt13, posxytxt13 = dts[3]

								if dts[4] != None: txt14, posxytxt14 = dts[4]

								if dts[5] != None: txt15, posxytxt15 = dts[5]

								if dts[6] != None: txt16, posxytxt16 = dts[6]

								if dts[7] != None: txt17, posxytxt17 = dts[7]

								if dts[8] != None: txt20, posxytxt20 = dts[8]

								if dts[9] != None: posesxybot2, posesxy2bot2, bot2 = dts[9]

								if dts[10] != None: posesxybot3, posesxy2bot3, bot3 = dts[10]

								if dts[11] != None: posesxybot4, posesxy2bot4, bot4 = dts[11]

								if dts[12] != None: posesxybot5, posesxy2bot5, bot5 = dts[12]

								if dts[13] != None: posesxybot6, posesxy2bot6, bot6 = dts[13]

								if dts[14] != None: txt22, posxytxt22, bot8, posesxybot8 = dts[14]

							bot7_alpha = pygame.image.load("Imagenes/play.png")

							bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

							posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

				elif ajuste_act == "MaxFPS":

					if evento.type == MOUSEBUTTONDOWN:

						if bot4 != "" and ratonx > posesxybot4[0] and ratony > posesxybot4[1] and ratonx < posesxy2bot4[0] and ratony < posesxy2bot4[1]:

							actualizar_dato("MaxFPS", str(MaxFPSact))

							ventana.fill(negro)

							txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

							pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

							if user_act[1] != "None":
								bot9 =  crear_boton3(ventana, posx1bot9, posy1bot9, posx2bot9, posy2bot9, "Guardar usuario actual: " + str(guardado), tamañotxtat, round(0.0015625 * ancho), errordebotat + 6, blanco, debug_font, blanco)

							else:
								bot9 = ["", ""]

							todas = set_botones(caracteristicaspolygons, ventana, vent_act)

							txt2, posxytxt2 = todas[0]
								
							txt3, posxytxt3 = todas[1]

							txt4, posxytxt4 = todas[2]

							posesxybot1, posesxy2bot1, botonreturn = todas[3]

							txt19, posxytxt19 = todas[4]

							todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act, ajuste_act)

							txt5, posxytxt5 = todas[0]

							txt6, posxytxt6 = todas[1]

							txt7, posxytxt7 = todas[2]

							txt18, posxytxt18 = todas[3]

							txt8, posxytxt8 = print_pantalla("Carcteristicas de ajuste:", posxtxt8y9, posytxt8, tamañotxtpolygon, (255, 255, 255), debug_font)

							txt9, posxytxt9 = print_pantalla("Opciones de ajuste:", posxtxt8y9, posytxt9, tamañotxtpolygon, (255, 255, 255), debug_font)

							dts = set_parte_especifica(caracteristicas_especifico, ventana, ajuste_act)

							if dts != None:

								if dts[0] != None: txt10, posxytxt10 = dts[0]

								if dts[1] != None: txt11, posxytxt11 = dts[1]

								if dts[2] != None: txt12, posxytxt12 = dts[2]

								if dts[3] != None: txt13, posxytxt13 = dts[3]

								if dts[4] != None: txt14, posxytxt14 = dts[4]

								if dts[5] != None: txt15, posxytxt15 = dts[5]

								if dts[6] != None: txt16, posxytxt16 = dts[6]

								if dts[7] != None: txt17, posxytxt17 = dts[7]

								if dts[8] != None: txt20, posxytxt20 = dts[8]

								if dts[9] != None: posesxybot2, posesxy2bot2, bot2 = dts[9]

								if dts[10] != None: posesxybot3, posesxy2bot3, bot3 = dts[10]

								if dts[11] != None: posesxybot4, posesxy2bot4, bot4 = dts[11]

								if dts[12] != None: posesxybot5, posesxy2bot5, bot5 = dts[12]

								if dts[13] != None: posesxybot6, posesxy2bot6, bot6 = dts[13]

								if dts[14] != None: txt22, posxytxt22, bot8, posesxybot8 = dts[14]

							bot7_alpha = pygame.image.load("Imagenes/play.png")

							bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

							posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

				elif ajuste_act == "VSync":

					if evento.type == MOUSEBUTTONDOWN:

						if bot2 != "" and ratonx > posesxybot2[0] and ratony > posesxybot2[1] and ratonx < posesxy2bot2[0] and ratony < posesxy2bot2[1]:

							ajustes = extraer_ajustes()

							VSync = ajustes[10]

							if VSync == "True":
								actualizar_dato("VSync", "False")

							else:
								actualizar_dato("VSync", "True")

							ventana.fill(negro)

							txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

							pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

							pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

							if user_act[1] != "None":
								bot9 =  crear_boton3(ventana, posx1bot9, posy1bot9, posx2bot9, posy2bot9, "Guardar usuario actual: " + str(guardado), tamañotxtat, round(0.0015625 * ancho), errordebotat + 6, blanco, debug_font, blanco)

							else:
								bot9 = ["", ""]

							todas = set_botones(caracteristicaspolygons, ventana, vent_act)

							txt2, posxytxt2 = todas[0]
								
							txt3, posxytxt3 = todas[1]

							txt4, posxytxt4 = todas[2]

							posesxybot1, posesxy2bot1, botonreturn = todas[3]

							txt19, posxytxt19 = todas[4]

							todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act, ajuste_act)

							txt5, posxytxt5 = todas[0]

							txt6, posxytxt6 = todas[1]

							txt7, posxytxt7 = todas[2]

							txt18, posxytxt18 = todas[3]

							txt8, posxytxt8 = print_pantalla("Carcteristicas de ajuste:", posxtxt8y9, posytxt8, tamañotxtpolygon, (255, 255, 255), debug_font)

							txt9, posxytxt9 = print_pantalla("Opciones de ajuste:", posxtxt8y9, posytxt9, tamañotxtpolygon, (255, 255, 255), debug_font)

							dts = set_parte_especifica(caracteristicas_especifico, ventana, ajuste_act)

							if dts != None:

								if dts[0] != None: txt10, posxytxt10 = dts[0]

								if dts[1] != None: txt11, posxytxt11 = dts[1]

								if dts[2] != None: txt12, posxytxt12 = dts[2]

								if dts[3] != None: txt13, posxytxt13 = dts[3]

								if dts[4] != None: txt14, posxytxt14 = dts[4]

								if dts[5] != None: txt15, posxytxt15 = dts[5]

								if dts[6] != None: txt16, posxytxt16 = dts[6]

								if dts[7] != None: txt17, posxytxt17 = dts[7]

								if dts[8] != None: txt20, posxytxt20 = dts[8]

								if dts[9] != None: posesxybot2, posesxy2bot2, bot2 = dts[9]

								if dts[10] != None: posesxybot3, posesxy2bot3, bot3 = dts[10]

								if dts[11] != None: posesxybot4, posesxy2bot4, bot4 = dts[11]

								if dts[12] != None: posesxybot5, posesxy2bot5, bot5 = dts[12]

								if dts[13] != None: posesxybot6, posesxy2bot6, bot6 = dts[13]

								if dts[14] != None: txt22, posxytxt22, bot8, posesxybot8 = dts[14]

							bot7_alpha = pygame.image.load("Imagenes/play.png")

							bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

							posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))


			if ratonx > posesxybot1[0] -  errordebotat and ratony > posesxybot1[1] - errordebotat and ratonx < posesxy2bot1[0] and ratony < posesxy2bot1[1]:

				if evento.type == MOUSEBUTTONDOWN:

					print("Boton salida pulsado")

					ajustes = extraer_ajustes()

					pantalla_comp_ext = ajustes[2]

					if pantalla_comp_ext == "False":
						actualizar_dato("pantcomp", "False")
						try:
							pygame.display.set_mode((int(ancho), int(alto)))
						except:
							pass

					else:
						actualizar_dato("pantcomp", "True")
						try:
							pygame.display.set_mode((int(ancho), int(alto)), pygame.FULLSCREEN)
						except:
							pass

					txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

					pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

					todas = set_botones(caracteristicaspolygons, ventana, vent_act)

					txt2, posxytxt2 = todas[0]
								
					txt3, posxytxt3 = todas[1]

					txt4, posxytxt4 = todas[2]

					posesxybot1, posesxy2bot1, botonreturn = todas[3]

					txt19, posxytxt19 = todas[4]

					todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act, ajuste_act)

					txt5, posxytxt5 = todas[0]

					txt6, posxytxt6 = todas[1]

					txt7, posxytxt7 = todas[2]

					txt18, posxytxt18 = todas[3]

					txt8, posxytxt8 = print_pantalla("Carcteristicas de ajuste:", posxtxt8y9, posytxt8, tamañotxtpolygon, (255, 255, 255), debug_font)

					txt9, posxytxt9 = print_pantalla("Opciones de ajuste:", posxtxt8y9, posytxt9, tamañotxtpolygon, (255, 255, 255), debug_font)

					if user_act[1] != "None":
						bot9 =  crear_boton3(ventana, posx1bot9, posy1bot9, posx2bot9, posy2bot9, "Guardar usuario actual: " + str(guardado), tamañotxtat, round(0.0015625 * ancho), errordebotat + 6, blanco, debug_font, blanco)

					else:
						bot9 = ["", ""]

					dts = set_parte_especifica(caracteristicas_especifico, ventana, ajuste_act)

					if dts != None:

						if dts[0] != None: txt10, posxytxt10 = dts[0]

						if dts[1] != None: txt11, posxytxt11 = dts[1]

						if dts[2] != None: txt12, posxytxt12 = dts[2]

						if dts[3] != None: txt13, posxytxt13 = dts[3]

						if dts[4] != None: txt14, posxytxt14 = dts[4]

						if dts[5] != None: txt15, posxytxt15 = dts[5]

						if dts[6] != None: txt16, posxytxt16 = dts[6]

						if dts[7] != None: txt17, posxytxt17 = dts[7]

						if dts[8] != None: txt20, posxytxt20 = dts[8]

						if dts[9] != None: posesxybot2, posesxy2bot2, bot2 = dts[9]

						if dts[10] != None: posesxybot3, posesxy2bot3, bot3 = dts[10]

						if dts[11] != None: posesxybot4, posesxy2bot4, bot4 = dts[11]

						if dts[12] != None: posesxybot5, posesxy2bot5, bot5 = dts[12]

						if dts[13] != None: posesxybot6, posesxy2bot6, bot6 = dts[13]

						if dts[14] != None: txt22, posxytxt22, bot8, posesxybot8 = dts[14]

					bot7_alpha = pygame.image.load("Imagenes/play.png")

					bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

					posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

					time.sleep(0.01)

					Exit_presionado = True

			if ratonx > posx1bot9 -  (errordebotat+6) and ratony > posy1bot9 - (errordebotat+6) and ratonx < posx2bot9 and ratony < posy2bot9:

				if evento.type == MOUSEBUTTONDOWN:

					ajustes = extraer_ajustes()

					Usuario = ajustes[11]

					if Usuario == "None":
						actualizar_dato("Usuario", user_act[1])

						guardado = True

						print("Se ha guardado el usuario")

					else:
						actualizar_dato("Usuario", "None")
						guardado = False

						print("Se ha desguardado el usuario")

					ventana.fill(negro)

					txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

					pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

					ajustes = extraer_ajustes()

					Usuario = ajustes[11]

					if user_act[1] != "None":
						txt26 = print_pantalla("Usuario actual guardado: " + Usuario, posx1bot9, posytxt26, tamañotxtgen, (255, 255, 255), debug_font)
						bot9 =  crear_boton3(ventana, posx1bot9, posy1bot9, posx2bot9, posy2bot9, "Guardar usuario actual: " + str(guardado), tamañotxtat, round(0.0015625 * ancho), errordebotat + 6, blanco, debug_font, blanco)

					else:
						txt26 = ["", ""]
						bot9 = ["", ""]

					todas = set_botones(caracteristicaspolygons, ventana, vent_act)

					txt2, posxytxt2 = todas[0]
								
					txt3, posxytxt3 = todas[1]

					txt4, posxytxt4 = todas[2]

					posesxybot1, posesxy2bot1, botonreturn = todas[3]

					txt19, posxytxt19 = todas[4]

					todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act, ajuste_act)

					txt5, posxytxt5 = todas[0]

					txt6, posxytxt6 = todas[1]

					txt7, posxytxt7 = todas[2]

					txt18, posxytxt18 = todas[3]

					txt8, posxytxt8 = print_pantalla("Carcteristicas de ajuste:", posxtxt8y9, posytxt8, tamañotxtpolygon, (255, 255, 255), debug_font)

					txt9, posxytxt9 = print_pantalla("Opciones de ajuste:", posxtxt8y9, posytxt9, tamañotxtpolygon, (255, 255, 255), debug_font)

					dts = set_parte_especifica(caracteristicas_especifico, ventana, ajuste_act)

					if dts != None:

						if dts[0] != None: txt10, posxytxt10 = dts[0]

						if dts[1] != None: txt11, posxytxt11 = dts[1]

						if dts[2] != None: txt12, posxytxt12 = dts[2]

						if dts[3] != None: txt13, posxytxt13 = dts[3]

						if dts[4] != None: txt14, posxytxt14 = dts[4]

						if dts[5] != None: txt15, posxytxt15 = dts[5]

						if dts[6] != None: txt16, posxytxt16 = dts[6]

						if dts[7] != None: txt17, posxytxt17 = dts[7]

						if dts[8] != None: txt20, posxytxt20 = dts[8]

						if dts[9] != None: posesxybot2, posesxy2bot2, bot2 = dts[9]

						if dts[10] != None: posesxybot3, posesxy2bot3, bot3 = dts[10]

						if dts[11] != None: posesxybot4, posesxy2bot4, bot4 = dts[11]

						if dts[12] != None: posesxybot5, posesxy2bot5, bot5 = dts[12]

						if dts[13] != None: posesxybot6, posesxy2bot6, bot6 = dts[13]

						if dts[14] != None: txt22, posxytxt22, bot8, posesxybot8 = dts[14]

					bot7_alpha = pygame.image.load("Imagenes/play.png")

					bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

					posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

			ventana.blit(txt1, posxytxt1)
			ventana.blit(txt2, posxytxt2)
			ventana.blit(txt3, posxytxt3)
			ventana.blit(txt4, posxytxt4)
			ventana.blit(txt5, posxytxt5)
			ventana.blit(txt6, posxytxt6)
			ventana.blit(txt7, posxytxt7)
			ventana.blit(txt8, posxytxt8)
			ventana.blit(txt9, posxytxt9)
			if txt10 != None: ventana.blit(txt10, posxytxt10)
			if txt11 != None: ventana.blit(txt11, posxytxt11)
			if txt12 != None: ventana.blit(txt12, posxytxt12)
			if txt13 != None: ventana.blit(txt13, posxytxt13)
			if txt14 != None: ventana.blit(txt14, posxytxt14)
			if txt15 != None: ventana.blit(txt15, posxytxt15)
			if txt16 != None: ventana.blit(txt16, posxytxt16)
			if txt17 != None: ventana.blit(txt17, posxytxt17)
			ventana.blit(txt18, posxytxt18)
			ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
			ventana.blit(txt19, posxytxt19)
			if txt20 != "": ventana.blit(txt20, posxytxt20)
			if bot2 != "": ventana.blit(bot2, (posesxybot2[0], posesxybot2[1]))
			if bot3 != "": ventana.blit(bot3, (posesxybot3[0], posesxybot3[1]))
			if bot4 != "": ventana.blit(bot4, (posesxybot4[0], posesxybot4[1]))
			if bot5 != "": ventana.blit(bot5, (posesxybot5[0], posesxybot5[1]))
			if bot5 != "": ventana.blit(bot5, (posesxybot5[0], posesxybot5[1]))
			if bot6 != "": ventana.blit(bot6, (posesxybot6[0], posesxybot6[1]))
			if bot7 != ["", ""] and vent_act == "Sonido" and ajuste_act != "AddCancion" and ajuste_act != None: ventana.blit(bot7, (posesxybot7[0], posesxybot7[1]))
			if bot9[0] != "": ventana.blit(bot9[0], (posx1bot9, posy1bot9))
			ventana.blit(txt21, posxytxt21)
			if txt22 != "": ventana.blit(txt22, posxytxt22)
			if txt23[0] != "": ventana.blit(txt23[0], (posxtxt232425, posytxt23))
			if txt24[0] != "": ventana.blit(txt24[0], (posxtxt232425, posytxt24))
			if txt25[0] != "": ventana.blit(txt25[0], (posxtxt232425, posytxt25))
			if txt26[0] != "": ventana.blit(txt26[0], (posx1bot9, posytxt26))
			acabadodepulsar = False
			pygame.display.update()

		if pygame.mixer.get_busy() != True and musicapulsed == True:

			bot7_alpha = pygame.image.load("Imagenes/play.png")

			bot7 = pygame.transform.scale(bot7_alpha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

			posesxybot7, posesxy2bot7 = ((posx1bot7, posy1bot7), (posx2bot7, posy2bot7))

			musicapulsed = False

			pause_play = "play"

			ventana.blit(bot7, (posesxybot7[0], posesxybot7[1]))

			pygame.display.update()

		if ultimoevento == MOUSEBUTTONDOWN and vent_act == "Sonido" or vent_act == "Animaciones" and ultimoevento == MOUSEBUTTONDOWN:

			if ajuste_act == "VolGen":

				if bot2 != "" and ratonx > posesxybot2[0] and ratony > posesxybot2[1] and ratonx < posesxy2bot2[0] and ratony < posesxy2bot2[1]: #Volumen General/-

					if volgenact > 0:

						volgenant = volgenact

						if shiftpressed == True and volgenact > 9:

							volgenact = volgenact - 10

						else:

							volgenact = volgenact - 1

						txt20, posxytxt20 = print_pantalla(str(volgenant) + "%", round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), negro, debug_font)

						ventana.blit(txt20, posxytxt20)

						pygame.display.update()

						txt20, posxytxt20 = print_pantalla(str(volgenact) + "%", round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), blanco, debug_font)

						ventana.blit(txt20, posxytxt20)

						pygame.display.update()

						time.sleep(0.08)

				elif bot3 != "" and ratonx > posesxybot3[0] and ratony > posesxybot3[1] and ratonx < posesxy2bot3[0] and ratony < posesxy2bot3[1]: #Volumen General/+

					if volgenact < 100:

						volgenant = volgenact

						if shiftpressed == True and volgenact < 91:

							volgenact = volgenact + 10

						else:

							volgenact = volgenact + 1

						txt20, posxytxt20 = print_pantalla(str(volgenant) + "%", round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), negro, debug_font)

						ventana.blit(txt20, posxytxt20)

						pygame.display.update()

						txt20, posxytxt20 = print_pantalla(str(volgenact) + "%", round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), blanco, debug_font)

						ventana.blit(txt20, posxytxt20)

						pygame.display.update()

						time.sleep(0.08)

			elif ajuste_act == "VolEffect":

				if bot2 != "" and ratonx > posesxybot2[0] and ratony > posesxybot2[1] and ratonx < posesxy2bot2[0] and ratony < posesxy2bot2[1]: #Volumen Effectos/-

					if voleffectact > 0:

						voleffectant = voleffectact

						if shiftpressed == True and voleffectact > 9:

							voleffectact = voleffectact - 10

						else:

							voleffectact = voleffectact - 1

						txt20, posxytxt20 = print_pantalla(str(voleffectant) + "%", round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), negro, debug_font)

						ventana.blit(txt20, posxytxt20)

						pygame.display.update()

						txt20, posxytxt20 = print_pantalla(str(voleffectact) + "%", round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), blanco, debug_font)

						ventana.blit(txt20, posxytxt20)

						pygame.display.update()

						time.sleep(0.08)

				elif bot3 != "" and ratonx > posesxybot3[0] and ratony > posesxybot3[1] and ratonx < posesxy2bot3[0] and ratony < posesxy2bot3[1]: #Volumen Effectos/+

					if voleffectact < 100:

						voleffectant = voleffectact

						if shiftpressed == True and voleffectact < 91:

							voleffectact = voleffectact + 10

						else:

							voleffectact = voleffectact + 1

						txt20, posxytxt20 = print_pantalla(str(voleffectant) + "%", round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), negro, debug_font)

						ventana.blit(txt20, posxytxt20)

						pygame.display.update()

						txt20, posxytxt20 = print_pantalla(str(voleffectact) + "%", round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), blanco, debug_font)

						ventana.blit(txt20, posxytxt20)

						pygame.display.update()

						time.sleep(0.08)

			elif ajuste_act == "VolFondo":

				if bot2 != "" and ratonx > posesxybot2[0] and ratony > posesxybot2[1] and ratonx < posesxy2bot2[0] and ratony < posesxy2bot2[1]:

					if volmusicact > 0:

						volmusicant = volmusicact

						if shiftpressed == True and volmusicact > 9:

							volmusicact = volmusicact - 10

						else:

							volmusicact = volmusicact - 1

						txt20, posxytxt20 = print_pantalla(str(volmusicant) + "%", round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), negro, debug_font)

						ventana.blit(txt20, posxytxt20)

						pygame.display.update()

						txt20, posxytxt20 = print_pantalla(str(volmusicact) + "%", round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), blanco, debug_font)

						ventana.blit(txt20, posxytxt20)

						pygame.display.update()

						time.sleep(0.08)

				elif bot3 != "" and ratonx > posesxybot3[0] and ratony > posesxybot3[1] and ratonx < posesxy2bot3[0] and ratony < posesxy2bot3[1]:

					if volmusicact < 100:

						volmusicant = volmusicact

						if shiftpressed == True and volmusicact < 91:

							volmusicact = volmusicact + 10

						else:

							volmusicact = volmusicact + 1

						txt20, posxytxt20 = print_pantalla(str(volmusicant) + "%", round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), negro, debug_font)

						ventana.blit(txt20, posxytxt20)

						pygame.display.update()

						txt20, posxytxt20 = print_pantalla(str(volmusicact) + "%", round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), blanco, debug_font)

						ventana.blit(txt20, posxytxt20)

						pygame.display.update()

						time.sleep(0.08)

			elif ajuste_act == "MaxFPS":

				if bot2 != "" and ratonx > posesxybot2[0] and ratony > posesxybot2[1] and ratonx < posesxy2bot2[0] and ratony < posesxy2bot2[1]:

					if MaxFPSact > 40:

						MaxFPSant = MaxFPSact

						if shiftpressed == True and MaxFPSact > 49:

							MaxFPSact = MaxFPSact - 10

						else:

							MaxFPSact = MaxFPSact - 1

						if MaxFPSant > 500:

							txt20, posxytxt20 = print_pantalla("Infinitos", round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), negro, debug_font)

						else:

							txt20, posxytxt20 = print_pantalla("FPS: " + str(MaxFPSant), round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), negro, debug_font)

						ventana.blit(txt20, posxytxt20)

						pygame.display.update()

						if MaxFPSact > 500:

							txt20, posxytxt20 = print_pantalla("Infinitos", round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), blanco, debug_font)

						else:

							txt20, posxytxt20 = print_pantalla("FPS: " + str(MaxFPSact), round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), blanco, debug_font)

						ventana.blit(txt20, posxytxt20)

						pygame.display.update()

						time.sleep(0.08)

				elif bot3 != "" and ratonx > posesxybot3[0] and ratony > posesxybot3[1] and ratonx < posesxy2bot3[0] and ratony < posesxy2bot3[1]:

					if MaxFPSact < 502:

						MaxFPSant = MaxFPSact

						if MaxFPSant > 500:

							txt20, posxytxt20 = print_pantalla("Infinitos", round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), negro, debug_font)

						else:

							if shiftpressed == True and MaxFPSact < 491:

								MaxFPSact = MaxFPSact + 10

							else:

								MaxFPSact = MaxFPSact + 1

							txt20, posxytxt20 = print_pantalla("FPS: " + str(MaxFPSant), round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), negro, debug_font)

						ventana.blit(txt20, posxytxt20)

						pygame.display.update()

						if MaxFPSact > 500:

							txt20, posxytxt20 = print_pantalla("Infinitos", round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), blanco, debug_font)

						else:

							txt20, posxytxt20 = print_pantalla("FPS: " + str(MaxFPSact), round(0.669 * ancho), round(0.6041666 * alto), round(0.01875 * ancho), blanco, debug_font)

						ventana.blit(txt20, posxytxt20)

						pygame.display.update()

						time.sleep(0.08)