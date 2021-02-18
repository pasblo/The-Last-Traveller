import pygame

import sys

import sqlite3

import os

from Modulos.generador_de_pantalla_ajustes import *

from Modulos.generador_de_recuadro_seleccionLv import *

from pygame.locals import *

def EjecutarSeleccionLv(ventana, user_act):

	ajustes = extraer_ajustes()

	ancho = int(ajustes[0])
	alto = int(ajustes[1])
	pantalla_comp = ajustes[2]
	font = ajustes[3]

	vol_general = ajustes[4]
	vol_efectos = ajustes[5]
	vol_musica = ajustes[6]

	blanco = (255, 255, 255)
	negro = (0, 0, 0)
	gris_fondo = (90, 90, 90)

	tamañoline = 3

	posyline1 = 120
	posyline2 = 600

	posxline3 = 200
	posxline4 = 1080

	posxflecha1 = 100
	posyflecha1 = 360

	posxflecha2 = 1180
	posyflecha2 = 360

	tamañotxt1 = 40

	posytxt2 = 50
	posxtxt3 = 550

	errordebotat = round(0.00390625 * ancho)
	tamañopolygon = round(0.00190625 * ancho)
	posx1botat = round(0.015625 * ancho)
	posy1botat = round(0.9305555 * alto)
	posx2botat = round(0.234375 * ancho)
	posy2botat = round(0.9722222 * alto)
	tamañotxt2 = round(0.0234375 * ancho)

	caracteristicasfondo = [tamañoline, posyline1, posyline2, posxline3, posxline4, tamañotxt1, posytxt2, errordebotat, tamañopolygon, posx1botat, posy1botat, posx2botat, posy2botat, tamañotxt2, posxtxt3]

	ventana.fill(gris_fondo)

	punt_act = obtenerdato("Records", "records", user_act[1], 0)

	def generarfondo(ventana, caracteristicas, user_act, punt_act):

		ajustes = extraer_ajustes()

		print(user_act)
		print(punt_act)

		ancho = int(ajustes[0])
		alto = int(ajustes[1])
		fuente_act = ajustes[3]

		tamañoline = caracteristicas[0]
		posyline1 = caracteristicas[1]
		posyline2 = caracteristicas[2]
		posxline3 = caracteristicas[3]
		posxline4 = caracteristicas[4]
		tamañotxt1 = caracteristicas[5]
		posytxt2 = caracteristicas[6]
		errordebotat = caracteristicas[7]
		tamañopolygon = caracteristicas[8]
		posx1botat = caracteristicas[9]
		posy1botat = caracteristicas[10]
		posx2botat = caracteristicas[11]
		posy2botat = caracteristicas[12]
		tamañotxt2 = caracteristicas[13]
		posxtxt3 = caracteristicas[14]

		pygame.draw.line(ventana, negro, (0, posyline1), (ancho, posyline1), tamañoline)
		pygame.draw.line(ventana, negro, (0, posyline2), (ancho, posyline2), tamañoline)
		pygame.draw.line(ventana, negro, (posxline3, posyline1), (posxline3, posyline2), tamañoline)
		pygame.draw.line(ventana, negro, (posxline4, posyline1), (posxline4, posyline2), tamañoline)

		flecha_derecha = pygame.image.load("Imagenes/flecha_derecha.png")
		flecha_izquierda = pygame.image.load("Imagenes/flecha_izquierda.png")

		if user_act[1] == "None":
			txt1, posxytxt1 = print_pantalla("Jugador actual: None", 0, 0, tamañotxt1, negro, fuente_act)
			txt2, posxytxt2 = print_pantalla("Puntuacion actual: None", 0, posytxt2, tamañotxt1, negro, fuente_act)
			txt3, posxytxt3 = print_pantalla("Esta es la version demo para jugar a todos los", posxtxt3, 0, tamañotxt1, negro, fuente_act)
			txt4, posxytxt4 = print_pantalla("niveles, registrese", posxtxt3, posytxt2, tamañotxt1, negro, fuente_act)

		else:
			txt1, posxytxt1 = print_pantalla("Jugador actual: " + user_act[1], 0, 0, tamañotxt1, negro, fuente_act)
			txt2, posxytxt2 = print_pantalla("Puntuacion actual: " + str(punt_act[1]), 0, posytxt2, tamañotxt1, negro, fuente_act)
			txt3 = None
			posxytxt3 = (None, None)
			txt4 = None
			posxytxt4 = (None, None)

		bot1 = crear_boton3(ventana, posx1botat, posy1botat, posx2botat, posy2botat, "<-- Pantalla anterior", tamañotxt2, tamañopolygon, errordebotat, negro, fuente_act, negro)

		posesxybot1, posesxy2bot1 = bot1[1]

		return(flecha_derecha, flecha_izquierda, (txt1, posxytxt1), (txt2, posxytxt2), (posesxybot1, posesxy2bot1, bot1[0]), (txt3, posxytxt3), (txt4, posxytxt4))

	Exit_presionado = False

	results1 = generarfondo(ventana, caracteristicasfondo, user_act, punt_act)

	flecha_derecha = results1[0]
	flecha_izquierda = results1[1]
	txt1 = (results1[2])[0]
	posxytxt1 = (results1[2])[1]
	txt2 = (results1[3])[0]
	posxytxt2 = (results1[3])[1]
	posesxybot1, posesxy2bot1, botonreturn = results1[4]
	txt3 = (results1[5])[0]
	posxytxt3 = (results1[5])[1]
	txt4 = (results1[6])[0]
	posxytxt4 = (results1[6])[1]

	punto1, punto2, punto3, punto4, punto5, punto6, sumgen = crear_recuadro_seleccionLv(ventana, user_act, 1)

	ventana.blit(flecha_izquierda, (posxflecha1 - 32, posyflecha1 - 32))
	ventana.blit(flecha_derecha, (posxflecha2 - 32, posyflecha2 - 32))
	ventana.blit(txt1, (posxytxt1[0], posxytxt1[1]))
	ventana.blit(txt2, (posxytxt2[0], posxytxt2[1]))
	if txt3 != None: ventana.blit(txt3, (posxytxt3[0], posxytxt3[1]))
	if txt4 != None: ventana.blit(txt4, (posxytxt4[0], posxytxt4[1]))
	ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
	pygame.display.update()

	while Exit_presionado == False:

		for evento in pygame.event.get():
			ratonx, ratony = pygame.mouse.get_pos()

			if evento.type == QUIT:
				print("Juego terminado")
				Exit_presionado = True
				pygame.quit()
				sys.exit()

			elif evento.type == KEYDOWN:

				if evento.key == 285:
					print("Juego terminado")
					Exit_presionado = True
					pygame.quit()
					sys.exit()

			elif ratonx > punto1[0] and ratony > punto1[1] and ratonx < punto1[0] + sumgen and ratony < punto1[1] + sumgen:

				if evento.type == MOUSEBUTTONDOWN:
					print(1)

			elif ratonx > punto2[0] and ratony > punto2[1] and ratonx < punto2[0] + sumgen and ratony < punto2[1] + sumgen:

				if evento.type == MOUSEBUTTONDOWN:
					print(2)

			elif ratonx > punto3[0] and ratony > punto3[1] and ratonx < punto3[0] + sumgen and ratony < punto3[1] + sumgen:

				if evento.type == MOUSEBUTTONDOWN:
					print(3)

			elif ratonx > punto4[0] and ratony > punto4[1] and ratonx < punto4[0] + sumgen and ratony < punto4[1] + sumgen:

				if evento.type == MOUSEBUTTONDOWN:
					print(4)

			elif ratonx > punto5[0] and ratony > punto5[1] and ratonx < punto5[0] + sumgen and ratony < punto5[1] + sumgen:

				if evento.type == MOUSEBUTTONDOWN:
					print(5)

			elif ratonx > punto6[0] and ratony > punto6[1] and ratonx < punto6[0] + sumgen and ratony < punto6[1] + sumgen:

				if evento.type == MOUSEBUTTONDOWN:
					print(6)

			elif ratonx > posesxybot1[0] -  errordebotat and ratony > posesxybot1[1] - errordebotat and ratonx < posesxy2bot1[0] and ratony < posesxy2bot1[1]:

				if evento.type == MOUSEBUTTONDOWN:

					Exit_presionado = True