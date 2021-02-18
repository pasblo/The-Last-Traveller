import pygame

import sys

import sqlite3

import os

from Modulos.generador_de_pantalla_ajustes import *

from Modulos.generador_de_recuadro_seleccionLv import *

from pygame.locals import *

def EjecutarSeleccionLv(ventana, user_act):

	# ========================================= NIVELES INFINITOS =============================================      MAX CHAR POR LINEA 64

	Lv1Inf_L1 = "Hola Este es el nivel Infinito 1"
	Lv1Inf_L2 = "2"
	Lv1Inf_L3 = "3"
	Lv1Inf_L4 = "4"
	Lv1Inf_L5 = "5"

	lista_textos_Lv1Inf = (Lv1Inf_L1, Lv1Inf_L2, Lv1Inf_L3, Lv1Inf_L4, Lv1Inf_L5) #Nivel Infinito 1

	Lv2Inf_L1 = "Hola Este es el nivel Infinito 2"
	Lv2Inf_L2 = "2"
	Lv2Inf_L3 = "3"
	Lv2Inf_L4 = "4"
	Lv2Inf_L5 = "5"

	lista_textos_Lv2Inf = (Lv2Inf_L1, Lv2Inf_L2, Lv2Inf_L3, Lv2Inf_L4, Lv2Inf_L5) #Nivel Infinito 2

	Lv3Inf_L1 = "Hola Este es el nivel Infinito 3"
	Lv3Inf_L2 = "2"
	Lv3Inf_L3 = "3"
	Lv3Inf_L4 = "4"
	Lv3Inf_L5 = "5"

	lista_textos_Lv3Inf = (Lv3Inf_L1, Lv3Inf_L2, Lv3Inf_L3, Lv3Inf_L4, Lv3Inf_L5) #Nivel Infinito 3

	Lv4Inf_L1 = "Hola Este es el nivel Infinito 4"
	Lv4Inf_L2 = "2"
	Lv4Inf_L3 = "3"
	Lv4Inf_L4 = "4"
	Lv4Inf_L5 = "5"

	lista_textos_Lv4Inf = (Lv4Inf_L1, Lv4Inf_L2, Lv4Inf_L3, Lv4Inf_L4, Lv4Inf_L5) #Nivel Infinito 4

	Lv5Inf_L1 = "Hola Este es el nivel Infinito 5"
	Lv5Inf_L2 = "2"
	Lv5Inf_L3 = "3"
	Lv5Inf_L4 = "4"
	Lv5Inf_L5 = "5"

	lista_textos_Lv5Inf = (Lv5Inf_L1, Lv5Inf_L2, Lv5Inf_L3, Lv5Inf_L4, Lv5Inf_L5) #Nivel Infinito 5

	lista_textos_LvsInfinitos = (lista_textos_Lv1Inf, lista_textos_Lv2Inf, lista_textos_Lv3Inf, lista_textos_Lv4Inf, lista_textos_Lv5Inf)

	# ========================================= NIVELES FINITOS =============================================      MAX CHAR POR LINEA 64

	Lv1_L1 = "Hola Este es el nivel 1"
	Lv1_L2 = "2"
	Lv1_L3 = "3"
	Lv1_L4 = "4"
	Lv1_L5 = "5"

	lista_textos_Lv1 = (Lv1_L1, Lv1_L2, Lv1_L3, Lv1_L4, Lv1_L5) #Nivel 1

	Lv2_L1 = "Hola Este es el nivel 2"
	Lv2_L2 = "2"
	Lv2_L3 = "3"
	Lv2_L4 = "4"
	Lv2_L5 = "5"

	lista_textos_Lv2 = (Lv2_L1, Lv2_L2, Lv2_L3, Lv2_L4, Lv2_L5) #Nivel 2

	Lv3_L1 = "Hola Este es el nivel 3"
	Lv3_L2 = "2"
	Lv3_L3 = "3"
	Lv3_L4 = "4"
	Lv3_L5 = "5"

	lista_textos_Lv3 = (Lv3_L1, Lv3_L2, Lv3_L3, Lv3_L4, Lv3_L5) #Nivel 3

	Lv4_L1 = "Hola Este es el nivel 4"
	Lv4_L2 = "2"
	Lv4_L3 = "3"
	Lv4_L4 = "4"
	Lv4_L5 = "5"

	lista_textos_Lv4 = (Lv4_L1, Lv4_L2, Lv4_L3, Lv4_L4, Lv4_L5) #Nivel 4

	Lv5_L1 = "Hola Este es el nivel 5"
	Lv5_L2 = "2"
	Lv5_L3 = "3"
	Lv5_L4 = "4"
	Lv5_L5 = "5"

	lista_textos_Lv5 = (Lv5_L1, Lv5_L2, Lv5_L3, Lv5_L4, Lv5_L5) #Nivel 5

	Lv6_L1 = "Hola Este es el nivel 6"
	Lv6_L2 = "2"
	Lv6_L3 = "3"
	Lv6_L4 = "4"
	Lv6_L5 = "5"

	lista_textos_Lv6 = (Lv6_L1, Lv6_L2, Lv6_L3, Lv6_L4, Lv6_L5) #Nivel 6

	Lv7_L1 = "Hola Este es el nivel 7"
	Lv7_L2 = "2"
	Lv7_L3 = "3"
	Lv7_L4 = "4"
	Lv7_L5 = "5"

	lista_textos_Lv7 = (Lv7_L1, Lv7_L2, Lv7_L3, Lv7_L4, Lv7_L5) #Nivel 7

	Lv8_L1 = "Hola Este es el nivel 8"
	Lv8_L2 = "2"
	Lv8_L3 = "3"
	Lv8_L4 = "4"
	Lv8_L5 = "5"

	lista_textos_Lv8 = (Lv8_L1, Lv8_L2, Lv8_L3, Lv8_L4, Lv8_L5) #Nivel 8

	Lv9_L1 = "Hola Este es el nivel 9"
	Lv9_L2 = "2"
	Lv9_L3 = "3"
	Lv9_L4 = "4"
	Lv9_L5 = "5"

	lista_textos_Lv9 = (Lv9_L1, Lv9_L2, Lv9_L3, Lv9_L4, Lv9_L5) #Nivel 9

	Lv10_L1 = "Hola Este es el nivel 10"
	Lv10_L2 = "2"
	Lv10_L3 = "3"
	Lv10_L4 = "4"
	Lv10_L5 = "5"

	lista_textos_Lv10 = (Lv10_L1, Lv10_L2, Lv10_L3, Lv10_L4, Lv10_L5) #Nivel 10

	Lv11_L1 = "Hola Este es el nivel 11"
	Lv11_L2 = "2"
	Lv11_L3 = "3"
	Lv11_L4 = "4"
	Lv11_L5 = "5"

	lista_textos_Lv11 = (Lv11_L1, Lv11_L2, Lv11_L3, Lv11_L4, Lv11_L5) #Nivel 11

	Lv12_L1 = "Hola Este es el nivel 12"
	Lv12_L2 = "2"
	Lv12_L3 = "3"
	Lv12_L4 = "4"
	Lv12_L5 = "5"

	lista_textos_Lv12 = (Lv12_L1, Lv12_L2, Lv12_L3, Lv12_L4, Lv12_L5) #Nivel 12

	Lv13_L1 = "Hola Este es el nivel 13"
	Lv13_L2 = "2"
	Lv13_L3 = "3"
	Lv13_L4 = "4"
	Lv13_L5 = "5"

	lista_textos_Lv13 = (Lv13_L1, Lv13_L2, Lv13_L3, Lv13_L4, Lv13_L5) #Nivel 13

	Lv14_L1 = "Hola Este es el nivel 14"
	Lv14_L2 = "2"
	Lv14_L3 = "3"
	Lv14_L4 = "4"
	Lv14_L5 = "5"

	lista_textos_Lv14 = (Lv14_L1, Lv14_L2, Lv14_L3, Lv14_L4, Lv14_L5) #Nivel 14

	Lv15_L1 = "Hola Este es el nivel 15"
	Lv15_L2 = "2"
	Lv15_L3 = "3"
	Lv15_L4 = "4"
	Lv15_L5 = "5"

	lista_textos_Lv15 = (Lv15_L1, Lv15_L2, Lv15_L3, Lv15_L4, Lv15_L5) #Nivel 15

	Lv16_L1 = "Hola Este es el nivel 16"
	Lv16_L2 = "2"
	Lv16_L3 = "3"
	Lv16_L4 = "4"
	Lv16_L5 = "5"

	lista_textos_Lv16 = (Lv16_L1, Lv16_L2, Lv16_L3, Lv16_L4, Lv16_L5) #Nivel 16

	Lv17_L1 = "Hola Este es el nivel 17"
	Lv17_L2 = "2"
	Lv17_L3 = "3"
	Lv17_L4 = "4"
	Lv17_L5 = "5"

	lista_textos_Lv17 = (Lv17_L1, Lv17_L2, Lv17_L3, Lv17_L4, Lv17_L5) #Nivel 17

	Lv18_L1 = "Hola Este es el nivel 18"
	Lv18_L2 = "2"
	Lv18_L3 = "3"
	Lv18_L4 = "4"
	Lv18_L5 = "5"

	lista_textos_Lv18 = (Lv18_L1, Lv18_L2, Lv18_L3, Lv18_L4, Lv18_L5) #Nivel 18

	Lv19_L1 = "Hola Este es el nivel 19"
	Lv19_L2 = "2"
	Lv19_L3 = "3"
	Lv19_L4 = "4"
	Lv19_L5 = "5"

	lista_textos_Lv19 = (Lv19_L1, Lv19_L2, Lv19_L3, Lv19_L4, Lv19_L5) #Nivel 19

	Lv20_L1 = "Hola Este es el nivel 20"
	Lv20_L2 = "2"
	Lv20_L3 = "3"
	Lv20_L4 = "4"
	Lv20_L5 = "5"

	lista_textos_Lv20 = (Lv20_L1, Lv20_L2, Lv20_L3, Lv20_L4, Lv20_L5) #Nivel 20

	Lv21_L1 = "Hola Este es el nivel 21"
	Lv21_L2 = "2"
	Lv21_L3 = "3"
	Lv21_L4 = "4"
	Lv21_L5 = "5"

	lista_textos_Lv21 = (Lv21_L1, Lv21_L2, Lv21_L3, Lv21_L4, Lv21_L5) #Nivel 21

	Lv22_L1 = "Hola Este es el nivel 22"
	Lv22_L2 = "2"
	Lv22_L3 = "3"
	Lv22_L4 = "4"
	Lv22_L5 = "5"

	lista_textos_Lv22 = (Lv22_L1, Lv22_L2, Lv22_L3, Lv22_L4, Lv22_L5) #Nivel 22

	Lv23_L1 = "Hola Este es el nivel 23"
	Lv23_L2 = "2"
	Lv23_L3 = "3"
	Lv23_L4 = "4"
	Lv23_L5 = "5"

	lista_textos_Lv23 = (Lv23_L1, Lv23_L2, Lv23_L3, Lv23_L4, Lv23_L5) #Nivel 23

	Lv24_L1 = "Hola Este es el nivel 24"
	Lv24_L2 = "2"
	Lv24_L3 = "3"
	Lv24_L4 = "4"
	Lv24_L5 = "5"

	lista_textos_Lv24 = (Lv24_L1, Lv24_L2, Lv24_L3, Lv24_L4, Lv24_L5) #Nivel 24

	Lv25_L1 = "Hola Este es el nivel 25"
	Lv25_L2 = "2"
	Lv25_L3 = "3"
	Lv25_L4 = "4"
	Lv25_L5 = "5"

	lista_textos_Lv25 = (Lv25_L1, Lv25_L2, Lv25_L3, Lv25_L4, Lv25_L5) #Nivel 25

	lista_textos = [lista_textos_Lv1, lista_textos_Lv2, lista_textos_Lv3, lista_textos_Lv4, lista_textos_Lv5, lista_textos_Lv6, lista_textos_Lv7, lista_textos_Lv8, lista_textos_Lv9, lista_textos_Lv10, lista_textos_Lv11, lista_textos_Lv12, lista_textos_Lv13, lista_textos_Lv14, lista_textos_Lv15, lista_textos_Lv16, lista_textos_Lv17, lista_textos_Lv18, lista_textos_Lv19, lista_textos_Lv20, lista_textos_Lv21, lista_textos_Lv22, lista_textos_Lv23, lista_textos_Lv24, lista_textos_Lv25]

	ajustes = extraer_ajustes()

	ancho = int(ajustes[0])
	alto = int(ajustes[1])
	pantalla_comp = ajustes[2]
	font = ajustes[3]

	vol_general = ajustes[4]
	vol_efectos = ajustes[5]
	vol_musica = ajustes[6]

	blanco = (255, 255, 255)
	negro = (0, 0, 0) # = sin desbloquear
	rojo = (255, 0, 0) # = siguienteLv a completar	
	amarillo = (255, 255, 0) # = Lv actual
	azul = (0, 0, 255) # = Lv pasado
	gris_fondo = (90, 90, 90)

	tamañoline = 3

	posyline1 = 120
	posyline2 = 600

	posxline3 = 200
	posxline4 = 1080

	posxflecha1 = 100
	posyflecha1 = 360
	posx1flecha1 = posxflecha1 - 32
	posy1flecha1 = posyflecha1 - 32
	posx2flecha1 = posxflecha1 + 32
	posy2flecha1 = posyflecha1 + 32

	posxflecha2 = 1180
	posyflecha2 = 360
	posx1flecha2 = posxflecha2 - 32
	posy1flecha2 = posyflecha2 - 32
	posx2flecha2 = posxflecha2 + 32
	posy2flecha2 = posyflecha2 + 32

	tamañotxt1 = 40

	posytxt2 = 50
	posxtxt3 = 550

	posxtxt5678 = 560
	posytxt5 = 0
	posytxt6 = 30
	posytxt7 = 60
	posytxt8 = 90

	errordebotgeneral = round(0.00390625 * ancho)
	tamañopolygon = round(0.00190625 * ancho)
	posx1botat = round(0.015625 * ancho)
	posy1botat = round(0.9305555 * alto)
	posx2botat = round(0.234375 * ancho)
	posy2botat = round(0.9722222 * alto)
	tamañotxt2 = round(0.0234375 * ancho)

	posx1botaj = round(0.015625 * ancho)
	posy1botaj = round(0.855 * alto)
	posx2botaj = round(0.1041875 * ancho)
	posy2botaj = round(0.89666666667 * alto)

	tamañocirculo = 10
	posxcirclegen = 550
	posycircle1 = 15
	posycircle2 = 45
	posycircle3 = 75
	posycircle4 = 105

	posxtxt91011121314 = 320
	posytxt9 = 603
	posytxt10 = 625
	posytxt11 = 647
	posytxt12 = 669
	posytxt13 = 691

	posxtxt14151617 = 1085
	posytxt14 = 125
	posytxt15 = 150
	posytxt16 = 175
	posytxt17 = 200

	posx1bot5 = 1100
	posy1bot5 = 500
	posx2bot5 = 1255
	posy2bot5 = 533

	#==========No copiar a partir de aqui============
	#Variables de cosas que no sean posiciones o tamaños

	pantalla_act = 1

	punto1 = None
	punto2 = None
	punto3 = None
	punto4 = None
	punto5 = None
	punto6 = None
	sumgen = None

	nivel_act = 11

	caracteristicasfondo = [tamañoline, posyline1, posyline2, posxline3, posxline4, tamañotxt1, posytxt2, errordebotgeneral, tamañopolygon, posx1botat, posy1botat, posx2botat, posy2botat, tamañotxt2, posxtxt3, tamañocirculo, posxcirclegen, posycircle1, posycircle2, posycircle3, posycircle4, posxtxt5678, posytxt5, posytxt6, posytxt7, posytxt8]

	caracteristicas_panelInfo = [posxtxt91011121314, posytxt9, posytxt10, posytxt11, posytxt12, posytxt13, lista_textos, lista_textos_LvsInfinitos, posxtxt14151617, posytxt14, posytxt15, posytxt16, posytxt17]

	navestotales = [15, 20, 30, 25, 30, 36, 50, 58, 62, 56, 72, 75, 77, 80]

	ventana.fill(gris_fondo)

	imagen_fondo_seleccion_pantalla_alpha = pygame.image.load("Imagenes/imagen_fondo_seleccion_pantalla.jpg").convert()

	imagen_fondo_seleccion_pantalla = pygame.transform.scale(imagen_fondo_seleccion_pantalla_alpha, (876, 476))

	punt_act = obtenerdato("Records", "records", user_act[1], 0)

	def generarfondo(ventana, caracteristicas, user_act, punt_act):

		ajustes = extraer_ajustes()

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
		tamañocirculo = caracteristicas[15]
		posxcirclegen = caracteristicas[16]
		posycircle1 = caracteristicas[17]
		posycircle2 = caracteristicas[18]
		posycircle3 = caracteristicas[19]
		posycircle4 = caracteristicas[20]
		posxtxt5678 = caracteristicas[21]
		posytxt5 = caracteristicas[22]
		posxtxt6 = caracteristicas[23]
		posxtxt7 = caracteristicas[24]
		posxtxt8 = caracteristicas[25]

		pygame.draw.line(ventana, negro, (0, posyline1), (ancho, posyline1), tamañoline)
		pygame.draw.line(ventana, negro, (0, posyline2), (ancho, posyline2), tamañoline)
		pygame.draw.line(ventana, negro, (posxline3, posyline1), (posxline3, posyline2), tamañoline)
		pygame.draw.line(ventana, negro, (posxline4, posyline1), (posxline4, posyline2), tamañoline)

		flecha_derecha = pygame.image.load("Imagenes/flecha_derecha.png")
		flecha_izquierda = pygame.image.load("Imagenes/flecha_izquierda.png")

		#bot3 = pygame.transform.scale(flecha_derecha, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))
		#bot4 = pygame.transform.scale(flecha_izquierda, (posx2bot7 - posx1bot7, posy2bot7 - posy1bot7))

		if user_act[1] == "None":
			txt1, posxytxt1 = print_pantalla("Jugador actual: None", 0, 0, tamañotxt1, negro, fuente_act)
			txt2, posxytxt2 = print_pantalla("Puntuacion actual: None", 0, posytxt2, tamañotxt1, negro, fuente_act)
			txt3, posxytxt3 = print_pantalla("Esta es la version demo para jugar a todos los", posxtxt3, 0, tamañotxt1, negro, fuente_act)
			txt4, posxytxt4 = print_pantalla("niveles, registrese", posxtxt3, posytxt2, tamañotxt1, negro, fuente_act)
			txt5 = None
			posxytxt5 = (None, None)
			txt6 = None
			posxytxt6 = (None, None)
			txt7 = None
			posxytxt7 = (None, None)
			txt8 = None
			posxytxt8 = (None, None)

		else:
			txt1, posxytxt1 = print_pantalla("Jugador actual: " + user_act[1], 0, 0, tamañotxt1, negro, fuente_act)
			txt2, posxytxt2 = print_pantalla("Puntuacion actual: " + str(punt_act[1]), 0, posytxt2, tamañotxt1, negro, fuente_act)
			txt3 = None
			posxytxt3 = (None, None)
			txt4 = None
			posxytxt4 = (None, None)
			pygame.draw.circle(ventana, azul, (posxcirclegen, posycircle1), tamañocirculo)
			pygame.draw.circle(ventana, amarillo, (posxcirclegen, posycircle2), tamañocirculo)
			pygame.draw.circle(ventana, rojo, (posxcirclegen, posycircle3), tamañocirculo)
			pygame.draw.circle(ventana, negro, (posxcirclegen, posycircle4), tamañocirculo)
			txt5, posxytxt5 = print_pantalla("--> Nivel completado", posxtxt5678, posytxt5, tamañotxt2, negro, fuente_act)
			txt6, posxytxt6 = print_pantalla("--> Nivel en el que tu personaje se encuentra", posxtxt5678, posytxt6, tamañotxt2, negro, fuente_act)
			txt7, posxytxt7 = print_pantalla("--> Siguiente nivel a completar", posxtxt5678, posytxt7, tamañotxt2, negro, fuente_act)
			txt8, posxytxt8 = print_pantalla("--> Nivel bloqueado", posxtxt5678, posytxt8, tamañotxt2, negro, fuente_act)

		bot1 = crear_boton3(ventana, posx1botat, posy1botat, posx2botat, posy2botat, "<-- Pantalla anterior", tamañotxt2, tamañopolygon, errordebotgeneral, negro, fuente_act, negro)

		bot2 = crear_boton3(ventana, posx1botaj, posy1botaj, posx2botaj, posy2botaj, "AJUSTES", tamañotxt2, tamañopolygon, errordebotgeneral, negro, fuente_act, negro)

		posesxybot1, posesxy2bot1 = bot1[1]

		posesxybot2, posesxy2bot2 = bot2[1]

		return(flecha_derecha, flecha_izquierda, (txt1, posxytxt1), (txt2, posxytxt2), (posesxybot1, posesxy2bot1, bot1[0]), (txt3, posxytxt3), (txt4, posxytxt4), (posesxybot2, posesxy2bot2, bot2[0]), (txt5, posxytxt5), (txt6, posxytxt6), (txt7, posxytxt7), (txt8, posxytxt8))

	def generar_panel_informativo(caracteristicas_panelInfo, Lv_act, pantalla_act, demo, infinito):

		posxtxt91011121314 = caracteristicas_panelInfo[0]
		posytxt9 = caracteristicas_panelInfo[1]
		posytxt10 = caracteristicas_panelInfo[2]
		posytxt11 = caracteristicas_panelInfo[3]
		posytxt12 = caracteristicas_panelInfo[4]
		posytxt13 = caracteristicas_panelInfo[5]
		lista_textos = caracteristicas_panelInfo[6]
		lista_textos_LvsInfinitos = caracteristicas_panelInfo[7]
		posxtxt1415 = caracteristicas_panelInfo[8]
		posytxt14 = caracteristicas_panelInfo[9]
		posytxt15 = caracteristicas_panelInfo[10]
		posytxt16 = caracteristicas_panelInfo[11]
		posytxt17 = caracteristicas_panelInfo[12]

		ajustes = extraer_ajustes()
		
		ancho = int(ajustes[0])
		alto = int(ajustes[1])
		fuente_act = ajustes[3]

		if Lv_act == 4 or Lv_act == 9 or Lv_act == 14 or Lv_act == 19 or Lv_act == 24:
			boss = True

		else:
			boss = False

		if demo == True:
			txt9, posxytxt9 = print_pantalla( "Estas en la version demo para poder jugar todos los niveles", posxtxt91011121314, posytxt9, tamañotxt2, negro, fuente_act) # Max 64 char
			txt10, posxytxt10 = print_pantalla( "tiene que registrarse como usuario. Para ello vaya a ventana", posxtxt91011121314, posytxt10, tamañotxt2, negro, fuente_act) # Max 64 char
			txt11, posxytxt11 = print_pantalla( "principal y pulse al boton LOGEAR/CREAR USUARIO, y siga las", posxtxt91011121314, posytxt11, tamañotxt2, negro, fuente_act) # Max 64 char
			txt12, posxytxt12 = print_pantalla( "instrucciones indicadas", posxtxt91011121314, posytxt12, tamañotxt2, negro, fuente_act) # Max 64 char
			txt13, posxytxt13 = print_pantalla( "", posxtxt91011121314, posytxt13, tamañotxt2, negro, fuente_act) # Max 64 char
			txt14 = ["", ""]
			posxytxt14 = ""
			txt15 = ["", ""]
			posxytxt15 = ""
			txt16 = ["", ""]
			posxytxt16 = ""
			txt17 = ["", ""]
			posxytxt17 = ""

		elif infinito == True:
			txt9, posxytxt9 = print_pantalla((lista_textos_LvsInfinitos[Lv_act])[0], posxtxt91011121314, posytxt9, tamañotxt2, negro, fuente_act) # Max 64 char
			txt10, posxytxt10 = print_pantalla((lista_textos_LvsInfinitos[Lv_act])[1], posxtxt91011121314, posytxt10, tamañotxt2, negro, fuente_act) # Max 64 char
			txt11, posxytxt11 = print_pantalla((lista_textos_LvsInfinitos[Lv_act])[2], posxtxt91011121314, posytxt11, tamañotxt2, negro, fuente_act) # Max 64 char
			txt12, posxytxt12 = print_pantalla((lista_textos_LvsInfinitos[Lv_act])[3], posxtxt91011121314, posytxt12, tamañotxt2, negro, fuente_act) # Max 64 char
			txt13, posxytxt13 = print_pantalla((lista_textos_LvsInfinitos[Lv_act])[4], posxtxt91011121314, posytxt13, tamañotxt2, negro, fuente_act) # Max 64 char
			txt14, posxytxt14 = print_pantalla("Nivel actual: " + str(Lv_act + 1), posxtxt1415, posytxt14, tamañotxt2, negro, fuente_act)
			txt15, posxytxt15 = print_pantalla("Infinito: True", posxtxt14151617, posytxt15, tamañotxt2, negro, fuente_act)
			txt16, posxytxt16 = print_pantalla("Boss: False", posxtxt14151617, posytxt16, tamañotxt2, negro, fuente_act)
			txt17, posxytxt17 = print_pantalla("Nº Naves: ", posxtxt14151617, posytxt17, tamañotxt2, negro, fuente_act)

		else:

			txt9, posxytxt9 = print_pantalla((lista_textos[Lv_act])[0], posxtxt91011121314, posytxt9, tamañotxt2, negro, fuente_act) # Max 64 char
			txt10, posxytxt10 = print_pantalla((lista_textos[Lv_act])[1], posxtxt91011121314, posytxt10, tamañotxt2, negro, fuente_act) # Max 64 char
			txt11, posxytxt11 = print_pantalla((lista_textos[Lv_act])[2], posxtxt91011121314, posytxt11, tamañotxt2, negro, fuente_act) # Max 64 char
			txt12, posxytxt12 = print_pantalla((lista_textos[Lv_act])[3], posxtxt91011121314, posytxt12, tamañotxt2, negro, fuente_act) # Max 64 char
			txt13, posxytxt13 = print_pantalla((lista_textos[Lv_act])[4], posxtxt91011121314, posytxt13, tamañotxt2, negro, fuente_act) # Max 64 char
			txt14, posxytxt14 = print_pantalla("Nivel actual: " + str(Lv_act + 1), posxtxt14151617, posytxt14, tamañotxt2, negro, fuente_act)
			txt15, posxytxt15 = print_pantalla("Infinito: False", posxtxt14151617, posytxt15, tamañotxt2, negro, fuente_act)
			txt16, posxytxt16 = print_pantalla("Boss: " + str(boss), posxtxt14151617, posytxt16, tamañotxt2, negro, fuente_act)
			txt17, posxytxt17 = print_pantalla("Nº Naves: ", posxtxt14151617, posytxt17, tamañotxt2, negro, fuente_act)

		return((txt9, posxytxt9), (txt10, posxytxt10), (txt11, posxytxt11), (txt12, posxytxt12), (txt13, posxytxt13), (txt14, posxytxt14), (txt15, posxytxt15), (txt16, posxytxt16), (txt17, posxytxt17))


	Exit_presionado = False

	results1 = generarfondo(ventana, caracteristicasfondo, user_act, punt_act)

	flecha_derecha = results1[0]
	flecha_izquierda = results1[1]
	txt1, posxytxt1 = results1[2]
	txt2, posxytxt2 = results1[3]
	posesxybot1, posesxy2bot1, botonreturn = results1[4]
	txt3, posxytxt3 = results1[5]
	txt4, posxytxt4 = results1[6]
	posesxybot2, posesxy2bot2, botonreturn2 = results1[7]
	txt5, posxytxt5 = results1[8]
	txt6, posxytxt6 = results1[9]
	txt7, posxytxt7 = results1[10]
	txt8, posxytxt8 = results1[11]

	ventana.blit(imagen_fondo_seleccion_pantalla, (202, 122))

	pygame.display.update()

	punto1, punto2, punto3, punto4, punto5, punto6, sumgen = crear_recuadro_seleccionLv(ventana, nivel_act, pantalla_act)

	ajustes = extraer_ajustes()

	fuente_act = ajustes[3]

	txt9 = ["", ""]
	txt10 = ["", ""]
	txt11 = ["", ""]
	txt12 = ["", ""]
	txt13 = ["", ""]
	txt14, posxytxt14 = print_pantalla("Nivel actual: ", posxtxt14151617, posytxt14, tamañotxt2, negro, fuente_act)
	txt15, posxytxt15 = print_pantalla("Infinito: ", posxtxt14151617, posytxt15, tamañotxt2, negro, fuente_act)
	txt16, posxytxt16 = print_pantalla("Boss: ", posxtxt14151617, posytxt16, tamañotxt2, negro, fuente_act)
	txt17, posxytxt17 = print_pantalla("Nº Naves: ", posxtxt14151617, posytxt17, tamañotxt2, negro, fuente_act)


	ventana.blit(flecha_izquierda, (posx1flecha1, posy1flecha1))
	ventana.blit(flecha_derecha, (posx1flecha2, posy1flecha2))
	ventana.blit(txt1, (posxytxt1[0], posxytxt1[1]))
	ventana.blit(txt2, (posxytxt2[0], posxytxt2[1]))
	if txt3 != None: ventana.blit(txt3, (posxytxt3[0], posxytxt3[1]))
	if txt4 != None: ventana.blit(txt4, (posxytxt4[0], posxytxt4[1]))
	if txt5 != None: ventana.blit(txt5, (posxytxt5[0], posxytxt5[1]))
	if txt6 != None: ventana.blit(txt6, (posxytxt6[0], posxytxt6[1]))
	if txt7 != None: ventana.blit(txt7, (posxytxt7[0], posxytxt7[1]))
	if txt8 != None: ventana.blit(txt8, (posxytxt8[0], posxytxt8[1]))
	if txt9 != ["", ""]: ventana.blit(txt9, (posxytxt9[0], posxytxt9[1]))
	if txt10 != ["", ""]: ventana.blit(txt10, (posxytxt10[0], posxytxt10[1]))
	if txt11 != ["", ""]: ventana.blit(txt11, (posxytxt11[0], posxytxt11[1]))
	if txt12 != ["", ""]: ventana.blit(txt12, (posxytxt12[0], posxytxt12[1]))
	if txt13 != ["", ""]: ventana.blit(txt13, (posxytxt13[0], posxytxt13[1]))
	if txt14 != ["", ""]: ventana.blit(txt14, (posxytxt14[0], posxytxt14[1]))
	if txt15 != ["", ""]: ventana.blit(txt15, (posxytxt15[0], posxytxt15[1]))
	if txt16 != ["", ""]: ventana.blit(txt16, (posxytxt16[0], posxytxt16[1]))
	if txt17 != ["", ""]: ventana.blit(txt17, (posxytxt17[0], posxytxt17[1]))
	ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
	ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))

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

			elif ratonx > punto1[0] - sumgen and ratony > punto1[1] - sumgen and ratonx < punto1[0] + sumgen and ratony < punto1[1] + sumgen:

				if evento.type == MOUSEBUTTONDOWN:
					print("Nivel: " + str(5 * (pantalla_act - 1) + 1))

					output = generar_panel_informativo(caracteristicas_panelInfo, 5 * (pantalla_act - 1), pantalla_act, False, False)

					txt9, posxytxt9 = output[0]
					txt10, posxytxt10 = output[1]
					txt11, posxytxt11 = output[2]
					txt12, posxytxt12 = output[3]
					txt13, posxytxt13 = output[4]
					txt14, posxytxt14 = output[5]
					txt15, posxytxt15 = output[6]
					txt16, posxytxt16 = output[7]
					txt17, posxytxt17 = output[8]

					ventana.fill(gris_fondo)

					if nivel_act < (5 * (pantalla_act - 1)):
						bot5 = ["",""]

					elif nivel_act >= (5 * (pantalla_act - 1)):
						bot5 = crear_boton3(ventana, posx1bot5, posy1bot5, posx2bot5, posy2bot5, "COMENZAR", tamañotxt2, tamañopolygon, errordebotgeneral, negro, fuente_act, negro)
						posesxybot5, posesxy2bot5 = bot5[1]

					results1 = generarfondo(ventana, caracteristicasfondo, user_act, punt_act)

					flecha_derecha = results1[0]
					flecha_izquierda = results1[1]
					txt1, posxytxt1 = results1[2]
					txt2, posxytxt2 = results1[3]
					posesxybot1, posesxy2bot1, botonreturn = results1[4]
					txt3, posxytxt3 = results1[5]
					txt4, posxytxt4 = results1[6]
					posesxybot2, posesxy2bot2, botonreturn2 = results1[7]
					txt5, posxytxt5 = results1[8]
					txt6, posxytxt6 = results1[9]
					txt7, posxytxt7 = results1[10]
					txt8, posxytxt8 = results1[11]

					ventana.blit(imagen_fondo_seleccion_pantalla, (202, 122))

					pygame.display.update()

					punto1, punto2, punto3, punto4, punto5, punto6, sumgen = crear_recuadro_seleccionLv(ventana, nivel_act, pantalla_act)

					ventana.blit(flecha_izquierda, (posx1flecha1, posy1flecha1))
					ventana.blit(flecha_derecha, (posx1flecha2, posy1flecha2))
					ventana.blit(txt1, (posxytxt1[0], posxytxt1[1]))
					ventana.blit(txt2, (posxytxt2[0], posxytxt2[1]))
					if txt3 != None: ventana.blit(txt3, (posxytxt3[0], posxytxt3[1]))
					if txt4 != None: ventana.blit(txt4, (posxytxt4[0], posxytxt4[1]))
					if txt5 != None: ventana.blit(txt5, (posxytxt5[0], posxytxt5[1]))
					if txt6 != None: ventana.blit(txt6, (posxytxt6[0], posxytxt6[1]))
					if txt7 != None: ventana.blit(txt7, (posxytxt7[0], posxytxt7[1]))
					if txt8 != None: ventana.blit(txt8, (posxytxt8[0], posxytxt8[1]))
					if txt9 != None: ventana.blit(txt9, (posxytxt9[0], posxytxt9[1]))
					if txt10 != None: ventana.blit(txt10, (posxytxt10[0], posxytxt10[1]))
					if txt11 != None: ventana.blit(txt11, (posxytxt11[0], posxytxt11[1]))
					if txt12 != None: ventana.blit(txt12, (posxytxt12[0], posxytxt12[1]))
					if txt13 != None: ventana.blit(txt13, (posxytxt13[0], posxytxt13[1]))
					if txt14 != ["", ""]: ventana.blit(txt14, (posxytxt14[0], posxytxt14[1]))
					if txt15 != ["", ""]: ventana.blit(txt15, (posxytxt15[0], posxytxt15[1]))
					if txt16 != ["", ""]: ventana.blit(txt16, (posxytxt16[0], posxytxt16[1]))
					if txt17 != ["", ""]: ventana.blit(txt17, (posxytxt17[0], posxytxt17[1]))
					ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
					ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))
					if bot5 != ["", ""]: ventana.blit(bot5[0], (posesxybot5[0], posesxybot5[1]))

					pygame.display.update()

			elif ratonx > punto2[0] - sumgen and ratony > punto2[1] - sumgen and ratonx < punto2[0] + sumgen and ratony < punto2[1] + sumgen:

				if evento.type == MOUSEBUTTONDOWN:
					print("Nivel: " + str(5 * (pantalla_act - 1) + 2))

					output = generar_panel_informativo(caracteristicas_panelInfo, 5 * (pantalla_act - 1) + 1, pantalla_act, False, False)

					txt9, posxytxt9 = output[0]
					txt10, posxytxt10 = output[1]
					txt11, posxytxt11 = output[2]
					txt12, posxytxt12 = output[3]
					txt13, posxytxt13 = output[4]
					txt14, posxytxt14 = output[5]
					txt15, posxytxt15 = output[6]
					txt16, posxytxt16 = output[7]
					txt17, posxytxt17 = output[8]

					ventana.fill(gris_fondo)

					if nivel_act < (5 * (pantalla_act - 1) + 1):
						bot5 = ["",""]

					elif nivel_act >= (5 * (pantalla_act - 1) + 1):
						bot5 = crear_boton3(ventana, posx1bot5, posy1bot5, posx2bot5, posy2bot5, "COMENZAR", tamañotxt2, tamañopolygon, errordebotgeneral, negro, fuente_act, negro)
						posesxybot5, posesxy2bot5 = bot5[1]

					results1 = generarfondo(ventana, caracteristicasfondo, user_act, punt_act)

					flecha_derecha = results1[0]
					flecha_izquierda = results1[1]
					txt1, posxytxt1 = results1[2]
					txt2, posxytxt2 = results1[3]
					posesxybot1, posesxy2bot1, botonreturn = results1[4]
					txt3, posxytxt3 = results1[5]
					txt4, posxytxt4 = results1[6]
					posesxybot2, posesxy2bot2, botonreturn2 = results1[7]
					txt5, posxytxt5 = results1[8]
					txt6, posxytxt6 = results1[9]
					txt7, posxytxt7 = results1[10]
					txt8, posxytxt8 = results1[11]

					ventana.blit(imagen_fondo_seleccion_pantalla, (202, 122))

					pygame.display.update()

					punto1, punto2, punto3, punto4, punto5, punto6, sumgen = crear_recuadro_seleccionLv(ventana, nivel_act, pantalla_act)

					ventana.blit(flecha_izquierda, (posx1flecha1, posy1flecha1))
					ventana.blit(flecha_derecha, (posx1flecha2, posy1flecha2))
					ventana.blit(txt1, (posxytxt1[0], posxytxt1[1]))
					ventana.blit(txt2, (posxytxt2[0], posxytxt2[1]))
					if txt3 != None: ventana.blit(txt3, (posxytxt3[0], posxytxt3[1]))
					if txt4 != None: ventana.blit(txt4, (posxytxt4[0], posxytxt4[1]))
					if txt5 != None: ventana.blit(txt5, (posxytxt5[0], posxytxt5[1]))
					if txt6 != None: ventana.blit(txt6, (posxytxt6[0], posxytxt6[1]))
					if txt7 != None: ventana.blit(txt7, (posxytxt7[0], posxytxt7[1]))
					if txt8 != None: ventana.blit(txt8, (posxytxt8[0], posxytxt8[1]))
					if txt9 != None: ventana.blit(txt9, (posxytxt9[0], posxytxt9[1]))
					if txt10 != None: ventana.blit(txt10, (posxytxt10[0], posxytxt10[1]))
					if txt11 != None: ventana.blit(txt11, (posxytxt11[0], posxytxt11[1]))
					if txt12 != None: ventana.blit(txt12, (posxytxt12[0], posxytxt12[1]))
					if txt13 != None: ventana.blit(txt13, (posxytxt13[0], posxytxt13[1]))
					if txt14 != ["", ""]: ventana.blit(txt14, (posxytxt14[0], posxytxt14[1]))
					if txt15 != ["", ""]: ventana.blit(txt15, (posxytxt15[0], posxytxt15[1]))
					if txt16 != ["", ""]: ventana.blit(txt16, (posxytxt16[0], posxytxt16[1]))
					if txt17 != ["", ""]: ventana.blit(txt17, (posxytxt17[0], posxytxt17[1]))
					ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
					ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))
					if bot5 != ["", ""]: ventana.blit(bot5[0], (posesxybot5[0], posesxybot5[1]))

					pygame.display.update()

			elif ratonx > punto3[0] - sumgen and ratony > punto3[1] - sumgen and ratonx < punto3[0] + sumgen and ratony < punto3[1] + sumgen:

				if evento.type == MOUSEBUTTONDOWN:
					print("Nivel: " + str(5 * (pantalla_act - 1) + 3))

					output = generar_panel_informativo(caracteristicas_panelInfo, 5 * (pantalla_act - 1) + 2, pantalla_act, False, False)

					txt9, posxytxt9 = output[0]
					txt10, posxytxt10 = output[1]
					txt11, posxytxt11 = output[2]
					txt12, posxytxt12 = output[3]
					txt13, posxytxt13 = output[4]
					txt14, posxytxt14 = output[5]
					txt15, posxytxt15 = output[6]
					txt16, posxytxt16 = output[7]
					txt17, posxytxt17 = output[8]

					ventana.fill(gris_fondo)

					if nivel_act < (5 * (pantalla_act - 1) + 2):
						bot5 = ["",""]

					elif nivel_act >= (5 * (pantalla_act - 1) + 2):
						bot5 = crear_boton3(ventana, posx1bot5, posy1bot5, posx2bot5, posy2bot5, "COMENZAR", tamañotxt2, tamañopolygon, errordebotgeneral, negro, fuente_act, negro)
						posesxybot5, posesxy2bot5 = bot5[1]

					results1 = generarfondo(ventana, caracteristicasfondo, user_act, punt_act)

					flecha_derecha = results1[0]
					flecha_izquierda = results1[1]
					txt1, posxytxt1 = results1[2]
					txt2, posxytxt2 = results1[3]
					posesxybot1, posesxy2bot1, botonreturn = results1[4]
					txt3, posxytxt3 = results1[5]
					txt4, posxytxt4 = results1[6]
					posesxybot2, posesxy2bot2, botonreturn2 = results1[7]
					txt5, posxytxt5 = results1[8]
					txt6, posxytxt6 = results1[9]
					txt7, posxytxt7 = results1[10]
					txt8, posxytxt8 = results1[11]

					ventana.blit(imagen_fondo_seleccion_pantalla, (202, 122))

					pygame.display.update()

					punto1, punto2, punto3, punto4, punto5, punto6, sumgen = crear_recuadro_seleccionLv(ventana, nivel_act, pantalla_act)

					ventana.blit(flecha_izquierda, (posx1flecha1, posy1flecha1))
					ventana.blit(flecha_derecha, (posx1flecha2, posy1flecha2))
					ventana.blit(txt1, (posxytxt1[0], posxytxt1[1]))
					ventana.blit(txt2, (posxytxt2[0], posxytxt2[1]))
					if txt3 != None: ventana.blit(txt3, (posxytxt3[0], posxytxt3[1]))
					if txt4 != None: ventana.blit(txt4, (posxytxt4[0], posxytxt4[1]))
					if txt5 != None: ventana.blit(txt5, (posxytxt5[0], posxytxt5[1]))
					if txt6 != None: ventana.blit(txt6, (posxytxt6[0], posxytxt6[1]))
					if txt7 != None: ventana.blit(txt7, (posxytxt7[0], posxytxt7[1]))
					if txt8 != None: ventana.blit(txt8, (posxytxt8[0], posxytxt8[1]))
					if txt9 != None: ventana.blit(txt9, (posxytxt9[0], posxytxt9[1]))
					if txt10 != None: ventana.blit(txt10, (posxytxt10[0], posxytxt10[1]))
					if txt11 != None: ventana.blit(txt11, (posxytxt11[0], posxytxt11[1]))
					if txt12 != None: ventana.blit(txt12, (posxytxt12[0], posxytxt12[1]))
					if txt13 != None: ventana.blit(txt13, (posxytxt13[0], posxytxt13[1]))
					if txt14 != ["", ""]: ventana.blit(txt14, (posxytxt14[0], posxytxt14[1]))
					if txt15 != ["", ""]: ventana.blit(txt15, (posxytxt15[0], posxytxt15[1]))
					if txt16 != ["", ""]: ventana.blit(txt16, (posxytxt16[0], posxytxt16[1]))
					if txt17 != ["", ""]: ventana.blit(txt17, (posxytxt17[0], posxytxt17[1]))
					ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
					ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))
					if bot5 != ["", ""]: ventana.blit(bot5[0], (posesxybot5[0], posesxybot5[1]))

					pygame.display.update()

			elif ratonx > punto4[0] - sumgen and ratony > punto4[1] - sumgen and ratonx < punto4[0] + sumgen and ratony < punto4[1] + sumgen:

				if evento.type == MOUSEBUTTONDOWN:
					print("Nivel: " + str(5 * (pantalla_act - 1) + 4))

					output = generar_panel_informativo(caracteristicas_panelInfo, 5 * (pantalla_act - 1) + 3, pantalla_act, False, False)

					txt9, posxytxt9 = output[0]
					txt10, posxytxt10 = output[1]
					txt11, posxytxt11 = output[2]
					txt12, posxytxt12 = output[3]
					txt13, posxytxt13 = output[4]
					txt14, posxytxt14 = output[5]
					txt15, posxytxt15 = output[6]
					txt16, posxytxt16 = output[7]
					txt17, posxytxt17 = output[8]

					ventana.fill(gris_fondo)

					if nivel_act < (5 * (pantalla_act - 1) + 3):
						bot5 = ["",""]

					elif nivel_act >= (5 * (pantalla_act - 1) + 3):
						bot5 = crear_boton3(ventana, posx1bot5, posy1bot5, posx2bot5, posy2bot5, "COMENZAR", tamañotxt2, tamañopolygon, errordebotgeneral, negro, fuente_act, negro)
						posesxybot5, posesxy2bot5 = bot5[1]

					results1 = generarfondo(ventana, caracteristicasfondo, user_act, punt_act)

					flecha_derecha = results1[0]
					flecha_izquierda = results1[1]
					txt1, posxytxt1 = results1[2]
					txt2, posxytxt2 = results1[3]
					posesxybot1, posesxy2bot1, botonreturn = results1[4]
					txt3, posxytxt3 = results1[5]
					txt4, posxytxt4 = results1[6]
					posesxybot2, posesxy2bot2, botonreturn2 = results1[7]
					txt5, posxytxt5 = results1[8]
					txt6, posxytxt6 = results1[9]
					txt7, posxytxt7 = results1[10]
					txt8, posxytxt8 = results1[11]

					ventana.blit(imagen_fondo_seleccion_pantalla, (202, 122))

					pygame.display.update()

					punto1, punto2, punto3, punto4, punto5, punto6, sumgen = crear_recuadro_seleccionLv(ventana, nivel_act, pantalla_act)

					ventana.blit(flecha_izquierda, (posx1flecha1, posy1flecha1))
					ventana.blit(flecha_derecha, (posx1flecha2, posy1flecha2))
					ventana.blit(txt1, (posxytxt1[0], posxytxt1[1]))
					ventana.blit(txt2, (posxytxt2[0], posxytxt2[1]))
					if txt3 != None: ventana.blit(txt3, (posxytxt3[0], posxytxt3[1]))
					if txt4 != None: ventana.blit(txt4, (posxytxt4[0], posxytxt4[1]))
					if txt5 != None: ventana.blit(txt5, (posxytxt5[0], posxytxt5[1]))
					if txt6 != None: ventana.blit(txt6, (posxytxt6[0], posxytxt6[1]))
					if txt7 != None: ventana.blit(txt7, (posxytxt7[0], posxytxt7[1]))
					if txt8 != None: ventana.blit(txt8, (posxytxt8[0], posxytxt8[1]))
					if txt9 != None: ventana.blit(txt9, (posxytxt9[0], posxytxt9[1]))
					if txt10 != None: ventana.blit(txt10, (posxytxt10[0], posxytxt10[1]))
					if txt11 != None: ventana.blit(txt11, (posxytxt11[0], posxytxt11[1]))
					if txt12 != None: ventana.blit(txt12, (posxytxt12[0], posxytxt12[1]))
					if txt13 != None: ventana.blit(txt13, (posxytxt13[0], posxytxt13[1]))
					if txt14 != ["", ""]: ventana.blit(txt14, (posxytxt14[0], posxytxt14[1]))
					if txt15 != ["", ""]: ventana.blit(txt15, (posxytxt15[0], posxytxt15[1]))
					if txt16 != ["", ""]: ventana.blit(txt16, (posxytxt16[0], posxytxt16[1]))
					if txt17 != ["", ""]: ventana.blit(txt17, (posxytxt17[0], posxytxt17[1]))
					ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
					ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))
					if bot5 != ["", ""]: ventana.blit(bot5[0], (posesxybot5[0], posesxybot5[1]))

					pygame.display.update()

			elif ratonx > punto5[0] - sumgen and ratony > punto5[1] - sumgen and ratonx < punto5[0] + sumgen and ratony < punto5[1] + sumgen:

				if evento.type == MOUSEBUTTONDOWN:
					print("Nivel: " + str(5 * (pantalla_act - 1) + 5))

					output = generar_panel_informativo(caracteristicas_panelInfo, 5 * (pantalla_act - 1) + 4, pantalla_act, False, False)

					txt9, posxytxt9 = output[0]
					txt10, posxytxt10 = output[1]
					txt11, posxytxt11 = output[2]
					txt12, posxytxt12 = output[3]
					txt13, posxytxt13 = output[4]
					txt14, posxytxt14 = output[5]
					txt15, posxytxt15 = output[6]
					txt16, posxytxt16 = output[7]
					txt17, posxytxt17 = output[8]

					ventana.fill(gris_fondo)

					if nivel_act < (5 * (pantalla_act - 1) + 4):
						bot5 = ["",""]

					elif nivel_act >= (5 * (pantalla_act - 1) + 4):
						bot5 = crear_boton3(ventana, posx1bot5, posy1bot5, posx2bot5, posy2bot5, "COMENZAR", tamañotxt2, tamañopolygon, errordebotgeneral, negro, fuente_act, negro)
						posesxybot5, posesxy2bot5 = bot5[1]

					results1 = generarfondo(ventana, caracteristicasfondo, user_act, punt_act)

					flecha_derecha = results1[0]
					flecha_izquierda = results1[1]
					txt1, posxytxt1 = results1[2]
					txt2, posxytxt2 = results1[3]
					posesxybot1, posesxy2bot1, botonreturn = results1[4]
					txt3, posxytxt3 = results1[5]
					txt4, posxytxt4 = results1[6]
					posesxybot2, posesxy2bot2, botonreturn2 = results1[7]
					txt5, posxytxt5 = results1[8]
					txt6, posxytxt6 = results1[9]
					txt7, posxytxt7 = results1[10]
					txt8, posxytxt8 = results1[11]

					ventana.blit(imagen_fondo_seleccion_pantalla, (202, 122))

					pygame.display.update()

					punto1, punto2, punto3, punto4, punto5, punto6, sumgen = crear_recuadro_seleccionLv(ventana, nivel_act, pantalla_act)

					ventana.blit(flecha_izquierda, (posx1flecha1, posy1flecha1))
					ventana.blit(flecha_derecha, (posx1flecha2, posy1flecha2))
					ventana.blit(txt1, (posxytxt1[0], posxytxt1[1]))
					ventana.blit(txt2, (posxytxt2[0], posxytxt2[1]))
					if txt3 != None: ventana.blit(txt3, (posxytxt3[0], posxytxt3[1]))
					if txt4 != None: ventana.blit(txt4, (posxytxt4[0], posxytxt4[1]))
					if txt5 != None: ventana.blit(txt5, (posxytxt5[0], posxytxt5[1]))
					if txt6 != None: ventana.blit(txt6, (posxytxt6[0], posxytxt6[1]))
					if txt7 != None: ventana.blit(txt7, (posxytxt7[0], posxytxt7[1]))
					if txt8 != None: ventana.blit(txt8, (posxytxt8[0], posxytxt8[1]))
					if txt9 != None: ventana.blit(txt9, (posxytxt9[0], posxytxt9[1]))
					if txt10 != None: ventana.blit(txt10, (posxytxt10[0], posxytxt10[1]))
					if txt11 != None: ventana.blit(txt11, (posxytxt11[0], posxytxt11[1]))
					if txt12 != None: ventana.blit(txt12, (posxytxt12[0], posxytxt12[1]))
					if txt13 != None: ventana.blit(txt13, (posxytxt13[0], posxytxt13[1]))
					if txt14 != ["", ""]: ventana.blit(txt14, (posxytxt14[0], posxytxt14[1]))
					if txt15 != ["", ""]: ventana.blit(txt15, (posxytxt15[0], posxytxt15[1]))
					if txt16 != ["", ""]: ventana.blit(txt16, (posxytxt16[0], posxytxt16[1]))
					if txt17 != ["", ""]: ventana.blit(txt17, (posxytxt17[0], posxytxt17[1]))
					ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
					ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))
					if bot5 != ["", ""]: ventana.blit(bot5[0], (posesxybot5[0], posesxybot5[1]))

					pygame.display.update()

			elif ratonx > punto6[0] - sumgen and ratony > punto6[1] - sumgen and ratonx < punto6[0] + sumgen and ratony < punto6[1] + sumgen:

				if evento.type == MOUSEBUTTONDOWN:

					print("Nivel Infinito: " + str(pantalla_act))

					output = generar_panel_informativo(caracteristicas_panelInfo, pantalla_act - 1, pantalla_act, False, True)

					txt9, posxytxt9 = output[0]
					txt10, posxytxt10 = output[1]
					txt11, posxytxt11 = output[2]
					txt12, posxytxt12 = output[3]
					txt13, posxytxt13 = output[4]
					txt14, posxytxt14 = output[5]
					txt15, posxytxt15 = output[6]
					txt16, posxytxt16 = output[7]
					txt17, posxytxt17 = output[8]

					ventana.fill(gris_fondo)

					results1 = generarfondo(ventana, caracteristicasfondo, user_act, punt_act)

					flecha_derecha = results1[0]
					flecha_izquierda = results1[1]
					txt1, posxytxt1 = results1[2]
					txt2, posxytxt2 = results1[3]
					posesxybot1, posesxy2bot1, botonreturn = results1[4]
					txt3, posxytxt3 = results1[5]
					txt4, posxytxt4 = results1[6]
					posesxybot2, posesxy2bot2, botonreturn2 = results1[7]
					txt5, posxytxt5 = results1[8]
					txt6, posxytxt6 = results1[9]
					txt7, posxytxt7 = results1[10]
					txt8, posxytxt8 = results1[11]

					ventana.blit(imagen_fondo_seleccion_pantalla, (202, 122))

					pygame.display.update()

					punto1, punto2, punto3, punto4, punto5, punto6, sumgen = crear_recuadro_seleccionLv(ventana, nivel_act, pantalla_act)

					ventana.blit(flecha_izquierda, (posx1flecha1, posy1flecha1))
					ventana.blit(flecha_derecha, (posx1flecha2, posy1flecha2))
					ventana.blit(txt1, (posxytxt1[0], posxytxt1[1]))
					ventana.blit(txt2, (posxytxt2[0], posxytxt2[1]))
					if txt3 != None: ventana.blit(txt3, (posxytxt3[0], posxytxt3[1]))
					if txt4 != None: ventana.blit(txt4, (posxytxt4[0], posxytxt4[1]))
					if txt5 != None: ventana.blit(txt5, (posxytxt5[0], posxytxt5[1]))
					if txt6 != None: ventana.blit(txt6, (posxytxt6[0], posxytxt6[1]))
					if txt7 != None: ventana.blit(txt7, (posxytxt7[0], posxytxt7[1]))
					if txt8 != None: ventana.blit(txt8, (posxytxt8[0], posxytxt8[1]))
					if txt9 != None: ventana.blit(txt9, (posxytxt9[0], posxytxt9[1]))
					if txt10 != None: ventana.blit(txt10, (posxytxt10[0], posxytxt10[1]))
					if txt11 != None: ventana.blit(txt11, (posxytxt11[0], posxytxt11[1]))
					if txt12 != None: ventana.blit(txt12, (posxytxt12[0], posxytxt12[1]))
					if txt13 != None: ventana.blit(txt13, (posxytxt13[0], posxytxt13[1]))
					if txt14 != ["", ""]: ventana.blit(txt14, (posxytxt14[0], posxytxt14[1]))
					if txt15 != ["", ""]: ventana.blit(txt15, (posxytxt15[0], posxytxt15[1]))
					if txt16 != ["", ""]: ventana.blit(txt16, (posxytxt16[0], posxytxt16[1]))
					if txt17 != ["", ""]: ventana.blit(txt17, (posxytxt17[0], posxytxt17[1]))
					ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
					ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))

					pygame.display.update()

			elif ratonx > posx1flecha1 and ratony > posy1flecha1 and ratonx < posx2flecha1 and ratony < posy2flecha1:

				if evento.type == MOUSEBUTTONDOWN:

					if pantalla_act > 1:
						pantalla_act -= 1

					print("Pantalla: " + str(pantalla_act))

					txt9 = ["", ""]
					txt10 = ["", ""]
					txt11 = ["", ""]
					txt12 = ["", ""]
					txt13 = ["", ""]
					txt14, posxytxt14 = print_pantalla("Nivel actual: ", posxtxt14151617, posytxt14, tamañotxt2, negro, fuente_act)
					txt15, posxytxt15 = print_pantalla("Infinito: ", posxtxt14151617, posytxt15, tamañotxt2, negro, fuente_act)
					txt16, posxytxt16 = print_pantalla("Boss: ", posxtxt14151617, posytxt16, tamañotxt2, negro, fuente_act)
					txt17, posxytxt17 = print_pantalla("Nº Naves: ", posxtxt14151617, posytxt17, tamañotxt2, negro, fuente_act)

					ventana.fill(gris_fondo)

					results1 = generarfondo(ventana, caracteristicasfondo, user_act, punt_act)

					flecha_derecha = results1[0]
					flecha_izquierda = results1[1]
					txt1, posxytxt1 = results1[2]
					txt2, posxytxt2 = results1[3]
					posesxybot1, posesxy2bot1, botonreturn = results1[4]
					txt3, posxytxt3 = results1[5]
					txt4, posxytxt4 = results1[6]
					posesxybot2, posesxy2bot2, botonreturn2 = results1[7]
					txt5, posxytxt5 = results1[8]
					txt6, posxytxt6 = results1[9]
					txt7, posxytxt7 = results1[10]
					txt8, posxytxt8 = results1[11]

					ventana.blit(imagen_fondo_seleccion_pantalla, (202, 122))

					pygame.display.update()

					punto1, punto2, punto3, punto4, punto5, punto6, sumgen = crear_recuadro_seleccionLv(ventana, nivel_act, pantalla_act)

					ventana.blit(flecha_izquierda, (posx1flecha1, posy1flecha1))
					ventana.blit(flecha_derecha, (posx1flecha2, posy1flecha2))
					ventana.blit(txt1, (posxytxt1[0], posxytxt1[1]))
					ventana.blit(txt2, (posxytxt2[0], posxytxt2[1]))
					if txt3 != None: ventana.blit(txt3, (posxytxt3[0], posxytxt3[1]))
					if txt4 != None: ventana.blit(txt4, (posxytxt4[0], posxytxt4[1]))
					if txt5 != None: ventana.blit(txt5, (posxytxt5[0], posxytxt5[1]))
					if txt6 != None: ventana.blit(txt6, (posxytxt6[0], posxytxt6[1]))
					if txt7 != None: ventana.blit(txt7, (posxytxt7[0], posxytxt7[1]))
					if txt8 != None: ventana.blit(txt8, (posxytxt8[0], posxytxt8[1]))
					if txt9 != ["", ""]: ventana.blit(txt9, (posxytxt9[0], posxytxt9[1]))
					if txt10 != ["", ""]: ventana.blit(txt10, (posxytxt10[0], posxytxt10[1]))
					if txt11 != ["", ""]: ventana.blit(txt11, (posxytxt11[0], posxytxt11[1]))
					if txt12 != ["", ""]: ventana.blit(txt12, (posxytxt12[0], posxytxt12[1]))
					if txt13 != ["", ""]: ventana.blit(txt13, (posxytxt13[0], posxytxt13[1]))
					if txt14 != ["", ""]: ventana.blit(txt14, (posxytxt14[0], posxytxt14[1]))
					if txt15 != ["", ""]: ventana.blit(txt15, (posxytxt15[0], posxytxt15[1]))
					if txt16 != ["", ""]: ventana.blit(txt16, (posxytxt16[0], posxytxt16[1]))
					if txt17 != ["", ""]: ventana.blit(txt17, (posxytxt17[0], posxytxt17[1]))
					ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
					ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))

					pygame.display.update()

			elif ratonx > posx1flecha2 and ratony > posy1flecha2 and ratonx < posx2flecha2 and ratony < posy2flecha2:

				if evento.type == MOUSEBUTTONDOWN:

					if pantalla_act < 5:
						pantalla_act += 1

					print("Pantalla: " + str(pantalla_act))

					txt9 = ["", ""]
					txt10 = ["", ""]
					txt11 = ["", ""]
					txt12 = ["", ""]
					txt13 = ["", ""]
					txt14, posxytxt14 = print_pantalla("Nivel actual: ", posxtxt14151617, posytxt14, tamañotxt2, negro, fuente_act)
					txt15, posxytxt15 = print_pantalla("Infinito: ", posxtxt14151617, posytxt15, tamañotxt2, negro, fuente_act)
					txt16, posxytxt16 = print_pantalla("Boss: ", posxtxt14151617, posytxt16, tamañotxt2, negro, fuente_act)
					txt17, posxytxt17 = print_pantalla("Nº Naves: ", posxtxt14151617, posytxt17, tamañotxt2, negro, fuente_act)

					ventana.fill(gris_fondo)

					results1 = generarfondo(ventana, caracteristicasfondo, user_act, punt_act)

					flecha_derecha = results1[0]
					flecha_izquierda = results1[1]
					txt1, posxytxt1 = results1[2]
					txt2, posxytxt2 = results1[3]
					posesxybot1, posesxy2bot1, botonreturn = results1[4]
					txt3, posxytxt3 = results1[5]
					txt4, posxytxt4 = results1[6]
					posesxybot2, posesxy2bot2, botonreturn2 = results1[7]
					txt5, posxytxt5 = results1[8]
					txt6, posxytxt6 = results1[9]
					txt7, posxytxt7 = results1[10]
					txt8, posxytxt8 = results1[11]

					ventana.blit(imagen_fondo_seleccion_pantalla, (202, 122))

					pygame.display.update()

					punto1, punto2, punto3, punto4, punto5, punto6, sumgen = crear_recuadro_seleccionLv(ventana, nivel_act, pantalla_act)

					ventana.blit(flecha_izquierda, (posx1flecha1, posy1flecha1))
					ventana.blit(flecha_derecha, (posx1flecha2, posy1flecha2))
					ventana.blit(txt1, (posxytxt1[0], posxytxt1[1]))
					ventana.blit(txt2, (posxytxt2[0], posxytxt2[1]))
					if txt3 != None: ventana.blit(txt3, (posxytxt3[0], posxytxt3[1]))
					if txt4 != None: ventana.blit(txt4, (posxytxt4[0], posxytxt4[1]))
					if txt5 != None: ventana.blit(txt5, (posxytxt5[0], posxytxt5[1]))
					if txt6 != None: ventana.blit(txt6, (posxytxt6[0], posxytxt6[1]))
					if txt7 != None: ventana.blit(txt7, (posxytxt7[0], posxytxt7[1]))
					if txt8 != None: ventana.blit(txt8, (posxytxt8[0], posxytxt8[1]))
					if txt9 != ["", ""]: ventana.blit(txt9, (posxytxt9[0], posxytxt9[1]))
					if txt10 != ["", ""]: ventana.blit(txt10, (posxytxt10[0], posxytxt10[1]))
					if txt11 != ["", ""]: ventana.blit(txt11, (posxytxt11[0], posxytxt11[1]))
					if txt12 != ["", ""]: ventana.blit(txt12, (posxytxt12[0], posxytxt12[1]))
					if txt13 != ["", ""]: ventana.blit(txt13, (posxytxt13[0], posxytxt13[1]))
					if txt14 != ["", ""]: ventana.blit(txt14, (posxytxt14[0], posxytxt14[1]))
					if txt15 != ["", ""]: ventana.blit(txt15, (posxytxt15[0], posxytxt15[1]))
					if txt16 != ["", ""]: ventana.blit(txt16, (posxytxt16[0], posxytxt16[1]))
					if txt17 != ["", ""]: ventana.blit(txt17, (posxytxt17[0], posxytxt17[1]))
					ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
					ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))

					pygame.display.update()

			elif ratonx > posesxybot1[0] -  errordebotgeneral and ratony > posesxybot1[1] - errordebotgeneral and ratonx < posesxy2bot1[0] and ratony < posesxy2bot1[1]:

				if evento.type == MOUSEBUTTONDOWN:

					Exit_presionado = True

			elif ratonx > posesxybot2[0] -  errordebotgeneral and ratony > posesxybot2[1] - errordebotgeneral and ratonx < posesxy2bot2[0] and ratony < posesxy2bot2[1]:

				if evento.type == MOUSEBUTTONDOWN:
					ajustes = extraer_ajustes()

					ancho = int(ajustes[0])
					alto = int(ajustes[1])

					Ejecutarajustes(ventana, user_act, ancho, alto)

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

					ventana.fill(gris_fondo)

					errordebotgeneral = round(0.00390625 * ancho)
					tamañopolygon = round(0.00190625 * ancho)
					posx1botat = round(0.015625 * ancho)
					posy1botat = round(0.9305555 * alto)
					posx2botat = round(0.234375 * ancho)
					posy2botat = round(0.9722222 * alto)
					tamañotxt2 = round(0.0234375 * ancho)

					posx1botaj = round(0.015625 * ancho)
					posy1botaj = round(0.855 * alto)
					posx2botaj = round(0.1041875 * ancho)
					posy2botaj = round(0.89666666667 * alto)

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
					posesxybot2, posesxy2bot2, botonreturn2 = results1[7]

					ventana.blit(imagen_fondo_seleccion_pantalla, (202, 122))

					pygame.display.update()

					punto1, punto2, punto3, punto4, punto5, punto6, sumgen = crear_recuadro_seleccionLv(ventana, nivel_act, pantalla_act)

					ventana.blit(flecha_izquierda, (posx1flecha1, posy1flecha1))
					ventana.blit(flecha_derecha, (posx1flecha2, posy1flecha2))
					ventana.blit(txt1, (posxytxt1[0], posxytxt1[1]))
					ventana.blit(txt2, (posxytxt2[0], posxytxt2[1]))
					if txt3 != None: ventana.blit(txt3, (posxytxt3[0], posxytxt3[1]))
					if txt4 != None: ventana.blit(txt4, (posxytxt4[0], posxytxt4[1]))
					if txt5 != None: ventana.blit(txt5, (posxytxt5[0], posxytxt5[1]))
					if txt6 != None: ventana.blit(txt6, (posxytxt6[0], posxytxt6[1]))
					if txt7 != None: ventana.blit(txt7, (posxytxt7[0], posxytxt7[1]))
					if txt8 != None: ventana.blit(txt8, (posxytxt8[0], posxytxt8[1]))
					ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
					ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))

					pygame.display.update()




