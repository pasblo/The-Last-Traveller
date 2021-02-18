import pygame

import sys

import sqlite3

import os

import time

import math

from Modulos.objetos_de_pantalla import *

from pygame.locals import *

from Modulos.user import *

from Modulos.cifrador import *

from Modulos.sqlite3faciliter import *

from Modulos.sqlite3igualador import *

from Modulos.basededatosajustesfaciliter import *

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

	existe = comprovarexistencia()

	if existe == False:

		datosiniciales = [("ancho", 1280), ("alto", 720), ("pantcomp", "False"), ("fuentegen", "Calibri"), ("Volgen", 10), ("Volefect", 100), ("Volmusic", 100)]

		crearbasededatosajustes(datosiniciales)

	printbasededatos("all", "_data_aj", "ajustes")

	negro = (0, 0, 0)

	blanco = (255, 255, 255)

	rojo = (255, 0, 0)

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
	posyline4 = round(0.41666666 * alto)

	posxline5 = round(0.6265625 * ancho) #Caracteristicas de la linea 5
	posyline5 = round(0.4722222 * alto)

	posxfinishlines = round(0.6265625 * ancho)

	posyline6 = round(0.2083333 * alto)
	posyline7 = round(0.2638888 * alto)
	posyline8 = round(0.3194444 * alto)

	bytesperenterline = 100

	posy1polygon = round(0.08333333 * alto) #Caracteristicas de los botones principales
	posy2polygon = round(0.138888888 * alto)
	posx3polygon = round(0.19625 * ancho)
	posy3polygon = round(0.138888888 * alto)
	posx4polygon = round(0.2353125 * ancho)
	posy4polygon = round(0.08333333 * alto)
	tamañopolygon = round(0.00190625 * ancho)
	tamañotxtpolygon = round(0.02734375 * ancho)

	caracteristicaspolygons = [posy1polygon, posy2polygon, posx3polygon, posy3polygon, posx4polygon, posy4polygon, tamañopolygon, tamañotxtpolygon]

	posxcircle1 = round(0.015625 * ancho)
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

	posytxt10 = 350

	posytxt11 = 380

	caracteristicas_especifico = [posxtxtgen, posytxt1_es, posytxt2_es, posytxt3_es, posytxt4_es, posytxt5_es, posytxt6_es, tamañotxtgen, posytxt10, posytxt11]

	posxtxt8y9 = round(0.671875 * ancho) #Caracteristicas de textos enunciados 1 y 2
	posytxt8 = round(0.09028 * alto)
	posytxt9 = round(0.423611 * alto)

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

		return ((txt2, posxytxt2), (txt3, posxytxt3), (txt4, posxytxt4))

	def set_ajustes(caracteristicas, ventana, vent): #Por terminar

		posxcircle1 = caracteristicas[0]
		posycircle1 = caracteristicas[1]
		posxtxt = caracteristicas[2]
		posytxt = caracteristicas[3]
		tamañotxtajustes = caracteristicas[4]
		ydeinterlineado = caracteristicas[5]

		ajustes = extraer_ajustes()

		ancho_ext = ajustes[0]
		alto_ext = ajustes[1]
		pantalla_comp_ext = ajustes[2]
		font_ext = ajustes[3]

		vol_general = ajustes[4]
		vol_efectos = ajustes[5]
		vol_musica = ajustes[6]

		if vent == "Pantalla":

			pygame.draw.circle(ventana, rojo, (posxcircle1, posycircle1), 5)

			txt5, posxytxt5 = print_pantalla("Tamaño de pantalla: " + str(ancho_ext) + " X " + str(alto_ext), posxtxt, posytxt, tamañotxtajustes, blanco, debug_font)

			pygame.draw.circle(ventana, rojo, (posxcircle1, posycircle1 + ydeinterlineado), 5)

			txt6, posxytxt6 = print_pantalla("Pantalla completa: " + str(pantalla_comp_ext), posxtxt, posytxt + ydeinterlineado, tamañotxtajustes, blanco, debug_font)

			pygame.draw.circle(ventana, rojo, (posxcircle1, posycircle1 + ydeinterlineado * 2), 5)

			txt7, posxytxt7 = print_pantalla("Fuente de letra: " + str(font_ext), posxtxt, posytxt + ydeinterlineado * 2, tamañotxtajustes, blanco, debug_font)


		elif vent == "Sonido":

			pygame.draw.circle(ventana, rojo, (posxcircle1, posycircle1), 5)

			txt5, posxytxt5 = print_pantalla("Volumen general: " + str(vol_general) + "%", posxtxt, posytxt, tamañotxtajustes, blanco, debug_font)

			pygame.draw.circle(ventana, rojo, (posxcircle1, posycircle1 + ydeinterlineado), 5)

			txt6, posxytxt6 = print_pantalla("Volumen efectos de sonido: " + str(vol_efectos) + "%", posxtxt, posytxt + ydeinterlineado, tamañotxtajustes, blanco, debug_font)

			pygame.draw.circle(ventana, rojo, (posxcircle1, posycircle1 + ydeinterlineado * 2), 5)

			txt7, posxytxt7 = print_pantalla("Volumen musica de fondo: " + str(vol_musica) + "%", posxtxt, posytxt + ydeinterlineado * 2, tamañotxtajustes, blanco, debug_font)


		elif vent == "Animaciones":
			pass

		return((txt5, posxytxt5), (txt6, posxytxt6), (txt7, posxytxt7))

	def set_parte_especifica(caracteristicas, ventana, ajuste = None): #Por terminar

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

		if ajuste == None:

			dts1 = print_pantalla("", posxtxtgen, posytxt1, tamañotxtgen, blanco, debug_font)

			dts2 = print_pantalla("", posxtxtgen, posytxt2, tamañotxtgen, blanco, debug_font)

			dts3 = print_pantalla("", posxtxtgen, posytxt3, tamañotxtgen, blanco, debug_font)

			dts4 = print_pantalla("", posxtxtgen, posytxt4, tamañotxtgen, blanco, debug_font)

			dts5 = print_pantalla("", posxtxtgen, posytxt5, tamañotxtgen, blanco, debug_font)

			dts6 = print_pantalla("", posxtxtgen, posytxt6, tamañotxtgen, blanco, debug_font)

			txt_debajo1 = print_pantalla("", posxtxtgen, posytxt10, tamañotxtgen, blanco, debug_font)

			txt_debajo2 = print_pantalla("", posxtxtgen, posytxt11, tamañotxtgen, blanco, debug_font)


		elif ajuste == "TamañoPant":

			dts1 = print_pantalla("Hola1 Hola2 Hola3 Hola4", posxtxtgen, posytxt1, tamañotxtgen, blanco, debug_font)

			dts2 = print_pantalla("Hola5 Hola6 Hola7 Hola8", posxtxtgen, posytxt2, tamañotxtgen, blanco, debug_font)

			dts3 = print_pantalla("Hola9 Hola10 Hola11 Hola12", posxtxtgen, posytxt3, tamañotxtgen, blanco, debug_font)

			dts4 = print_pantalla("Hola13 Hola14 Hola15 Hola16", posxtxtgen, posytxt4, tamañotxtgen, blanco, debug_font)

			dts5 = print_pantalla("Hola17 Hola18 Hola19 Hola20", posxtxtgen, posytxt5, tamañotxtgen, blanco, debug_font)

			dts6 = print_pantalla("Hola21 Hola22 Hola23 Hola24 primero", posxtxtgen, posytxt6, tamañotxtgen, blanco, debug_font)

			txt_debajo1 = print_pantalla("Linea1", posxtxtgen, posytxt10, tamañotxtgen, blanco, debug_font)

			txt_debajo2 = print_pantalla("Linea2", posxtxtgen, posytxt11, tamañotxtgen, blanco, debug_font)

		elif ajuste == "PantComp":

			dts1 = print_pantalla("Hola1 Hola2 Hola3 Hola4", posxtxtgen, posytxt1, tamañotxtgen, blanco, debug_font)

			dts2 = print_pantalla("Hola5 Hola6 Hola7 Hola8", posxtxtgen, posytxt2, tamañotxtgen, blanco, debug_font)

			dts3 = print_pantalla("Hola9 Hola10 Hola11 Hola12", posxtxtgen, posytxt3, tamañotxtgen, blanco, debug_font)

			dts4 = print_pantalla("Hola13 Hola14 Hola15 Hola16", posxtxtgen, posytxt4, tamañotxtgen, blanco, debug_font)

			dts5 = print_pantalla("Hola17 Hola18 Hola19 Hola20", posxtxtgen, posytxt5, tamañotxtgen, blanco, debug_font)

			dts6 = print_pantalla("Hola21 Hola22 Hola23 Hola24 segundo", posxtxtgen, posytxt6, tamañotxtgen, blanco, debug_font)

		elif ajuste == "Fuente":

			dts1 = print_pantalla("Hola1 Hola2 Hola3 Hola4", posxtxtgen, posytxt1, tamañotxtgen, blanco, debug_font)

			dts2 = print_pantalla("Hola5 Hola6 Hola7 Hola8", posxtxtgen, posytxt2, tamañotxtgen, blanco, debug_font)

			dts3 = print_pantalla("Hola9 Hola10 Hola11 Hola12", posxtxtgen, posytxt3, tamañotxtgen, blanco, debug_font)

			dts4 = print_pantalla("Hola13 Hola14 Hola15 Hola16", posxtxtgen, posytxt4, tamañotxtgen, blanco, debug_font)

			dts5 = print_pantalla("Hola17 Hola18 Hola19 Hola20", posxtxtgen, posytxt5, tamañotxtgen, blanco, debug_font)

			dts6 = print_pantalla("Hola21 Hola22 Hola23 Hola24 tercero", posxtxtgen, posytxt6, tamañotxtgen, blanco, debug_font)

		dts = [dts1, dts2, dts3, dts4, dts5, dts6, txt_debajo1, txt_debajo2]

		return dts

	Exit_presionado = False

	sucedio_accion = False

	pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

	pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

	pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

	pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

	pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

	pygame.draw.line(ventana, blanco, (0, posyline6), (posxfinishlines, posyline6), tamañoline)

	pygame.draw.line(ventana, blanco, (0, posyline7), (posxfinishlines, posyline7), tamañoline)

	pygame.draw.line(ventana, blanco, (0, posyline8), (posxfinishlines, posyline8), tamañoline)

	todas = set_botones(caracteristicaspolygons, ventana, debug_vent)

	txt2, posxytxt2 = todas[0]

	txt3, posxytxt3 = todas[1]

	txt4, posxytxt4 = todas[2]

	todas = set_ajustes(caracteristicastxtajustes, ventana, debug_vent)

	txt5, posxytxt5 = todas[0]

	txt6, posxytxt6 = todas[1]

	txt7, posxytxt7 = todas[2]

	txt8, posxytxt8 = print_pantalla("Carcteristicas de ajuste:", posxtxt8y9, posytxt8, tamañotxtpolygon, (255, 255, 255), debug_font)

	txt9, posxytxt9 = print_pantalla("Opciones de ajuste:", posxtxt8y9, posytxt9, tamañotxtpolygon, (255, 255, 255), debug_font)

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

	else: txt8 = None

	while Exit_presionado == False:

		sucedio_accion = False

		for evento in pygame.event.get():

			sucedio_accion = False

			ratonx, ratony = pygame.mouse.get_pos()

			conjdrect = ratonx - posx3polygon
			conjdrect2 = ratony - posy1polygon

			if evento.type == QUIT:
				print("Juego terminado")
				pygame.quit()
				sys.exit()

			if evento.type == KEYDOWN:

				if evento.key == 285: # F4
					print("Juego terminado")
					pygame.quit()
					sys.exit()

				elif evento.key == 27: # Esc

					pantalla_comp = False

					pygame.display.set_mode((ancho, alto))

					actualizar_dato("pantcomp", pantalla_comp)

					pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline6), (posxfinishlines, posyline6), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline7), (posxfinishlines, posyline7), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline8), (posxfinishlines, posyline8), tamañoline)

					todas = set_botones(caracteristicaspolygons, ventana, vent_act)

					txt2, posxytxt2 = todas[0]

					txt3, posxytxt3 = todas[1]

					txt4, posxytxt4 = todas[2]

					todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act)

					txt5, posxytxt5 = todas[0]

					txt6, posxytxt6 = todas[1]

					txt7, posxytxt7 = todas[2]

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

				elif evento.key == 292: # F11

					pantalla_comp = True

					pygame.display.set_mode((ancho, alto), pygame.FULLSCREEN)

					actualizar_dato("pantcomp", pantalla_comp)

					pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline6), (posxfinishlines, posyline6), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline7), (posxfinishlines, posyline7), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline8), (posxfinishlines, posyline8), tamañoline)

					todas = set_botones(caracteristicaspolygons, ventana, vent_act)

					txt2, posxytxt2 = todas[0]

					txt3, posxytxt3 = todas[1]

					txt4, posxytxt4 = todas[2]

					todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act)

					txt5, posxytxt5 = todas[0]

					txt6, posxytxt6 = todas[1]

					txt7, posxytxt7 = todas[2]

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

			if ratonx > 0 and ratony > posy1polygon and (ratony - posy1polygon)*(ratonx - posx3polygon) < 550 and ratony < posy2polygon and ratonx < posx4polygon:

				if evento.type == MOUSEBUTTONDOWN:

					vent_act = "Pantalla"

					print("Boton 1 pulsado, cambiando a ajustes de la pantalla")

					ventana.fill(negro)

					txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

					pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline6), (posxfinishlines, posyline6), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline7), (posxfinishlines, posyline7), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline8), (posxfinishlines, posyline8), tamañoline)

					todas = set_botones(caracteristicaspolygons, ventana, vent_act)

					txt2, posxytxt2 = todas[0]

					txt3, posxytxt3 = todas[1]

					txt4, posxytxt4 = todas[2]

					todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act)

					txt5, posxytxt5 = todas[0]

					txt6, posxytxt6 = todas[1]

					txt7, posxytxt7 = todas[2]

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

			elif ratonx > 0 and ratony > posy1polygon and (ratony - posy1polygon)*(ratonx - posx3polygon * 2) < 550 and ratony < posy2polygon and ratonx < (posx4polygon * 2 - (posx4polygon - posx3polygon)):

				if evento.type == MOUSEBUTTONDOWN:

					vent_act = "Sonido"

					print("Boton 2 pulsado, cambiando a ajustes del sonido")

					ventana.fill(negro)

					txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

					pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline6), (posxfinishlines, posyline6), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline7), (posxfinishlines, posyline7), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline8), (posxfinishlines, posyline8), tamañoline)

					todas = set_botones(caracteristicaspolygons, ventana, vent_act)

					txt2, posxytxt2 = todas[0]

					txt3, posxytxt3 = todas[1]

					txt4, posxytxt4 = todas[2]

					todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act)

					txt5, posxytxt5 = todas[0]

					txt6, posxytxt6 = todas[1]

					txt7, posxytxt7 = todas[2]

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

			elif ratonx > 0 and ratony > posy1polygon and (ratony - posy1polygon)*(ratonx - posx3polygon * 3) < 550 and ratony < posy2polygon and ratonx < (posx4polygon * 3 - (posx4polygon - posx3polygon) * 2):

				if evento.type == MOUSEBUTTONDOWN:

					vent_act = "Animaciones"

					print("Boton 3 pulsado, cambiando a ajustes de las animaciones")

					ventana.fill(negro)

					txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

					pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline6), (posxfinishlines, posyline6), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline7), (posxfinishlines, posyline7), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline8), (posxfinishlines, posyline8), tamañoline)

					todas = set_botones(caracteristicaspolygons, ventana, vent_act)

					txt2, posxytxt2 = todas[0]

					txt3, posxytxt3 = todas[1]

					txt4, posxytxt4 = todas[2]

					todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act)

					txt5, posxytxt5 = todas[0]

					txt6, posxytxt6 = todas[1]

					txt7, posxytxt7 = todas[2]

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

			elif ratonx > 0 and ratony > posy2polygon and ratonx < posxfinishlines and ratony < posyline6:

				if vent_act == "Pantalla":
					ajuste_act = "TamañoPant"

				elif vent_act == "Sonido":
					pass

				elif vent_act == "Animaciones":
					pass

				if evento.type == MOUSEBUTTONDOWN:

					print("Boton 4 pulsado, cambiando a ajuste " + ajuste_act)

					ventana.fill(negro)

					txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

					pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline6), (posxfinishlines, posyline6), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline7), (posxfinishlines, posyline7), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline8), (posxfinishlines, posyline8), tamañoline)

					todas = set_botones(caracteristicaspolygons, ventana, vent_act)

					txt2, posxytxt2 = todas[0]

					txt3, posxytxt3 = todas[1]

					txt4, posxytxt4 = todas[2]

					todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act)

					txt5, posxytxt5 = todas[0]

					txt6, posxytxt6 = todas[1]

					txt7, posxytxt7 = todas[2]

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

			elif ratonx > 0 and ratony > posyline6 and ratonx < posxfinishlines and ratony < posyline7:

				if vent_act == "Pantalla":
					ajuste_act = "PantComp"

				elif vent_act == "Sonido":
					pass

				elif vent_act == "Animaciones":
					pass

				if evento.type == MOUSEBUTTONDOWN:

					print("Boton 4 pulsado, cambiando a ajuste " + ajuste_act)

					ventana.fill(negro)

					txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

					pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline6), (posxfinishlines, posyline6), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline7), (posxfinishlines, posyline7), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline8), (posxfinishlines, posyline8), tamañoline)

					todas = set_botones(caracteristicaspolygons, ventana, vent_act)

					txt2, posxytxt2 = todas[0]

					txt3, posxytxt3 = todas[1]

					txt4, posxytxt4 = todas[2]

					todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act)

					txt5, posxytxt5 = todas[0]

					txt6, posxytxt6 = todas[1]

					txt7, posxytxt7 = todas[2]

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

			elif ratonx > 0 and ratony > posyline7 and ratonx < posxfinishlines and ratony < posyline8:

				if vent_act == "Pantalla":
					ajuste_act = "Fuente"

				elif vent_act == "Sonido":
					pass

				elif vent_act == "Animaciones":
					pass

				if evento.type == MOUSEBUTTONDOWN:

					print("Boton 4 pulsado, cambiando a ajuste " + ajuste_act)

					ventana.fill(negro)

					txt1, posxytxt1 = print_pantalla("Ajustes de " + vent_act + ":", posxtxt1, posytxt1, tamañotxt1, blanco, debug_font)

					pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline2, posyline2), (posxline2, alto), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline3, posyline3), (ancho, posyline3), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline4, posyline4), (ancho, posyline4), tamañoline)

					pygame.draw.line(ventana, blanco, (posxline5, posyline5), (ancho, posyline5), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline6), (posxfinishlines, posyline6), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline7), (posxfinishlines, posyline7), tamañoline)

					pygame.draw.line(ventana, blanco, (0, posyline8), (posxfinishlines, posyline8), tamañoline)

					todas = set_botones(caracteristicaspolygons, ventana, vent_act)

					txt2, posxytxt2 = todas[0]

					txt3, posxytxt3 = todas[1]

					txt4, posxytxt4 = todas[2]

					todas = set_ajustes(caracteristicastxtajustes, ventana, vent_act)

					txt5, posxytxt5 = todas[0]

					txt6, posxytxt6 = todas[1]

					txt7, posxytxt7 = todas[2]

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

			#elif ratonx > posesxybot1[0] and ratony > posesxybot1[1] and ratonx < posesxy2bot1[0] and ratony < posesxy2bot1[1]:

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
			#ventana.blit(botytxt1[0], (posesxybot1[0], posesxybot1[1]))
			pygame.display.update()