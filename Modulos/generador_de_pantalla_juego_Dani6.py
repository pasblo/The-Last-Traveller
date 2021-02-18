#!/usr/bin/python3

"""
Este modulo ejecuta el juego principal con todas sus extensiones

"""

import pygame

import sys

import sqlite3

import os

import time

import math

import random

from Modulos.clasificador import SoundObj, BGMObj

from Modulos.basededatosajustesfaciliter import *

from Modulos.objetos_de_pantalla import *

from Modulos.generador_de_recuadro_salida import *

from Modulos.generador_de_niveles import *

from datetime import datetime

from pygame.locals import *

from Modulos.generador_de_pantalla_resultados import *

def ejecutar_juego(ventana, user_act, Lv_act, infinito, pantalla_act, demo, Nº_Naves, txt_1, posxytxt_1, puntuacion_total, monedas_totales):
	"""

	rec = recuadro de relleno
	bot = boton
	txt = texto
	img = imagen
	line = linea

	AD = Arriba derecha
	DD = Debajo derecha
	AI = Arriba izquierda
	DI = Debajo izquierda

	PARA SUMAR Y RESTAR MONEDAS

	identuser = identde("Records", "monedas", user_comp[1], 0)

    datos_a_insertar_monedas = (nombredeusuario, -6, identuser)

    insertardatos("Records", datos_a_insertar_monedas, "Datos insertados correctamente", "Hubo un error al insertar los datos", "monedas")

	"""

	ajustes = extraer_ajustes()

	ancho = int(ajustes[0])
	alto = int(ajustes[1])
	fuente = ajustes[3]

	vol_general = int(ajustes[4])
	vol_efectos = int(ajustes[5])
	vol_musica = int(ajustes[6])

	blanco = (255, 255, 255)
	negro = (0, 0, 0)
	rojo = (255, 0, 0)
	amarillo = (255, 255, 0)
	azul = (0, 0, 255)
	gris_fondo = (90, 90, 90)
	verde = (0, 255, 0)
	rosa = (255, 0, 188)
	verde_claro = [100, 255, 0]

	colores_seleccion = [blanco, rojo, amarillo, azul, verde, rosa, verde_claro]

	dire = "Imagenes/Barra/Barra1.png" #Copiar desde aquí
	barra_alpha = pygame.image.load(dire)
	barra = pygame.transform.scale(barra_alpha, (round(0.2265625 * ancho), round(0.20833333333333333333333333333333 * alto)))
	ventana.fill(negro)
	ventana.blit(barra, (round(0.38671875 * ancho), round(0.39583333333333333333333333333333 * alto)))
	ventana.blit(txt_1, (posxytxt_1[0], posxytxt_1[1]))
	pygame.display.update() #Hasta aqui

	colorline = blanco
	colortxt = blanco
	colorfondo = negro

	pygame.mouse.set_visible(False)

	tamañoline = round(0.00234375 * ancho) #======= INICIO DEFINICION DE TAMAÑOS ======
	tamañotxt1 = round(0.0234375 * ancho)
	tamañotxt2 = 22 #======= FINAL DEFINICION DE TAMAÑOS ======

	dire = "Imagenes/Barra/Barra2.png" #Copiar desde aquí
	barra_alpha = pygame.image.load(dire)
	barra = pygame.transform.scale(barra_alpha, (round(0.2265625 * ancho), round(0.20833333333333333333333333333333 * alto)))
	ventana.fill(negro)
	ventana.blit(barra, (round(0.38671875 * ancho), round(0.39583333333333333333333333333333 * alto)))
	ventana.blit(txt_1, (posxytxt_1[0], posxytxt_1[1]))
	pygame.display.update() #Hasta aqui

	posxline1 = round(0.25 * ancho) #======= INICIO DEFINICION DE POSICIONES ======
	posxline2 = round(0.75 * ancho)

	posy2rec1 = round(0.5 * alto)

	posytxt_derecha_ariba = round(0.03572222222222222222222222222222 * alto) #======= FINAL DEFINICION DE POSICIONES ======

	posytxt_derecha_debajo = round(0.05 * alto)

	possumando_izquierda_abajo = round(0.05 * alto)

	plusninguno = round(0.0390625 * ancho)

	posximag123 = round(0.2109375 * ancho)

	posx1rectcentre = round(0.25 * ancho)

	posxnaveprueva = round(0.5 * ancho)

	tamañoControladorx = 168
	tamañoControladory = 104

	tamañoEscudox = 184
	tamañoEscudoy = 120

	posxControlador = 1036
	posyControlador = 128

	posxbarrera = 320
	posybarrera = 50

	#Caracteristicas: Primero = Proteccion, Segundo = Daño de disparo, Tercero = Daño cuerpo a cuerpo, Cuarto = Velocidad, Quinto = Si tiene escudo o no. (El escudo es que cuando lo mata se regenera y se le desactiva el escudo)

	caracteristicas_naves_enemigas = [(5, 25, 2, 100, False), (15, 25, 5, 100, False), (20, 30, 8, 150, False), (20, 60, 10, 140, True), (40, 100, 20, 130, False), (60, 135, 45, 150, False), (100, 200, 50, 200, True), (250, 250, 70, 250, True), (400, 350, 85, 225, False), (800, 500, 100, 220, True)]

	nivel_de_aparecimiento = [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]

	daño_por_proyectil = [5, 10, 15, 20, 25]

	list_naves = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	posxvuelta = [420, 540, 700, 820]

	posiciones_ocupadas = 0

	usados = []

	DisparoNegro_alpha = pygame.image.load("Imagenes/Disparos/Disparo_1.png")
	DisparoNegro = pygame.transform.scale(DisparoNegro_alpha, (2, 8)) # 1 X 4
	DisparoBlanco_alpha = pygame.image.load("Imagenes/Disparos/Disparo_2.png")
	DisparoBlanco = pygame.transform.scale(DisparoBlanco_alpha, (2, 8)) # 1 X 4
	DisparoRojo_alpha = pygame.image.load("Imagenes/Disparos/Disparo_3.png")
	DisparoRojo = pygame.transform.scale(DisparoRojo_alpha, (2, 8)) # 1 X 4
	DisparoAzul_alpha = pygame.image.load("Imagenes/Disparos/Disparo_4.png")
	DisparoAzul = pygame.transform.scale(DisparoAzul_alpha, (2, 8)) # 1 X 4
	DisparoAmarillo_alpha = pygame.image.load("Imagenes/Disparos/Disparo_5.png")
	DisparoAmarillo = pygame.transform.scale(DisparoAmarillo_alpha, (2, 8)) # 1 X 4

	NavePrincipal_alpha = pygame.image.load("Imagenes/Naves_Amigas/NavePrin.png")
	NavePrincipal = pygame.transform.scale(NavePrincipal_alpha, (42, 26)) # 21 X 13
	NavePrincipalNegro_alpha = pygame.image.load("Imagenes/Naves_Amigas/NavePrinNegro.png")
	NavePrincipalNegro = pygame.transform.scale(NavePrincipalNegro_alpha, (42, 26)) # 21 X 13
	NavePrincipal_SinAla_Derecha_aplha = pygame.image.load("Imagenes/Naves_Amigas/NavePrin_SinAla_Derecha.png")
	NavePrincipal_SinAla_Derecha = pygame.transform.scale(NavePrincipal_SinAla_Derecha_aplha, (42, 26)) # 21 X 13
	NavePrincipal_SinAla_Izquierda_alpha = pygame.image.load("Imagenes/Naves_Amigas/NavePrin_SinAla_Izquierda.png")
	NavePrincipal_SinAla_Izquierda = pygame.transform.scale(NavePrincipal_SinAla_Izquierda_alpha, (42, 26)) # 21 X 13
	NavePrincipal_SinAlas_aplha = pygame.image.load("Imagenes/Naves_Amigas/NavePrin_SinAla_Derecha_e_Izquierda.png")
	NavePrincipal_SinAlas = pygame.transform.scale(NavePrincipal_SinAlas_aplha, (42, 26)) # 21 X 13
	NavePrincipal_SinPico_alpha = pygame.image.load("Imagenes/Naves_Amigas/NavePrin_SinPico.png")
	NavePrincipal_SinPico = pygame.transform.scale(NavePrincipal_SinPico_alpha, (42, 26)) # 21 X 13
	NavePrincipal_SinPico_y_Ala_Derecha_aplha = pygame.image.load("Imagenes/Naves_Amigas/NavePrin_SinPico_y_Ala_Derecha.png")
	NavePrincipal_SinPico_y_Ala_Derecha = pygame.transform.scale(NavePrincipal_SinPico_y_Ala_Derecha_aplha, (42, 26)) # 21 X 13
	NavePrincipal_SinPico_y_Ala_Izquierda_alpha = pygame.image.load("Imagenes/Naves_Amigas/NavePrin_SinPico_y_Ala_Izquierda.png")
	NavePrincipal_SinPico_y_Ala_Izquierda = pygame.transform.scale(NavePrincipal_SinPico_y_Ala_Izquierda_alpha, (42, 26)) # 21 X 13
	NavePrincipal_SinPico_y_Motor_alpha = pygame.image.load("Imagenes/Naves_Amigas/NavePrin_SinPico_y_Ala_Izquierda.png")
	NavePrincipal_SinPico_y_Motor = pygame.transform.scale(NavePrincipal_SinPico_y_Motor_alpha, (42, 26)) # 21 X 13
	Escudo_alpha = pygame.image.load("Imagenes/Naves_Amigas/NavePrin_Escudo.png")
	Escudo = pygame.transform.scale(Escudo_alpha, (tamañoEscudox, tamañoEscudoy)) # 23 X 15

	Tipos_De_Naves_Prin = [NavePrincipal, NavePrincipal_SinAla_Izquierda, NavePrincipal_SinAla_Derecha, NavePrincipal_SinAlas, NavePrincipal_SinPico, NavePrincipal_SinPico_y_Ala_Derecha, NavePrincipal_SinPico_y_Ala_Izquierda, NavePrincipal_SinPico_y_Motor]
	Data_Prin = [[True, True, True, True], [True, True, True, False], [True, True, False, True], [True, True, False, False], [False, True, True, True], [False, True, False, True], [False, True, True, False], [False, False, True, True]]

	dire = "Imagenes/Barra/Barra3.png" #Copiar desde aquí
	barra_alpha = pygame.image.load(dire)
	barra = pygame.transform.scale(barra_alpha, (round(0.2265625 * ancho), round(0.20833333333333333333333333333333 * alto)))
	ventana.fill(negro)
	ventana.blit(barra, (round(0.38671875 * ancho), round(0.39583333333333333333333333333333 * alto)))
	ventana.blit(txt_1, (posxytxt_1[0], posxytxt_1[1]))
	pygame.display.update() #Hasta aqui

	Explosion1_alpha = pygame.image.load("Imagenes/Explosion_Naves_Enemigas/1.png")
	Explosion1 = pygame.transform.scale(Explosion1_alpha, (52, 34)) # 26 X 17 to 52 X 34
	Explosion2_alpha = pygame.image.load("Imagenes/Explosion_Naves_Enemigas/2.png")
	Explosion2 = pygame.transform.scale(Explosion2_alpha, (52, 34)) # 26 X 17 to 52 X 34
	Explosion3_alpha = pygame.image.load("Imagenes/Explosion_Naves_Enemigas/3.png")
	Explosion3 = pygame.transform.scale(Explosion3_alpha, (52, 34)) # 26 X 17 to 52 X 34
	Explosion4_alpha = pygame.image.load("Imagenes/Explosion_Naves_Enemigas/4.png")
	Explosion4 = pygame.transform.scale(Explosion4_alpha, (52, 34)) # 26 X 17 to 52 X 34
	Explosion5_alpha = pygame.image.load("Imagenes/Explosion_Naves_Enemigas/5.png")
	Explosion5 = pygame.transform.scale(Explosion5_alpha, (52, 34)) # 26 X 17 to 52 X 34
	Explosion6_alpha = pygame.image.load("Imagenes/Explosion_Naves_Enemigas/6.png")
	Explosion6 = pygame.transform.scale(Explosion6_alpha, (52, 34)) # 26 X 17 to 52 X 34
	Explosion7_alpha = pygame.image.load("Imagenes/Explosion_Naves_Enemigas/7.png")
	Explosion7 = pygame.transform.scale(Explosion7_alpha, (52, 34)) # 26 X 17 to 52 X 34

	dire = "Imagenes/Barra/Barra4.png" #Copiar desde aquí
	barra_alpha = pygame.image.load(dire)
	barra = pygame.transform.scale(barra_alpha, (round(0.2265625 * ancho), round(0.20833333333333333333333333333333 * alto)))
	ventana.fill(negro)
	ventana.blit(barra, (round(0.38671875 * ancho), round(0.39583333333333333333333333333333 * alto)))
	ventana.blit(txt_1, (posxytxt_1[0], posxytxt_1[1]))
	pygame.display.update() #Hasta aqui

	Explosion1_Negro_alpha = pygame.image.load("Imagenes/Explosion_Naves_Enemigas/1_Negro.png")
	Explosion1_Negro = pygame.transform.scale(Explosion1_Negro_alpha, (52, 34)) # 26 X 17 to 52 X 34
	Explosion2_Negro_alpha = pygame.image.load("Imagenes/Explosion_Naves_Enemigas/2_Negro.png")
	Explosion2_Negro = pygame.transform.scale(Explosion2_Negro_alpha, (52, 34)) # 26 X 17 to 52 X 34
	Explosion3_Negro_alpha = pygame.image.load("Imagenes/Explosion_Naves_Enemigas/3_Negro.png")
	Explosion3_Negro = pygame.transform.scale(Explosion3_Negro_alpha, (52, 34)) # 26 X 17 to 52 X 34
	Explosion4_Negro_alpha = pygame.image.load("Imagenes/Explosion_Naves_Enemigas/4_Negro.png")
	Explosion4_Negro = pygame.transform.scale(Explosion4_Negro_alpha, (52, 34)) # 26 X 17 to 52 X 34
	Explosion5_Negro_alpha = pygame.image.load("Imagenes/Explosion_Naves_Enemigas/5_Negro.png")
	Explosion5_Negro = pygame.transform.scale(Explosion5_Negro_alpha, (52, 34)) # 26 X 17 to 52 X 34
	Explosion6_Negro_alpha = pygame.image.load("Imagenes/Explosion_Naves_Enemigas/6_Negro.png")
	Explosion6_Negro = pygame.transform.scale(Explosion6_Negro_alpha, (52, 34)) # 26 X 17 to 52 X 34
	Explosion7_Negro_alpha = pygame.image.load("Imagenes/Explosion_Naves_Enemigas/7_Negro.png")
	Explosion7_Negro = pygame.transform.scale(Explosion7_Negro_alpha, (52, 34)) # 26 X 17 to 52 X 34

	Nave1_Negro_alpha = pygame.image.load("Imagenes/Naves_Enemigas/EBEN1_negra.png")
	Nave1_Negro = pygame.transform.scale(Nave1_Negro_alpha, (round(0.03125 * ancho), round(0.03055555555555555555555555555556 * alto))) # 20 X 11 to 40 X 22

	disparos = [DisparoBlanco, DisparoRojo, DisparoAzul, DisparoAmarillo]

	dire = "Imagenes/Barra/Barra5.png" #Copiar desde aquí
	barra_alpha = pygame.image.load(dire)
	barra = pygame.transform.scale(barra_alpha, (round(0.2265625 * ancho), round(0.20833333333333333333333333333333 * alto)))
	ventana.fill(negro)
	ventana.blit(barra, (round(0.38671875 * ancho), round(0.39583333333333333333333333333333 * alto)))
	ventana.blit(txt_1, (posxytxt_1[0], posxytxt_1[1]))
	pygame.display.update() #Hasta aqui

	Barrera_Azul = pygame.image.load("Imagenes/Barreras/Barrera_Azul.png")
	Barrera_Rojo = pygame.image.load("Imagenes/Barreras/Barrera_Roja.png")

	Deteccion_De_Daños1_alpha = pygame.image.load("Imagenes/Det/0000.png")
	Deteccion_De_Daños1 = pygame.transform.scale(Deteccion_De_Daños1_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños2_alpha = pygame.image.load("Imagenes/Det/0001.png")
	Deteccion_De_Daños2 = pygame.transform.scale(Deteccion_De_Daños2_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños3_alpha = pygame.image.load("Imagenes/Det/0002.png")
	Deteccion_De_Daños3 = pygame.transform.scale(Deteccion_De_Daños3_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños4_alpha = pygame.image.load("Imagenes/Det/0010.png")
	Deteccion_De_Daños4 = pygame.transform.scale(Deteccion_De_Daños4_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños5_alpha = pygame.image.load("Imagenes/Det/0011.png")
	Deteccion_De_Daños5 = pygame.transform.scale(Deteccion_De_Daños5_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños6_alpha = pygame.image.load("Imagenes/Det/0012.png")
	Deteccion_De_Daños6 = pygame.transform.scale(Deteccion_De_Daños6_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños7_alpha = pygame.image.load("Imagenes/Det/0020.png")
	Deteccion_De_Daños7 = pygame.transform.scale(Deteccion_De_Daños7_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños8_alpha = pygame.image.load("Imagenes/Det/0021.png")
	Deteccion_De_Daños8 = pygame.transform.scale(Deteccion_De_Daños8_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños9_alpha = pygame.image.load("Imagenes/Det/0022.png")
	Deteccion_De_Daños9 = pygame.transform.scale(Deteccion_De_Daños9_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños10_alpha = pygame.image.load("Imagenes/Det/0100.png")
	Deteccion_De_Daños10 = pygame.transform.scale(Deteccion_De_Daños10_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños11_alpha = pygame.image.load("Imagenes/Det/0101.png")
	Deteccion_De_Daños11 = pygame.transform.scale(Deteccion_De_Daños11_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños12_alpha = pygame.image.load("Imagenes/Det/0102.png")
	Deteccion_De_Daños12 = pygame.transform.scale(Deteccion_De_Daños12_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños13_alpha = pygame.image.load("Imagenes/Det/0110.png")
	Deteccion_De_Daños13 = pygame.transform.scale(Deteccion_De_Daños13_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños14_alpha = pygame.image.load("Imagenes/Det/0111.png")
	Deteccion_De_Daños14 = pygame.transform.scale(Deteccion_De_Daños14_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños15_alpha = pygame.image.load("Imagenes/Det/0112.png")
	Deteccion_De_Daños15 = pygame.transform.scale(Deteccion_De_Daños15_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños16_alpha = pygame.image.load("Imagenes/Det/0120.png")
	Deteccion_De_Daños16 = pygame.transform.scale(Deteccion_De_Daños16_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños17_alpha = pygame.image.load("Imagenes/Det/0121.png")
	Deteccion_De_Daños17 = pygame.transform.scale(Deteccion_De_Daños17_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños18_alpha = pygame.image.load("Imagenes/Det/0122.png")
	Deteccion_De_Daños18 = pygame.transform.scale(Deteccion_De_Daños18_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños19_alpha = pygame.image.load("Imagenes/Det/0200.png")
	Deteccion_De_Daños19 = pygame.transform.scale(Deteccion_De_Daños19_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños20_alpha = pygame.image.load("Imagenes/Det/0201.png")
	Deteccion_De_Daños20 = pygame.transform.scale(Deteccion_De_Daños20_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños21_alpha = pygame.image.load("Imagenes/Det/0202.png")
	Deteccion_De_Daños21 = pygame.transform.scale(Deteccion_De_Daños21_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños22_alpha = pygame.image.load("Imagenes/Det/0210.png")
	Deteccion_De_Daños22 = pygame.transform.scale(Deteccion_De_Daños22_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños23_alpha = pygame.image.load("Imagenes/Det/0211.png")
	Deteccion_De_Daños23 = pygame.transform.scale(Deteccion_De_Daños23_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños24_alpha = pygame.image.load("Imagenes/Det/0212.png")
	Deteccion_De_Daños24 = pygame.transform.scale(Deteccion_De_Daños24_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños25_alpha = pygame.image.load("Imagenes/Det/0220.png")
	Deteccion_De_Daños25 = pygame.transform.scale(Deteccion_De_Daños25_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños26_alpha = pygame.image.load("Imagenes/Det/0221.png")
	Deteccion_De_Daños26 = pygame.transform.scale(Deteccion_De_Daños26_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños27_alpha = pygame.image.load("Imagenes/Det/0222.png")
	Deteccion_De_Daños27 = pygame.transform.scale(Deteccion_De_Daños27_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños28_alpha = pygame.image.load("Imagenes/Det/1000.png")
	Deteccion_De_Daños28 = pygame.transform.scale(Deteccion_De_Daños28_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños29_alpha = pygame.image.load("Imagenes/Det/1001.png")
	Deteccion_De_Daños29 = pygame.transform.scale(Deteccion_De_Daños29_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños30_alpha = pygame.image.load("Imagenes/Det/1002.png")
	Deteccion_De_Daños30 = pygame.transform.scale(Deteccion_De_Daños30_alpha, (tamañoControladorx, tamañoControladory))

	dire = "Imagenes/Barra/Barra6.png" #Copiar desde aquí
	barra_alpha = pygame.image.load(dire)
	barra = pygame.transform.scale(barra_alpha, (round(0.2265625 * ancho), round(0.20833333333333333333333333333333 * alto)))
	ventana.fill(negro)
	ventana.blit(barra, (round(0.38671875 * ancho), round(0.39583333333333333333333333333333 * alto)))
	ventana.blit(txt_1, (posxytxt_1[0], posxytxt_1[1]))
	pygame.display.update() #Hasta aqui

	Deteccion_De_Daños31_alpha = pygame.image.load("Imagenes/Det/1010.png")
	Deteccion_De_Daños31 = pygame.transform.scale(Deteccion_De_Daños31_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños32_alpha = pygame.image.load("Imagenes/Det/1011.png")
	Deteccion_De_Daños32 = pygame.transform.scale(Deteccion_De_Daños32_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños33_alpha = pygame.image.load("Imagenes/Det/1012.png")
	Deteccion_De_Daños33 = pygame.transform.scale(Deteccion_De_Daños33_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños34_alpha = pygame.image.load("Imagenes/Det/1020.png")
	Deteccion_De_Daños34 = pygame.transform.scale(Deteccion_De_Daños34_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños35_alpha = pygame.image.load("Imagenes/Det/1021.png")
	Deteccion_De_Daños35 = pygame.transform.scale(Deteccion_De_Daños35_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños36_alpha = pygame.image.load("Imagenes/Det/1022.png")
	Deteccion_De_Daños36 = pygame.transform.scale(Deteccion_De_Daños36_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños37_alpha = pygame.image.load("Imagenes/Det/1100.png")
	Deteccion_De_Daños37 = pygame.transform.scale(Deteccion_De_Daños37_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños38_alpha = pygame.image.load("Imagenes/Det/1101.png")
	Deteccion_De_Daños38 = pygame.transform.scale(Deteccion_De_Daños38_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños39_alpha = pygame.image.load("Imagenes/Det/1102.png")
	Deteccion_De_Daños39 = pygame.transform.scale(Deteccion_De_Daños39_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños40_alpha = pygame.image.load("Imagenes/Det/1110.png")
	Deteccion_De_Daños40 = pygame.transform.scale(Deteccion_De_Daños40_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños41_alpha = pygame.image.load("Imagenes/Det/1111.png")
	Deteccion_De_Daños41 = pygame.transform.scale(Deteccion_De_Daños41_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños42_alpha = pygame.image.load("Imagenes/Det/1112.png")
	Deteccion_De_Daños42 = pygame.transform.scale(Deteccion_De_Daños42_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños43_alpha = pygame.image.load("Imagenes/Det/1120.png")
	Deteccion_De_Daños43 = pygame.transform.scale(Deteccion_De_Daños43_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños44_alpha = pygame.image.load("Imagenes/Det/1121.png")
	Deteccion_De_Daños44 = pygame.transform.scale(Deteccion_De_Daños44_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños45_alpha = pygame.image.load("Imagenes/Det/1122.png")
	Deteccion_De_Daños45 = pygame.transform.scale(Deteccion_De_Daños45_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños46_alpha = pygame.image.load("Imagenes/Det/1200.png")
	Deteccion_De_Daños46 = pygame.transform.scale(Deteccion_De_Daños46_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños47_alpha = pygame.image.load("Imagenes/Det/1201.png")
	Deteccion_De_Daños47 = pygame.transform.scale(Deteccion_De_Daños47_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños48_alpha = pygame.image.load("Imagenes/Det/1202.png")
	Deteccion_De_Daños48 = pygame.transform.scale(Deteccion_De_Daños48_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños49_alpha = pygame.image.load("Imagenes/Det/1210.png")
	Deteccion_De_Daños49 = pygame.transform.scale(Deteccion_De_Daños49_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños50_alpha = pygame.image.load("Imagenes/Det/1211.png")
	Deteccion_De_Daños50 = pygame.transform.scale(Deteccion_De_Daños50_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños51_alpha = pygame.image.load("Imagenes/Det/1212.png")
	Deteccion_De_Daños51 = pygame.transform.scale(Deteccion_De_Daños51_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños52_alpha = pygame.image.load("Imagenes/Det/1220.png")
	Deteccion_De_Daños52 = pygame.transform.scale(Deteccion_De_Daños52_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños53_alpha = pygame.image.load("Imagenes/Det/1221.png")
	Deteccion_De_Daños53 = pygame.transform.scale(Deteccion_De_Daños53_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños54_alpha = pygame.image.load("Imagenes/Det/1222.png")
	Deteccion_De_Daños54 = pygame.transform.scale(Deteccion_De_Daños54_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños55_alpha = pygame.image.load("Imagenes/Det/2000.png")
	Deteccion_De_Daños55 = pygame.transform.scale(Deteccion_De_Daños55_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños56_alpha = pygame.image.load("Imagenes/Det/2001.png")
	Deteccion_De_Daños56 = pygame.transform.scale(Deteccion_De_Daños56_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños57_alpha = pygame.image.load("Imagenes/Det/2002.png")
	Deteccion_De_Daños57 = pygame.transform.scale(Deteccion_De_Daños57_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños58_alpha = pygame.image.load("Imagenes/Det/2010.png")
	Deteccion_De_Daños58 = pygame.transform.scale(Deteccion_De_Daños58_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños59_alpha = pygame.image.load("Imagenes/Det/2011.png")
	Deteccion_De_Daños59 = pygame.transform.scale(Deteccion_De_Daños59_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños60_alpha = pygame.image.load("Imagenes/Det/2012.png")
	Deteccion_De_Daños60 = pygame.transform.scale(Deteccion_De_Daños60_alpha, (tamañoControladorx, tamañoControladory))

	dire = "Imagenes/Barra/Barra7.png" #Copiar desde aquí
	barra_alpha = pygame.image.load(dire)
	barra = pygame.transform.scale(barra_alpha, (round(0.2265625 * ancho), round(0.20833333333333333333333333333333 * alto)))
	ventana.fill(negro)
	ventana.blit(barra, (round(0.38671875 * ancho), round(0.39583333333333333333333333333333 * alto)))
	ventana.blit(txt_1, (posxytxt_1[0], posxytxt_1[1]))
	pygame.display.update() #Hasta aqui

	Deteccion_De_Daños61_alpha = pygame.image.load("Imagenes/Det/2020.png")
	Deteccion_De_Daños61 = pygame.transform.scale(Deteccion_De_Daños61_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños62_alpha = pygame.image.load("Imagenes/Det/2021.png")
	Deteccion_De_Daños62 = pygame.transform.scale(Deteccion_De_Daños62_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños63_alpha = pygame.image.load("Imagenes/Det/2022.png")
	Deteccion_De_Daños63 = pygame.transform.scale(Deteccion_De_Daños63_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños64_alpha = pygame.image.load("Imagenes/Det/2100.png")
	Deteccion_De_Daños64 = pygame.transform.scale(Deteccion_De_Daños64_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños65_alpha = pygame.image.load("Imagenes/Det/2101.png")
	Deteccion_De_Daños65 = pygame.transform.scale(Deteccion_De_Daños65_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños66_alpha = pygame.image.load("Imagenes/Det/2102.png")
	Deteccion_De_Daños66 = pygame.transform.scale(Deteccion_De_Daños66_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños67_alpha = pygame.image.load("Imagenes/Det/2110.png")
	Deteccion_De_Daños67 = pygame.transform.scale(Deteccion_De_Daños67_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños68_alpha = pygame.image.load("Imagenes/Det/2111.png")
	Deteccion_De_Daños68 = pygame.transform.scale(Deteccion_De_Daños68_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños69_alpha = pygame.image.load("Imagenes/Det/2112.png")
	Deteccion_De_Daños69 = pygame.transform.scale(Deteccion_De_Daños69_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños70_alpha = pygame.image.load("Imagenes/Det/2120.png")
	Deteccion_De_Daños70 = pygame.transform.scale(Deteccion_De_Daños70_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños71_alpha = pygame.image.load("Imagenes/Det/2121.png")
	Deteccion_De_Daños71 = pygame.transform.scale(Deteccion_De_Daños71_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños72_alpha = pygame.image.load("Imagenes/Det/2122.png")
	Deteccion_De_Daños72 = pygame.transform.scale(Deteccion_De_Daños72_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños73_alpha = pygame.image.load("Imagenes/Det/2200.png")
	Deteccion_De_Daños73 = pygame.transform.scale(Deteccion_De_Daños73_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños74_alpha = pygame.image.load("Imagenes/Det/2201.png")
	Deteccion_De_Daños74 = pygame.transform.scale(Deteccion_De_Daños74_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños75_alpha = pygame.image.load("Imagenes/Det/2202.png")
	Deteccion_De_Daños75 = pygame.transform.scale(Deteccion_De_Daños75_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños76_alpha = pygame.image.load("Imagenes/Det/2210.png")
	Deteccion_De_Daños76 = pygame.transform.scale(Deteccion_De_Daños76_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños77_alpha = pygame.image.load("Imagenes/Det/2211.png")
	Deteccion_De_Daños77 = pygame.transform.scale(Deteccion_De_Daños77_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños78_alpha = pygame.image.load("Imagenes/Det/2212.png")
	Deteccion_De_Daños78 = pygame.transform.scale(Deteccion_De_Daños78_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños79_alpha = pygame.image.load("Imagenes/Det/2220.png")
	Deteccion_De_Daños79 = pygame.transform.scale(Deteccion_De_Daños79_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños80_alpha = pygame.image.load("Imagenes/Det/2221.png")
	Deteccion_De_Daños80 = pygame.transform.scale(Deteccion_De_Daños80_alpha, (tamañoControladorx, tamañoControladory))
	Deteccion_De_Daños81_alpha = pygame.image.load("Imagenes/Det/2222.png")
	Deteccion_De_Daños81 = pygame.transform.scale(Deteccion_De_Daños81_alpha, (tamañoControladorx, tamañoControladory))

	Moneda_Oro_0_alpha = pygame.image.load("Imagenes/Monedas/Moneda_De_Oro_0.png")
	Moneda_Oro_0 = pygame.transform.scale(Moneda_Oro_0_alpha, (18, 26))
	Moneda_Oro_1_alpha = pygame.image.load("Imagenes/Monedas/Moneda_De_Oro_1.png")
	Moneda_Oro_1 = pygame.transform.scale(Moneda_Oro_1_alpha, (18, 26))

	Moneda_Diamante_0_alpha = pygame.image.load("Imagenes/Monedas/Moneda_De_Diamante_0.png")
	Moneda_Diamante_0 = pygame.transform.scale(Moneda_Diamante_0_alpha, (18, 26))
	Moneda_Diamante_1_alpha = pygame.image.load("Imagenes/Monedas/Moneda_De_Diamante_1.png")
	Moneda_Diamante_1 = pygame.transform.scale(Moneda_Diamante_1_alpha, (18, 26))

	Moneda_Esmeralda_0_alpha = pygame.image.load("Imagenes/Monedas/Moneda_De_Esmeralda_0.png")
	Moneda_Esmeralda_0 = pygame.transform.scale(Moneda_Esmeralda_0_alpha, (18, 26))
	Moneda_Esmeralda_1_alpha = pygame.image.load("Imagenes/Monedas/Moneda_De_Esmeralda_1.png")
	Moneda_Esmeralda_1 = pygame.transform.scale(Moneda_Esmeralda_1_alpha, (18, 26))

	Moneda_0_Negra_alpha = pygame.image.load("Imagenes/Monedas/Moneda_0_Negra.png")
	Moneda_0_Negra = pygame.transform.scale(Moneda_0_Negra_alpha, (18, 26))
	Moneda_1_Negra_alpha = pygame.image.load("Imagenes/Monedas/Moneda_1_Negra.png")
	Moneda_1_Negra = pygame.transform.scale(Moneda_1_Negra_alpha, (18, 26))

	monedas_Imag = [Moneda_Oro_0, Moneda_Oro_1, Moneda_Diamante_0, Moneda_Diamante_1, Moneda_Esmeralda_0, Moneda_Esmeralda_1]
	monedas_Negras_Imag = [Moneda_0_Negra, Moneda_1_Negra]

	listbase2 = ["0000", "0001", "0002", "0010", "0011", "0012", "0020", "0021", "0022", "0100", "0101", "0102", "0110", "0111", "0112", "0120", "0121", "0122", "0200", "0201", "0202", "0210", "0211", "0212", "0220", "0221", "0222", "1000", "1001", "1002", "1010", "1011", "1012", "1020", "1021", "1022", "1100", "1101", "1102", "1110", "1111", "1112", "1120", "1121", "1122", "1200", "1201", "1202", "1210", "1211", "1212", "1220", "1221", "1222", "2000", "2001", "2002", "2010", "2011", "2012", "2020", "2021", "2022", "2100", "2101", "2102", "2110", "2111", "2112", "2120", "2121", "2122", "2200", "2201", "2202", "2210", "2211", "2212", "2220", "2221", "2222"]

	Ordinal = ["Primera", "Segunda", "Tercera", "Cuarta", "Quinta", "Sexta", "Séptima", "Octava", "Novena", "Décima"]

	listDet = [Deteccion_De_Daños1, Deteccion_De_Daños2, Deteccion_De_Daños3, Deteccion_De_Daños4, Deteccion_De_Daños5, Deteccion_De_Daños6, Deteccion_De_Daños7, Deteccion_De_Daños8, Deteccion_De_Daños9, Deteccion_De_Daños10, Deteccion_De_Daños11, Deteccion_De_Daños12, Deteccion_De_Daños13, Deteccion_De_Daños14, Deteccion_De_Daños15, Deteccion_De_Daños16, Deteccion_De_Daños17, Deteccion_De_Daños18, Deteccion_De_Daños19, Deteccion_De_Daños20, Deteccion_De_Daños21, Deteccion_De_Daños22, Deteccion_De_Daños23, Deteccion_De_Daños24, Deteccion_De_Daños25, Deteccion_De_Daños26, Deteccion_De_Daños27, Deteccion_De_Daños28, Deteccion_De_Daños29, Deteccion_De_Daños30, Deteccion_De_Daños31, Deteccion_De_Daños32, Deteccion_De_Daños33, Deteccion_De_Daños34, Deteccion_De_Daños35, Deteccion_De_Daños36, Deteccion_De_Daños37, Deteccion_De_Daños38, Deteccion_De_Daños39, Deteccion_De_Daños40, Deteccion_De_Daños41, Deteccion_De_Daños42, Deteccion_De_Daños43, Deteccion_De_Daños44, Deteccion_De_Daños45, Deteccion_De_Daños46, Deteccion_De_Daños47, Deteccion_De_Daños48, Deteccion_De_Daños49, Deteccion_De_Daños50, Deteccion_De_Daños51, Deteccion_De_Daños52, Deteccion_De_Daños53, Deteccion_De_Daños54, Deteccion_De_Daños55, Deteccion_De_Daños56, Deteccion_De_Daños57, Deteccion_De_Daños58, Deteccion_De_Daños59, Deteccion_De_Daños60, Deteccion_De_Daños61, Deteccion_De_Daños62, Deteccion_De_Daños63, Deteccion_De_Daños64, Deteccion_De_Daños65, Deteccion_De_Daños66, Deteccion_De_Daños67, Deteccion_De_Daños68, Deteccion_De_Daños69, Deteccion_De_Daños70, Deteccion_De_Daños71, Deteccion_De_Daños72, Deteccion_De_Daños73, Deteccion_De_Daños74, Deteccion_De_Daños75, Deteccion_De_Daños76, Deteccion_De_Daños77, Deteccion_De_Daños78, Deteccion_De_Daños79, Deteccion_De_Daños80, Deteccion_De_Daños81]

	dire = "Imagenes/Barra/Barra8.png" #Copiar desde aquí
	barra_alpha = pygame.image.load(dire)
	barra = pygame.transform.scale(barra_alpha, (round(0.2265625 * ancho), round(0.20833333333333333333333333333333 * alto)))
	ventana.fill(negro)
	ventana.blit(barra, (round(0.38671875 * ancho), round(0.39583333333333333333333333333333 * alto)))
	ventana.blit(txt_1, (posxytxt_1[0], posxytxt_1[1]))
	pygame.display.update() #Hasta aqui

	### ========== ESTADO DE LA NAVE AMIGA ========== ###

	alaDerecha = True
	vida_alaDerecha = 10
	vida_alaDerecha_org = vida_alaDerecha
	porcent_vida_alaDerecha = (vida_alaDerecha/vida_alaDerecha_org)* 100

	alaIzquierda = True
	vida_alaIzquierda = 10
	vida_alaIzquierda_org = vida_alaIzquierda
	porcent_vida_alaIzquierda = (vida_alaIzquierda/vida_alaIzquierda_org)* 100

	motor = True
	vida_motor = 10
	vida_motor_org = vida_motor
	porcent_vida_motor = (vida_motor/vida_motor_org)* 100

	frontal = True
	vida_frontal = 10
	vida_frontal_org = vida_frontal
	porcent_vida_frontal = (vida_frontal/vida_frontal_org)* 100

	tipos_de_vidas = [frontal, motor, alaDerecha, alaIzquierda]

	caracteristicas = [vida_alaDerecha, vida_alaDerecha_org, vida_alaIzquierda, vida_alaIzquierda_org, vida_motor, vida_motor_org, vida_frontal, vida_frontal_org, alaDerecha, alaIzquierda, motor, frontal]

	def generar_fondo(ventana):

		pygame.draw.line(ventana, colorline, (posxline1, 0), (posxline1, alto), tamañoline)
		pygame.draw.line(ventana, colorline, (posxline2, 0), (posxline2, alto), tamañoline)
		pygame.draw.line(ventana, colorline, (0, posy2rec1), (posxline1, posy2rec1), tamañoline)
		pygame.draw.line(ventana, colorline, (posxline2, posy2rec1), (ancho, posy2rec1), tamañoline)

	def actualizar_pantalla_derecha_arriba(ventana, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, Mostrar, infinito, segundostranscurridos):

		pygame.draw.rect(ventana, negro, (0, 0, posxline1 - tamañoline + 2, posy2rec1 - tamañoline + 2))

		if infinito == True:

			txt1_AD, posxytxt1_AD = print_pantalla("Nivel Infinito: " + str(Lv_act), 0, posytxt_derecha_ariba * 0, tamañotxt1, colortxt, fuente)

		else:

			txt1_AD, posxytxt1_AD = print_pantalla("Nivel: " + str(Lv_act), 0, posytxt_derecha_ariba * 0, tamañotxt1, colortxt, fuente)

		txt2_AD, posxytxt2_AD = print_pantalla("Porcentaje: " + str(porcentaje) + "%", 0, posytxt_derecha_ariba * 1, tamañotxt1, colortxt, fuente)
		txt3_AD, posxytxt3_AD = print_pantalla("Naves destruidas: " + str(Naves_destruidas), 0, posytxt_derecha_ariba * 2, tamañotxt1, colortxt, fuente)

		if infinito == True:
			txt4_AD, posxytxt4_AD = print_pantalla("Naves totales: ∞", 0, posytxt_derecha_ariba * 3, tamañotxt1, colortxt, fuente)

		else:
			txt4_AD, posxytxt4_AD = print_pantalla("Naves totales: " + str(Nº_Naves), 0, posytxt_derecha_ariba * 3, tamañotxt1, colortxt, fuente)

		txt5_AD, posxytxt5_AD = print_pantalla("Monedas recogidas: " + str(Monedas), 0, posytxt_derecha_ariba * 4, tamañotxt1, colortxt, fuente) #A partir de aqui se pondran las mejoras compadas en la tienda
		txt6_AD, posxytxt6_AD = print_pantalla("Minutos:" + str(math.floor(segundostranscurridos/60)) + " Segundos: " + str(segundostranscurridos%60), 0, posytxt_derecha_ariba * 5, tamañotxt1, colortxt, fuente)

		if Mostrar == True:

			txt7_AD, posxytxt7_AD = print_pantalla("FPS: " + str(FPS), 0, posytxt_derecha_ariba * 6, tamañotxt1, colortxt, fuente)

		else:
			txt7_AD = ["", ""]
			posxytxt7_AD = ""

		return((txt1_AD, posxytxt1_AD), (txt2_AD, posxytxt2_AD), (txt3_AD, posxytxt3_AD), (txt4_AD, posxytxt4_AD), (txt5_AD, posxytxt5_AD), (txt6_AD, posxytxt6_AD), (txt7_AD, posxytxt7_AD))

	def actualizar_pantalla_derecha_debajo(ventana):
		
		pygame.draw.rect(ventana, negro, (0, posy2rec1 + tamañoline - 2, posxline1 - tamañoline + 2, alto))

		i = 0

		nivel_de_aparecimiento_1 = []

		while i < Lv_act:
			nivel_de_aparecimiento_1.append(nivel_de_aparecimiento[i])
			i += 1

		cant_unos = nivel_de_aparecimiento_1.count(1)

		if cant_unos > 0: #Nave Tipo 1

			txt1_DD, posxytxt1_DD = print_pantalla("Nave Exploradora nº1: " , 0, posytxt_derecha_debajo * 0 + posy2rec1, tamañotxt1, colortxt, fuente)
			Nave_Tipo1_alpha = pygame.image.load("Imagenes/Naves_Enemigas/EBEN1.png")
			Nave_Tipo1 = pygame.transform.scale(Nave_Tipo1_alpha, (round(0.03125 * ancho), round(0.03055555555555555555555555555556 * alto))) # 20 X 11 to 40 X 22

		else:

			txt1_DD, posxytxt1_DD = print_pantalla("Nave: ¿?" , 0, posytxt_derecha_debajo * 0 + posy2rec1, tamañotxt1, colortxt, fuente)
			Nave_Tipo1 = ""

		if cant_unos > 1: #Nave Tipo 2

			txt2_DD, posxytxt2_DD = print_pantalla("Nave Exploradora nº2: " , 0, posytxt_derecha_debajo * 1 + posy2rec1, tamañotxt1, colortxt, fuente)
			Nave_Tipo2_alpha = pygame.image.load("Imagenes/Naves_Enemigas/EBEN2.png")
			Nave_Tipo2 = pygame.transform.scale(Nave_Tipo2_alpha, (round(0.03125 * ancho), round(0.03055555555555555555555555555556 * alto))) # 20 X 11

		else:

			txt2_DD, posxytxt2_DD = print_pantalla("Nave: ¿?" , 0, posytxt_derecha_debajo * 1 + posy2rec1, tamañotxt1, colortxt, fuente)
			Nave_Tipo2 = ""

		if cant_unos > 2: #Nave Tipo 3

			txt3_DD, posxytxt3_DD = print_pantalla("Nave Exploradora nº3: " , 0, posytxt_derecha_debajo * 2 + posy2rec1, tamañotxt1, colortxt, fuente)
			Nave_Tipo3_alpha = pygame.image.load("Imagenes/Naves_Enemigas/EBEN3.png")
			Nave_Tipo3 = pygame.transform.scale(Nave_Tipo3_alpha, (round(0.03125 * ancho), round(0.03055555555555555555555555555556 * alto))) # 20 X 11

		else:

			txt3_DD, posxytxt3_DD = print_pantalla("Nave: ¿?" , 0, posytxt_derecha_debajo * 2 + posy2rec1, tamañotxt1, colortxt, fuente)
			Nave_Tipo3 = ""

		if cant_unos > 3: #Nave Tipo 4

			txt4_DD, posxytxt4_DD = print_pantalla("Nave Defensora nº1: " , 0, posytxt_derecha_debajo * 3 + posy2rec1, tamañotxt1, colortxt, fuente)
			Nave_Tipo4_alpha = pygame.image.load("Imagenes/Naves_Enemigas/EBEN4.png")
			Nave_Tipo4 = pygame.transform.scale(Nave_Tipo4_alpha, (round(0.028125 * ancho), round(0.04166666666666666666666666666667 * alto))) # 18 X 15

		else:

			txt4_DD, posxytxt4_DD = print_pantalla("Nave: ¿?" , 0, posytxt_derecha_debajo * 3 + posy2rec1, tamañotxt1, colortxt, fuente)
			Nave_Tipo4 = ""

		if cant_unos > 4:

			txt5_DD, posxytxt5_DD = print_pantalla("Nave Defensora nº2: " , 0, posytxt_derecha_debajo * 4 + posy2rec1, tamañotxt1, colortxt, fuente)
			Nave_Tipo5_alpha = pygame.image.load("Imagenes/Naves_Enemigas/EBEN5.png")
			Nave_Tipo5 = pygame.transform.scale(Nave_Tipo5_alpha, (round(0.028125 * ancho), round(0.04166666666666666666666666666667 * alto))) # 18 X 15

		else:

			txt5_DD, posxytxt5_DD = print_pantalla("Nave: ¿?" , 0, posytxt_derecha_debajo * 4 + posy2rec1, tamañotxt1, colortxt, fuente)
			Nave_Tipo5 = ""

		if cant_unos > 5:

			txt6_DD, posxytxt6_DD = print_pantalla("Nave Nuclear: " , 0, posytxt_derecha_debajo * 5 + posy2rec1, tamañotxt1, colortxt, fuente)
			Nave_Tipo6_alpha = pygame.image.load("Imagenes/Naves_Enemigas/EBEN6.png")
			Nave_Tipo6 = pygame.transform.scale(Nave_Tipo6_alpha, (round(0.028125 * ancho), round(0.04583333333333333333333333333333 * alto))) # 24 X 22

		else:

			txt6_DD, posxytxt6_DD = print_pantalla("Nave: ¿?" , 0, posytxt_derecha_debajo * 5 + posy2rec1, tamañotxt1, colortxt, fuente)
			Nave_Tipo6 = ""

		if cant_unos > 6:

			txt7_DD, posxytxt7_DD = print_pantalla("Nave Interceptora: " , 0, posytxt_derecha_debajo * 6 + posy2rec1, tamañotxt1, colortxt, fuente)
			Nave_Tipo7_alpha = pygame.image.load("Imagenes/Naves_Enemigas/EBEN7_1.png")
			Nave_Tipo7 = pygame.transform.scale(Nave_Tipo7_alpha, (round(0.0265625 * ancho), round(0.05 * alto))) # 17 X 18

		else:

			txt7_DD, posxytxt7_DD = print_pantalla("Nave: ¿?" , 0, posytxt_derecha_debajo * 6 + posy2rec1, tamañotxt1, colortxt, fuente)
			Nave_Tipo7 = ""

		if cant_unos > 7:

			txt8_DD, posxytxt8_DD = print_pantalla("Nave Comandante: " , 0, posytxt_derecha_debajo * 7 + posy2rec1, tamañotxt1, colortxt, fuente)
			Nave_Tipo8_alpha = pygame.image.load("Imagenes/Naves_Enemigas/EBEN8_1.png")
			Nave_Tipo8 = pygame.transform.scale(Nave_Tipo8_alpha, (round(0.0265625 * ancho), round(0.05 * alto))) # 17 X 18

		else:

			txt8_DD, posxytxt8_DD = print_pantalla("Nave: ¿?" , 0, posytxt_derecha_debajo * 7 + posy2rec1, tamañotxt1, colortxt, fuente)
			Nave_Tipo8 = ""

		if cant_unos > 8:

			txt9_DD, posxytxt9_DD = print_pantalla("Nave Tipo9: " , 0, posytxt_derecha_debajo * 8 + posy2rec1, tamañotxt1, colortxt, fuente)

		else:

			txt9_DD, posxytxt9_DD = print_pantalla("Nave: ¿?" , 0, posytxt_derecha_debajo * 8 + posy2rec1, tamañotxt1, colortxt, fuente)

		if cant_unos > 9:

			txt10_DD, posxytxt10_DD = print_pantalla("Nave Tipo10: " , 0, posytxt_derecha_debajo * 9 + posy2rec1, tamañotxt1, colortxt, fuente)

		else:

			txt10_DD, posxytxt10_DD = print_pantalla("Nave: ¿?" , 0, posytxt_derecha_debajo * 9 + posy2rec1, tamañotxt1, colortxt, fuente)

		return((txt1_DD, posxytxt1_DD), (txt2_DD, posxytxt2_DD), (txt3_DD, posxytxt3_DD), (txt4_DD, posxytxt4_DD), (txt5_DD, posxytxt5_DD), (txt6_DD, posxytxt6_DD), (txt7_DD, posxytxt7_DD), (txt8_DD, posxytxt8_DD), (txt9_DD, posxytxt9_DD), (txt10_DD, posxytxt10_DD), Nave_Tipo1, Nave_Tipo2, Nave_Tipo3, Nave_Tipo4, Nave_Tipo5, Nave_Tipo6, Nave_Tipo7, Nave_Tipo8)

	def actualizar_pantalla_izquierda_arriba(ventana, caracteristicas):

		vida_alaDerecha = caracteristicas[0]
		vida_alaDerecha_org = caracteristicas[1]
		vida_alaIzquierda = caracteristicas[2]
		vida_alaIzquierda_org = caracteristicas[3]
		vida_motor = caracteristicas[4]
		vida_motor_org = caracteristicas[5]
		vida_frontal = caracteristicas[6]
		vida_frontal_org = caracteristicas[7]
		alaDerecha = caracteristicas[8]
		alaIzquierda = caracteristicas[9]
		motor = caracteristicas[10]
		frontal = caracteristicas[11]
		
		pygame.draw.rect(ventana, negro, (posxline2 + tamañoline, 0, ancho, posy2rec1))

		txt1_AI, posxytxt1_AI = print_pantalla("Controlador de daños:", posxline2 + tamañoline, 0 + tamañoline, tamañotxt1, colortxt, fuente)

		viva = True

		destruidos = 0

		###########################################

		if vida_alaDerecha == vida_alaDerecha_org:
			numero3 = "0"

		elif vida_alaDerecha < 1:
			numero3 = "2"
			alaDerecha = False
			destruidos += 1

		elif vida_alaDerecha < vida_alaDerecha_org:
			numero3 = "1"

		###########################################

		if vida_alaIzquierda == vida_alaIzquierda_org:
			numero4 = "0"

		elif vida_alaIzquierda < 1:
			numero4 = "2"
			alaIzquierda = False
			destruidos += 1

		elif vida_alaIzquierda < vida_alaIzquierda_org:
			numero4 = "1"

		###########################################

		if vida_motor == vida_motor_org:
			numero2 = "0"

		elif vida_motor < 1:
			numero2 = "2"
			motor = False
			viva = False

		elif vida_motor < vida_motor_org:
			numero2 = "1"

		###########################################

		if vida_frontal == vida_frontal_org:
			numero1 = "0"

		elif vida_frontal < 1:
			numero1 = "2"
			frontal = False
			destruidos += 1

		elif vida_frontal < vida_frontal_org:
			numero1 = "1"

		###########################################

		if destruidos > 1:
			viva = False

		if viva == False:
			numeroimag = "2222"

		else:
			numeroimag = numero1 + numero2 + numero3 + numero4

		ident = listbase2.index(numeroimag)

		imag = listDet[ident]

		return((txt1_AI, posxytxt1_AI), imag, vida_alaDerecha, vida_alaIzquierda, vida_motor, vida_frontal, viva, alaDerecha, alaIzquierda, motor, frontal)

	def actualizar_pantalla_izquierda_debajo(ventana, mensajelinesenemigo = None, mensajelinesenviados = None): # Lines max = 8 De momento

		pygame.draw.rect(ventana, negro, (posxline2, posy2rec1, ancho, alto))
		
		txt1_DI, posxytxt1_DI = print_pantalla("Chat:", posxline2 + tamañoline, posy2rec1 + tamañoline, tamañotxt1, colortxt, fuente)
		txt2_DI, posxytxt2_DI = print_pantalla("Mensajes recibidos:", posxline2 + tamañoline, posy2rec1 + tamañoline + possumando_izquierda_abajo, tamañotxt1, rojo, fuente)
		txt3_DI, posxytxt3_DI = print_pantalla("Mensajes enviados:", posxline2 + tamañoline, posy2rec1 + tamañoline + round(possumando_izquierda_abajo * 5), tamañotxt1, verde, fuente)

		if mensajelinesenemigo != None:

			try: # Txt 1
				txt4_DI, posxytxt4_DI = print_pantalla(str(mensajelinesenemigo[0]), posxline2 + tamañoline, posy2rec1 + tamañoline + possumando_izquierda_abajo * 2, round(tamañotxt1/2), blanco, fuente)

			except:
				txt4_DI = ["", ""]
				posxytxt4_DI = ""

			try: # Txt 2
				txt5_DI, posxytxt5_DI = print_pantalla(str(mensajelinesenemigo[1]), posxline2 + tamañoline, posy2rec1 + tamañoline + round(possumando_izquierda_abajo * 2.5), round(tamañotxt1/2), blanco, fuente)

			except:
				txt5_DI = ["", ""]
				posxytxt5_DI = ""

			try: # Txt 3
				txt6_DI, posxytxt6_DI = print_pantalla(str(mensajelinesenemigo[2]), posxline2 + tamañoline, posy2rec1 + tamañoline + possumando_izquierda_abajo * 3, round(tamañotxt1/2), blanco, fuente)

			except:
				txt6_DI = ["", ""]
				posxytxt6_DI = ""

			try: # Txt 4
				txt7_DI, posxytxt7_DI = print_pantalla(str(mensajelinesenemigo[3]), posxline2 + tamañoline, posy2rec1 + tamañoline + round(possumando_izquierda_abajo * 3.5), round(tamañotxt1/2), blanco, fuente)

			except:
				txt7_DI = ["", ""]
				posxytxt7_DI = ""

			try: # Txt 5
				txt8_DI, posxytxt8_DI = print_pantalla(str(mensajelinesenemigo[4]), posxline2 + tamañoline, posy2rec1 + tamañoline + possumando_izquierda_abajo * 4, round(tamañotxt1/2), blanco, fuente)

			except:
				txt8_DI = ["", ""]
				posxytxt8_DI = ""

			try: # Txt 6
				txt9_DI, posxytxt9_DI = print_pantalla(str(mensajelinesenemigo[5]), posxline2 + tamañoline, posy2rec1 + tamañoline + possumando_izquierda_abajo * 4.5, round(tamañotxt1/2), blanco, fuente)

			except:
				txt9_DI = ["", ""]
				posxytxt9_DI = ""

		else:
			txt4_DI = ["", ""]
			posxytxt4_DI = ""

			txt5_DI = ["", ""]
			posxytxt5_DI = ""

			txt6_DI, posxytxt6_DI = print_pantalla("Ningun mensaje recibido", posxline2 + tamañoline + plusninguno, posy2rec1 + tamañoline + possumando_izquierda_abajo * 3, round(tamañotxt1/1.5), gris_fondo, fuente)

			txt7_DI = ["", ""]
			posxytxt7_DI = ""

			txt8_DI = ["", ""]
			posxytxt8_DI = ""

			txt9_DI = ["", ""]
			posxytxt9_DI = ""

		if mensajelinesenviados != None:

			try: # Txt 1
				txt10_DI, posxytxt10_DI = print_pantalla(str(mensajelinesenviados[0]), posxline2 + tamañoline, posy2rec1 + tamañoline + possumando_izquierda_abajo * 6, round(tamañotxt1/2), blanco, fuente)

			except:
				txt10_DI = ["", ""]
				posxytxt10_DI = ""

			try: # Txt 2
				txt11_DI, posxytxt11_DI = print_pantalla(str(mensajelinesenviados[1]), posxline2 + tamañoline, posy2rec1 + tamañoline + round(possumando_izquierda_abajo * 6.5), round(tamañotxt1/2), blanco, fuente)

			except:
				txt11_DI = ["", ""]
				posxytxt11_DI = ""

			try: # Txt 3
				txt12_DI, posxytxt12_DI = print_pantalla(str(mensajelinesenviados[2]), posxline2 + tamañoline, posy2rec1 + tamañoline + possumando_izquierda_abajo * 7, round(tamañotxt1/2), blanco, fuente)

			except:
				txt12_DI = ["", ""]
				posxytxt12_DI = ""

			try: # Txt 4
				txt13_DI, posxytxt13_DI = print_pantalla(str(mensajelinesenviados[3]), posxline2 + tamañoline, posy2rec1 + tamañoline + round(possumando_izquierda_abajo * 7.5), round(tamañotxt1/2), blanco, fuente)

			except:
				txt13_DI = ["", ""]
				posxytxt13_DI = ""

			try: # Txt 5
				txt14_DI, posxytxt14_DI = print_pantalla(str(mensajelinesenviados[4]), posxline2 + tamañoline, posy2rec1 + tamañoline + possumando_izquierda_abajo * 8, round(tamañotxt1/2), blanco, fuente)

			except:
				txt14_DI = ["", ""]
				posxytxt14_DI = ""

			try: # Txt 6
				txt15_DI, posxytxt15_DI = print_pantalla(str(mensajelinesenviados[5]), posxline2 + tamañoline, posy2rec1 + tamañoline + possumando_izquierda_abajo * 8.5, round(tamañotxt1/2), blanco, fuente)

			except:
				txt15_DI = ["", ""]
				posxytxt15_DI = ""

		else:

			txt10_DI = ["", ""]
			posxytxt10_DI = ""

			txt11_DI = ["", ""]
			posxytxt11_DI = ""

			txt12_DI, posxytxt12_DI = print_pantalla("Ningún mensaje enviado", posxline2 + tamañoline + plusninguno, posy2rec1 + tamañoline + possumando_izquierda_abajo * 7, round(tamañotxt1/1.5), gris_fondo, fuente)

			txt13_DI = ["", ""]
			posxytxt13_DI = ""

			txt14_DI = ["", ""]
			posxytxt14_DI = ""

			txt15_DI = ["", ""]
			posxytxt15_DI = ""

		return((txt1_DI, posxytxt1_DI), (txt2_DI, posxytxt2_DI), (txt3_DI, posxytxt3_DI), (txt4_DI, posxytxt4_DI), (txt5_DI, posxytxt5_DI), (txt6_DI, posxytxt6_DI), (txt7_DI, posxytxt7_DI), (txt8_DI, posxytxt8_DI), (txt9_DI, posxytxt9_DI), (txt10_DI, posxytxt10_DI), (txt11_DI, posxytxt11_DI), (txt12_DI, posxytxt12_DI), (txt13_DI, posxytxt13_DI), (txt14_DI, posxytxt14_DI), (txt15_DI, posxytxt15_DI))

	def generar_juego(ventana, user_act, Lv_act, demo, Nº_Naves):
		pygame.draw.rect(ventana, negro, (posxline1 + tamañoline, 0, 640 - tamañoline - 1, alto))

	def generar_oleada(ventana, sprites, clasificacion_sprites):
		pass

	def calcularx(letras):

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

	def crear_texto_en_pantalla(ventana, texto, tiempo_en_pantalla):
		posxtxt_centre = ancho/2 - (calcularx(texto))/2
		txt_centre, posxytxt_centre = print_pantalla(texto, posxtxt_centre, alto/2 - tamañotxt1/2, tamañotxt1, blanco, fuente)
		ventana.blit(txt_centre, (posxytxt_centre[0], posxytxt_centre[1]))
		pygame.display.update()
		time.sleep(tiempo_en_pantalla)

		if datetime.now().hour < 10:
			hora = "0" + str(datetime.now().hour)

		else:
			hora = datetime.now().hour

		if datetime.now().minute < 10:
			minuto = "0" + str(datetime.now().minute)

		else:
			minuto = datetime.now().minute

		if datetime.now().second < 10:
			segundo = "0" + str(datetime.now().second)

		else:
			segundo = datetime.now().second

		strpos = str(hora) + str(minuto) + str(segundo)
		nwstrpos = strpos
		r = 255
		g = 255
		b = 255

		while int(strpos) + 2 > int(nwstrpos):
			if r > 2:
				r -= 1
				g -= 1
				b -= 1

			txt_centre, posxytxt_centre = print_pantalla(texto, posxtxt_centre, alto/2 - tamañotxt1/2, tamañotxt1, (r, g, b), fuente)
			ventana.blit(txt_centre, (posxytxt_centre[0], posxytxt_centre[1]))
			pygame.display.update()

			if datetime.now().hour < 10:
				hora = "0" + str(datetime.now().hour)

			else:
				hora = datetime.now().hour

			if datetime.now().minute < 10:
				minuto = "0" + str(datetime.now().minute)

			else:
				minuto = datetime.now().minute

			if datetime.now().second < 10:
				segundo = "0" + str(datetime.now().second)

			else:
				segundo = datetime.now().second

			nwstrpos = str(hora) + str(minuto) + str(segundo)

		txt_centre, posxytxt_centre = print_pantalla(texto, posxtxt_centre, alto/2 - tamañotxt1/2, tamañotxt1, negro, fuente)
		ventana.blit(txt_centre, (posxytxt_centre[0], posxytxt_centre[1]))
		pygame.display.update()

	def ejecutar_daño_CAC(escudo):

		nave.recibirdañoEBA(dañocac)
					
		if escudo == True:
			viva = True
			escudo = False

		else:
			viva = False

		return [viva, escudo]

	porcentaje = 0
	Naves_destruidas = 0
	Monedas = 0

	second = datetime.now().second
	microsecond = datetime.now().microsecond

	x = 0
	y = 0

	xn = ancho/2 - 21
	yn = alto/4 * 3

	radio = 30

	oleada = 1

	### ========== PROYECTILES AMIGOS ========== ###

	nºdisparos = 1

	segundostranscurridos = 0

	velocidad_de_disparo_amigo = 300

	tiempo_de_diferencia_entre_disparos = 450000 #En microsegundos con base 6

	tiempo_disparo_amigo_ant = 0

	tipodeproyectilamigo = 0 #0 = Blanco, 1 = Rojo, 2 = Azul, 3 = Amarillo

	### ========== ESTRELLAS ========== ###

	estrellasmoviendose = ajustes[8]

	estrellasparpadeando = True

	estrellasenpantalla = True

	velocidadparpadeo = 40 #Cantidad de frames que tiene que esperar para poder elegir encendida y apagada

	velocidades = [0.2, 0.1, 0.05]

	### ========== VSync ========== ###

	VSyncactivado = ajustes[10]

	### ========== FPS ========== ###

	FPS = 0
	fpsactivos = False
	cambioFps = False

	MaxFPS = int(ajustes[9])
	sumer = MaxFPS

	### ========== CARACTERISTICAS DE LA NAVE AMIGA ========== ###

	viva = True
	escudo = True
	dañocac = 10
	tamañox = 42
	tamañoy = 26
	nave_prin_explotando = False

	dire = "Imagenes/Barra/Barra9.png" #Copiar desde aquí
	barra_alpha = pygame.image.load(dire)
	barra = pygame.transform.scale(barra_alpha, (round(0.2265625 * ancho), round(0.20833333333333333333333333333333 * alto)))
	ventana.fill(negro)
	ventana.blit(barra, (round(0.38671875 * ancho), round(0.39583333333333333333333333333333 * alto)))
	ventana.blit(txt_1, (posxytxt_1[0], posxytxt_1[1]))
	pygame.display.update() #Hasta aqui

	resultados = actualizar_pantalla_derecha_arriba(ventana, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, False, infinito, segundostranscurridos)

	txt1_AD, posxytxt1_AD = resultados[0]
	txt2_AD, posxytxt2_AD = resultados[1]
	txt3_AD, posxytxt3_AD = resultados[2]
	txt4_AD, posxytxt4_AD = resultados[3]
	txt5_AD, posxytxt5_AD = resultados[4]
	txt6_AD, posxytxt6_AD = resultados[5]
	txt7_AD, posxytxt7_AD = resultados[6]

	resultados2 = actualizar_pantalla_derecha_debajo(ventana)

	txt1_DD, posxytxt1_DD = resultados2[0]
	txt2_DD, posxytxt2_DD = resultados2[1]
	txt3_DD, posxytxt3_DD = resultados2[2]
	txt4_DD, posxytxt4_DD = resultados2[3]
	txt5_DD, posxytxt5_DD = resultados2[4]
	txt6_DD, posxytxt6_DD = resultados2[5]
	txt7_DD, posxytxt7_DD = resultados2[6]
	txt8_DD, posxytxt8_DD = resultados2[7]
	txt9_DD, posxytxt9_DD = resultados2[8]
	txt10_DD, posxytxt10_DD = resultados2[9]

	Nave_Tipo1 = resultados2[10]
	Nave_Tipo2 = resultados2[11]
	Nave_Tipo3 = resultados2[12]
	Nave_Tipo4 = resultados2[13]
	Nave_Tipo5 = resultados2[14]
	Nave_Tipo6 = resultados2[15]
	Nave_Tipo7 = resultados2[16]
	Nave_Tipo8 = resultados2[17]

	resultados4 = actualizar_pantalla_izquierda_arriba(ventana, caracteristicas)

	txt1_AI, posxytxt1_AI = resultados4[0]
	Nave_act_Controlador_De_Daños = resultados4[1]
	vida_alaDerecha = resultados4[2]
	vida_alaIzquierda = resultados4[3]
	vida_motor = resultados4[4]
	vida_frontal = resultados4[5]
	viva = resultados4[6]
	alaDerecha = resultados4[7]
	alaIzquierda = resultados4[8]
	motor = resultados4[9]
	frontal = resultados4[10]

	resultados3 = actualizar_pantalla_izquierda_debajo(ventana)

	txt1_DI, posxytxt1_DI = resultados3[0]
	txt2_DI, posxytxt2_DI = resultados3[1]
	txt3_DI, posxytxt3_DI = resultados3[2]
	txt4_DI, posxytxt4_DI = resultados3[3]
	txt5_DI, posxytxt5_DI = resultados3[4]
	txt6_DI, posxytxt6_DI = resultados3[5]
	txt7_DI, posxytxt7_DI = resultados3[6]
	txt8_DI, posxytxt8_DI = resultados3[7]
	txt9_DI, posxytxt9_DI = resultados3[8]
	txt10_DI, posxytxt10_DI = resultados3[9]
	txt11_DI, posxytxt11_DI = resultados3[10]
	txt12_DI, posxytxt12_DI = resultados3[11]
	txt13_DI, posxytxt13_DI = resultados3[12]
	txt14_DI, posxytxt14_DI = resultados3[13]
	txt15_DI, posxytxt15_DI = resultados3[14]

	ventana.fill(negro)

	generar_fondo(ventana)

	if txt1_AD != ["", ""]: ventana.blit(txt1_AD, (posxytxt1_AD[0], posxytxt1_AD[1]))
	if txt2_AD != ["", ""]: ventana.blit(txt2_AD, (posxytxt2_AD[0], posxytxt2_AD[1]))
	if txt3_AD != ["", ""]: ventana.blit(txt3_AD, (posxytxt3_AD[0], posxytxt3_AD[1]))
	if txt4_AD != ["", ""]: ventana.blit(txt4_AD, (posxytxt4_AD[0], posxytxt4_AD[1]))
	if txt5_AD != ["", ""]: ventana.blit(txt5_AD, (posxytxt5_AD[0], posxytxt5_AD[1]))
	if txt6_AD != ["", ""]: ventana.blit(txt6_AD, (posxytxt6_AD[0], posxytxt6_AD[1]))
	if txt7_AD != ["", ""]: ventana.blit(txt7_AD, (posxytxt7_AD[0], posxytxt7_AD[1]))

	if txt1_DD != ["", ""]: ventana.blit(txt1_DD, (posxytxt1_DD[0], posxytxt1_DD[1]))
	if txt2_DD != ["", ""]: ventana.blit(txt2_DD, (posxytxt2_DD[0], posxytxt2_DD[1]))
	if txt3_DD != ["", ""]: ventana.blit(txt3_DD, (posxytxt3_DD[0], posxytxt3_DD[1]))
	if txt4_DD != ["", ""]: ventana.blit(txt4_DD, (posxytxt4_DD[0], posxytxt4_DD[1]))
	if txt5_DD != ["", ""]: ventana.blit(txt5_DD, (posxytxt5_DD[0], posxytxt5_DD[1]))
	if txt6_DD != ["", ""]: ventana.blit(txt6_DD, (posxytxt6_DD[0], posxytxt6_DD[1]))
	if txt7_DD != ["", ""]: ventana.blit(txt7_DD, (posxytxt7_DD[0], posxytxt7_DD[1]))
	if txt8_DD != ["", ""]: ventana.blit(txt8_DD, (posxytxt8_DD[0], posxytxt8_DD[1]))
	if txt9_DD != ["", ""]: ventana.blit(txt9_DD, (posxytxt9_DD[0], posxytxt9_DD[1]))
	if txt10_DD != ["", ""]: ventana.blit(txt10_DD, (posxytxt10_DD[0], posxytxt10_DD[1]))

	if Nave_Tipo1 != "": ventana.blit(Nave_Tipo1, (posximag123, posytxt_derecha_debajo * 0 + posy2rec1)) #Sguir transformando a decimal en vaiables2
	if Nave_Tipo2 != "": ventana.blit(Nave_Tipo2, (posximag123, posytxt_derecha_debajo * 1 + posy2rec1))
	if Nave_Tipo3 != "": ventana.blit(Nave_Tipo3, (posximag123, posytxt_derecha_debajo * 2 + posy2rec1))
	if Nave_Tipo4 != "": ventana.blit(Nave_Tipo4, (round(0.19921875 * ancho), posytxt_derecha_debajo * 3 + posy2rec1))
	if Nave_Tipo5 != "": ventana.blit(Nave_Tipo5, (round(0.19921875 * ancho), posytxt_derecha_debajo * 4 + posy2rec1))
	if Nave_Tipo6 != "": ventana.blit(Nave_Tipo6, (round(0.13671875 * ancho), posytxt_derecha_debajo * 5 + posy2rec1))
	if Nave_Tipo7 != "": ventana.blit(Nave_Tipo7, (round(0.1796875 * ancho), posytxt_derecha_debajo * 6 + posy2rec1))
	if Nave_Tipo8 != "": ventana.blit(Nave_Tipo8, (round(0.18359375 * ancho), posytxt_derecha_debajo * 7 + posy2rec1))

	if txt1_AI != ["", ""]: ventana.blit(txt1_AI, (posxytxt1_AI[0], posxytxt1_AI[1]))
	ventana.blit(Nave_act_Controlador_De_Daños, (posxControlador, posyControlador))

	if txt1_DI != ["", ""]: ventana.blit(txt1_DI, (posxytxt1_DI[0], posxytxt1_DI[1]))
	if txt2_DI != ["", ""]: ventana.blit(txt2_DI, (posxytxt2_DI[0], posxytxt2_DI[1]))
	if txt3_DI != ["", ""]: ventana.blit(txt3_DI, (posxytxt3_DI[0], posxytxt3_DI[1]))
	if txt4_DI != ["", ""]: ventana.blit(txt4_DI, (posxytxt4_DI[0], posxytxt4_DI[1]))
	if txt5_DI != ["", ""]: ventana.blit(txt5_DI, (posxytxt5_DI[0], posxytxt5_DI[1]))
	if txt6_DI != ["", ""]: ventana.blit(txt6_DI, (posxytxt6_DI[0], posxytxt6_DI[1]))
	if txt7_DI != ["", ""]: ventana.blit(txt7_DI, (posxytxt7_DI[0], posxytxt7_DI[1]))
	if txt8_DI != ["", ""]: ventana.blit(txt8_DI, (posxytxt8_DI[0], posxytxt8_DI[1]))
	if txt9_DI != ["", ""]: ventana.blit(txt9_DI, (posxytxt9_DI[0], posxytxt9_DI[1]))
	if txt10_DI != ["", ""]: ventana.blit(txt10_DI, (posxytxt10_DI[0], posxytxt10_DI[1]))
	if txt11_DI != ["", ""]: ventana.blit(txt11_DI, (posxytxt11_DI[0], posxytxt11_DI[1]))
	if txt12_DI != ["", ""]: ventana.blit(txt12_DI, (posxytxt12_DI[0], posxytxt12_DI[1]))
	if txt13_DI != ["", ""]: ventana.blit(txt13_DI, (posxytxt13_DI[0], posxytxt13_DI[1]))
	if txt14_DI != ["", ""]: ventana.blit(txt14_DI, (posxytxt14_DI[0], posxytxt14_DI[1]))
	if txt15_DI != ["", ""]: ventana.blit(txt15_DI, (posxytxt15_DI[0], posxytxt15_DI[1]))
	ventana.blit(Barrera_Azul, (posxbarrera, posybarrera))

	ventana.blit(NavePrincipal, (round(xn), round(yn)))

	naves, list_naves, usados = crear_oleada(ventana, Lv_act, infinito, list_naves, usados, oleada, radio)

	if escudo: ventana.blit(Escudo, (posxControlador - 8, posyControlador - 8))

	pygame.display.update()

	#print(usados)

	monedas_en_pantalla = []

	estrellas = []

	if estrellasenpantalla == True:

		nºestrellas = random.randrange(25, 75)

		for x in range(nºestrellas):
			estrella = [random.randrange(330, 950), random.randrange(0, 710), colores_seleccion[random.randrange(0, 1)], velocidades[random.randrange(0, 3) - 1], 0, True] # estrella = [posx, poxy, (R, G, B)]
			estrellas.append(estrella)

		for estrella in estrellas:
			pygame.draw.rect(ventana, estrella[2], (round(estrella[0]), round(estrella[1]), 2, 2))

	pygame.display.update()

	for nave in naves:

		ventana.blit(nave.ImagenNave, (nave.posx, nave.posy))

		time.sleep(0.05)

		pygame.display.update()

	Exit_presionado = False

	accion = False

	pant_escond = False

	press = False

	ant_FPS = 0

	fpslist = []

	aborrar = []

	movimientos = [1, 3, 1, 2] #1 = abajo antura de nave, 2 = derecha, 3 = izquierda

	hacer = 0

	ciclo = 0

	cambiar = False

	recien_salido = False

	primeravuelta = True

	turno = True

	navecayendo = False

	avanzarhasta = None

	margenerror = 2

	nave_a_ordenar = -1

	tocada = False

	eliminarposicionesocupadas = False

	disparado = False

	eleabuscar = []

	puntuacion = 0

	datos_conseguidos = [False, 0]

	dañoProyectiles = [5, 10, 15]

	velocidad_fondo = 0.1

	explotada = False

	vueltas = 0

	dispararya = False

	ultimoseventos = []

	for vida in tipos_de_vidas:

		eleabuscar.append(vida)

	index_Nave_Prin = Data_Prin.index(eleabuscar)

	listdisparos_NA = [] #[[x, y, imagen, v], [x2, y2, imagen2, v2]]...

	listdisparos_NE = [] #[[x, y, imagen, v, t], [x2, y2, imagen2, v2, t2]]...

	naves_destruidas_a_explotar = [] # dentro va [[posx, posy, tipo, explosion_actual], [posx, posy, tipo, explosion_actual]]

	data_time_microsecond = str(datetime.now().microsecond)
	data_time_second = str(datetime.now().second)
	data_time_minute = datetime.now().minute

	if len(data_time_second) != 2:
		data_time_second = "0" + data_time_second

	for i in range(6 - len(data_time_microsecond)):
		data_time_microsecond = "0" + data_time_microsecond

	data_time = int(str(data_time_minute) + data_time_second + data_time_microsecond)

	teclaizquierdapress = False
	tecladerechapress = False
	teclaabajopress = False
	teclaarribapress = False
	disparoAmigo = False

	crear_texto_en_pantalla(ventana, "OLEADA Nº1", 0.5)

	while Exit_presionado == False: #Funciona para cerrar

		### ========== ZONA DE PROBABILIDADES ========== ###

		if primeravuelta == False and FPS > 3 and int(random.randrange(1, math.ceil(150*(FPS/400)))) == 1 and estrellasmoviendose == "True" and estrellasenpantalla == True:
			estrella = [random.randrange(330, 950), 0, colores_seleccion[random.randrange(0, 1)], velocidades[random.randrange(0, 3) - 1], 0, True] # estrella = [posx, poxy, color, velocidad, countdown, modo]
			estrellas.append(estrella)

		if primeravuelta == False and FPS > 3 and int(random.randrange(0, 1 + math.ceil(4000*(FPS/400)))) == 1:
			tipo = random.randrange(0, 301)

			if tipo > -1 and tipo < 180:
				monedatipo = 1

			elif tipo > 179 and tipo < 300:
				monedatipo = 2

			elif tipo > 299:
				monedatipo = 3

			x = random.randrange(0, 2)

			if x == 1:
				posmonx = 322
				posmonxalt = 942

			else:
				posmonx = 940
				posmonxalt = 322

			posmony = random.randrange(400, 710)

			moneda = [posmonx, posmony, 0, x, 40, posmonxalt, random.randrange(350, 710), monedatipo] # moneda = [posx, poxy, forma*, en que lado empezó, counter, gotox, gotoy, tipo] *Forma es si esta de canto o de cara

			monedas_en_pantalla.append(moneda)

		for evento in pygame.event.get():

			if evento.type == KEYDOWN or evento.type == KEYUP:
				ultimoseventos.append(evento)
				press = True

			if evento.type == QUIT:
				print("Juego terminado")
				Exit_presionado = True
				pygame.quit()
				raise KeyError

			elif evento.type == KEYDOWN: #Teclas que se presionen una vez

				if evento.key == 285: #F4 = para cerrar el programa; hecho
					print("Juego terminado")
					Exit_presionado = True
					pygame.quit()
					raise KeyError

				elif evento.key == 112 or evento.key == 27: # Letra "P" y ESC
					salida = crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

					if salida == True:
						Exit_presionado = True

					pygame.mouse.set_visible(False)
					pygame.draw.rect(ventana, negro, (posx1rectcentre + round(tamañoline/2), 0, 640 - round(tamañoline/2), alto))

					recien_salido = True

					teclaizquierdapress = False
					tecladerechapress = False
					teclaabajopress = False
					teclaarribapress = False
					disparoAmigo = False

					primeravuelta = True
					vueltas = 0

					pygame.display.update()

				elif evento.key == 102: #Letra "F"

					if fpsactivos == True:
						fpsactivos = False
						cambioFps = True

					else:
						fpsactivos = True

		antsecond = second
		second = datetime.now().second
		
		### CONTROL DE LOS FPS ### CONTROL DE LOS FPS ### CONTROL DE LOS FPS ### CONTROL DE LOS FPS ### CONTROL DE LOS FPS ###

		antmicrosecond = microsecond
		microsecond = datetime.now().microsecond

		if second != antsecond:
			antmicrosecond = 0

		if microsecond != antmicrosecond:
			FPS = round(1/((microsecond - antmicrosecond)/1000000))

		if FPS < MaxFPS and sumer > 1 and MaxFPS > 0:
			sumer += 1

		elif FPS > MaxFPS and MaxFPS > 0:
			sumer -= 1

		### ACCIONES DE MOVIMIENTO ### ACCIONES DE MOVIMIENTO ### ACCIONES DE MOVIMIENTO ### ACCIONES DE MOVIMIENTO ### ACCIONES DE MOVIMIENTO ###

		if vueltas > 3:
			for estrella in estrellas:
				pygame.draw.rect(ventana, negro, (round(estrella[0]), round(estrella[1]), 2, 2))

				yact = estrella[1]

				velocidad_estrella = estrella[3]

				if yact < 720:

					if estrellasmoviendose == "True":

						estrella.pop(1)
						estrella.insert(1, yact + (450/FPS)*velocidad_estrella)

				else:

					aborrar.append(estrellas.index(estrella))
					aborrar.sort()
					aborrar.reverse()

				if round(estrella[4]) == 0:

					if estrellasparpadeando == True:
						modo = random.randrange(0, 2)
						estrella.pop(4)
						estrella.insert(4, (350/FPS)*velocidadparpadeo)

						if modo == 1: #Apagada
							estrella.pop(5)
							estrella.insert(5, False)

						else: #Encendida
							estrella.pop(5)
							estrella.insert(5, True)

				else:

					if estrellasparpadeando == True:
						counter_ant = estrella[4]
						estrella.pop(4)
						estrella.insert(4, counter_ant - 1)

				if estrella[5] == True:
					pygame.draw.rect(ventana, estrella[2], (round(estrella[0]), round(estrella[1]), 2, 2))

				else:
					pygame.draw.rect(ventana, negro, (round(estrella[0]), round(estrella[1]), 2, 2))

			for borrado in aborrar:
				pygame.draw.rect(ventana, negro, (round((estrellas[borrado])[0]), round((estrellas[borrado])[1]), 2, 2))
				estrellas.pop(borrado)

			aborrar = []

			for moneda in monedas_en_pantalla: #[posx, poxy, forma*, en que lado empezó, counter, gotox, gotoy]
				ventana.blit(monedas_Negras_Imag[moneda[2]], (moneda[0], moneda[1]))

				if moneda[4] > 0:
					ant_counter = moneda[4]
					moneda.pop(4)
					moneda.insert(4, ant_counter -1)
					imag = monedas_Imag[moneda[2]]

				else:
					moneda.pop(4)
					moneda.insert(4, 40)

					if moneda[2] == 0:
						moneda.pop(2)
						moneda.insert(2, 1)

					else:
						moneda.pop(2)
						moneda.insert(2, 0)

				if moneda[7] == 1:
					summer = 0

				elif moneda[7] == 2:
					summer = 2

				elif moneda[7] == 3:
					summer = 4

				xavanzado = (450/FPS)*0.4

				#print(moneda[3], moneda[0])

				if moneda[0] > 940 and moneda[3] == 0:
					moneda.pop(3)
					moneda.insert(3, 1)

				elif moneda[0] > 950 - 18 and moneda[3] == 1:
					aborrar.append(monedas_en_pantalla.index(moneda))
					aborrar.sort()
					aborrar.reverse()

				elif moneda[0] < 330 and moneda[3] == 0:
					aborrar.append(monedas_en_pantalla.index(moneda))
					aborrar.sort()
					aborrar.reverse()

				elif moneda[0] > moneda[5] and moneda[1] > moneda[6]:
					x_ant = moneda[0]
					y_ant = moneda[1]
					ydiferencia = moneda[1] - moneda[6]
					xdiferencia = moneda[0] - moneda[5]
					yavanzado = ydiferencia/xdiferencia
					moneda.pop(0)
					moneda.insert(0, x_ant - xavanzado)
					moneda.pop(1)
					moneda.insert(1, y_ant - (yavanzado * xavanzado))

				elif moneda[0] > moneda[5] and moneda[1] < moneda[6]:
					x_ant = moneda[0]
					y_ant = moneda[1]
					ydiferencia = moneda[6] - moneda[1]
					xdiferencia = moneda[0] - moneda[5]
					yavanzado = ydiferencia/xdiferencia
					moneda.pop(0)
					moneda.insert(0, x_ant - xavanzado)
					moneda.pop(1)
					moneda.insert(1, y_ant + (yavanzado * xavanzado))

				elif moneda[0] < moneda[5] and moneda[1] > moneda[6]:
					x_ant = moneda[0]
					y_ant = moneda[1]
					ydiferencia = moneda[1] - moneda[6]
					xdiferencia = moneda[5] - moneda[0]
					yavanzado = ydiferencia/xdiferencia
					moneda.pop(0)
					moneda.insert(0, x_ant + xavanzado)
					moneda.pop(1)
					moneda.insert(1, y_ant - (yavanzado * xavanzado))

				elif moneda[0] < moneda[5] and moneda[1] < moneda[6]:
					x_ant = moneda[0]
					y_ant = moneda[1]
					ydiferencia = moneda[6] - moneda[1]
					xdiferencia = moneda[5] - moneda[0]
					yavanzado = ydiferencia/ydiferencia
					moneda.pop(0)
					moneda.insert(0, x_ant + xavanzado)
					moneda.pop(1)
					moneda.insert(1, y_ant + (yavanzado * xavanzado))

				else:
					x_ant = moneda[0]
					moneda.pop(0)
					moneda.insert(0, x_ant + xavanzado)

				ventana.blit(monedas_Imag[moneda[2] + summer], (moneda[0], moneda[1]))

			for borrado in aborrar:
				ventana.blit(monedas_Negras_Imag[(monedas_en_pantalla[borrado])[2]], ((monedas_en_pantalla[borrado])[0], (monedas_en_pantalla[borrado])[1]))
				monedas_en_pantalla.pop(borrado)

			aborrar = []

		for evento in pygame.event.get():

			if evento.type == KEYDOWN or evento.type == KEYUP:
				ultimoseventos.append(evento)
				press = True

			if evento.type == QUIT:
				print("Juego terminado")
				Exit_presionado = True
				#time.sleep(1)
				pygame.quit()
				raise KeyError

			elif evento.type == KEYDOWN: #Teclas que se presionen una vez

				if evento.key == 285: #F4 = para cerrar el programa; hecho
					print("Juego terminado")
					Exit_presionado = True
					pygame.quit()
					raise KeyError

				elif evento.key == 112 or evento.key == 27: # Letra "P" y ESC
					salida = crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

					if salida == True:
						Exit_presionado = True

					pygame.mouse.set_visible(False)
					pygame.draw.rect(ventana, negro, (posx1rectcentre + round(tamañoline/2), 0, 640 - round(tamañoline/2), alto))

					recien_salido = True

					teclaizquierdapress = False
					tecladerechapress = False
					teclaabajopress = False
					teclaarribapress = False
					disparoAmigo = False

					primeravuelta = True
					vueltas = 0

					pygame.display.update()

				elif evento.key == 102: #Letra "F"

					if fpsactivos == True:
						fpsactivos = False
						cambioFps = True

					else:
						fpsactivos = True

		if recien_salido == False:

			for disparo in listdisparos_NA: #Naves amigas
				
				ventana.blit(DisparoNegro, (disparo[0], disparo[1]))

				yact = disparo[1]

				if yact > posybarrera:

					disparo.pop(1)
					disparo.insert(1, round(yact - (450/FPS)*disparo[2]))

				else:

					aborrar.append(listdisparos_NA.index(disparo))
					aborrar.sort()
					aborrar.reverse()
					tocada = True
					tempcontroler = 20

				ventana.blit(disparo[2], (disparo[0], disparo[1]))

			for borrado in aborrar:
				puntuacion -= 1
				pygame.draw.rect(ventana, negro, ((listdisparos_NA[borrado])[0], (listdisparos_NA[borrado])[1], 2, 16))
				listdisparos_NA.pop(borrado)

			aborrar = []

			for disparo in listdisparos_NE: #Naves enemigas

				ventana.blit(DisparoNegro, (disparo[0], disparo[1]))

				disparo_org = disparo

				yact = disparo[1]

				if yact < alto:

					disparo.pop(1)
					disparo.insert(1, yact + (450/FPS)*disparo[2])


				else:
					aborrar.append(listdisparos_NE.index(disparo))
					aborrar.sort()
					aborrar.reverse()

				ventana.blit(disparo[2], (disparo[0], disparo[1]))

			for borrado in aborrar:
				puntuacion += 1
				pygame.draw.rect(ventana, negro, ((listdisparos_NE[borrado])[0] - 8, (listdisparos_NE[borrado])[1], 2, (listdisparos_NE[borrado])[0] + 8))
				listdisparos_NE.pop(borrado)

			aborrar = []

		recien_salido = False

		fpslist.append(FPS)

		for evento in pygame.event.get():

			if evento.type == KEYDOWN or evento.type == KEYUP:
				ultimoseventos.append(evento)
				press = True

			if evento.type == QUIT:
				print("Juego terminado")
				Exit_presionado = True
				#time.sleep(1)
				pygame.quit()
				raise KeyError

			elif evento.type == KEYDOWN: #Teclas que se presionen una vez

				if evento.key == 285: #F4 = para cerrar el programa; hecho
					print("Juego terminado")
					Exit_presionado = True
					#time.sleep(1)
					pygame.quit()
					raise KeyError

				elif evento.key == 112 or evento.key == 27: # Letra "P" y ESC
					salida = crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

					if salida == True:
						Exit_presionado = True

					pygame.mouse.set_visible(False)
					pygame.draw.rect(ventana, negro, (posx1rectcentre + round(tamañoline/2), 0, 640 - round(tamañoline/2), alto))

					recien_salido = True

					teclaizquierdapress = False
					tecladerechapress = False
					teclaabajopress = False
					teclaarribapress = False
					disparoAmigo = False

					primeravuelta = True
					vueltas = 0

					pygame.display.update()

				elif evento.key == 102: #Letra "F"

					if fpsactivos == True:
						fpsactivos = False
						cambioFps = True

					else:
						fpsactivos = True

		if primeravuelta == False:

			for nave in naves:

				#ultimoseventos = calcevento(ultimoseventos)

				if nave.viva == True:

					ventana.blit(Nave1_Negro, (nave.posx, nave.posy))

					mix = nave.calculardisparo(Lv_act, FPS)

					if mix != "False":
						listdisparos_NE.append(mix[1])

					if nave.posy > alto - 22:

						nave.primeracosset()

						if posiciones_ocupadas > 3:

							nave.actualizarpos(nave.posx, nave.posy + (450/FPS)*nave.velocidad)
							
						else:

							nave.actualizarpos(posxvuelta[posiciones_ocupadas], 10)

							posiciones_ocupadas += 1

							nave.esperandoset(True)

							if nave.caida != False:
								navecayendo = False
								nave.caidaset(False)

							#print(posiciones_ocupadas)

					if posiciones_ocupadas > 3 or list_naves.count(1) - posiciones_ocupadas == 0:

						eliminarposicionesocupadas = True
						puntuacion -= 5*posiciones_ocupadas
						if puntuacion < 0: puntuacion = 0
						
					if nave.caida == 100:

						if nave.posy > posybarrera + 20: #Alto de la barrera
							nave.actualizarpos(nave.posx, nave.posy + (450/FPS)*nave.velocidad)
							nave.caidaset(False)

						else:
							nave.actualizarpos(nave.posx, nave.posy + (450/FPS)*nave.velocidad)

					elif nave.posy < 600 and navecayendo != True and nave.esperando == False:

						value = random.randrange(1, round(5000/300) * (FPS + 1)) #Hay 4 tipos d caidas

						if value > 0 and value < round(1000/300) * (FPS + 1): #Recta diagonal hacia la nave
							xnavetoir = xn
							ynavetoir = alto
							nave.caidaset(1)
							navecayendo = True

						elif value > round(1000/300) * (FPS + 1) and value < (2000/300) * (FPS + 1) and nave.posxinic > 350 + round(0.03125 * ancho) and nave.posxinic < 930 - round(0.03125 * ancho) - 18: #Ancho de la nave
							y = round(nave.posy)
							#print(y)
							#print(nave.posx)
							encontrada = False
							nave.iniciocosxset(nave.posx)

							while encontrada != True:

								if round(nave.posx) == round(nave.posx) + round(math.cos((y)/20)*30):
									encontrada = True

								y += 1

							nave.caidaset(2)
							navecayendo = True
							yerror = y - round(nave.posy)

						elif value > (2000/300) * (FPS + 1) and value < (3000/300) * (FPS + 1) and nave.posx < 960 - radio - round(0.03125 * ancho) and nave.posx > 320 + radio + round(0.03125 * ancho):
							nave.xavanzadoset(radio * -1)
							pxcaida = random.randrange(10, ((alto - 22) - round(nave.posy)) - radio*2)
							posytoir = round(nave.posy) + pxcaida
							fase = 1
							nave.caidaset(3)
							navecayendo = True
							velocidad = (450/FPS)*nave.velocidad*2

						elif value == None:
							nave.caidaset(4)
							navecayendo = True

						else:
							nave.caidaset(False)
							navecayendo = False

					if nave.caida == False and nave.esperando == False:

						if movimientos[hacer] == 1:

							if ciclo < 50:

								nave.actualizarpos(nave.posx, nave.posy + (450/FPS)*nave.velocidad)

							else:

								nave.actualizarpos(nave.posx, nave.posy + (450/FPS)*nave.velocidad)
								cambiar = True

						elif movimientos[hacer] == 2:

							if  nave.posx > 335:

								nave.actualizarpos(nave.posx - (450/FPS)*nave.velocidad, nave.posy)

							else:

								nave.actualizarpos(nave.posx - (450/FPS)*nave.velocidad, nave.posy)
								cambiar = True

						elif movimientos[hacer] == 3:

							if  nave.posx < 905:

								nave.actualizarpos(nave.posx + (450/FPS)*nave.velocidad, nave.posy)

							else:

								nave.actualizarpos(nave.posx + (450/FPS)*nave.velocidad, nave.posy)
								cambiar = True

					elif nave.caida == 1 and nave.esperando == False: #Diagonal

						yavanzado = (450/FPS)*nave.velocidad*2

						if round(xnavetoir) == round(nave.posx) and round(ynavetoir) == round(nave.posy):

							xnavetoir = False
							ynavetoir = False

							nave.caidaset(False)
							navecayendo = False

						if nave.posx > xnavetoir and nave.posy > ynavetoir:
							ydiferencia = nave.posy - ynavetoir
							xdiferencia = nave.posx - xnavetoir
							xavanzado = xdiferencia/ydiferencia
							nave.actualizarpos(nave.posx - (xavanzado * yavanzado), nave.posy - yavanzado)

						elif nave.posx > xnavetoir and nave.posy < ynavetoir:
							ydiferencia = ynavetoir - nave.posy
							xdiferencia = nave.posx - xnavetoir
							xavanzado = xdiferencia/ydiferencia
							nave.actualizarpos(nave.posx - (xavanzado * yavanzado), nave.posy + yavanzado)

						elif nave.posx < xnavetoir and nave.posy > ynavetoir:
							ydiferencia = nave.posy - ynavetoir
							xdiferencia = xnavetoir - nave.posx
							xavanzado = xdiferencia/ydiferencia
							nave.actualizarpos(nave.posx + (xavanzado * yavanzado), nave.posy - yavanzado)

						elif nave.posx < xnavetoir and nave.posy < ynavetoir:
							ydiferencia = ynavetoir - nave.posy
							xdiferencia = xnavetoir - nave.posx
							xavanzado = xdiferencia/ydiferencia
							nave.actualizarpos(nave.posx + (xavanzado * yavanzado), nave.posy + yavanzado)

					elif nave.caida == 2 and nave.esperando == False:

						if nave.primeracos == True:
							#print("Primera Passada")
							nave.primeracosset()

						else:
							yavanzado = (450/FPS)*nave.velocidad*2
							nave.actualizarpos(nave.inicosenx + math.cos((nave.posy + yavanzado + yerror)/20)*30, nave.posy + yavanzado)

					elif nave.caida == 3 and nave.esperando == False:
						
						if fase == 1:
							if nave.posy + margenerror > posytoir and nave.posy - margenerror < posytoir:
								fase = 2
								xinicial = round(nave.posx)
								yinicial = round(nave.posy)

							else:
								nave.actualizarpos(nave.posx, nave.posy + velocidad)

						elif fase == 2: #Giro debajo

							nave.xavanzadoset(nave.xavanzado + velocidad*1.5)

							if nave.xavanzado > radio:
								fase = 3

							else:
								yavanzado = math.sqrt(radio**2 - round(nave.xavanzado)**2)
								nave.actualizarpos(xinicial + round(nave.xavanzado) + radio, yinicial + yavanzado)

						elif fase == 3: #Giro arriba

							nave.xavanzadoset(nave.xavanzado - velocidad*1.5)

							if nave.xavanzado < radio * -1:
								fase = False
								xnavetoir = xn
								ynavetoir = alto
								nave.caidaset(1)
								navecayendo = True

							else:
								yavanzado = math.sqrt(radio**2 - round(nave.xavanzado)**2) * -1
								nave.actualizarpos(xinicial + round(nave.xavanzado) + radio, yinicial + yavanzado)

					elif nave.caida == 4 and nave.esperando == False:
						pass

					ventana.blit(nave.ImagenNave, (round(nave.posx), round(nave.posy))) 

				else:
					if nave.muerteprimera == True:

						list_naves.pop(nave.pos)
						list_naves.insert(nave.pos, 0)
						if nave.caida != False:
							nave.caidaset(False)
							navecayendo = False
						#explosion_sound.play()

						ventana.blit(Nave1_Negro, (nave.posx, nave.posy))

						naves_destruidas_a_explotar.append([nave.posx, nave.posy, nave.tipo, 1])

						nave.Muerteprimera()

			if eliminarposicionesocupadas == True:

				for nave in naves:

					if nave.esperando == True:
						nave.esperandoset(False)
						
						#print("Liberada nave: " + str(naves.index(nave)))
						nave.caidaset(100)

				eliminarposicionesocupadas = False
				posiciones_ocupadas = 0

			if movimientos[hacer] == 1:

				if ciclo < 50:

					ciclo += (400/FPS)

			if cambiar == True:

				ciclo = 0
				cambiar = False

				if hacer == 3:
					hacer = 0

				else:
					hacer += 1

		for evento in pygame.event.get():

			if evento.type == KEYDOWN or evento.type == KEYUP:
				ultimoseventos.append(evento)
				press = True

			if evento.type == QUIT:
				print("Juego terminado")
				Exit_presionado = True
				#time.sleep(1)
				pygame.quit()
				raise KeyError

			elif evento.type == KEYDOWN: #Teclas que se presionen una vez

				if evento.key == 285: #F4 = para cerrar el programa; hecho
					print("Juego terminado")
					Exit_presionado = True
					#time.sleep(1)
					pygame.quit()
					raise KeyError

				elif evento.key == 112 or evento.key == 27: # Letra "P" y ESC
					salida = crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

					if salida == True:
						Exit_presionado = True

					pygame.mouse.set_visible(False)
					pygame.draw.rect(ventana, negro, (posx1rectcentre + round(tamañoline/2), 0, 640 - round(tamañoline/2), alto))

					recien_salido = True

					teclaizquierdapress = False
					tecladerechapress = False
					teclaabajopress = False
					teclaarribapress = False
					disparoAmigo = False

					primeravuelta = True
					vueltas = 0

					pygame.display.update()

				elif evento.key == 102: #Letra "F"

					if fpsactivos == True:
						fpsactivos = False
						cambioFps = True

					else:
						fpsactivos = True

		for moneda in monedas_en_pantalla: #Monedas contra nave amiga

			if moneda[0] + 4 > xn and moneda[0] - 4 < xn + tamañox and moneda[1] + 4 > yn and moneda[1]  - 4 < yn + tamañoy: #Arriba izquierda

				if moneda[7] == 1:
					puntuacion += 20
					Monedas += 1

				elif moneda[7] == 2:
					puntuacion += 100
					Monedas += 10

				elif moneda[7] == 3:
					puntuacion += 500
					Monedas += 100

				resultados = actualizar_pantalla_derecha_arriba(ventana, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, fpsactivos, infinito, segundostranscurridos)

				txt1_AD, posxytxt1_AD = resultados[0]
				txt2_AD, posxytxt2_AD = resultados[1]
				txt3_AD, posxytxt3_AD = resultados[2]
				txt4_AD, posxytxt4_AD = resultados[3]
				txt5_AD, posxytxt5_AD = resultados[4]
				txt6_AD, posxytxt6_AD = resultados[5]
				txt7_AD, posxytxt7_AD = resultados[6]

				if txt1_AD != ["", ""]: ventana.blit(txt1_AD, (posxytxt1_AD[0], posxytxt1_AD[1]))
				if txt2_AD != ["", ""]: ventana.blit(txt2_AD, (posxytxt2_AD[0], posxytxt2_AD[1]))
				if txt3_AD != ["", ""]: ventana.blit(txt3_AD, (posxytxt3_AD[0], posxytxt3_AD[1]))
				if txt4_AD != ["", ""]: ventana.blit(txt4_AD, (posxytxt4_AD[0], posxytxt4_AD[1]))
				if txt5_AD != ["", ""]: ventana.blit(txt5_AD, (posxytxt5_AD[0], posxytxt5_AD[1]))
				if txt6_AD != ["", ""]: ventana.blit(txt6_AD, (posxytxt6_AD[0], posxytxt6_AD[1]))
				if txt7_AD != ["", ""]: ventana.blit(txt7_AD, (posxytxt7_AD[0], posxytxt7_AD[1]))

				aborrar.append(monedas_en_pantalla.index(moneda))
				aborrar.sort()
				aborrar.reverse()

			elif moneda[0] + 18 + 4 > xn and moneda[0] + 18  - 4 < xn + tamañox and moneda[1] + 4 > yn and moneda[1]  - 4 < yn + tamañoy: #Arriba derecha
				
				if moneda[7] == 1:
					puntuacion += 20
					Monedas += 1

				elif moneda[7] == 2:
					puntuacion += 100
					Monedas += 10

				elif moneda[7] == 3:
					puntuacion += 500
					Monedas += 100

				resultados = actualizar_pantalla_derecha_arriba(ventana, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, fpsactivos, infinito, segundostranscurridos)

				txt1_AD, posxytxt1_AD = resultados[0]
				txt2_AD, posxytxt2_AD = resultados[1]
				txt3_AD, posxytxt3_AD = resultados[2]
				txt4_AD, posxytxt4_AD = resultados[3]
				txt5_AD, posxytxt5_AD = resultados[4]
				txt6_AD, posxytxt6_AD = resultados[5]
				txt7_AD, posxytxt7_AD = resultados[6]

				if txt1_AD != ["", ""]: ventana.blit(txt1_AD, (posxytxt1_AD[0], posxytxt1_AD[1]))
				if txt2_AD != ["", ""]: ventana.blit(txt2_AD, (posxytxt2_AD[0], posxytxt2_AD[1]))
				if txt3_AD != ["", ""]: ventana.blit(txt3_AD, (posxytxt3_AD[0], posxytxt3_AD[1]))
				if txt4_AD != ["", ""]: ventana.blit(txt4_AD, (posxytxt4_AD[0], posxytxt4_AD[1]))
				if txt5_AD != ["", ""]: ventana.blit(txt5_AD, (posxytxt5_AD[0], posxytxt5_AD[1]))
				if txt6_AD != ["", ""]: ventana.blit(txt6_AD, (posxytxt6_AD[0], posxytxt6_AD[1]))
				if txt7_AD != ["", ""]: ventana.blit(txt7_AD, (posxytxt7_AD[0], posxytxt7_AD[1]))

				aborrar.append(monedas_en_pantalla.index(moneda))
				aborrar.sort()
				aborrar.reverse()

			elif moneda[0] + 18 + 4 > xn and moneda[0] + 18  - 4 < xn + tamañox and moneda[1] +  26 + 4 > yn and moneda[1] + 26 - 4 < yn + tamañoy: #Abajo derecha
				
				if moneda[7] == 1:
					puntuacion += 20
					Monedas += 1

				elif moneda[7] == 2:
					puntuacion += 100
					Monedas += 10

				elif moneda[7] == 3:
					puntuacion += 500
					Monedas += 100
					
				resultados = actualizar_pantalla_derecha_arriba(ventana, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, fpsactivos, infinito, segundostranscurridos)

				txt1_AD, posxytxt1_AD = resultados[0]
				txt2_AD, posxytxt2_AD = resultados[1]
				txt3_AD, posxytxt3_AD = resultados[2]
				txt4_AD, posxytxt4_AD = resultados[3]
				txt5_AD, posxytxt5_AD = resultados[4]
				txt6_AD, posxytxt6_AD = resultados[5]
				txt7_AD, posxytxt7_AD = resultados[6]

				if txt1_AD != ["", ""]: ventana.blit(txt1_AD, (posxytxt1_AD[0], posxytxt1_AD[1]))
				if txt2_AD != ["", ""]: ventana.blit(txt2_AD, (posxytxt2_AD[0], posxytxt2_AD[1]))
				if txt3_AD != ["", ""]: ventana.blit(txt3_AD, (posxytxt3_AD[0], posxytxt3_AD[1]))
				if txt4_AD != ["", ""]: ventana.blit(txt4_AD, (posxytxt4_AD[0], posxytxt4_AD[1]))
				if txt5_AD != ["", ""]: ventana.blit(txt5_AD, (posxytxt5_AD[0], posxytxt5_AD[1]))
				if txt6_AD != ["", ""]: ventana.blit(txt6_AD, (posxytxt6_AD[0], posxytxt6_AD[1]))
				if txt7_AD != ["", ""]: ventana.blit(txt7_AD, (posxytxt7_AD[0], posxytxt7_AD[1]))

				aborrar.append(monedas_en_pantalla.index(moneda))
				aborrar.sort()
				aborrar.reverse()

			elif moneda[0] + 4 > xn and moneda[0]  - 4 < xn + tamañox and moneda[1] + 26 + 4 > yn and moneda[1] + 26 - 4 < yn + tamañoy: #Abajo izquierda
				
				if moneda[7] == 1:
					puntuacion += 20
					Monedas += 1

				elif moneda[7] == 2:
					puntuacion += 100
					Monedas += 10

				elif moneda[7] == 3:
					puntuacion += 500
					Monedas += 100
					
				resultados = actualizar_pantalla_derecha_arriba(ventana, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, fpsactivos, infinito, segundostranscurridos)

				txt1_AD, posxytxt1_AD = resultados[0]
				txt2_AD, posxytxt2_AD = resultados[1]
				txt3_AD, posxytxt3_AD = resultados[2]
				txt4_AD, posxytxt4_AD = resultados[3]
				txt5_AD, posxytxt5_AD = resultados[4]
				txt6_AD, posxytxt6_AD = resultados[5]
				txt7_AD, posxytxt7_AD = resultados[6]

				if txt1_AD != ["", ""]: ventana.blit(txt1_AD, (posxytxt1_AD[0], posxytxt1_AD[1]))
				if txt2_AD != ["", ""]: ventana.blit(txt2_AD, (posxytxt2_AD[0], posxytxt2_AD[1]))
				if txt3_AD != ["", ""]: ventana.blit(txt3_AD, (posxytxt3_AD[0], posxytxt3_AD[1]))
				if txt4_AD != ["", ""]: ventana.blit(txt4_AD, (posxytxt4_AD[0], posxytxt4_AD[1]))
				if txt5_AD != ["", ""]: ventana.blit(txt5_AD, (posxytxt5_AD[0], posxytxt5_AD[1]))
				if txt6_AD != ["", ""]: ventana.blit(txt6_AD, (posxytxt6_AD[0], posxytxt6_AD[1]))
				if txt7_AD != ["", ""]: ventana.blit(txt7_AD, (posxytxt7_AD[0], posxytxt7_AD[1]))

				aborrar.append(monedas_en_pantalla.index(moneda))
				aborrar.sort()
				aborrar.reverse()

		for borrado in aborrar:
			ventana.blit(monedas_Negras_Imag[(monedas_en_pantalla[borrado])[2]], ((monedas_en_pantalla[borrado])[0], (monedas_en_pantalla[borrado])[1]))
			monedas_en_pantalla.pop(borrado)

		aborrar = []

		for disparo in listdisparos_NE: #Balas enemigas contra nave amiga

			if xn < disparo[0] and xn + 42 > disparo[0] + 2 and yn < disparo[1] + 8 and yn + 26 > disparo[1]: #Comprueva si esta tocando la nave amiga
				disparado = True
				puntuacion -= 10
				if puntuacion < 0: puntuacion = 0

				if xn + 14 > disparo[0] + 2 and alaIzquierda == True and escudo == False: #14px primera ala
					vida_alaIzquierda -= dañoProyectiles[disparo[4] - 1]
					aborrar.append(listdisparos_NE.index(disparo))
					aborrar.sort()
					aborrar.reverse()

				elif xn + 28 < disparo[0] and alaDerecha == True and escudo == False: #28px segunda ala
					vida_alaDerecha -= dañoProyectiles[disparo[4] - 1]
					aborrar.append(listdisparos_NE.index(disparo))
					aborrar.sort()
					aborrar.reverse()

				elif frontal == False and escudo == False: #Deteccion del motor
					vida_motor -= dañoProyectiles[disparo[4] - 1]
					aborrar.append(listdisparos_NE.index(disparo))
					aborrar.sort()
					aborrar.reverse()

				elif xn + 13 < disparo[0] and xn + 29 > disparo[0] and escudo == False: #Deteccion del frontal
					vida_frontal -= dañoProyectiles[disparo[4] - 1]
					aborrar.append(listdisparos_NE.index(disparo))
					aborrar.sort()
					aborrar.reverse()

				elif escudo == True:
					escudo = False
					aborrar.append(listdisparos_NE.index(disparo))
					aborrar.sort()
					aborrar.reverse()

		for borrado in aborrar:
			pygame.draw.rect(ventana, negro, ((listdisparos_NE[borrado])[0], (listdisparos_NE[borrado])[1], 4, 16))
			listdisparos_NE.pop(borrado)

		aborrar = []

		for evento in pygame.event.get():

			if evento.type == KEYDOWN or evento.type == KEYUP:
				ultimoseventos.append(evento)
				press = True

			if evento.type == QUIT:
				print("Juego terminado")
				Exit_presionado = True
				#time.sleep(1)
				pygame.quit()
				raise KeyError

			elif evento.type == KEYDOWN: #Teclas que se presionen una vez

				if evento.key == 285: #F4 = para cerrar el programa; hecho
					print("Juego terminado")
					Exit_presionado = True
					#time.sleep(1)
					pygame.quit()
					raise KeyError

				elif evento.key == 112 or evento.key == 27: # Letra "P" y ESC
					salida = crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

					if salida == True:
						Exit_presionado = True

					pygame.mouse.set_visible(False)
					pygame.draw.rect(ventana, negro, (posx1rectcentre + round(tamañoline/2), 0, 640 - round(tamañoline/2), alto))

					recien_salido = True

					teclaizquierdapress = False
					tecladerechapress = False
					teclaabajopress = False
					teclaarribapress = False
					disparoAmigo = False

					primeravuelta = True
					vueltas = 0

					pygame.display.update()

				elif evento.key == 102: #Letra "F"

					if fpsactivos == True:
						fpsactivos = False
						cambioFps = True

					else:
						fpsactivos = True

		for nave in naves: #Nave enemiga contra nave amiga

			if nave.viva == True:

				if tamañox > nave.tamañox: #Si se cumple la nave enemiga es mas pequeña

					if nave.posx + 4 > xn and nave.posx - 4 < xn + tamañox and nave.posy + 4 > yn and nave.posy  - 4 < yn + tamañoy: #Arriba izquierda
						viva, escudo = ejecutar_daño_CAC(escudo)
						disparado = True
						puntuacion -= 50

						if nave.caida == True:
							navecayendo = False
							nave.caidaset(False)

					elif nave.posx + nave.tamañox + 4 > xn and nave.posx + nave.tamañox  - 4 < xn + tamañox and nave.posy + 4 > yn and nave.posy  - 4 < yn + tamañoy: #Arriba derecha
						viva, escudo = ejecutar_daño_CAC(escudo)
						disparado = True
						puntuacion -= 50

						if nave.caida == True:
							navecayendo = False
							nave.caidaset(False)

					elif nave.posx + nave.tamañox + 4 > xn and nave.posx + nave.tamañox  - 4 < xn + tamañox and nave.posy +  nave.tamañoy + 4 > yn and nave.posy + nave.tamañoy - 4 < yn + tamañoy: #Abajo derecha
						viva, escudo = ejecutar_daño_CAC(escudo)
						disparado = True
						puntuacion -= 50

						if nave.caida == True:
							navecayendo = False
							nave.caidaset(False)	

					elif nave.posx + 4 > xn and nave.posx  - 4 < xn + tamañox and nave.posy + nave.tamañoy + 4 > yn and nave.posy + nave.tamañoy - 4 < yn + tamañoy: #Abajo izquierda
						viva, escudo = ejecutar_daño_CAC(escudo)
						disparado = True
						puntuacion -= 50

						if nave.caida == True:
							navecayendo = False
							nave.caidaset(False)

					if puntuacion < 0: puntuacion = 0

				else:
					pass

		if Naves_destruidas == Nº_Naves or viva == False and infinito == True: #Para comprovar que hayas ganado
			pygame.draw.rect(ventana, negro, (posxline1 + tamañoline, 0, 640 - tamañoline - 1, alto))
			pygame.display.update()

			if viva == True:
				crear_texto_en_pantalla(ventana, "¡GANASTE!, este texto es temporal", 2) #NUEVO
				resultado = "¡Has ganado!" #NUEVO
				porcentaje_alcanzado_exportar = 100
				porcent_vida_alaIzquierda = vida_alaIzquierda/vida_alaIzquierda_org
				porcent_vida_alaDerecha = vida_alaDerecha/vida_alaDerecha_org
				porcent_vida_motor = vida_motor/vida_motor_org
				porcent_vida_frontal = vida_frontal/vida_frontal_org
				porcentaje_Medio_de_vida_exportar = (round((porcent_vida_alaIzquierda + porcent_vida_alaDerecha + porcent_vida_motor + porcent_vida_frontal)/4, 2))*100

				#NUEVO -->

				porcent_vida_alaIzquierda *= 100
				porcent_vida_alaDerecha *= 100
				porcent_vida_motor *= 100
				porcent_vida_frontal *= 100

				if porcent_vida_alaIzquierda == 100:
					estado_alaizquierda = 0

				elif porcent_vida_alaIzquierda < 100 and porcent_vida_alaIzquierda > 0:
					estado_alaizquierda = 1

				elif porcent_vida_alaIzquierda == 0:
					estado_alaizquierda = 2

				if porcent_vida_alaDerecha == 100:
					estado_aladerecha = 0

				elif porcent_vida_alaDerecha < 100 and porcent_vida_alaDerecha > 0:
					estado_aladerecha = 1

				elif porcent_vida_alaDerecha == 0:
					estado_aladerecha = 2

				if porcent_vida_motor == 100:
					estado_motor = 0

				elif porcent_vida_motor < 100 and porcent_vida_motor > 0:
					estado_motor = 1

				elif porcent_vida_motor == 0:
					estado_motor = 2

				if porcent_vida_frontal == 100:
					estado_frontal = 0

				elif porcent_vida_frontal < 100 and porcent_vida_frontal > 0:
					estado_frontal = 1

				elif porcent_vida_frontal == 0:
					estado_frontal = 2


				if escudo == True:
					puntuacion_exportar = puntuacion * 2
					estado_escudo = 0

				else:
					puntuacion_exportar = puntuacion
					estado_escudo = 2

				estado_final_nave = "No destruida"

				# --> NUEVO

				ejecutar_pantalla_resultados(ventana, user_act[1], Lv_act, pantalla_act, puntuacion_total, monedas_totales, Naves_destruidas, segundostranscurridos, Monedas, puntuacion_exportar, resultado, Nº_Naves, estado_escudo, estado_alaizquierda, estado_aladerecha, estado_motor, estado_frontal, estado_final_nave)

			else:
				crear_texto_en_pantalla(ventana, "¡PERDISTE!, este texto es temporal", 2)
				resultado = "¡Has perdido!" #NUEVO
				porcentaje_alcanzado_exportar = 0
				porcentaje_Medio_de_vida_exportar = 0
				puntuacion_exportar = puntuacion #NUEVO
				estado_escudo = 2 #NUEVO
				estado_alaizquierda = 2 #NUEVO
				estado_aladerecha = 2 #NUEVO
				estado_motor = 2 #NUEVO
				estado_frontal = 2 #NUEVO
				estado_final_nave = "Destruida" #NUEVO

				ejecutar_pantalla_resultados(ventana, user_act[1], Lv_act, pantalla_act, puntuacion_total, monedas_totales, Naves_destruidas, segundostranscurridos, Monedas, puntuacion_exportar, resultado, Nº_Naves, estado_escudo, estado_alaizquierda, estado_aladerecha, estado_motor, estado_frontal, estado_final_nave)

			if escudo == True: 
				puntuacion_exportar = puntuacion * 2

			else:
				puntuacion_exportar = puntuacion

			naves_destruidas_exportar = Naves_destruidas
			tiempo_exportar = segundostranscurridos

			datos_conseguidos = [True, [puntuacion_exportar, naves_destruidas_exportar, porcentaje_Medio_de_vida_exportar, tiempo_exportar, porcentaje_alcanzado_exportar, Monedas]]
			Exit_presionado = True

		if viva == False and nave_prin_explotando == False:
			ventana.blit(NavePrincipalNegro, (round(xn), round(yn)))
			nave_prin_explotando = True

			naves_destruidas_a_explotar.append([round(xn), round(yn), "Principal", 1])

		for evento in pygame.event.get():

			if evento.type == KEYDOWN or evento.type == KEYUP:
				ultimoseventos.append(evento)
				press = True

			if evento.type == QUIT:
				print("Juego terminado")
				Exit_presionado = True
				#time.sleep(1)
				pygame.quit()
				raise KeyError

			elif evento.type == KEYDOWN: #Teclas que se presionen una vez

				if evento.key == 285: #F4 = para cerrar el programa; hecho
					print("Juego terminado")
					Exit_presionado = True
					#time.sleep(1)
					pygame.quit()
					raise KeyError

				elif evento.key == 112 or evento.key == 27: # Letra "P" y ESC
					salida = crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

					if salida == True:
						Exit_presionado = True

					pygame.mouse.set_visible(False)
					pygame.draw.rect(ventana, negro, (posx1rectcentre + round(tamañoline/2), 0, 640 - round(tamañoline/2), alto))

					recien_salido = True

					teclaizquierdapress = False
					tecladerechapress = False
					teclaabajopress = False
					teclaarribapress = False
					disparoAmigo = False

					primeravuelta = True
					vueltas = 0

					pygame.display.update()

				elif evento.key == 102: #Letra "F"

					if fpsactivos == True:
						fpsactivos = False
						cambioFps = True

					else:
						fpsactivos = True

		for disparo in listdisparos_NA: #Balas amigas contra naves enemigas

			for nave in naves:

				if nave.posx < disparo[0] and nave.posx + 40 > disparo[0] + 2 and nave.posy < disparo[1] and nave.posy + 22 > disparo[1] and nave.viva == True:

					puntuacion += 10
					aborrar.append(listdisparos_NA.index(disparo))
					aborrar.sort()
					aborrar.reverse()

					nave.recibirdañoEBA(daño_por_proyectil[tipodeproyectilamigo])

		for borrado in aborrar:
			pygame.draw.rect(ventana, negro, ((listdisparos_NA[borrado])[0], (listdisparos_NA[borrado])[1], 4, 16))
			listdisparos_NA.pop(borrado)

		aborrar = []

		if disparado == True:
			disparado = False

			caracteristicas = [vida_alaDerecha, vida_alaDerecha_org, vida_alaIzquierda, vida_alaIzquierda_org, vida_motor, vida_motor_org, vida_frontal, vida_frontal_org, alaDerecha, alaIzquierda, motor, frontal]

			resultados4 = actualizar_pantalla_izquierda_arriba(ventana, caracteristicas)

			txt1_AI, posxytxt1_AI = resultados4[0]
			Nave_act_Controlador_De_Daños = resultados4[1]
			vida_alaDerecha = resultados4[2]
			vida_alaIzquierda = resultados4[3]
			vida_motor = resultados4[4]
			vida_frontal = resultados4[5]
			viva = resultados4[6]
			alaDerecha = resultados4[7]
			alaIzquierda = resultados4[8]
			motor = resultados4[9]
			frontal = resultados4[10]

			if escudo: ventana.blit(Escudo, (posxControlador - 8, posyControlador - 8))

			caracteristicas = [vida_alaDerecha, vida_alaDerecha_org, vida_alaIzquierda, vida_alaIzquierda_org, vida_motor, vida_motor_org, vida_frontal, vida_frontal_org, alaDerecha, alaIzquierda, motor, frontal]

			if txt1_AI != ["", ""]: ventana.blit(txt1_AI, (posxytxt1_AI[0], posxytxt1_AI[1]))
			ventana.blit(Nave_act_Controlador_De_Daños, (posxControlador, posyControlador))

			tipos_de_vidas = [frontal, motor, alaDerecha, alaIzquierda]

			eleabuscar = []

			for vida in tipos_de_vidas:

				eleabuscar.append(vida)

			index_Nave_Prin = Data_Prin.index(eleabuscar)

		for evento in pygame.event.get():

			if evento.type == KEYDOWN or evento.type == KEYUP:
				ultimoseventos.append(evento)
				press = True

			if evento.type == QUIT:
				print("Juego terminado")
				Exit_presionado = True
				#time.sleep(1)
				pygame.quit()
				raise KeyError

			elif evento.type == KEYDOWN: #Teclas que se presionen una vez

				if evento.key == 285: #F4 = para cerrar el programa; hecho
					print("Juego terminado")
					Exit_presionado = True
					#time.sleep(1)
					pygame.quit()
					raise KeyError

				elif evento.key == 112 or evento.key == 27: # Letra "P" y ESC
					salida = crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

					if salida == True:
						Exit_presionado = True

					pygame.mouse.set_visible(False)
					pygame.draw.rect(ventana, negro, (posx1rectcentre + round(tamañoline/2), 0, 640 - round(tamañoline/2), alto))

					recien_salido = True

					teclaizquierdapress = False
					tecladerechapress = False
					teclaabajopress = False
					teclaarribapress = False
					disparoAmigo = False

					primeravuelta = True
					vueltas = 0

					pygame.display.update()

				elif evento.key == 102: #Letra "F"

					if fpsactivos == True:
						fpsactivos = False
						cambioFps = True

					else:
						fpsactivos = True

		if turno == True:
			turno = False

			for nave_a_explotar in naves_destruidas_a_explotar:

				if nave_a_explotar[3] == 7:

					ventana.blit(Explosion7_Negro, (nave_a_explotar[0], nave_a_explotar[1]))

					aborrar.append(naves_destruidas_a_explotar.index(nave_a_explotar))
					aborrar.sort()
					aborrar.reverse()

					explotada = True

					if nave_a_explotar[2] == "Principal":

						pygame.draw.rect(ventana, negro, (posxline1 + tamañoline, 0, 640 - tamañoline - 1, alto))
						pygame.display.update()

						crear_texto_en_pantalla(ventana, "¡PERDISTE!, este texto es temporal", 2) #Poner aqui la direccion al la página de perdiste
						resultado = "¡Has perdido!" #NUEVO
						Exit_presionado = True

						puntuacion_exportar = puntuacion #NUEVO
						estado_escudo = 2 #NUEVO
						estado_alaizquierda = 2 #NUEVO
						estado_aladerecha = 2 #NUEVO
						estado_motor = 2 #NUEVO
						estado_frontal = 2 #NUEVO
						estado_final_nave = "Destruida" #NUEVO

						ejecutar_pantalla_resultados(ventana, user_acet[1], Lv_act, pantalla_act, puntuacion_total, monedas_totales, Naves_destruidas, segundostranscurridos, Monedas, puntuacion_exportar, resultado, Nº_Naves, estado_escudo, estado_alaizquierda, estado_aladerecha, estado_motor, estado_frontal, estado_final_nave)
						
						break

					else:
						
						Naves_destruidas += 1

						resultados = actualizar_pantalla_derecha_arriba(ventana, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, fpsactivos, infinito, segundostranscurridos)

						txt1_AD, posxytxt1_AD = resultados[0]
						txt2_AD, posxytxt2_AD = resultados[1]
						txt3_AD, posxytxt3_AD = resultados[2]
						txt4_AD, posxytxt4_AD = resultados[3]
						txt5_AD, posxytxt5_AD = resultados[4]
						txt6_AD, posxytxt6_AD = resultados[5]
						txt7_AD, posxytxt7_AD = resultados[6]

						if txt1_AD != ["", ""]: ventana.blit(txt1_AD, (posxytxt1_AD[0], posxytxt1_AD[1]))
						if txt2_AD != ["", ""]: ventana.blit(txt2_AD, (posxytxt2_AD[0], posxytxt2_AD[1]))
						if txt3_AD != ["", ""]: ventana.blit(txt3_AD, (posxytxt3_AD[0], posxytxt3_AD[1]))
						if txt4_AD != ["", ""]: ventana.blit(txt4_AD, (posxytxt4_AD[0], posxytxt4_AD[1]))
						if txt5_AD != ["", ""]: ventana.blit(txt5_AD, (posxytxt5_AD[0], posxytxt5_AD[1]))
						if txt6_AD != ["", ""]: ventana.blit(txt6_AD, (posxytxt6_AD[0], posxytxt6_AD[1]))
						if txt7_AD != ["", ""]: ventana.blit(txt7_AD, (posxytxt7_AD[0], posxytxt7_AD[1]))

				elif nave_a_explotar[3] == 1:
					
					ventana.blit(Explosion1, (nave_a_explotar[0], nave_a_explotar[1]))

					indexnave = naves_destruidas_a_explotar.index(nave_a_explotar)

					naves_destruidas_a_explotar[indexnave].pop(3)

					naves_destruidas_a_explotar[indexnave].insert(3, 2)

				elif nave_a_explotar[3] == 2:

					ventana.blit(Explosion1_Negro, (nave_a_explotar[0], nave_a_explotar[1]))

					ventana.blit(Explosion2, (nave_a_explotar[0], nave_a_explotar[1]))

					indexnave = naves_destruidas_a_explotar.index(nave_a_explotar)

					naves_destruidas_a_explotar[indexnave].pop(3)

					naves_destruidas_a_explotar[indexnave].insert(3, 3)

				elif nave_a_explotar[3] == 3:

					ventana.blit(Explosion2_Negro, (nave_a_explotar[0], nave_a_explotar[1]))

					ventana.blit(Explosion3, (nave_a_explotar[0], nave_a_explotar[1]))

					indexnave = naves_destruidas_a_explotar.index(nave_a_explotar)

					naves_destruidas_a_explotar[indexnave].pop(3)

					naves_destruidas_a_explotar[indexnave].insert(3, 4)

				elif nave_a_explotar[3] == 4:
					
					ventana.blit(Explosion4_Negro, (nave_a_explotar[0], nave_a_explotar[1]))

					ventana.blit(Explosion5, (nave_a_explotar[0], nave_a_explotar[1]))

					indexnave = naves_destruidas_a_explotar.index(nave_a_explotar)

					naves_destruidas_a_explotar[indexnave].pop(3)

					naves_destruidas_a_explotar[indexnave].insert(3, 5)

				elif nave_a_explotar[3] == 5:
					
					ventana.blit(Explosion5_Negro, (nave_a_explotar[0], nave_a_explotar[1]))

					ventana.blit(Explosion6, (nave_a_explotar[0], nave_a_explotar[1]))

					indexnave = naves_destruidas_a_explotar.index(nave_a_explotar)

					naves_destruidas_a_explotar[indexnave].pop(3)

					naves_destruidas_a_explotar[indexnave].insert(3, 6)

				elif nave_a_explotar[3] == 6:
					
					ventana.blit(Explosion6_Negro, (nave_a_explotar[0], nave_a_explotar[1]))

					ventana.blit(Explosion7, (nave_a_explotar[0], nave_a_explotar[1]))

					indexnave = naves_destruidas_a_explotar.index(nave_a_explotar)

					naves_destruidas_a_explotar[indexnave].pop(3)

					naves_destruidas_a_explotar[indexnave].insert(3, 7)

			for borrado in aborrar:

				naves_destruidas_a_explotar.pop(borrado)

			aborrar = []

		else:
			turno = True

		for evento in pygame.event.get():

			if evento.type == KEYDOWN or evento.type == KEYUP:
				ultimoseventos.append(evento)
				press = True

			if evento.type == QUIT:
				print("Juego terminado")
				Exit_presionado = True
				#time.sleep(1)
				pygame.quit()
				raise KeyError

			elif evento.type == KEYDOWN: #Teclas que se presionen una vez

				if evento.key == 285: #F4 = para cerrar el programa; hecho
					print("Juego terminado")
					Exit_presionado = True
					#time.sleep(1)
					pygame.quit()
					raise KeyError

				elif evento.key == 112 or evento.key == 27: # Letra "P" y ESC
					salida = crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

					if salida == True:
						Exit_presionado = True

					pygame.mouse.set_visible(False)
					pygame.draw.rect(ventana, negro, (posx1rectcentre + round(tamañoline/2), 0, 640 - round(tamañoline/2), alto))

					recien_salido = True

					teclaizquierdapress = False
					tecladerechapress = False
					teclaabajopress = False
					teclaarribapress = False
					disparoAmigo = False

					primeravuelta = True
					vueltas = 0

					pygame.display.update()

				elif evento.key == 102: #Letra "F"

					if fpsactivos == True:
						fpsactivos = False
						cambioFps = True

					else:
						fpsactivos = True

		if antsecond < second: #Acciones que ocurran cada segundo

			med = round(math.fsum(fpslist)/len(fpslist))

			fpslist = []

			segundostranscurridos += 1

			resultados = actualizar_pantalla_derecha_arriba(ventana, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, med, fpsactivos, infinito, segundostranscurridos)

			txt1_AD, posxytxt1_AD = resultados[0]
			txt2_AD, posxytxt2_AD = resultados[1]
			txt3_AD, posxytxt3_AD = resultados[2]
			txt4_AD, posxytxt4_AD = resultados[3]
			txt5_AD, posxytxt5_AD = resultados[4]
			txt6_AD, posxytxt6_AD = resultados[5]
			txt7_AD, posxytxt7_AD = resultados[6]

			if txt1_AD != ["", ""]: ventana.blit(txt1_AD, (posxytxt1_AD[0], posxytxt1_AD[1]))
			if txt2_AD != ["", ""]: ventana.blit(txt2_AD, (posxytxt2_AD[0], posxytxt2_AD[1]))
			if txt3_AD != ["", ""]: ventana.blit(txt3_AD, (posxytxt3_AD[0], posxytxt3_AD[1]))
			if txt4_AD != ["", ""]: ventana.blit(txt4_AD, (posxytxt4_AD[0], posxytxt4_AD[1]))
			if txt5_AD != ["", ""]: ventana.blit(txt5_AD, (posxytxt5_AD[0], posxytxt5_AD[1]))
			if txt6_AD != ["", ""]: ventana.blit(txt6_AD, (posxytxt6_AD[0], posxytxt6_AD[1]))
			if txt7_AD != ["", ""]: ventana.blit(txt7_AD, (posxytxt7_AD[0], posxytxt7_AD[1]))

		### ACCIONES DE CONTROL ### ACCIONES DE CONTROL ### ACCIONES DE CONTROL ### ACCIONES DE CONTROL ### ACCIONES DE CONTROL ###

		for evento in pygame.event.get():

			if evento.type == KEYDOWN or evento.type == KEYUP:
				ultimoseventos.append(evento)
				press = True

			if evento.type == QUIT:
				print("Juego terminado")
				Exit_presionado = True
				#time.sleep(1)
				pygame.quit()
				raise KeyError

			elif evento.type == KEYDOWN: #Teclas que se presionen una vez

				if evento.key == 285: #F4 = para cerrar el programa; hecho
					print("Juego terminado")
					Exit_presionado = True
					#time.sleep(1)
					pygame.quit()
					raise KeyError

				elif evento.key == 112 or evento.key == 27: # Letra "P" y ESC
					salida = crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

					if salida == True:
						Exit_presionado = True

					pygame.mouse.set_visible(False)
					pygame.draw.rect(ventana, negro, (posx1rectcentre + round(tamañoline/2), 0, 640 - round(tamañoline/2), alto))

					recien_salido = True

					teclaizquierdapress = False
					tecladerechapress = False
					teclaabajopress = False
					teclaarribapress = False
					disparoAmigo = False

					primeravuelta = True
					vueltas = 0

					pygame.display.update()

				elif evento.key == 102: #Letra "F"

					if fpsactivos == True:
						fpsactivos = False
						cambioFps = True

					else:
						fpsactivos = True

		if press == True and primeravuelta == False: #Teclas de control que puedan estar presionadas mucho tiempo

			for ultimoevento in ultimoseventos:

				if ultimoevento.type == KEYDOWN:

					if ultimoevento.key == 276 or ultimoevento.key == 97: #Izquierda
						teclaizquierdapress = True

					if ultimoevento.key == 275 or ultimoevento.key == 100: #Derecha
						tecladerechapress = True

					if ultimoevento.key == 274 or ultimoevento.key == 115: #Abajo
						teclaabajopress = True

					if ultimoevento.key == 273 or ultimoevento.key == 119: #Arriba
						teclaarribapress = True

					if ultimoevento.key == 32: #Espacio
						disparoAmigo = True

				elif ultimoevento.type == KEYUP and primeravuelta == False:

					if ultimoevento.key == 276 or ultimoevento.key == 97: #Izquierda
						teclaizquierdapress = False

					if ultimoevento.key == 275 or ultimoevento.key == 100: #Derecha
						tecladerechapress = False

					if ultimoevento.key == 274 or ultimoevento.key == 115: #Abajo
						teclaabajopress = False

					if ultimoevento.key == 273 or ultimoevento.key == 119: #Arriba
						teclaarribapress = False

					if ultimoevento.key == 32: #Espacio
						disparoAmigo = False

			ultimoseventos = []

		if teclaizquierdapress == True and viva == True:

			ventana.blit(NavePrincipalNegro, (round(xn), round(yn)))

			if xn > 330:

				xn -= (450/FPS)*0.5

			ventana.blit(Tipos_De_Naves_Prin[index_Nave_Prin], (round(xn), round(yn)))

		if tecladerechapress == True and viva == True:

			ventana.blit(NavePrincipalNegro, (round(xn), round(yn)))

			if xn < 910:

				xn += (450/FPS)*0.5

			ventana.blit(Tipos_De_Naves_Prin[index_Nave_Prin], (round(xn), round(yn)))

		if teclaabajopress == True and viva == True:

			ventana.blit(NavePrincipalNegro, (round(xn), round(yn)))

			if yn < 688:

				yn += (450/FPS)*0.5

			ventana.blit(Tipos_De_Naves_Prin[index_Nave_Prin], (round(xn), round(yn)))

		if teclaarribapress == True and viva == True:

			ventana.blit(NavePrincipalNegro, (round(xn), round(yn)))

			if yn > 370:

				yn -= (450/FPS)*0.5

			ventana.blit(Tipos_De_Naves_Prin[index_Nave_Prin], (round(xn), round(yn)))

		if teclaarribapress == False and teclaabajopress == False and tecladerechapress == False and teclaizquierdapress == False and primeravuelta == False and viva == True:

			ventana.blit(NavePrincipalNegro, (round(xn), round(yn)))

			if alaDerecha == False or alaIzquierda == False:
				multiplicador = 0.2

			else:
				multiplicador = 0.1

			if yn < 688:

				yn += (450/FPS)*multiplicador

			ventana.blit(Tipos_De_Naves_Prin[index_Nave_Prin], (round(xn), round(yn)))

		for evento in pygame.event.get():

			if evento.type == KEYDOWN or evento.type == KEYUP:
				ultimoseventos.append(evento)
				press = True

			if evento.type == QUIT:
				print("Juego terminado")
				Exit_presionado = True
				#time.sleep(1)
				pygame.quit()
				raise KeyError

			elif evento.type == KEYDOWN: #Teclas que se presionen una vez

				if evento.key == 285: #F4 = para cerrar el programa; hecho
					print("Juego terminado")
					Exit_presionado = True
					#time.sleep(1)
					pygame.quit()
					raise KeyError

				elif evento.key == 112 or evento.key == 27: # Letra "P" y ESC
					salida = crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

					if salida == True:
						Exit_presionado = True

					pygame.mouse.set_visible(False)
					pygame.draw.rect(ventana, negro, (posx1rectcentre + round(tamañoline/2), 0, 640 - round(tamañoline/2), alto))

					recien_salido = True

					teclaizquierdapress = False
					tecladerechapress = False
					teclaabajopress = False
					teclaarribapress = False
					disparoAmigo = False

					primeravuelta = True
					vueltas = 0

					pygame.display.update()

				elif evento.key == 102: #Letra "F"

					if fpsactivos == True:
						fpsactivos = False
						cambioFps = True

					else:
						fpsactivos = True

		if disparoAmigo == True and viva == True: #Sirve para disparar una cantidad determinada de disparos

			data_time_ant = data_time

			data_time_microsecond = str(datetime.now().microsecond)
			data_time_second = str(datetime.now().second)
			data_time_minute = datetime.now().minute

			if len(data_time_second) != 2:
				data_time_second = "0" + data_time_second

			for i in range(6 - len(data_time_microsecond)):
				data_time_microsecond = "0" + data_time_microsecond

			data_time_prueva = int(str(data_time_minute) + data_time_second + data_time_microsecond)
			
			if data_time_prueva - data_time_ant > tiempo_de_diferencia_entre_disparos:

				data_time = data_time_prueva

				dispararya = True

			if alaDerecha == True and alaIzquierda == True and frontal == True:

				if nºdisparos == 1 and dispararya == True:

					disparoaañadir = [xn + 21, yn, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 2 and dispararya == True:

					disparoaañadir = [xn + 40, yn, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn, yn + 1, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 3 and dispararya == True:

					disparoaañadir = [xn + 40, yn, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn, yn + 1, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 21, yn - 1, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 4 and dispararya == True:

					disparoaañadir = [xn + 40, yn, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn, yn + 1, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 8, yn + 4, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 32, yn + 5, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 5 and dispararya == True:

					disparoaañadir = [xn + 40, yn, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn, yn + 1, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 8, yn + 4, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 32, yn + 5, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 21, yn - 1, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

			elif alaDerecha == False:

				if nºdisparos == 1 and dispararya == True:

					disparoaañadir = [xn + 21, yn, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 2 and dispararya == True:

					disparoaañadir = [xn + 21, yn, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn, yn + 1, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 3 and dispararya == True:

					disparoaañadir = [xn + 21, yn, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn, yn + 1, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 8, yn -1, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 4 and dispararya == True:

					disparoaañadir = [xn + 21, yn, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn, yn + 1, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 8, yn -1, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 5 and dispararya == True:

					disparoaañadir = [xn + 21, yn, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn, yn + 1, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 8, yn -1, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

			elif alaIzquierda == False:

				if nºdisparos == 1 and dispararya == True:

					disparoaañadir = [xn + 21, yn, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 2 and dispararya == True:

					disparoaañadir = [xn + 40, yn, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 21, yn, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 3 and dispararya == True:

					disparoaañadir = [xn + 40, yn, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 32, yn + 5, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 21, yn - 1, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 4 and dispararya == True:

					disparoaañadir = [xn + 40, yn, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 32, yn + 5, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 21, yn - 1, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 5 and dispararya == True:

					disparoaañadir = [xn + 40, yn, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 32, yn + 5, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 21, yn - 1, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

			elif frontal == False:

				if nºdisparos == 1 and dispararya == True:

					disparoaañadir = [xn + 32, yn + 5, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 2 and dispararya == True:

					disparoaañadir = [xn + 32, yn + 5, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 8, yn + 4, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 3 and dispararya == True:

					disparoaañadir = [xn + 40, yn, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 32, yn + 5, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 8, yn + 4, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 4 and dispararya == True:

					disparoaañadir = [xn + 40, yn, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn, yn + 1, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 8, yn + 4, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 32, yn + 5, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 5 and dispararya == True:

					disparoaañadir = [xn + 40, yn, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn, yn + 1, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 8, yn + 4, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 32, yn + 5, disparos[tipodeproyectilamigo], 1]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

		### ACCIONES DE OBJETOS ### ACCIONES DE OBJETOS ### ACCIONES DE OBJETOS ### ACCIONES DE OBJETOS ### ACCIONES DE OBJETOS ###

		if fpsactivos == False and cambioFps == True: #Esconder los FPS
			cambioFps = False

			resultados = actualizar_pantalla_derecha_arriba(ventana, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, False, infinito, segundostranscurridos)

			txt1_AD, posxytxt1_AD = resultados[0]
			txt2_AD, posxytxt2_AD = resultados[1]
			txt3_AD, posxytxt3_AD = resultados[2]
			txt4_AD, posxytxt4_AD = resultados[3]
			txt5_AD, posxytxt5_AD = resultados[4]
			txt6_AD, posxytxt6_AD = resultados[5]
			txt7_AD, posxytxt7_AD = resultados[6]

			if txt1_AD != ["", ""]: ventana.blit(txt1_AD, (posxytxt1_AD[0], posxytxt1_AD[1]))
			if txt2_AD != ["", ""]: ventana.blit(txt2_AD, (posxytxt2_AD[0], posxytxt2_AD[1]))
			if txt3_AD != ["", ""]: ventana.blit(txt3_AD, (posxytxt3_AD[0], posxytxt3_AD[1]))
			if txt4_AD != ["", ""]: ventana.blit(txt4_AD, (posxytxt4_AD[0], posxytxt4_AD[1]))
			if txt5_AD != ["", ""]: ventana.blit(txt5_AD, (posxytxt5_AD[0], posxytxt5_AD[1]))
			if txt6_AD != ["", ""]: ventana.blit(txt6_AD, (posxytxt6_AD[0], posxytxt6_AD[1]))
			if txt7_AD != ["", ""]: ventana.blit(txt7_AD, (posxytxt7_AD[0], posxytxt7_AD[1]))

		if tocada == True:

			if tempcontroler < 1:
				tocada = False

			else:
				ventana.blit(Barrera_Rojo, (320, posybarrera))
				tempcontroler -= (400/FPS)

		else:

			ventana.blit(Barrera_Azul, (320, posybarrera))

		if Exit_presionado == False:

			pygame.display.update()

		if MaxFPS > 0: time.sleep(1/sumer)

		primeravuelta = False

		if list_naves.count(1) == 0 and Naves_destruidas != Nº_Naves and explotada == True and Exit_presionado == False: 

			ultimoseventos = []

			if infinito == True:
				Nº_Naves += 20

			for disparo in listdisparos_NA: #Naves amigas
				
				ventana.blit(DisparoNegro, (disparo[0], disparo[1]))

			for disparo in listdisparos_NE: #Naves enemigas

				ventana.blit(DisparoNegro, (disparo[0], disparo[1]))

			listdisparos_NA = []
			listdisparos_NE = []

			usados = []
			oleada += 1

			naves, list_naves, usados = crear_oleada(ventana, Lv_act, infinito, list_naves, usados, oleada, radio)

			for nave in naves:

				ventana.blit(nave.ImagenNave, (nave.posx, nave.posy))

				time.sleep(0.05)

				pygame.display.update()

			crear_texto_en_pantalla(ventana,"OLEADA Nº" + str(oleada), 0.5)

			primeravuelta = True
			vueltas = 0
			navecayendo = False

			for evento in pygame.event.get():

				if evento.type == KEYDOWN or evento.type == KEYUP:
					ultimoseventos.append(evento)
					press = True

				if evento.type == QUIT:
					print("Juego terminado")
					Exit_presionado = True
					#time.sleep(1)
					pygame.quit()
					raise KeyError

				elif evento.type == KEYDOWN: #Teclas que se presionen una vez

					if evento.key == 285: #F4 = para cerrar el programa; hecho
						print("Juego terminado")
						Exit_presionado = True
						#time.sleep(1)
						pygame.quit()
						raise KeyError

					elif evento.key == 112 or evento.key == 27: # Letra "P" y ESC
						salida = crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

						if salida == True:
							Exit_presionado = True

						pygame.mouse.set_visible(False)
						pygame.draw.rect(ventana, negro, (posx1rectcentre + round(tamañoline/2), 0, 640 - round(tamañoline/2), alto))

						recien_salido = True

						teclaizquierdapress = False
						tecladerechapress = False
						teclaabajopress = False
						teclaarribapress = False
						disparoAmigo = False

						primeravuelta = True
						vueltas = 0

						pygame.display.update()

					elif evento.key == 102: #Letra "F"

						if fpsactivos == True:
							fpsactivos = False
							cambioFps = True

						else:
							fpsactivos = True

			ultimoseventos = []

			teclaizquierdapress = False
			tecladerechapress = False
			teclaabajopress = False
			teclaarribapress = False
			disparoAmigo = False

		explotada = False

		vueltas += 1

	if datos_conseguidos[0] == True:
		return datos_conseguidos[1]

	else:
		return False