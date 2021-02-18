import pygame

import sys

import sqlite3

import os

import time

from Modulos.objetos_de_pantalla import *

from Modulos.basededatosajustesfaciliter import *

def generarpantallacontroles(ventana):

	ajustes = extraer_ajustes()

	ancho = int(ajustes[0])
	alto = int(ajustes[1])
	fuente = ajustes[3]

	blanco = (255, 255, 255)
	negro = (0, 0, 0)
	rojo = (255, 0, 0)
	amarillo = (255, 255, 0)
	azul = (0, 0, 255)
	gris_fondo = (90, 90, 90)
	verde = (0, 255, 0)

	colortxt = blanco
	colorline = blanco

	controles = ["Pantalla completa: F11*", "Quitar pantalla completa: ESC*", "Cerrar juego: F4", "Fijar pantalla a tamaño predefinido(1280x720): F1", "Mover la nave: Flechas de dirección o WASD", "Pausar juego: P", "Ver los FPS: F", "Disparar: Espacio", "Disparar por atras: Q (Solo a partir del nivel 12)"]

	tamañoline = round(0.00234375 * ancho) #======= INICIO DEFINICION DE TAMAÑOS ======
	tamañotxt1 = round(0.03906 * ancho)
	tamañopolygon = round(0.00190625 * ancho)
	tamañotxt2 = 25 
	tamañotxt3 = round(0.0234375 * ancho)#======= FINAL DEFINICION DE TAMAÑOS ======

	posxcircle1 = 20
	posycircle1 = 80

	sumandocircle = 50

	posx1botat = round(0.015625 * ancho)
	posy1botat = round(0.9305555 * alto)
	posx2botat = round(0.234375 * ancho)
	posy2botat = round(0.9722222 * alto)

	errordebotgeneral = round(0.00390625 * ancho)

	#========== GENERACION DE PANTALLAS ==========

	pygame.draw.line(ventana, colorline, (0, tamañotxt1), (ancho, tamañotxt1), tamañoline)

	x = 0

	for i in controles:

		pygame.draw.circle(ventana, blanco, (posxcircle1, posycircle1 + sumandocircle*x), round(0.00490625 * ancho))

		txt2, posxytxt2 = print_pantalla(str(i), posxcircle1 + 20, posycircle1 + sumandocircle*x - 11, tamañotxt2, colortxt, fuente)
		ventana.blit(txt2, (posxytxt2[0], posxytxt2[1]))
		pygame.display.update()
		x +=1

	txt1, posxytxt1 = print_pantalla("Controles: ", 0, 0, tamañotxt1, colortxt, fuente)
	bot1 = crear_boton3(ventana, posx1botat, posy1botat, posx2botat, posy2botat, "<-- Pantalla anterior", tamañotxt3, tamañopolygon, errordebotgeneral, blanco, fuente, blanco)
	posesxybot1, posesxy2bot1 = bot1[1]

	if txt1 != ["", ""]: ventana.blit(txt1, (posxytxt1[0], posxytxt1[1]))
	ventana.blit(bot1[0], (posesxybot1[0], posesxybot1[1]))

	pygame.display.update()

	Exit_presionado = False

	while Exit_presionado == False:

		for evento in pygame.event.get():
			ratonx, ratony = pygame.mouse.get_pos()

			if evento.type == QUIT:
				print("Juego terminado")
				Exit_presionado = True
				pygame.quit()
				raise KeyError

			elif evento.type == KEYDOWN:

				if evento.key == 285:
					print("Juego terminado")
					Exit_presionado = True
					pygame.quit()
					raise KeyError

			elif bot1 != ["", ""] and ratonx > posesxybot1[0] -  errordebotgeneral and ratony > posesxybot1[1] - errordebotgeneral and ratonx < posesxy2bot1[0] and ratony < posesxy2bot1[1]:

				if evento.type == MOUSEBUTTONDOWN:

					Exit_presionado = True