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

from Modulos.basededatosmejorasfaciliter import *

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

	datos_nave_prin = extraerdatosmejoras(user_act[1])# [Proteccion, Daño, Velocidad, Escudo]

	print(datos_nave_prin)

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

	tamañoControladorx = round(0.13125 * ancho)
	tamañoControladory = round(0.14444444444444 * alto)

	tamañoEscudox = round(0.14375 * ancho)
	tamañoEscudoy = round(0.166666666 * alto)

	posxControlador = round(0.809375 * ancho)
	posyControlador = round(80)

	posxbarrera = round(0.25 * ancho)
	posybarrera = round(0.069444444444 * alto)

	posbossx = 384
	posbossy = 10
	tamañobossx = 512
	tamañobossy = 336

	multiplier_boss = 8

	tamaño_Barra_Vida_Bossx = 240
	tamaño_Barra_Vida_Bossy = 22

	posxbarraboss = int(640 - round(tamaño_Barra_Vida_Bossx/2))
	print(posxbarraboss)
	posybarraboss = posbossy

	nave_ancho = 42

	nave_alto = 26

	nave_ancho_escudo = 46
	nave_alto_escudo = 30

	tamañox_Explosion_Nuclear = 90
	tamañoy_Explosion_Nuclear = 94

	#Caracteristicas: Primero = Proteccion, Segundo = Daño de disparo, Tercero = Daño cuerpo a cuerpo, Cuarto = Velocidad, Quinto = Si tiene escudo o no. (El escudo es que cuando lo mata se regenera y se le desactiva el escudo)

	caracteristicas_naves_enemigas = [(5, 25, 2, 100, False), (15, 25, 5, 100, False), (20, 30, 8, 150, False), (20, 60, 10, 140, True), (40, 100, 20, 130, False), (60, 135, 45, 150, False), (100, 200, 50, 200, True), (250, 250, 70, 250, True), (400, 350, 85, 225, False), (800, 500, 100, 220, True)]

	nivel_de_aparecimiento = [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]

	daño_por_proyectil = [(datos_nave_prin[0])[1], 0]

	list_naves = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	posxvuelta = [420, 540, 700, 820]

	probabilidad_nave_boss = [0.2, 0.2, 0.5]

	Velocidades_boss = [0.05, 0.1, 0.2]

	probabilidad_tipo_nave_boss = [[65, 95, 100, 0, 0, 0, 0, 0, 0, 0], [45, 70, 90, 100, 0, 0, 0, 0, 0, 0], [30, 55, 70, 90, 100, 0, 0, 0, 0, 0]]

	ladoboss = [[[120, 184, 228], [368 ,184, 48]], [[88, 224, 228], [376, 224, 48]], [270, 180, random.randrange(50, 400)]] #[[[diferenciax con punto inicio, diferenciay con punto de inicio, grados positivos con eje diagonal de las x y direccion izda], []]]

	posiciones_ocupadas = 0

	usados = []

	# ========== DISPAROS ==========

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
	DisparoVerde_alpha = pygame.image.load("Imagenes/Disparos/Disparo_6.png")
	DisparoVerde = pygame.transform.scale(DisparoVerde_alpha, (2, 8)) # 1 X 4
	DisparoNuclear_alpha = pygame.image.load("Imagenes/Disparos/Disparo_7.png")
	DisparoNuclear = pygame.transform.scale(DisparoNuclear_alpha, (6, 6)) # 6 X 6

	DisparoNuclearNegro_alpha = pygame.image.load("Imagenes/Disparos/Disparo_7_Negro.png")
	DisparoNuclearNegro = pygame.transform.scale(DisparoNuclearNegro_alpha, (6, 6)) # 6 X 6

	disparos = [DisparoBlanco, DisparoRojo, DisparoAzul, DisparoAmarillo, DisparoVerde, DisparoNuclear]

	DisparosNegros = [DisparoNegro, DisparoNegro, DisparoNegro, DisparoNegro, DisparoNegro, DisparoNuclearNegro]

	# ========== NAVES AMIGAS ==========

	NavePrincipal_alpha = pygame.image.load("Imagenes/Naves_Amigas/NavePrin.png")
	NavePrincipal = pygame.transform.scale(NavePrincipal_alpha, (nave_ancho, nave_alto)) # 21 X 13
	NavePrincipalNegro_alpha = pygame.image.load("Imagenes/Naves_Amigas/NavePrinNegro.png")
	NavePrincipalNegro = pygame.transform.scale(NavePrincipalNegro_alpha, (nave_ancho, nave_alto)) # 21 X 13
	NavePrincipal_SinAla_Derecha_aplha = pygame.image.load("Imagenes/Naves_Amigas/NavePrin_SinAla_Derecha.png")
	NavePrincipal_SinAla_Derecha = pygame.transform.scale(NavePrincipal_SinAla_Derecha_aplha, (nave_ancho, nave_alto)) # 21 X 13
	NavePrincipal_SinAla_Izquierda_alpha = pygame.image.load("Imagenes/Naves_Amigas/NavePrin_SinAla_Izquierda.png")
	NavePrincipal_SinAla_Izquierda = pygame.transform.scale(NavePrincipal_SinAla_Izquierda_alpha, (nave_ancho, nave_alto)) # 21 X 13
	NavePrincipal_SinAlas_aplha = pygame.image.load("Imagenes/Naves_Amigas/NavePrin_SinAla_Derecha_e_Izquierda.png")
	NavePrincipal_SinAlas = pygame.transform.scale(NavePrincipal_SinAlas_aplha, (nave_ancho, nave_alto)) # 21 X 13
	NavePrincipal_SinPico_alpha = pygame.image.load("Imagenes/Naves_Amigas/NavePrin_SinPico.png")
	NavePrincipal_SinPico = pygame.transform.scale(NavePrincipal_SinPico_alpha, (nave_ancho, nave_alto)) # 21 X 13
	NavePrincipal_SinPico_y_Ala_Derecha_aplha = pygame.image.load("Imagenes/Naves_Amigas/NavePrin_SinPico_y_Ala_Derecha.png")
	NavePrincipal_SinPico_y_Ala_Derecha = pygame.transform.scale(NavePrincipal_SinPico_y_Ala_Derecha_aplha, (nave_ancho, nave_alto)) # 21 X 13
	NavePrincipal_SinPico_y_Ala_Izquierda_alpha = pygame.image.load("Imagenes/Naves_Amigas/NavePrin_SinPico_y_Ala_Izquierda.png")
	NavePrincipal_SinPico_y_Ala_Izquierda = pygame.transform.scale(NavePrincipal_SinPico_y_Ala_Izquierda_alpha, (nave_ancho, nave_alto)) # 21 X 13
	NavePrincipal_SinPico_y_Motor_alpha = pygame.image.load("Imagenes/Naves_Amigas/NavePrin_SinPico_y_Ala_Izquierda.png")
	NavePrincipal_SinPico_y_Motor = pygame.transform.scale(NavePrincipal_SinPico_y_Motor_alpha, (nave_ancho, nave_alto)) # 21 X 13
	Escudo_alpha = pygame.image.load("Imagenes/Naves_Amigas/NavePrin_Escudo.png")
	Escudo = pygame.transform.scale(Escudo_alpha, (tamañoEscudox, tamañoEscudoy)) # 23 X 15
	Escudo_Nave = pygame.transform.scale(Escudo_alpha, (nave_ancho_escudo, nave_alto_escudo)) # 23 X 15
	Escudo_SinAla_Derecha_alpha = pygame.image.load("Imagenes/Naves_Amigas/NavePrin_Escudo_SinAla_Derecha.png")
	Escudo_SinAla_Derecha = pygame.transform.scale(Escudo_SinAla_Derecha_alpha, (nave_ancho_escudo, nave_alto_escudo)) # 23 X 15
	Escudo_SinAla_Izquierda_alpha = pygame.image.load("Imagenes/Naves_Amigas/NavePrin_Escudo_SinAla_Izquierda.png")
	Escudo_SinAla_Izquierda = pygame.transform.scale(Escudo_SinAla_Izquierda_alpha, (nave_ancho_escudo, nave_alto_escudo)) # 23 X 15
	Escudo_SinAla_Derecha_e_Izquierda_alpha = pygame.image.load("Imagenes/Naves_Amigas/NavePrin_Escudo_SinAla_Derecha_e_Izquierda.png")
	Escudo_SinAla_Derecha_e_Izquierda = pygame.transform.scale(Escudo_SinAla_Derecha_e_Izquierda_alpha, (nave_ancho_escudo, nave_alto_escudo)) # 23 X 15
	Escudo_SinPico_alpha = pygame.image.load("Imagenes/Naves_Amigas/NavePrin_Escudo_SinPico.png")
	Escudo_SinPico = pygame.transform.scale(Escudo_SinPico_alpha, (nave_ancho_escudo, nave_alto_escudo)) # 23 X 15

	Escudo_Negro_alpha = pygame.image.load("Imagenes/Naves_Amigas/NavePrin_Escudo_Negro.png")
	Escudo_Negro = pygame.transform.scale(Escudo_Negro_alpha, (nave_ancho_escudo, nave_alto_escudo)) # 23 X 15

	Escudos_Nave_Prin = [Escudo_Nave, Escudo_SinAla_Derecha, Escudo_SinAla_Izquierda, Escudo_SinAla_Derecha_e_Izquierda, Escudo_SinPico]
	Data_Escudos = [[True, True, True, True], [True, True, False, True], [True, True, True, False], [True, True, False, False], [False, True, True, True]]
	
	Tipos_De_Naves_Prin = [NavePrincipal, NavePrincipal_SinAla_Izquierda, NavePrincipal_SinAla_Derecha, NavePrincipal_SinAlas, NavePrincipal_SinPico, NavePrincipal_SinPico_y_Ala_Derecha, NavePrincipal_SinPico_y_Ala_Izquierda, NavePrincipal_SinPico_y_Motor, NavePrincipalNegro]
	Data_Prin = [[True, True, True, True], [True, True, True, False], [True, True, False, True], [True, True, False, False], [False, True, True, True], [False, True, False, True], [False, True, True, False], [False, False, True, True], [False, False, False, False]]

	### ========== NAVES ENEMIGAS ========== ###

	Nave1_Negro_alpha = pygame.image.load("Imagenes/Naves_Enemigas/EBEN1_negra.png")
	Nave1_Negro = pygame.transform.scale(Nave1_Negro_alpha, (round(0.03125 * ancho), round(0.03055555555555555555555555555556 * alto))) # 20 X 11 to 40 X 22
	Nave2_Negro_alpha = pygame.image.load("Imagenes/Naves_Enemigas/EBEN2_negra.png")
	Nave2_Negro = pygame.transform.scale(Nave2_Negro_alpha, (round(0.03125 * ancho), round(0.03055555555555555555555555555556 * alto))) # 20 X 11 to 40 X 22
	Nave3_Negro_alpha = pygame.image.load("Imagenes/Naves_Enemigas/EBEN3_negra.png")
	Nave3_Negro = pygame.transform.scale(Nave3_Negro_alpha, (round(0.03125 * ancho), round(0.03055555555555555555555555555556 * alto))) # 20 X 11 to 40 X 22
	Nave4_Negro_alpha = pygame.image.load("Imagenes/Naves_Enemigas/EBEN4_negra.png")
	Nave4_Negro = pygame.transform.scale(Nave4_Negro_alpha, (round(0.028125 * ancho), round(0.04166666666666666666666666666667 * alto)))
	Nave5_Negro_alpha = pygame.image.load("Imagenes/Naves_Enemigas/EBEN5_negra.png")
	Nave5_Negro = pygame.transform.scale(Nave5_Negro_alpha, (round(0.028125 * ancho), round(0.04166666666666666666666666666667 * alto)))
	Nave6_Negro_alpha = pygame.image.load("Imagenes/Naves_Enemigas/EBEN6_negra.png")
	Nave6_Negro = pygame.transform.scale(Nave6_Negro_alpha, (round(0.028125 * ancho), round(0.04583333333333333333333333333333 * alto)))

	Naves_Negro = [Nave1_Negro, Nave2_Negro, Nave3_Negro, Nave4_Negro, Nave5_Negro, Nave6_Negro]

	dire = "Imagenes/Barra/Barra3.png" #Copiar desde aquí
	barra_alpha = pygame.image.load(dire)
	barra = pygame.transform.scale(barra_alpha, (round(0.2265625 * ancho), round(0.20833333333333333333333333333333 * alto)))
	ventana.fill(negro)
	ventana.blit(barra, (round(0.38671875 * ancho), round(0.39583333333333333333333333333333 * alto)))
	ventana.blit(txt_1, (posxytxt_1[0], posxytxt_1[1]))
	pygame.display.update() #Hasta aqui

	# ========== EXPLOSIONES ==========

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

	ExplosionNuclear1_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_0.png")
	ExplosionNuclear1 = pygame.transform.scale(ExplosionNuclear1_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionNuclear2_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_1.png")
	ExplosionNuclear2 = pygame.transform.scale(ExplosionNuclear2_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionNuclear3_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_2.png")
	ExplosionNuclear3 = pygame.transform.scale(ExplosionNuclear3_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionNuclear4_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_3.png")
	ExplosionNuclear4 = pygame.transform.scale(ExplosionNuclear4_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionNuclear5_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_4.png")
	ExplosionNuclear5 = pygame.transform.scale(ExplosionNuclear5_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionNuclear6_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_5.png")
	ExplosionNuclear6 = pygame.transform.scale(ExplosionNuclear6_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionNuclear7_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_6.png")
	ExplosionNuclear7 = pygame.transform.scale(ExplosionNuclear7_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionNuclear8_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_7.png")
	ExplosionNuclear8 = pygame.transform.scale(ExplosionNuclear8_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionNuclear9_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_8.png")
	ExplosionNuclear9 = pygame.transform.scale(ExplosionNuclear9_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionNuclear10_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_9.png")
	ExplosionNuclear10 = pygame.transform.scale(ExplosionNuclear10_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionNuclear11_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_10.png")
	ExplosionNuclear11 = pygame.transform.scale(ExplosionNuclear11_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionNuclear12_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_11.png")
	ExplosionNuclear12 = pygame.transform.scale(ExplosionNuclear12_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47

	ExplosionesNucleares = [ExplosionNuclear1, ExplosionNuclear2, ExplosionNuclear3, ExplosionNuclear4, ExplosionNuclear5, ExplosionNuclear6, ExplosionNuclear7, ExplosionNuclear8, ExplosionNuclear9, ExplosionNuclear10, ExplosionNuclear11, ExplosionNuclear12]

	dire = "Imagenes/Barra/Barra5.png" #Copiar desde aquí
	barra_alpha = pygame.image.load(dire)
	barra = pygame.transform.scale(barra_alpha, (round(0.2265625 * ancho), round(0.20833333333333333333333333333333 * alto)))
	ventana.fill(negro)
	ventana.blit(barra, (round(0.38671875 * ancho), round(0.39583333333333333333333333333333 * alto)))
	ventana.blit(txt_1, (posxytxt_1[0], posxytxt_1[1]))
	pygame.display.update() #Hasta aqui

	ExplosionNuclear1_Negro_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_0_Negro.png")
	ExplosionNuclear1_Negro = pygame.transform.scale(ExplosionNuclear1_Negro_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionNuclear2_Negro_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_1_Negro.png")
	ExplosionNuclear2_Negro = pygame.transform.scale(ExplosionNuclear2_Negro_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionNuclear3_Negro_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_2_Negro.png")
	ExplosionNuclear3_Negro = pygame.transform.scale(ExplosionNuclear3_Negro_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionNuclear4_Negro_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_3_Negro.png")
	ExplosionNuclear4_Negro = pygame.transform.scale(ExplosionNuclear4_Negro_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionNuclear5_Negro_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_4_Negro.png")
	ExplosionNuclear5_Negro = pygame.transform.scale(ExplosionNuclear5_Negro_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionNuclear6_Negro_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_5_Negro.png")
	ExplosionNuclear6_Negro = pygame.transform.scale(ExplosionNuclear6_Negro_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionNuclear7_Negro_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_6_Negro.png")
	ExplosionNuclear7_Negro = pygame.transform.scale(ExplosionNuclear7_Negro_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionNuclear8_Negro_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_7_Negro.png")
	ExplosionNuclear8_Negro = pygame.transform.scale(ExplosionNuclear8_Negro_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionNuclear9_Negro_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_8_Negro.png")
	ExplosionNuclear9_Negro = pygame.transform.scale(ExplosionNuclear9_Negro_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionNuclear10_Negro_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_9_Negro.png")
	ExplosionNuclear10_Negro = pygame.transform.scale(ExplosionNuclear10_Negro_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionNuclear11_Negro_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_10_Negro.png")
	ExplosionNuclear11_Negro = pygame.transform.scale(ExplosionNuclear11_Negro_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionNuclear12_Negro_alpha = pygame.image.load("Imagenes/Explosion_Nuclear/Explosion_11_Negro.png")
	ExplosionNuclear12_Negro = pygame.transform.scale(ExplosionNuclear12_Negro_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47

	ExplosionesNucleares_Negro = [ExplosionNuclear1_Negro, ExplosionNuclear2_Negro, ExplosionNuclear3_Negro, ExplosionNuclear4_Negro, ExplosionNuclear5_Negro, ExplosionNuclear6_Negro, ExplosionNuclear7_Negro, ExplosionNuclear8_Negro, ExplosionNuclear9_Negro, ExplosionNuclear10_Negro, ExplosionNuclear11_Negro, ExplosionNuclear12_Negro]

	ExplosionDisparoBoss2_1_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_2/Explosion_0.png")
	ExplosionDisparoBoss2_1 = pygame.transform.scale(ExplosionDisparoBoss2_1_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionDisparoBoss2_2_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_2/Explosion_1.png")
	ExplosionDisparoBoss2_2 = pygame.transform.scale(ExplosionDisparoBoss2_2_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionDisparoBoss2_3_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_2/Explosion_2.png")
	ExplosionDisparoBoss2_3 = pygame.transform.scale(ExplosionDisparoBoss2_3_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionDisparoBoss2_4_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_2/Explosion_3.png")
	ExplosionDisparoBoss2_4 = pygame.transform.scale(ExplosionDisparoBoss2_4_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionDisparoBoss2_5_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_2/Explosion_4.png")
	ExplosionDisparoBoss2_5 = pygame.transform.scale(ExplosionDisparoBoss2_5_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionDisparoBoss2_6_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_2/Explosion_5.png")
	ExplosionDisparoBoss2_6 = pygame.transform.scale(ExplosionDisparoBoss2_6_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionDisparoBoss2_7_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_2/Explosion_6.png")
	ExplosionDisparoBoss2_7 = pygame.transform.scale(ExplosionDisparoBoss2_7_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionDisparoBoss2_8_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_2/Explosion_7.png")
	ExplosionDisparoBoss2_8 = pygame.transform.scale(ExplosionDisparoBoss2_8_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionDisparoBoss2_9_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_2/Explosion_8.png")
	ExplosionDisparoBoss2_9 = pygame.transform.scale(ExplosionDisparoBoss2_9_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionDisparoBoss2_10_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_2/Explosion_9.png")
	ExplosionDisparoBoss2_10 = pygame.transform.scale(ExplosionDisparoBoss2_10_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionDisparoBoss2_11_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_2/Explosion_10.png")
	ExplosionDisparoBoss2_11 = pygame.transform.scale(ExplosionDisparoBoss2_11_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionDisparoBoss2_12_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_2/Explosion_11.png")
	ExplosionDisparoBoss2_12 = pygame.transform.scale(ExplosionDisparoBoss2_12_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47

	ExplosionesDisparoBoss2 = [ExplosionDisparoBoss2_1, ExplosionDisparoBoss2_2, ExplosionDisparoBoss2_3, ExplosionDisparoBoss2_4, ExplosionDisparoBoss2_5, ExplosionDisparoBoss2_6, ExplosionDisparoBoss2_7, ExplosionDisparoBoss2_8, ExplosionDisparoBoss2_9, ExplosionDisparoBoss2_10, ExplosionDisparoBoss2_11, ExplosionDisparoBoss2_12]

	ExplosionDisparoBoss3_1_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_3/Explosion_0.png")
	ExplosionDisparoBoss3_1 = pygame.transform.scale(ExplosionDisparoBoss3_1_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionDisparoBoss3_2_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_3/Explosion_1.png")
	ExplosionDisparoBoss3_2 = pygame.transform.scale(ExplosionDisparoBoss3_2_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionDisparoBoss3_3_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_3/Explosion_2.png")
	ExplosionDisparoBoss3_3 = pygame.transform.scale(ExplosionDisparoBoss3_3_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionDisparoBoss3_4_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_3/Explosion_3.png")
	ExplosionDisparoBoss3_4 = pygame.transform.scale(ExplosionDisparoBoss3_4_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionDisparoBoss3_5_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_3/Explosion_4.png")
	ExplosionDisparoBoss3_5 = pygame.transform.scale(ExplosionDisparoBoss3_5_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionDisparoBoss3_6_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_3/Explosion_5.png")
	ExplosionDisparoBoss3_6 = pygame.transform.scale(ExplosionDisparoBoss3_6_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionDisparoBoss3_7_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_3/Explosion_6.png")
	ExplosionDisparoBoss3_7 = pygame.transform.scale(ExplosionDisparoBoss3_7_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionDisparoBoss3_8_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_3/Explosion_7.png")
	ExplosionDisparoBoss3_8 = pygame.transform.scale(ExplosionDisparoBoss3_8_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionDisparoBoss3_9_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_3/Explosion_8.png")
	ExplosionDisparoBoss3_9 = pygame.transform.scale(ExplosionDisparoBoss3_9_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionDisparoBoss3_10_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_3/Explosion_9.png")
	ExplosionDisparoBoss3_10 = pygame.transform.scale(ExplosionDisparoBoss3_10_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionDisparoBoss3_11_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_3/Explosion_10.png")
	ExplosionDisparoBoss3_11 = pygame.transform.scale(ExplosionDisparoBoss3_11_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47
	ExplosionDisparoBoss3_12_alpha = pygame.image.load("Imagenes/Explosion_Disparo_Boss_3/Explosion_11.png")
	ExplosionDisparoBoss3_12 = pygame.transform.scale(ExplosionDisparoBoss3_12_alpha, (tamañox_Explosion_Nuclear, tamañoy_Explosion_Nuclear)) # 45 X 47

	ExplosionesDisparoBoss3 = [ExplosionDisparoBoss3_1, ExplosionDisparoBoss3_2, ExplosionDisparoBoss3_3, ExplosionDisparoBoss3_4, ExplosionDisparoBoss3_5, ExplosionDisparoBoss3_6, ExplosionDisparoBoss3_7, ExplosionDisparoBoss3_8, ExplosionDisparoBoss3_9, ExplosionDisparoBoss3_10, ExplosionDisparoBoss3_11, ExplosionDisparoBoss3_12]

	dire = "Imagenes/Barra/Barra6.png" #Copiar desde aquí
	barra_alpha = pygame.image.load(dire)
	barra = pygame.transform.scale(barra_alpha, (round(0.2265625 * ancho), round(0.20833333333333333333333333333333 * alto)))
	ventana.fill(negro)
	ventana.blit(barra, (round(0.38671875 * ancho), round(0.39583333333333333333333333333333 * alto)))
	ventana.blit(txt_1, (posxytxt_1[0], posxytxt_1[1]))
	pygame.display.update() #Hasta aqui

	# ========== BARRERA ==========

	Barrera_Azul = pygame.image.load("Imagenes/Barreras/Barrera_Azul.png")
	Barrera_Rojo = pygame.image.load("Imagenes/Barreras/Barrera_Roja.png")

	# ========== DETECCION DE DAÑOS ==========

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

	dire = "Imagenes/Barra/Barra7.png" #Copiar desde aquí
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

	dire = "Imagenes/Barra/Barra8.png" #Copiar desde aquí
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

	dire = "Imagenes/Barra/Barra9.png" #Copiar desde aquí
	barra_alpha = pygame.image.load(dire)
	barra = pygame.transform.scale(barra_alpha, (round(0.2265625 * ancho), round(0.20833333333333333333333333333333 * alto)))
	ventana.fill(negro)
	ventana.blit(barra, (round(0.38671875 * ancho), round(0.39583333333333333333333333333333 * alto)))
	ventana.blit(txt_1, (posxytxt_1[0], posxytxt_1[1]))
	pygame.display.update() #Hasta aqui

	# ========== MONEDAS ==========

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

	dire = "Imagenes/Barra/Barra10.png" #Copiar desde aquí
	barra_alpha = pygame.image.load(dire)
	barra = pygame.transform.scale(barra_alpha, (round(0.2265625 * ancho), round(0.20833333333333333333333333333333 * alto)))
	ventana.fill(negro)
	ventana.blit(barra, (round(0.38671875 * ancho), round(0.39583333333333333333333333333333 * alto)))
	ventana.blit(txt_1, (posxytxt_1[0], posxytxt_1[1]))
	pygame.display.update() #Hasta aqui

	# ========== BARRA VIDA BOSS ==========

	Barra_Vida_Boss_100_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_100.png")
	Barra_Vida_Boss_100 = pygame.transform.scale(Barra_Vida_Boss_100_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_99_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_99.png")
	Barra_Vida_Boss_99 = pygame.transform.scale(Barra_Vida_Boss_99_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_98_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_98.png")
	Barra_Vida_Boss_98 = pygame.transform.scale(Barra_Vida_Boss_98_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_97_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_97.png")
	Barra_Vida_Boss_97 = pygame.transform.scale(Barra_Vida_Boss_97_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_96_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_96.png")
	Barra_Vida_Boss_96 = pygame.transform.scale(Barra_Vida_Boss_96_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_95_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_95.png")
	Barra_Vida_Boss_95 = pygame.transform.scale(Barra_Vida_Boss_95_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_94_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_94.png")
	Barra_Vida_Boss_94 = pygame.transform.scale(Barra_Vida_Boss_94_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_93_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_93.png")
	Barra_Vida_Boss_93 = pygame.transform.scale(Barra_Vida_Boss_93_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_92_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_92.png")
	Barra_Vida_Boss_92 = pygame.transform.scale(Barra_Vida_Boss_92_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_91_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_91.png")
	Barra_Vida_Boss_91 = pygame.transform.scale(Barra_Vida_Boss_91_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_90_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_90.png")
	Barra_Vida_Boss_90 = pygame.transform.scale(Barra_Vida_Boss_90_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_89_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_89.png")
	Barra_Vida_Boss_89 = pygame.transform.scale(Barra_Vida_Boss_89_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_88_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_88.png")
	Barra_Vida_Boss_88 = pygame.transform.scale(Barra_Vida_Boss_88_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_87_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_87.png")
	Barra_Vida_Boss_87 = pygame.transform.scale(Barra_Vida_Boss_87_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_86_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_86.png")
	Barra_Vida_Boss_86 = pygame.transform.scale(Barra_Vida_Boss_86_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_85_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_85.png")
	Barra_Vida_Boss_85 = pygame.transform.scale(Barra_Vida_Boss_85_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_84_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_84.png")
	Barra_Vida_Boss_84 = pygame.transform.scale(Barra_Vida_Boss_84_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_83_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_83.png")
	Barra_Vida_Boss_83 = pygame.transform.scale(Barra_Vida_Boss_83_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_82_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_82.png")
	Barra_Vida_Boss_82 = pygame.transform.scale(Barra_Vida_Boss_82_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_81_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_81.png")
	Barra_Vida_Boss_81 = pygame.transform.scale(Barra_Vida_Boss_81_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_80_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_80.png")
	Barra_Vida_Boss_80 = pygame.transform.scale(Barra_Vida_Boss_80_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_79_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_79.png")
	Barra_Vida_Boss_79 = pygame.transform.scale(Barra_Vida_Boss_79_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12

	dire = "Imagenes/Barra/Barra11.png" #Copiar desde aquí
	barra_alpha = pygame.image.load(dire)
	barra = pygame.transform.scale(barra_alpha, (round(0.2265625 * ancho), round(0.20833333333333333333333333333333 * alto)))
	ventana.fill(negro)
	ventana.blit(barra, (round(0.38671875 * ancho), round(0.39583333333333333333333333333333 * alto)))
	ventana.blit(txt_1, (posxytxt_1[0], posxytxt_1[1]))
	pygame.display.update() #Hasta aqui

	Barra_Vida_Boss_78_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_78.png")
	Barra_Vida_Boss_78 = pygame.transform.scale(Barra_Vida_Boss_78_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_77_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_77.png")
	Barra_Vida_Boss_77 = pygame.transform.scale(Barra_Vida_Boss_77_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_76_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_76.png")
	Barra_Vida_Boss_76 = pygame.transform.scale(Barra_Vida_Boss_76_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_75_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_75.png")
	Barra_Vida_Boss_75 = pygame.transform.scale(Barra_Vida_Boss_75_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_74_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_74.png")
	Barra_Vida_Boss_74 = pygame.transform.scale(Barra_Vida_Boss_74_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_73_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_73.png")
	Barra_Vida_Boss_73 = pygame.transform.scale(Barra_Vida_Boss_73_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_72_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_72.png")
	Barra_Vida_Boss_72 = pygame.transform.scale(Barra_Vida_Boss_72_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_71_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_71.png")
	Barra_Vida_Boss_71 = pygame.transform.scale(Barra_Vida_Boss_71_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_70_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_70.png")
	Barra_Vida_Boss_70 = pygame.transform.scale(Barra_Vida_Boss_70_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_69_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_69.png")
	Barra_Vida_Boss_69 = pygame.transform.scale(Barra_Vida_Boss_69_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_68_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_68.png")
	Barra_Vida_Boss_68 = pygame.transform.scale(Barra_Vida_Boss_68_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_67_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_67.png")
	Barra_Vida_Boss_67 = pygame.transform.scale(Barra_Vida_Boss_67_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_66_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_66.png")
	Barra_Vida_Boss_66 = pygame.transform.scale(Barra_Vida_Boss_66_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_65_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_65.png")
	Barra_Vida_Boss_65 = pygame.transform.scale(Barra_Vida_Boss_65_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_64_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_64.png")
	Barra_Vida_Boss_64 = pygame.transform.scale(Barra_Vida_Boss_64_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_63_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_63.png")
	Barra_Vida_Boss_63 = pygame.transform.scale(Barra_Vida_Boss_63_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_62_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_62.png")
	Barra_Vida_Boss_62 = pygame.transform.scale(Barra_Vida_Boss_62_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_61_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_61.png")
	Barra_Vida_Boss_61 = pygame.transform.scale(Barra_Vida_Boss_61_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_60_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_60.png")
	Barra_Vida_Boss_60 = pygame.transform.scale(Barra_Vida_Boss_60_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_59_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_59.png")
	Barra_Vida_Boss_59 = pygame.transform.scale(Barra_Vida_Boss_59_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_58_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_58.png")
	Barra_Vida_Boss_58 = pygame.transform.scale(Barra_Vida_Boss_58_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_57_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_57.png")
	Barra_Vida_Boss_57 = pygame.transform.scale(Barra_Vida_Boss_57_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_56_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_56.png")
	Barra_Vida_Boss_56 = pygame.transform.scale(Barra_Vida_Boss_56_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12

	dire = "Imagenes/Barra/Barra12.png" #Copiar desde aquí
	barra_alpha = pygame.image.load(dire)
	barra = pygame.transform.scale(barra_alpha, (round(0.2265625 * ancho), round(0.20833333333333333333333333333333 * alto)))
	ventana.fill(negro)
	ventana.blit(barra, (round(0.38671875 * ancho), round(0.39583333333333333333333333333333 * alto)))
	ventana.blit(txt_1, (posxytxt_1[0], posxytxt_1[1]))
	pygame.display.update() #Hasta aqui

	Barra_Vida_Boss_55_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_55.png")
	Barra_Vida_Boss_55 = pygame.transform.scale(Barra_Vida_Boss_55_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_54_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_54.png")
	Barra_Vida_Boss_54 = pygame.transform.scale(Barra_Vida_Boss_54_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_53_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_53.png")
	Barra_Vida_Boss_53 = pygame.transform.scale(Barra_Vida_Boss_53_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_52_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_52.png")
	Barra_Vida_Boss_52 = pygame.transform.scale(Barra_Vida_Boss_52_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_51_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_51.png")
	Barra_Vida_Boss_51 = pygame.transform.scale(Barra_Vida_Boss_51_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_50_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_50.png")
	Barra_Vida_Boss_50 = pygame.transform.scale(Barra_Vida_Boss_50_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_49_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_49.png")
	Barra_Vida_Boss_49 = pygame.transform.scale(Barra_Vida_Boss_49_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_48_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_48.png")
	Barra_Vida_Boss_48 = pygame.transform.scale(Barra_Vida_Boss_48_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_47_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_47.png")
	Barra_Vida_Boss_47 = pygame.transform.scale(Barra_Vida_Boss_47_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_46_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_46.png")
	Barra_Vida_Boss_46 = pygame.transform.scale(Barra_Vida_Boss_46_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_45_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_45.png")
	Barra_Vida_Boss_45 = pygame.transform.scale(Barra_Vida_Boss_45_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_44_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_44.png")
	Barra_Vida_Boss_44 = pygame.transform.scale(Barra_Vida_Boss_44_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_43_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_43.png")
	Barra_Vida_Boss_43 = pygame.transform.scale(Barra_Vida_Boss_43_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_42_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_42.png")
	Barra_Vida_Boss_42 = pygame.transform.scale(Barra_Vida_Boss_42_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_41_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_41.png")
	Barra_Vida_Boss_41 = pygame.transform.scale(Barra_Vida_Boss_41_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_40_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_40.png")
	Barra_Vida_Boss_40 = pygame.transform.scale(Barra_Vida_Boss_40_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_39_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_39.png")
	Barra_Vida_Boss_39 = pygame.transform.scale(Barra_Vida_Boss_39_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_38_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_38.png")
	Barra_Vida_Boss_38 = pygame.transform.scale(Barra_Vida_Boss_38_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_37_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_37.png")
	Barra_Vida_Boss_37 = pygame.transform.scale(Barra_Vida_Boss_37_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_36_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_36.png")
	Barra_Vida_Boss_36 = pygame.transform.scale(Barra_Vida_Boss_36_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_35_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_35.png")
	Barra_Vida_Boss_35 = pygame.transform.scale(Barra_Vida_Boss_35_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_34_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_34.png")
	Barra_Vida_Boss_34 = pygame.transform.scale(Barra_Vida_Boss_34_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_33_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_33.png")
	Barra_Vida_Boss_33 = pygame.transform.scale(Barra_Vida_Boss_33_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_32_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_32.png")
	Barra_Vida_Boss_32 = pygame.transform.scale(Barra_Vida_Boss_32_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_31_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_31.png")
	Barra_Vida_Boss_31 = pygame.transform.scale(Barra_Vida_Boss_31_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_30_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_30.png")
	Barra_Vida_Boss_30 = pygame.transform.scale(Barra_Vida_Boss_30_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_29_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_29.png")
	Barra_Vida_Boss_29 = pygame.transform.scale(Barra_Vida_Boss_29_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12

	dire = "Imagenes/Barra/Barra13.png" #Copiar desde aquí
	barra_alpha = pygame.image.load(dire)
	barra = pygame.transform.scale(barra_alpha, (round(0.2265625 * ancho), round(0.20833333333333333333333333333333 * alto)))
	ventana.fill(negro)
	ventana.blit(barra, (round(0.38671875 * ancho), round(0.39583333333333333333333333333333 * alto)))
	ventana.blit(txt_1, (posxytxt_1[0], posxytxt_1[1]))
	pygame.display.update() #Hasta aqui

	Barra_Vida_Boss_28_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_28.png")
	Barra_Vida_Boss_28 = pygame.transform.scale(Barra_Vida_Boss_28_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_27_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_27.png")
	Barra_Vida_Boss_27 = pygame.transform.scale(Barra_Vida_Boss_27_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_26_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_26.png")
	Barra_Vida_Boss_26 = pygame.transform.scale(Barra_Vida_Boss_26_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_25_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_25.png")
	Barra_Vida_Boss_25 = pygame.transform.scale(Barra_Vida_Boss_25_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_24_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_24.png")
	Barra_Vida_Boss_24 = pygame.transform.scale(Barra_Vida_Boss_24_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_23_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_23.png")
	Barra_Vida_Boss_23 = pygame.transform.scale(Barra_Vida_Boss_23_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_22_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_22.png")
	Barra_Vida_Boss_22 = pygame.transform.scale(Barra_Vida_Boss_22_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_21_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_21.png")
	Barra_Vida_Boss_21 = pygame.transform.scale(Barra_Vida_Boss_21_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_20_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_20.png")
	Barra_Vida_Boss_20 = pygame.transform.scale(Barra_Vida_Boss_20_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_19_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_19.png")
	Barra_Vida_Boss_19 = pygame.transform.scale(Barra_Vida_Boss_19_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_18_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_18.png")
	Barra_Vida_Boss_18 = pygame.transform.scale(Barra_Vida_Boss_18_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_17_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_17.png")
	Barra_Vida_Boss_17 = pygame.transform.scale(Barra_Vida_Boss_17_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_16_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_16.png")
	Barra_Vida_Boss_16 = pygame.transform.scale(Barra_Vida_Boss_16_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_15_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_15.png")
	Barra_Vida_Boss_15 = pygame.transform.scale(Barra_Vida_Boss_15_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_14_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_14.png")
	Barra_Vida_Boss_14 = pygame.transform.scale(Barra_Vida_Boss_14_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_13_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_13.png")
	Barra_Vida_Boss_13 = pygame.transform.scale(Barra_Vida_Boss_13_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_12_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_12.png")
	Barra_Vida_Boss_12 = pygame.transform.scale(Barra_Vida_Boss_12_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_11_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_11.png")
	Barra_Vida_Boss_11 = pygame.transform.scale(Barra_Vida_Boss_11_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_10_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_10.png")
	Barra_Vida_Boss_10 = pygame.transform.scale(Barra_Vida_Boss_10_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_9_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_9.png")
	Barra_Vida_Boss_9 = pygame.transform.scale(Barra_Vida_Boss_9_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_8_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_8.png")
	Barra_Vida_Boss_8 = pygame.transform.scale(Barra_Vida_Boss_8_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_7_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_7.png")
	Barra_Vida_Boss_7 = pygame.transform.scale(Barra_Vida_Boss_7_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_6_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_6.png")
	Barra_Vida_Boss_6 = pygame.transform.scale(Barra_Vida_Boss_6_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_5_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_5.png")
	Barra_Vida_Boss_5 = pygame.transform.scale(Barra_Vida_Boss_5_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_4_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_4.png")
	Barra_Vida_Boss_4 = pygame.transform.scale(Barra_Vida_Boss_4_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_3_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_3.png")
	Barra_Vida_Boss_3 = pygame.transform.scale(Barra_Vida_Boss_3_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_2_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_2.png")
	Barra_Vida_Boss_2 = pygame.transform.scale(Barra_Vida_Boss_2_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_1_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_1.png")
	Barra_Vida_Boss_1 = pygame.transform.scale(Barra_Vida_Boss_1_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12
	Barra_Vida_Boss_0_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_0.png")
	Barra_Vida_Boss_0 = pygame.transform.scale(Barra_Vida_Boss_0_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12

	Barra_Vida_Boss_Negro_alpha = pygame.image.load("Imagenes/Barra_Vida_Boss/Barra_Vida_Negro.png")
	Barra_Vida_Boss_Negro = pygame.transform.scale(Barra_Vida_Boss_Negro_alpha, (tamaño_Barra_Vida_Bossx, tamaño_Barra_Vida_Bossy)) #128 X 12

	dire = "Imagenes/Barra/Barra14.png" #Copiar desde aquí
	barra_alpha = pygame.image.load(dire)
	barra = pygame.transform.scale(barra_alpha, (round(0.2265625 * ancho), round(0.20833333333333333333333333333333 * alto)))
	ventana.fill(negro)
	ventana.blit(barra, (round(0.38671875 * ancho), round(0.39583333333333333333333333333333 * alto)))
	ventana.blit(txt_1, (posxytxt_1[0], posxytxt_1[1]))
	pygame.display.update() #Hasta aqui

	# ========== BOSSES Y SUS APARICIONES ==========

	# === BOSS Nº1 ===

	Boss_1_alpha = pygame.image.load("Imagenes/Bosses/Boss1.png")
	Boss_1 = pygame.transform.scale(Boss_1_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_1_Negro_alpha = pygame.image.load("Imagenes/Bosses/Boss1_Negro.png")
	Boss_1_Negro = pygame.transform.scale(Boss_1_Negro_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_1_Escudo_alpha = pygame.image.load("Imagenes/Bosses/Boss1_Escudo.png")
	Boss_1_Escudo = pygame.transform.scale(Boss_1_Escudo_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_1_Escudo_Negro_alpha = pygame.image.load("Imagenes/Bosses/Boss1_Escudo_Negro.png")
	Boss_1_Escudo_Negro = pygame.transform.scale(Boss_1_Escudo_Negro_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_1_ap_10_alpha = pygame.image.load("Imagenes/Bosses/Boss_1_ap_10.png")
	Boss_1_ap_10 = pygame.transform.scale(Boss_1_ap_10_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_1_ap_9_alpha = pygame.image.load("Imagenes/Bosses/Boss_1_ap_9.png")
	Boss_1_ap_9 = pygame.transform.scale(Boss_1_ap_9_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_1_ap_8_alpha = pygame.image.load("Imagenes/Bosses/Boss_1_ap_8.png")
	Boss_1_ap_8 = pygame.transform.scale(Boss_1_ap_8_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_1_ap_7_alpha = pygame.image.load("Imagenes/Bosses/Boss_1_ap_7.png")
	Boss_1_ap_7 = pygame.transform.scale(Boss_1_ap_7_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_1_ap_6_alpha = pygame.image.load("Imagenes/Bosses/Boss_1_ap_6.png")
	Boss_1_ap_6 = pygame.transform.scale(Boss_1_ap_6_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_1_ap_5_alpha = pygame.image.load("Imagenes/Bosses/Boss_1_ap_5.png")
	Boss_1_ap_5 = pygame.transform.scale(Boss_1_ap_5_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_1_ap_4_alpha = pygame.image.load("Imagenes/Bosses/Boss_1_ap_4.png")
	Boss_1_ap_4 = pygame.transform.scale(Boss_1_ap_4_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_1_ap_3_alpha = pygame.image.load("Imagenes/Bosses/Boss_1_ap_3.png")
	Boss_1_ap_3 = pygame.transform.scale(Boss_1_ap_3_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_1_ap_2_alpha = pygame.image.load("Imagenes/Bosses/Boss_1_ap_2.png")
	Boss_1_ap_2 = pygame.transform.scale(Boss_1_ap_2_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_1_ap_1_alpha = pygame.image.load("Imagenes/Bosses/Boss_1_ap_1.png")
	Boss_1_ap_1 = pygame.transform.scale(Boss_1_ap_1_alpha, (tamañobossx, tamañobossy)) #64 X 42

	# === BOSS Nº2 ===

	Boss_2_alpha = pygame.image.load("Imagenes/Bosses/Boss2.png")
	Boss_2 = pygame.transform.scale(Boss_2_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_2_Negro_alpha = pygame.image.load("Imagenes/Bosses/Boss2_Negro.png")
	Boss_2_Negro = pygame.transform.scale(Boss_2_Negro_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_2_Escudo_alpha = pygame.image.load("Imagenes/Bosses/Boss2_Escudo.png")
	Boss_2_Escudo = pygame.transform.scale(Boss_2_Escudo_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_2_Escudo_Negro_alpha = pygame.image.load("Imagenes/Bosses/Boss2_Escudo_Negro.png")
	Boss_2_Escudo_Negro = pygame.transform.scale(Boss_2_Escudo_Negro_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_2_ap_10_alpha = pygame.image.load("Imagenes/Bosses/Boss_2_ap_10.png")
	Boss_2_ap_10 = pygame.transform.scale(Boss_2_ap_10_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_2_ap_9_alpha = pygame.image.load("Imagenes/Bosses/Boss_2_ap_9.png")
	Boss_2_ap_9 = pygame.transform.scale(Boss_2_ap_9_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_2_ap_8_alpha = pygame.image.load("Imagenes/Bosses/Boss_2_ap_8.png")
	Boss_2_ap_8 = pygame.transform.scale(Boss_2_ap_8_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_2_ap_7_alpha = pygame.image.load("Imagenes/Bosses/Boss_2_ap_7.png")
	Boss_2_ap_7 = pygame.transform.scale(Boss_2_ap_7_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_2_ap_6_alpha = pygame.image.load("Imagenes/Bosses/Boss_2_ap_6.png")
	Boss_2_ap_6 = pygame.transform.scale(Boss_2_ap_6_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_2_ap_5_alpha = pygame.image.load("Imagenes/Bosses/Boss_2_ap_5.png")
	Boss_2_ap_5 = pygame.transform.scale(Boss_2_ap_5_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_2_ap_4_alpha = pygame.image.load("Imagenes/Bosses/Boss_2_ap_4.png")
	Boss_2_ap_4 = pygame.transform.scale(Boss_2_ap_4_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_2_ap_3_alpha = pygame.image.load("Imagenes/Bosses/Boss_2_ap_3.png")
	Boss_2_ap_3 = pygame.transform.scale(Boss_2_ap_3_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_2_ap_2_alpha = pygame.image.load("Imagenes/Bosses/Boss_2_ap_2.png")
	Boss_2_ap_2 = pygame.transform.scale(Boss_2_ap_2_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_2_ap_1_alpha = pygame.image.load("Imagenes/Bosses/Boss_2_ap_1.png")
	Boss_2_ap_1 = pygame.transform.scale(Boss_2_ap_1_alpha, (tamañobossx, tamañobossy)) #64 X 42

	# === BOSS Nº3 === 

	Boss_3_alpha = pygame.image.load("Imagenes/Bosses/Boss3.png")
	Boss_3 = pygame.transform.scale(Boss_3_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_3_Negro_alpha = pygame.image.load("Imagenes/Bosses/Boss3_Negro.png")
	Boss_3_Negro = pygame.transform.scale(Boss_3_Negro_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_3_Escudo_alpha = pygame.image.load("Imagenes/Bosses/Boss3_Escudo.png")
	Boss_3_Escudo = pygame.transform.scale(Boss_3_Escudo_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_3_Escudo_Negro_alpha = pygame.image.load("Imagenes/Bosses/Boss3_Escudo_Negro.png")
	Boss_3_Escudo_Negro = pygame.transform.scale(Boss_3_Escudo_Negro_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_3_ap_10_alpha = pygame.image.load("Imagenes/Bosses/Boss_3_ap_10.png")
	Boss_3_ap_10 = pygame.transform.scale(Boss_3_ap_10_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_3_ap_9_alpha = pygame.image.load("Imagenes/Bosses/Boss_3_ap_9.png")
	Boss_3_ap_9 = pygame.transform.scale(Boss_3_ap_9_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_3_ap_8_alpha = pygame.image.load("Imagenes/Bosses/Boss_3_ap_8.png")
	Boss_3_ap_8 = pygame.transform.scale(Boss_3_ap_8_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_3_ap_7_alpha = pygame.image.load("Imagenes/Bosses/Boss_3_ap_7.png")
	Boss_3_ap_7 = pygame.transform.scale(Boss_3_ap_7_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_3_ap_6_alpha = pygame.image.load("Imagenes/Bosses/Boss_3_ap_6.png")
	Boss_3_ap_6 = pygame.transform.scale(Boss_3_ap_6_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_3_ap_5_alpha = pygame.image.load("Imagenes/Bosses/Boss_3_ap_5.png")
	Boss_3_ap_5 = pygame.transform.scale(Boss_3_ap_5_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_3_ap_4_alpha = pygame.image.load("Imagenes/Bosses/Boss_3_ap_4.png")
	Boss_3_ap_4 = pygame.transform.scale(Boss_3_ap_4_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_3_ap_3_alpha = pygame.image.load("Imagenes/Bosses/Boss_3_ap_3.png")
	Boss_3_ap_3 = pygame.transform.scale(Boss_3_ap_3_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_3_ap_2_alpha = pygame.image.load("Imagenes/Bosses/Boss_3_ap_2.png")
	Boss_3_ap_2 = pygame.transform.scale(Boss_3_ap_2_alpha, (tamañobossx, tamañobossy)) #64 X 42
	Boss_3_ap_1_alpha = pygame.image.load("Imagenes/Bosses/Boss_3_ap_1.png")
	Boss_3_ap_1 = pygame.transform.scale(Boss_3_ap_1_alpha, (tamañobossx, tamañobossy)) #64 X 42

	Borrador_ap_bosses_alpha = pygame.image.load("Imagenes/Bosses/Borrador_ap_bosses.png")
	Borrador_ap_bosses = pygame.transform.scale(Borrador_ap_bosses_alpha, (tamañobossx, tamañobossy)) #64 X 42

	# ========== DISPAROS DE BOSSES ==========

	Disparo_Boss_1_alpha = pygame.image.load("Imagenes/disparos_boss/Disparo_boss_1.png")
	Disparo_Boss_1 = pygame.transform.scale(Disparo_Boss_1_alpha, (8, 8)) #8 X 8
	Disparo_Boss_1_negro_alpha = pygame.image.load("Imagenes/disparos_boss/Disparo_boss_1_negro.png")
	Disparo_Boss_1_negro = pygame.transform.scale(Disparo_Boss_1_negro_alpha, (8, 8)) #8 X 8

	Disparo_Boss_2_alpha = pygame.image.load("Imagenes/disparos_boss/Disparo_boss_2.png")
	Disparo_Boss_2 = pygame.transform.scale(Disparo_Boss_2_alpha, (16, 19)) #16 X 19
	Disparo_Boss_2_negro_alpha = pygame.image.load("Imagenes/disparos_boss/Disparo_boss_2_negro.png")
	Disparo_Boss_2_negro = pygame.transform.scale(Disparo_Boss_2_negro_alpha, (16, 19)) #16 X 19

	Disparo_Boss_3_alpha = pygame.image.load("Imagenes/disparos_boss/Disparo_boss_3.png")
	Disparo_Boss_3 = pygame.transform.scale(Disparo_Boss_3_alpha, (8, 8)) #8 X 8
	Disparo_Boss_3_negro_alpha = pygame.image.load("Imagenes/disparos_boss/Disparo_boss_3_negro.png")
	Disparo_Boss_3_negro = pygame.transform.scale(Disparo_Boss_3_negro_alpha, (8, 8)) #8 X 8

	# ========== MEJORAS ==========

	Upgrade_2_Disparos_alpha = pygame.image.load("Imagenes/upgrades/Upgrade_2_disparos.png")
	Upgrade_2_Disparos = pygame.transform.scale(Upgrade_2_Disparos_alpha, (45, 21)) #29 X 14
	Upgrade_3_Disparos_alpha = pygame.image.load("Imagenes/upgrades/Upgrade_3_disparos.png")
	Upgrade_3_Disparos = pygame.transform.scale(Upgrade_3_Disparos_alpha, (45, 21)) #29 X 14
	Upgrade_4_Disparos_alpha = pygame.image.load("Imagenes/upgrades/Upgrade_4_disparos.png")
	Upgrade_4_Disparos = pygame.transform.scale(Upgrade_4_Disparos_alpha, (45, 21)) #29 X 14
	Upgrade_5_Disparos_alpha = pygame.image.load("Imagenes/upgrades/Upgrade_5_disparos.png")
	Upgrade_5_Disparos = pygame.transform.scale(Upgrade_5_Disparos_alpha, (45, 21)) #29 X 14
	Upgrade_x2_velocidad_alpha = pygame.image.load("Imagenes/upgrades/Upgrade_x2_velocidad.png")
	Upgrade_x2_velocidad = pygame.transform.scale(Upgrade_x2_velocidad_alpha, (45, 21)) #29 X 14
	Upgrade_x3_velocidad_alpha = pygame.image.load("Imagenes/upgrades/Upgrade_x3_velocidad.png")
	Upgrade_x3_velocidad = pygame.transform.scale(Upgrade_x3_velocidad_alpha, (45, 21)) #29 X 14
	Upgrade_x4_velocidad_alpha = pygame.image.load("Imagenes/upgrades/Upgrade_x4_velocidad.png")
	Upgrade_x4_velocidad = pygame.transform.scale(Upgrade_x4_velocidad_alpha, (45, 21)) #29 X 14
	Upgrade_Escudo_alpha = pygame.image.load("Imagenes/upgrades/Upgrade_escudo.png")
	Upgrade_Escudo = pygame.transform.scale(Upgrade_Escudo_alpha, (45, 21)) #29 X 14
	Upgrade_Iman_alpha = pygame.image.load("Imagenes/upgrades/Upgrade_iman.png")
	Upgrade_Iman = pygame.transform.scale(Upgrade_Iman_alpha, (45, 21)) #29 X 14
	Upgrade_Masvida_alpha = pygame.image.load("Imagenes/upgrades/Upgrade_masvida.png")
	Upgrade_Masvida = pygame.transform.scale(Upgrade_Masvida_alpha, (45, 21)) #29 X 14
	Upgrade_Negra_alpha = pygame.image.load("Imagenes/upgrades/Upgrade_negra.png")
	Upgrade_Negra = pygame.transform.scale(Upgrade_Negra_alpha, (45, 21)) #29 X 14

	dire = "Imagenes/Barra/Barra15.png" #Copiar desde aquí
	barra_alpha = pygame.image.load(dire)
	barra = pygame.transform.scale(barra_alpha, (round(0.2265625 * ancho), round(0.20833333333333333333333333333333 * alto)))
	ventana.fill(negro)
	ventana.blit(barra, (round(0.38671875 * ancho), round(0.39583333333333333333333333333333 * alto)))
	ventana.blit(txt_1, (posxytxt_1[0], posxytxt_1[1]))
	pygame.display.update() #Hasta aqui

	Bosses = [[Boss_1, Boss_1_Escudo], [Boss_2, Boss_2_Escudo], [Boss_3, Boss_3_Escudo]]

	BosesNegros = [[Boss_1_Negro, Boss_1_Escudo_Negro], [Boss_2_Negro, Boss_2_Escudo_Negro], [Boss_3_Negro, Boss_3_Escudo_Negro]]

	AparicionBoss1 = [Boss_1_ap_1, Boss_1_ap_2, Boss_1_ap_3, Boss_1_ap_4, Boss_1_ap_5, Boss_1_ap_6, Boss_1_ap_7, Boss_1_ap_8, Boss_1_ap_9, Boss_1_ap_10]

	AparicionesBoss2 = [Boss_2_ap_1, Boss_2_ap_2, Boss_2_ap_3, Boss_2_ap_4, Boss_2_ap_5, Boss_2_ap_6, Boss_2_ap_7, Boss_2_ap_8, Boss_2_ap_9, Boss_2_ap_10]

	AparicionesBoss3 = [Boss_3_ap_1, Boss_3_ap_2, Boss_3_ap_3, Boss_3_ap_4, Boss_3_ap_5, Boss_3_ap_6, Boss_3_ap_7, Boss_3_ap_8, Boss_3_ap_9, Boss_3_ap_10]

	AparicionesBosses = [AparicionBoss1, AparicionesBoss2, AparicionesBoss3]

	Barras_Vida_Bosses = [Barra_Vida_Boss_100, Barra_Vida_Boss_99, Barra_Vida_Boss_98, Barra_Vida_Boss_97, Barra_Vida_Boss_96, Barra_Vida_Boss_95, Barra_Vida_Boss_94, Barra_Vida_Boss_93, Barra_Vida_Boss_92, Barra_Vida_Boss_91, Barra_Vida_Boss_90, Barra_Vida_Boss_89, Barra_Vida_Boss_88, Barra_Vida_Boss_87, Barra_Vida_Boss_86, Barra_Vida_Boss_85, Barra_Vida_Boss_84, Barra_Vida_Boss_83, Barra_Vida_Boss_82, Barra_Vida_Boss_81, Barra_Vida_Boss_80, Barra_Vida_Boss_79, Barra_Vida_Boss_78, Barra_Vida_Boss_77, Barra_Vida_Boss_76, Barra_Vida_Boss_75, Barra_Vida_Boss_74, Barra_Vida_Boss_73, Barra_Vida_Boss_72, Barra_Vida_Boss_71, Barra_Vida_Boss_70, Barra_Vida_Boss_69, Barra_Vida_Boss_68, Barra_Vida_Boss_67, Barra_Vida_Boss_66, Barra_Vida_Boss_65, Barra_Vida_Boss_64, Barra_Vida_Boss_63, Barra_Vida_Boss_62, Barra_Vida_Boss_61, Barra_Vida_Boss_60, Barra_Vida_Boss_59, Barra_Vida_Boss_58, Barra_Vida_Boss_57, Barra_Vida_Boss_56, Barra_Vida_Boss_55, Barra_Vida_Boss_54, Barra_Vida_Boss_53, Barra_Vida_Boss_52, Barra_Vida_Boss_51, Barra_Vida_Boss_50, Barra_Vida_Boss_49, Barra_Vida_Boss_48, Barra_Vida_Boss_47, Barra_Vida_Boss_46, Barra_Vida_Boss_45, Barra_Vida_Boss_44, Barra_Vida_Boss_43, Barra_Vida_Boss_42, Barra_Vida_Boss_41, Barra_Vida_Boss_40, Barra_Vida_Boss_39, Barra_Vida_Boss_38, Barra_Vida_Boss_37, Barra_Vida_Boss_36, Barra_Vida_Boss_35, Barra_Vida_Boss_34, Barra_Vida_Boss_33, Barra_Vida_Boss_32, Barra_Vida_Boss_31, Barra_Vida_Boss_30, Barra_Vida_Boss_29, Barra_Vida_Boss_28, Barra_Vida_Boss_27, Barra_Vida_Boss_26, Barra_Vida_Boss_25, Barra_Vida_Boss_24, Barra_Vida_Boss_23, Barra_Vida_Boss_22, Barra_Vida_Boss_21, Barra_Vida_Boss_20, Barra_Vida_Boss_19, Barra_Vida_Boss_18, Barra_Vida_Boss_17, Barra_Vida_Boss_16, Barra_Vida_Boss_15, Barra_Vida_Boss_14, Barra_Vida_Boss_13, Barra_Vida_Boss_12, Barra_Vida_Boss_11, Barra_Vida_Boss_10, Barra_Vida_Boss_9, Barra_Vida_Boss_8, Barra_Vida_Boss_7, Barra_Vida_Boss_6, Barra_Vida_Boss_5, Barra_Vida_Boss_4, Barra_Vida_Boss_3, Barra_Vida_Boss_2, Barra_Vida_Boss_1, Barra_Vida_Boss_0]

	Disparos_Boses = [Disparo_Boss_1, Disparo_Boss_2, Disparo_Boss_3]

	Disparos_Bosses_negros = [Disparo_Boss_1_negro, Disparo_Boss_2_negro, Disparo_Boss_3_negro]

	Upgrades = [[Upgrade_2_Disparos, 1, 7], [Upgrade_3_Disparos, 2, 7], [Upgrade_4_Disparos, 3, 7], [Upgrade_5_Disparos, 4, 7], [Upgrade_x2_velocidad, 5, 5], [Upgrade_x3_velocidad, 6, 5], [Upgrade_x4_velocidad, 7, 5], [Upgrade_Escudo, 57, 0], [Upgrade_Iman, 58, 10], [Upgrade_Masvida, 100, 0]] #[[Upgrade_Image, porcentaje_aparicion sobre 100, tiempo activos], 0]

	listbase2 = ["0000", "0001", "0002", "0010", "0011", "0012", "0020", "0021", "0022", "0100", "0101", "0102", "0110", "0111", "0112", "0120", "0121", "0122", "0200", "0201", "0202", "0210", "0211", "0212", "0220", "0221", "0222", "1000", "1001", "1002", "1010", "1011", "1012", "1020", "1021", "1022", "1100", "1101", "1102", "1110", "1111", "1112", "1120", "1121", "1122", "1200", "1201", "1202", "1210", "1211", "1212", "1220", "1221", "1222", "2000", "2001", "2002", "2010", "2011", "2012", "2020", "2021", "2022", "2100", "2101", "2102", "2110", "2111", "2112", "2120", "2121", "2122", "2200", "2201", "2202", "2210", "2211", "2212", "2220", "2221", "2222"]

	Ordinal = ["Primera", "Segunda", "Tercera", "Cuarta", "Quinta", "Sexta", "Séptima", "Octava", "Novena", "Décima"]

	listDet = [Deteccion_De_Daños1, Deteccion_De_Daños2, Deteccion_De_Daños3, Deteccion_De_Daños4, Deteccion_De_Daños5, Deteccion_De_Daños6, Deteccion_De_Daños7, Deteccion_De_Daños8, Deteccion_De_Daños9, Deteccion_De_Daños10, Deteccion_De_Daños11, Deteccion_De_Daños12, Deteccion_De_Daños13, Deteccion_De_Daños14, Deteccion_De_Daños15, Deteccion_De_Daños16, Deteccion_De_Daños17, Deteccion_De_Daños18, Deteccion_De_Daños19, Deteccion_De_Daños20, Deteccion_De_Daños21, Deteccion_De_Daños22, Deteccion_De_Daños23, Deteccion_De_Daños24, Deteccion_De_Daños25, Deteccion_De_Daños26, Deteccion_De_Daños27, Deteccion_De_Daños28, Deteccion_De_Daños29, Deteccion_De_Daños30, Deteccion_De_Daños31, Deteccion_De_Daños32, Deteccion_De_Daños33, Deteccion_De_Daños34, Deteccion_De_Daños35, Deteccion_De_Daños36, Deteccion_De_Daños37, Deteccion_De_Daños38, Deteccion_De_Daños39, Deteccion_De_Daños40, Deteccion_De_Daños41, Deteccion_De_Daños42, Deteccion_De_Daños43, Deteccion_De_Daños44, Deteccion_De_Daños45, Deteccion_De_Daños46, Deteccion_De_Daños47, Deteccion_De_Daños48, Deteccion_De_Daños49, Deteccion_De_Daños50, Deteccion_De_Daños51, Deteccion_De_Daños52, Deteccion_De_Daños53, Deteccion_De_Daños54, Deteccion_De_Daños55, Deteccion_De_Daños56, Deteccion_De_Daños57, Deteccion_De_Daños58, Deteccion_De_Daños59, Deteccion_De_Daños60, Deteccion_De_Daños61, Deteccion_De_Daños62, Deteccion_De_Daños63, Deteccion_De_Daños64, Deteccion_De_Daños65, Deteccion_De_Daños66, Deteccion_De_Daños67, Deteccion_De_Daños68, Deteccion_De_Daños69, Deteccion_De_Daños70, Deteccion_De_Daños71, Deteccion_De_Daños72, Deteccion_De_Daños73, Deteccion_De_Daños74, Deteccion_De_Daños75, Deteccion_De_Daños76, Deteccion_De_Daños77, Deteccion_De_Daños78, Deteccion_De_Daños79, Deteccion_De_Daños80, Deteccion_De_Daños81]

	dire = "Imagenes/Barra/Barra16.png" #Copiar desde aquí
	barra_alpha = pygame.image.load(dire)
	barra = pygame.transform.scale(barra_alpha, (round(0.2265625 * ancho), round(0.20833333333333333333333333333333 * alto)))
	ventana.fill(negro)
	ventana.blit(barra, (round(0.38671875 * ancho), round(0.39583333333333333333333333333333 * alto)))
	ventana.blit(txt_1, (posxytxt_1[0], posxytxt_1[1]))
	pygame.display.update() #Hasta aqui

	### ========== ESTADO DE LA NAVE AMIGA ========== ###

	alaDerecha = True
	vida_alaDerecha = (datos_nave_prin[0])[0]
	vida_alaDerecha_org = vida_alaDerecha
	porcent_vida_alaDerecha = (vida_alaDerecha/vida_alaDerecha_org)* 100

	alaIzquierda = True
	vida_alaIzquierda = (datos_nave_prin[0])[0]
	vida_alaIzquierda_org = vida_alaIzquierda
	porcent_vida_alaIzquierda = (vida_alaIzquierda/vida_alaIzquierda_org)* 100

	motor = True
	vida_motor = (datos_nave_prin[0])[0]
	vida_motor_org = vida_motor
	porcent_vida_motor = (vida_motor/vida_motor_org)* 100

	frontal = True
	vida_frontal = (datos_nave_prin[0])[0]
	vida_frontal_org = vida_frontal
	porcent_vida_frontal = (vida_frontal/vida_frontal_org)* 100

	tipos_de_vidas = [frontal, motor, alaDerecha, alaIzquierda]

	caracteristicas = [vida_alaDerecha, vida_alaDerecha_org, vida_alaIzquierda, vida_alaIzquierda_org, vida_motor, vida_motor_org, vida_frontal, vida_frontal_org, alaDerecha, alaIzquierda, motor, frontal]

	### ========== ESTADO DEL BOSS ========== ###

	try:

		Vidas_Boss = [100, 50, 30]

		vida_boss_act = Vidas_Boss[int(Lv_act/5) - 1]

		barra_vida_sum = 100/vida_boss_act #Cantidad de daño que tiene que recibir el boss para que baje una raya su vida

	except:
		pass

	#print(user_act)

	def generar_fondo(ventana):

		pygame.draw.line(ventana, colorline, (posxline1, 0), (posxline1, alto), tamañoline)
		pygame.draw.line(ventana, colorline, (posxline2, 0), (posxline2, alto), tamañoline)
		pygame.draw.line(ventana, colorline, (0, posy2rec1), (posxline1, posy2rec1), tamañoline)
		pygame.draw.line(ventana, colorline, (posxline2, posy2rec1), (ancho, posy2rec1), tamañoline)

	def actualizar_pantalla_derecha_arriba(ventana, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, Mostrar, infinito, segundostranscurridos, mejoras_activadas):

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

		mejoras_preparadas = []

		for mejora_activada in mejoras_activadas: #[tipo, tiempo, texto_a_mostrar, Color]

			texto_mejora = mejora_activada[2] + str(mejora_activada[1])

			posx_mejora = 0

			posy_mejora = posytxt_derecha_ariba * (mejoras_activadas.index(mejora_activada) + 8)

			txt_mejora, posxymejora = print_pantalla(texto_mejora, posx_mejora, posy_mejora, tamañotxt1, mejora_activada[3], fuente)

			mejora_to_export = [txt_mejora, posx_mejora, posy_mejora]

			mejoras_preparadas.append(mejora_to_export)

		return((txt1_AD, posxytxt1_AD), (txt2_AD, posxytxt2_AD), (txt3_AD, posxytxt3_AD), (txt4_AD, posxytxt4_AD), (txt5_AD, posxytxt5_AD), (txt6_AD, posxytxt6_AD), (txt7_AD, posxytxt7_AD), mejoras_preparadas)

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
			Nave_Tipo4 = pygame.transform.scale(Nave_Tipo4_alpha, (round(0.028125 * ancho), round(0.04166666666666666666666666666667 * alto))) # 18 X 15 to 36 X 30

		else:

			txt4_DD, posxytxt4_DD = print_pantalla("Nave: ¿?" , 0, posytxt_derecha_debajo * 3 + posy2rec1, tamañotxt1, colortxt, fuente)
			Nave_Tipo4 = ""

		if cant_unos > 4: #Nave Tipo 5

			txt5_DD, posxytxt5_DD = print_pantalla("Nave Defensora nº2: " , 0, posytxt_derecha_debajo * 4 + posy2rec1, tamañotxt1, colortxt, fuente)
			Nave_Tipo5_alpha = pygame.image.load("Imagenes/Naves_Enemigas/EBEN5.png")
			Nave_Tipo5 = pygame.transform.scale(Nave_Tipo5_alpha, (round(0.028125 * ancho), round(0.04166666666666666666666666666667 * alto))) # 18 X 15

		else:

			txt5_DD, posxytxt5_DD = print_pantalla("Nave: ¿?" , 0, posytxt_derecha_debajo * 4 + posy2rec1, tamañotxt1, colortxt, fuente)
			Nave_Tipo5 = ""

		if cant_unos > 5: #Nave Tipo 6

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

		txt2_AI, posxytxt2_AI = print_pantalla("Ala Izquierda: " + str(vida_alaIzquierda), posxline2 + 10, 200, tamañotxt1, colortxt, fuente)
		txt3_AI, posxytxt3_AI = print_pantalla("Ala Derecha: " + str(vida_alaDerecha), posxline2 + 10, 230, tamañotxt1, colortxt, fuente)
		txt4_AI, posxytxt4_AI = print_pantalla("Frontal: " + str(vida_frontal), posxline2 + 10, 260, tamañotxt1, colortxt, fuente)
		txt5_AI, posxytxt5_AI = print_pantalla("Motor: " + str(vida_motor), posxline2 + 10, 290, tamañotxt1, colortxt, fuente)
		txt6_AI, posxytxt6_AI = print_pantalla("Escudo activo: " + str(escudo), posxline2 + 10, 320, tamañotxt1, colortxt, fuente)

		return((txt1_AI, posxytxt1_AI), imag, vida_alaDerecha, vida_alaIzquierda, vida_motor, vida_frontal, viva, alaDerecha, alaIzquierda, motor, frontal, (txt2_AI, posxytxt2_AI), (txt3_AI, posxytxt3_AI), (txt4_AI, posxytxt4_AI), (txt5_AI, posxytxt5_AI), (txt6_AI, posxytxt6_AI))

	def actualizar_pantalla_izquierda_debajo(ventana, mensajelinesrecibidos = None, mensajelinesenviados = None): # Lines max = 8 De momento

		pygame.draw.rect(ventana, negro, (posxline2 + tamañoline, posy2rec1 + tamañoline, ancho, alto))
		
		txt1_DI, posxytxt1_DI = print_pantalla("Chat:", posxline2 + tamañoline, posy2rec1 + tamañoline, tamañotxt1, colortxt, fuente)
		txt2_DI, posxytxt2_DI = print_pantalla("Mensajes recibidos:", posxline2 + tamañoline, posy2rec1 + tamañoline + possumando_izquierda_abajo, tamañotxt1, rojo, fuente)
		txt3_DI, posxytxt3_DI = print_pantalla("Mensajes enviados:", posxline2 + tamañoline, posy2rec1 + tamañoline + round(possumando_izquierda_abajo * 5), tamañotxt1, verde, fuente)

		if mensajelinesrecibidos != None:

			try: # Txt 1
				txt4_DI, posxytxt4_DI = print_pantalla(str(mensajelinesrecibidos[0]), posxline2 + tamañoline, posy2rec1 + tamañoline + possumando_izquierda_abajo * 2, round(tamañotxt1/2), blanco, fuente)

			except:
				txt4_DI = ["", ""]
				posxytxt4_DI = ""

			try: # Txt 2
				txt5_DI, posxytxt5_DI = print_pantalla(str(mensajelinesrecibidos[1]), posxline2 + tamañoline, posy2rec1 + tamañoline + round(possumando_izquierda_abajo * 2.5), round(tamañotxt1/2), blanco, fuente)

			except:
				txt5_DI = ["", ""]
				posxytxt5_DI = ""

			try: # Txt 3
				txt6_DI, posxytxt6_DI = print_pantalla(str(mensajelinesrecibidos[2]), posxline2 + tamañoline, posy2rec1 + tamañoline + possumando_izquierda_abajo * 3, round(tamañotxt1/2), blanco, fuente)

			except:
				txt6_DI = ["", ""]
				posxytxt6_DI = ""

			try: # Txt 4
				txt7_DI, posxytxt7_DI = print_pantalla(str(mensajelinesrecibidos[3]), posxline2 + tamañoline, posy2rec1 + tamañoline + round(possumando_izquierda_abajo * 3.5), round(tamañotxt1/2), blanco, fuente)

			except:
				txt7_DI = ["", ""]
				posxytxt7_DI = ""

			try: # Txt 5
				txt8_DI, posxytxt8_DI = print_pantalla(str(mensajelinesrecibidos[4]), posxline2 + tamañoline, posy2rec1 + tamañoline + possumando_izquierda_abajo * 4, round(tamañotxt1/2), blanco, fuente)

			except:
				txt8_DI = ["", ""]
				posxytxt8_DI = ""

			try: # Txt 6
				txt9_DI, posxytxt9_DI = print_pantalla(str(mensajelinesrecibidos[5]), posxline2 + tamañoline, posy2rec1 + tamañoline + possumando_izquierda_abajo * 4.5, round(tamañotxt1/2), blanco, fuente)

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

	def crear_texto_en_pantalla(ventana, texto, tiempo_en_pantalla, FPS):
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

		while int(strpos) + 1 > int(nwstrpos):
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

		#print(escudo, "Escudo")
					
		if escudo == True:
			viva = True
			escudo = False
			ventana.blit(Escudo_Negro, (round(xn) - 2, round(yn) - 2))

		else:
			viva = True

		return [viva, escudo]

	def comprovartocandoboss(disparo, posbossx, posbossy, multiplier_boss):

		boss_tocado = False

		if valor == 1:

			if posbossx < disparo[0] and posbossx + 1 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 9 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 1 * multiplier_boss < disparo[0] and posbossx + 2 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 14 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 2 * multiplier_boss < disparo[0] and posbossx + 4 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 17 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 4 * multiplier_boss < disparo[0] and posbossx + 5 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 19 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 5 * multiplier_boss < disparo[0] and posbossx + 8 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 26 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 8 * multiplier_boss < disparo[0] and posbossx + 9 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 30 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 9 * multiplier_boss < disparo[0] and posbossx + 14 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 28 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 14 * multiplier_boss < disparo[0] and posbossx + 17 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 30 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 17 * multiplier_boss < disparo[0] and posbossx + 20 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 38 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 20 * multiplier_boss < disparo[0] and posbossx + 21 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 42 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 21 * multiplier_boss < disparo[0] and posbossx + 23 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 38 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 23 * multiplier_boss < disparo[0] and posbossx + 26 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 34 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 26 * multiplier_boss < disparo[0] and posbossx + 28 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 37 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 28 * multiplier_boss < disparo[0] and posbossx + 31 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 34 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 31 * multiplier_boss < disparo[0] and posbossx + 33 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 36 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 33 * multiplier_boss < disparo[0] and posbossx + 36 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 34 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 36 * multiplier_boss < disparo[0] and posbossx + 38 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 36 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 38 * multiplier_boss < disparo[0] and posbossx + 41 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 34 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 41 * multiplier_boss < disparo[0] and posbossx + 43 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 38 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 43 * multiplier_boss < disparo[0] and posbossx + 44 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 42 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 44 * multiplier_boss < disparo[0] and posbossx + 47 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 38 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 47 * multiplier_boss < disparo[0] and posbossx + 50 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 30 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 50 * multiplier_boss < disparo[0] and posbossx + 55 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 28 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 55 * multiplier_boss < disparo[0] and posbossx + 56 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 30 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 56 * multiplier_boss < disparo[0] and posbossx + 59 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 26 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 59 * multiplier_boss < disparo[0] and posbossx + 60 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 19 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 60 * multiplier_boss < disparo[0] and posbossx + 62 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 17 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 62 * multiplier_boss < disparo[0] and posbossx + 63 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 14 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 63 * multiplier_boss < disparo[0] and posbossx + 64 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 9 * multiplier_boss:
				boss_tocado = True

		elif valor == 2:

			if posbossx < disparo[0] and posbossx + 1 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 21 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 1 * multiplier_boss < disparo[0] and posbossx + 2 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 25 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 2 * multiplier_boss < disparo[0] and posbossx + 5 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 29 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 5 * multiplier_boss < disparo[0] and posbossx + 9 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 32 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 9 * multiplier_boss < disparo[0] and posbossx + 21 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 34 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 21 * multiplier_boss < disparo[0] and posbossx + 23 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 37 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 23 * multiplier_boss < disparo[0] and posbossx + 26 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 40 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 26 * multiplier_boss < disparo[0] and posbossx + 38 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 42 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 38 * multiplier_boss < disparo[0] and posbossx + 41 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 40 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 41 * multiplier_boss < disparo[0] and posbossx + 43 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 37 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 43 * multiplier_boss < disparo[0] and posbossx + 55 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 34 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 55 * multiplier_boss < disparo[0] and posbossx + 59 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 32 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 59 * multiplier_boss < disparo[0] and posbossx + 62 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 29 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 62 * multiplier_boss < disparo[0] and posbossx + 63 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 25 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 63  * multiplier_boss < disparo[0] and posbossx + 64 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 21 * multiplier_boss:
				boss_tocado = True

		elif valor == 3:

			if posbossx < disparo[0] and posbossx + 1 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 25 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 1  * multiplier_boss < disparo[0] and posbossx + 2 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 31 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 2  * multiplier_boss < disparo[0] and posbossx + 3 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 36 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 3  * multiplier_boss < disparo[0] and posbossx + 4 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 40 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 4  * multiplier_boss < disparo[0] and posbossx + 18 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 42 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 18  * multiplier_boss < disparo[0] and posbossx + 19 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 40 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 19  * multiplier_boss < disparo[0] and posbossx + 20 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 36 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 20  * multiplier_boss < disparo[0] and posbossx + 21 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 32 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 21  * multiplier_boss < disparo[0] and posbossx + 22 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 29 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 22  * multiplier_boss < disparo[0] and posbossx + 24 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 27 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 24  * multiplier_boss < disparo[0] and posbossx + 26 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 25 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 26  * multiplier_boss < disparo[0] and posbossx + 38 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 24 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 38  * multiplier_boss < disparo[0] and posbossx + 40 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 25 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 40  * multiplier_boss < disparo[0] and posbossx + 42 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 27 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 42  * multiplier_boss < disparo[0] and posbossx + 43 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 29 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 43  * multiplier_boss < disparo[0] and posbossx + 44 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 32 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 44  * multiplier_boss < disparo[0] and posbossx + 45 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 36 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 45  * multiplier_boss < disparo[0] and posbossx + 46 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 40 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 46  * multiplier_boss < disparo[0] and posbossx + 60 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 42 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 60  * multiplier_boss < disparo[0] and posbossx + 61 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 40 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 61  * multiplier_boss < disparo[0] and posbossx + 62 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 36 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 62  * multiplier_boss < disparo[0] and posbossx + 63 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 31 * multiplier_boss:
				boss_tocado = True

			elif posbossx + 63  * multiplier_boss < disparo[0] and posbossx + 64 * multiplier_boss > disparo[0] + 2 and disparo[1] < posbossy + 25 * multiplier_boss:
				boss_tocado = True

		return boss_tocado

	def comprovardistancia(x1, y1, x2, y2):
		if x1 > x2:
			x = x1 - x2

		else:
			x = x2 - x1

		if y1 > y2:
			y = y1 - y2

		else:
			y = y2 - y1
		return math.sqrt((x**2) + (y**2))

	def calcular_fraccion_avance(xinic, yinic, xtogo, ytogo):

		fraccion = 0

		diferenciax = 0
		diferenciay = 0

		if xinic > xtogo:
			diferenciax = xinic - xtogo
			ladox = "dch"

		elif xtogo > xinic:
			diferenciax = xtogo - xinic
			ladox = "izq"

		else:
			fraccion = "x"
			motor = "y"
			ladox = None

		if yinic > ytogo:
			diferenciay = yinic - ytogo
			ladoy = "abj"

		elif ytogo > yinic:
			diferenciay = ytogo - yinic
			ladoy = "arr"

		else:
			fraccion = "y"
			motor = "x"
			ladoy = None

		if fraccion == 0 and diferenciay > diferenciax:
			fraccion = diferenciax/diferenciay
			motor = "y"

		elif fraccion == 0 and diferenciax > diferenciay:
			fraccion = diferenciay/diferenciax
			motor = "x"

		else:
			fraccion = 0

		return fraccion, motor, ladox, ladoy

	#print(calcular_fraccion_avance(0, 0, 5, 99, "y"))

	second = datetime.now().second
	microsecond = datetime.now().microsecond

	x = 0
	y = 0

	radio = 30

	### ========== GENERALES ========== ###

	Exit_presionado = False # Salir del juego
	salida = False # Comprueva si quieres salir del juego
	reintentar = False # Comprueva si quieres reintentar el nivel

	oleada = 1
	Naves_destruidas = 0
	Monedas = 0
	porcentaje = 0

	vueltas = 0 # Algo de limitaciones con la ejecucion de los items(monedas, upgrades...)

	### ========== CONTROL DE EVENTOS ========== ###

	accion = False

	teclaizquierdapress = False
	tecladerechapress = False
	teclaabajopress = False
	teclaarribapress = False
	disparoAmigo = False

	### ========== CONTROL DE BUGS ========== ###

	recien_salido = False # Hace que las naves no se muevan hasta la segunda vuelta de bucle, para evitar bugs de FPS

	margenerror = 2 # Es la diferencia de px entre el limite del terreno de juego y la zona de juego

	primeravuelta = True # Para saber si la primera vuelta ha pasado y evitar el bug de los 0 fps

	### ========== CONTROL DE TIEMPO ========== ###

	data_time_microsecond = str(datetime.now().microsecond)
	data_time_second = str(datetime.now().second)
	data_time_minute = datetime.now().minute

	if len(data_time_second) != 2:
		data_time_second = "0" + data_time_second

	for i in range(6 - len(data_time_microsecond)):
		data_time_microsecond = "0" + data_time_microsecond

	data_time = int(str(data_time_minute) + data_time_second + data_time_microsecond)

	### ========== FONDO ========== ###

	velocidad_fondo = 0.1

	### ========== CONTROL DE LISTAS ========== ###

	aborrar = []

	aborrarlos = []

	### ========== PROYECTILES ENEMIGOS ========== ###

	listdisparos_NE = [] #[[x, y, imagen, v, t], [x2, y2, imagen2, v2, t2]]...

	dañoProyectiles = [5, 10, 15, 10, 15, 40]

	ancho_proyectiles = [2, 2, 2, 2, 2, 12]

	alto_proyectiles = [8, 8, 8, 8, 8, 12]

	### ========== PROYECTILES AMIGOS ========== ###

	listdisparos_NA = [] #[[x, y, imagen, v], [x2, y2, imagen2, v2]]...

	nºdisparos = 1

	segundostranscurridos = 0

	velocidad_de_disparo_amigo = (datos_nave_prin[0])[5]

	tiempo_de_diferencia_entre_disparos = (datos_nave_prin[0])[4] #En microsegundos con base 6

	tiempo_de_diferencia_entre_disparos_org = tiempo_de_diferencia_entre_disparos

	tiempo_disparo_amigo_ant = 0

	tipodeproyectilamigo = 0 #0 = Blanco, 1 = Rojo, 2 = Azul, 3 = Amarillo

	### ========== PROYECTILES BOSS ========== ###

	disparos_boss = []

	### ========== MOVIMIENTO DE NAVES ENEMIGAS ========== ###

	hacer = 0

	eliminarposicionesocupadas = False # "Suelta" las naves que estan que estan esperando arriba

	ciclo = 0

	### ========== ESTRELLAS ========== ###

	estrellas = []

	estrellasmoviendose = ajustes[8]

	estrellasparpadeando = True

	estrellasenpantalla = True

	velocidadparpadeo = 40 #Cantidad de frames que tiene que esperar para poder elegir encendida y apagada

	velocidades = [0.2, 0.1, 0.05]

	### ========== VSync ========== ###

	VSyncactivado = ajustes[10]

	### ========== FPS ========== ###

	ant_FPS = 0
	fpslist = []

	FPS = 0
	fpsactivos = False
	cambioFps = False

	MaxFPS = int(ajustes[9])
	sumer = MaxFPS

	### ========== CARACTERISTICAS NAVES ENEMIGAS =========== ###

	movimientos = [1, 3, 1, 2] #1 = abajo antura de nave, 2 = derecha, 3 = izquierda

	### ========== CARACTERISTICAS DE LA NAVE AMIGA ========== ###

	viva = True

	if (datos_nave_prin[0])[3] == 0:
		escudo = False

	else:
		escudo = True

	dañocac = 10
	tamañox = 42
	tamañoy = 26
	nave_prin_explotando = False
	Velocidad_Nave = (datos_nave_prin[0])[2]
	Velocidad_Nave_Org = Velocidad_Nave
	xn = ancho/2 - 21
	yn = alto/4 * 3
	disparado = False # Para saber si se tiene que actualizar o no

	### ========== BOSSES ========== ###

	boss_activo = False

	direccion_boss = 0 #0 = Izquierda 1 = Derecha

	escudo_boss = 1 #1 = Si tiene 0 = No tiene

	naves_destruidas_boss = 0 #Cuando llegues a 5 puedes disparar al boss

	escudo_desactivandose = False

	escudo_desactivado = False

	velocidad_disparo_boss = 1

	daño_disparo_bosses = [10, 5, 15]

	posicionesx_de_cañones_bosses = [[72, 168, 352, 448], 248, [80, 416]] # [9, 21, 44, 56]
	posicionesy_de_cañones_bosses = [[240, 336, 336, 240], 336, [336, 336]] # [30, 42, 42, 30]

	naves_a_matar = [5, 5, 5]

	### ========== UPGRADES ========== ###

	funcion_imantar = False

	mejoras = []

	ancho_mejoras = 45

	alto_mejoras = 21

	mejoras_activadas = []

	Color_Mejora = (0, 255, 0)

	### ========== EFECTOS ========== ###

	Efectos = [10, 5] # [Explosion Nuclear(Lentitud), Explosion Del Boss2(Envenentamiento)]

	Color_Efecto = (255, 0, 0)

	Multiplicador_Velocidad = 0

	### ========== EXPLOSIONES ========== ###

	ExplosionesNuclearesActivas = []

	explosion_nuclear_pos = 0

	ExplosionesDeBoss2Activas = []

	ExplosionesDeBoss3Activas = []

	### ========== EXPLOSIONES DE NAVES ========== ###

	explotada = False

	naves_destruidas_a_explotar = [] # dentro va [[posx, posy, tipo, explosion_actual], [posx, posy, tipo, explosion_actual]]

	### ========== MONEDAS ========== ###

	monedas_en_pantalla = []

	### ========== CREATIVO ========== ###

	inmortal = False

	desactivar_caida_con_parte_imaginaria = False

	disparos_boses_activos = True

	### ========== NOTIFICACIONES ========== ###

	notificacion_frontal = ["Ahora que no tienes frontal, los disparos te dan", "directamente en el motor, ten cuidado."]
	notificacion_ala = ["Sin un ala nos hemos quedado sin un tercio de la", "propulsion, sera mas complicado llevar la nave."]

	dire = "Imagenes/Barra/Barra17.png" #Copiar desde aquí
	barra_alpha = pygame.image.load(dire)
	barra = pygame.transform.scale(barra_alpha, (round(0.2265625 * ancho), round(0.20833333333333333333333333333333 * alto)))
	ventana.fill(negro)
	ventana.blit(barra, (round(0.38671875 * ancho), round(0.39583333333333333333333333333333 * alto)))
	ventana.blit(txt_1, (posxytxt_1[0], posxytxt_1[1]))
	pygame.display.update() #Hasta aqui

	resultados = actualizar_pantalla_derecha_arriba(ventana, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, False, infinito, segundostranscurridos, mejoras_activadas)

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
	txt2_AI, posxytxt2_AI = resultados4[11]
	txt3_AI, posxytxt3_AI = resultados4[12]
	txt4_AI, posxytxt4_AI = resultados4[13]
	txt5_AI, posxytxt5_AI = resultados4[14]
	txt6_AI, posxytxt6_AI = resultados4[15]

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

	if resultados[7] != False:

		for mejora_mostrada in resultados[7]:
			ventana.blit(mejora_mostrada[0], (mejora_mostrada[1], mejora_mostrada[2]))

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
	if txt2_AI != ["", ""]: ventana.blit(txt2_AI, (posxytxt2_AI[0], posxytxt2_AI[1]))
	if txt3_AI != ["", ""]: ventana.blit(txt3_AI, (posxytxt3_AI[0], posxytxt3_AI[1]))
	if txt4_AI != ["", ""]: ventana.blit(txt4_AI, (posxytxt4_AI[0], posxytxt4_AI[1]))
	if txt5_AI != ["", ""]: ventana.blit(txt5_AI, (posxytxt5_AI[0], posxytxt5_AI[1]))
	if txt6_AI != ["", ""]: ventana.blit(txt6_AI, (posxytxt6_AI[0], posxytxt6_AI[1]))
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
	#ventana.blit(Bosses[0], (384, 10))

	ventana.blit(NavePrincipal, (round(xn), round(yn)))

	naves, list_naves, usados = crear_oleada(ventana, Lv_act, infinito, list_naves, usados, oleada, radio)

	if escudo: ventana.blit(Escudo, (posxControlador - 8, posyControlador - 8))

	pygame.display.update()

	#print(usados)

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

	pant_escond = False

	press = False

	cambiar = False

	turno = True

	navecayendo = False

	avanzarhasta = None

	nave_a_ordenar = -1

	tocada = False

	eleabuscar = []

	puntuacion = 0

	#datos_conseguidos = [False, 0]

	dispararya = False

	ultimoseventos = []

	valor = int(Lv_act/5)

	for vida in tipos_de_vidas:

		eleabuscar.append(vida)

	index_Nave_Prin = Data_Prin.index(eleabuscar)
	index_Escudo = Data_Escudos.index(eleabuscar)

	crear_texto_en_pantalla(ventana, "OLEADA Nº1", 0.5, 300)

	while Exit_presionado == False: #Funciona para cerrar

		if inmortal == True:
			escudo = True #Intentandolo

		### ========== ZONA DE PROBABILIDADES ========== ###

		if primeravuelta == False and FPS > 3 and int(random.randrange(1, math.ceil(150*(FPS/400)))) == 1 and estrellasmoviendose == "True" and estrellasenpantalla == True: #Creacion de estrellas
			estrella = [random.randrange(330, 950), 0, colores_seleccion[random.randrange(0, 1)], velocidades[random.randrange(0, 3) - 1], 0, True] # estrella = [posx, poxy, color, velocidad, countdown, modo]
			estrellas.append(estrella)

		if primeravuelta == False and FPS > 3 and int(random.randrange(1, math.ceil(7000*(FPS/400)))) == 1: # Creacion de mejoras
			tipo_n = random.randrange(1, 100)
			encontrado = False

			for mejora in Upgrades:
				if tipo_n < mejora[1] and encontrado == False:
					tipo = Upgrades.index(mejora)
					encontrado = True

			lado_new = random.randrange(0, 2)

			if lado_new == 1:
				posx_new = 330
				posx_ir_new = 950 - ancho_mejoras

			else:
				posx_new = 950 - ancho_mejoras
				posx_ir_new = 330

			new_mejora = [lado_new, (Upgrades[tipo])[0], posx_new, random.randrange(370, 710 - alto_mejoras), posx_ir_new, random.randrange(370, 710 - alto_mejoras), tipo]# [lado de pant, imag, posx, posy, posx_ir, posy_ir, tipo]
			mejoras.append(new_mejora)

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
					salida, reintentar = crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

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

			for mejora in mejoras:# [lado de pant, imag, posx, posy, posx_ir, posy_ir]
				ventana.blit(Upgrade_Negra, (round(mejora[2]), round(mejora[3])))

				diferencia, motor_1, ladox, ladoy = calcular_fraccion_avance(mejora[4], mejora[5], mejora[2], mejora[3])

				if motor_1 == "x":
					xavanzado = (450/FPS)*0.3
					yavanzado = xavanzado * diferencia

				elif motor_1 == "y":
					yavanzado = (450/FPS)*0.3
					xavanzado = yavanzado * diferencia

				x_ant = mejora[2]
				y_ant = mejora[3]

				if ladox == "izq" and ladoy == "arr":
					mejora.pop(2)
					mejora.insert(2, x_ant - xavanzado)
					mejora.pop(3)
					mejora.insert(3, y_ant - yavanzado)

				elif ladox == "izq" and ladoy == "abj":
					mejora.pop(2)
					mejora.insert(2, x_ant - xavanzado)
					mejora.pop(3)
					mejora.insert(3, y_ant + yavanzado)

				elif ladox == "dch" and ladoy == "arr":
					mejora.pop(2)
					mejora.insert(2, x_ant + xavanzado)
					mejora.pop(3)
					mejora.insert(3, y_ant - yavanzado)

				elif ladox == "dch" and ladoy == "abj":
					mejora.pop(2)
					mejora.insert(2, x_ant + xavanzado)
					mejora.pop(3)
					mejora.insert(3, y_ant + yavanzado)

				elif ladox == None and ladoy == "arr":
					mejora.pop(3)
					mejora.insert(3, y_ant - yavanzado)

				elif ladox == None and ladoy == "abj":
					mejora.pop(3)
					mejora.insert(3, y_ant + yavanzado)

				elif ladoy == None and ladox == "izq":
					mejora.pop(2)
					mejora.insert(2, x_ant - xavanzado)

				elif ladoy == None and ladox == "dch":
					mejora.pop(2)
					mejora.insert(2, x_ant + xavanzado)

				if mejora[2] > 950 - ancho_mejoras and mejora[0] == 1:
					aborrar.append(mejoras.index(mejora))
					aborrar.sort()
					aborrar.reverse()

				elif mejora[2] < 330 and mejora[0] == 0:
					aborrar.append(mejoras.index(mejora))
					aborrar.sort()
					aborrar.reverse()

				ventana.blit(mejora[1], (round(mejora[2]), round(mejora[3])))

			for borrado in aborrar:
				ventana.blit(Upgrade_Negra, ((mejoras[borrado])[2], (mejoras[borrado])[3]))
				mejoras.pop(borrado)

			aborrar = []

			if boss_activo == True:
				if escudo_desactivandose == True:
					ventana.blit(BosesNegros[valor - 1][1], (round(posbossx), round(posbossy)))
					escudo_desactivandose = False

				else:
					ventana.blit(BosesNegros[valor - 1][escudo_boss], (round(posbossx), round(posbossy)))

				ventana.blit(Barra_Vida_Boss_Negro, (round(posxbarraboss), round(posybarraboss)))

				if posbossx > 950 - tamañobossx and direccion_boss == 1:
					direccion_boss = 0

				elif posbossx < 330 and direccion_boss == 0:
					direccion_boss = 1

				if direccion_boss == 0:
					posbossx -= Velocidades_boss[valor - 1]
					posxbarraboss -= Velocidades_boss[valor - 1]

				elif direccion_boss == 1:
					posbossx += Velocidades_boss[valor - 1]
					posxbarraboss += Velocidades_boss[valor - 1]

				ventana.blit(Bosses[valor - 1][escudo_boss], (round(posbossx), round(posbossy)))

				try:
					ventana.blit(Barras_Vida_Bosses[math.floor((Vidas_Boss[valor - 1] - vida_boss_act)/barra_vida_sum)], (round(posxbarraboss), round(posybarraboss)))

				except: # Se ha muerto el boss

					ventana.blit(Barras_Vida_Bosses[100], (round(posxbarraboss), round(posybarraboss)))

					for disparo in listdisparos_NA: #Naves amigas
						ventana.blit(DisparoNegro, (disparo[0], disparo[1]))

					for disparo in listdisparos_NE: #Naves enemigas
						ventana.blit(DisparosNegros[disparo[4] - 1], (disparo[0], disparo[1]))

					pygame.display.update()

					AparicionesBossAct = AparicionesBosses[valor - 1]
					AparicionesBossAct.reverse()

					ventana.blit(Barra_Vida_Boss_Negro, (round(posxbarraboss), round(posybarraboss)))

					for i in AparicionesBossAct:
						ventana.blit(BosesNegros[valor - 1][escudo_boss], (round(posbossx), round(posbossy)))
						ventana.blit(i, (round(posbossx), round(posbossy)))
						pygame.display.update()
						time.sleep(0.09)

					ventana.blit(BosesNegros[valor - 1][escudo_boss], (round(posbossx), round(posbossy)))
					pygame.display.update()

					#crear_texto_en_pantalla(ventana, "!GANASTE¡, este texto es temporal", 2, FPS)
					porcentaje_alcanzado_exportar = 100
					porcent_vida_alaIzquierda = vida_alaIzquierda/vida_alaIzquierda_org
					porcent_vida_alaDerecha = vida_alaDerecha/vida_alaDerecha_org
					porcent_vida_motor = vida_motor/vida_motor_org
					porcent_vida_frontal = vida_frontal/vida_frontal_org
					porcentaje_Medio_de_vida_exportar = (round((porcent_vida_alaIzquierda + porcent_vida_alaDerecha + porcent_vida_motor + porcent_vida_frontal)/4, 2))*100

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

					resultado = "¡Has ganado!"

					reintentar = ejecutar_pantalla_resultados(ventana, user_act[1], Lv_act, pantalla_act, puntuacion_total, monedas_totales, Naves_destruidas, segundostranscurridos, Monedas, puntuacion_exportar, resultado, Nº_Naves, estado_escudo, estado_alaizquierda, estado_aladerecha, estado_motor, estado_frontal, estado_final_nave, infinito, porcentaje_Medio_de_vida_exportar, porcentaje_alcanzado_exportar)

					victoria = True
					
					Exit_presionado = True
					###AQUI

			for moneda in monedas_en_pantalla: #[posx, poxy, forma*, en que lado empezó, counter, gotox, gotoy]
				ventana.blit(monedas_Negras_Imag[moneda[2]], (moneda[0], moneda[1]))

				movimiento_normal = True

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

				if funcion_imantar == True and comprovardistancia(moneda[0], moneda[1], xn, yn) < 200: #Comprueva si esta cerca como para ser atraido por el iman

					movimiento_normal = False

					#tiempo_a_tardar = comprovardistancia(moneda[0], moneda[1], xn, yn) * 0.01  #En sec

					diferencia, motor_1, ladox, ladoy = calcular_fraccion_avance(xn, yn, moneda[0], moneda[1])

					#print(diferencia, motor_1, ladox, ladoy)
					#print(motor_1)

					if motor_1 == "x":
						xavanzado = (450/FPS)*0.7
						yavanzado = xavanzado * diferencia

					elif motor_1 == "y":
						yavanzado = (450/FPS)*0.7
						xavanzado = yavanzado * diferencia

					x_ant = moneda[0]
					y_ant = moneda[1]

					if ladox == "izq" and ladoy == "arr":
						moneda.pop(0)
						moneda.insert(0, x_ant - xavanzado)
						moneda.pop(1)
						moneda.insert(1, y_ant - yavanzado)

					elif ladox == "izq" and ladoy == "abj":
						moneda.pop(0)
						moneda.insert(0, x_ant - xavanzado)
						moneda.pop(1)
						moneda.insert(1, y_ant + yavanzado)

					elif ladox == "dch" and ladoy == "arr":
						moneda.pop(0)
						moneda.insert(0, x_ant + xavanzado)
						moneda.pop(1)
						moneda.insert(1, y_ant - yavanzado)

					elif ladox == "dch" and ladoy == "abj":
						moneda.pop(0)
						moneda.insert(0, x_ant + xavanzado)
						moneda.pop(1)
						moneda.insert(1, y_ant + yavanzado)

					elif ladox == None and ladoy == "arr":
						moneda.pop(1)
						moneda.insert(1, y_ant - yavanzado)

					elif ladox == None and ladoy == "abj":
						moneda.pop(1)
						moneda.insert(1, y_ant + yavanzado)

					elif ladoy == None and ladoy == "arr":
						moneda.pop(0)
						moneda.insert(0, x_ant - xavanzado)

					elif ladoy == None and ladoy == "abj":
						moneda.pop(0)
						moneda.insert(0, x_ant - xavanzado)

				#print(moneda[3], moneda[0])

				xavanzado = (450/FPS)*0.4

				if moneda[0] > 940 and moneda[3] == 0 and movimiento_normal == True:
					moneda.pop(3)
					moneda.insert(3, 1)

				elif moneda[0] > 950 - 18 and moneda[3] == 1 and movimiento_normal == True:
					aborrar.append(monedas_en_pantalla.index(moneda))
					aborrar.sort()
					aborrar.reverse()

				elif moneda[0] < 330 and moneda[3] == 0 and movimiento_normal == True:
					aborrar.append(monedas_en_pantalla.index(moneda))
					aborrar.sort()
					aborrar.reverse()

				elif moneda[0] > moneda[5] and moneda[1] > moneda[6] and movimiento_normal == True:
					x_ant = moneda[0]
					y_ant = moneda[1]
					ydiferencia = moneda[1] - moneda[6]
					xdiferencia = moneda[0] - moneda[5]
					yavanzado = ydiferencia/xdiferencia
					moneda.pop(0)
					moneda.insert(0, x_ant - xavanzado)
					moneda.pop(1)
					moneda.insert(1, y_ant - (yavanzado * xavanzado))

				elif moneda[0] > moneda[5] and moneda[1] < moneda[6] and movimiento_normal == True:
					x_ant = moneda[0]
					y_ant = moneda[1]
					ydiferencia = moneda[6] - moneda[1]
					xdiferencia = moneda[0] - moneda[5]
					yavanzado = ydiferencia/xdiferencia
					moneda.pop(0)
					moneda.insert(0, x_ant - xavanzado)
					moneda.pop(1)
					moneda.insert(1, y_ant + (yavanzado * xavanzado))

				elif moneda[0] < moneda[5] and moneda[1] > moneda[6] and movimiento_normal == True:
					x_ant = moneda[0]
					y_ant = moneda[1]
					ydiferencia = moneda[1] - moneda[6]
					xdiferencia = moneda[5] - moneda[0]
					yavanzado = ydiferencia/xdiferencia
					moneda.pop(0)
					moneda.insert(0, x_ant + xavanzado)
					moneda.pop(1)
					moneda.insert(1, y_ant - (yavanzado * xavanzado))

				elif moneda[0] < moneda[5] and moneda[1] < moneda[6] and movimiento_normal == True:
					x_ant = moneda[0]
					y_ant = moneda[1]
					ydiferencia = moneda[6] - moneda[1]
					xdiferencia = moneda[5] - moneda[0]
					yavanzado = ydiferencia/ydiferencia
					moneda.pop(0)
					moneda.insert(0, x_ant + xavanzado)
					moneda.pop(1)
					moneda.insert(1, y_ant + (yavanzado * xavanzado))

				elif movimiento_normal == True:
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
					salida, reintentar = crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

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
				pygame.draw.rect(ventana, negro, ((listdisparos_NA[borrado])[0], (listdisparos_NA[borrado])[1], 2, 16))
				listdisparos_NA.pop(borrado)

			aborrar = []

			for disparo in listdisparos_NE: #Naves enemigas

				ventana.blit(DisparosNegros[disparo[4] - 1], (disparo[0], disparo[1]))

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
					salida, reintentar = crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

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

		# MOVIMIENTO DE NAVES ENEMIGAS

		if primeravuelta == False:

			if boss_activo == True:

				#print(int(1/(probabilidad_nave_boss[valor - 1]/100)))

				new_nave = random.randrange(0, int(1/(probabilidad_nave_boss[valor - 1]/100)))

				if disparos_boses_activos == True:
					new_disparo = random.randrange(0, int(1/(probabilidad_nave_boss[valor - 1]/100)))

				else:
					new_disparo = 100

				if new_nave == 1 and list_naves.count(1) < 5:
					tipo = random.randrange(0, 100)
					if valor != 3:
						lugarnum = random.randint(0, 1)

						if tipo >= 0 and tipo < (probabilidad_tipo_nave_boss[valor - 1])[0]:
							#Naves del tipo 1
							lugar = (ladoboss[valor - 1])[lugarnum]
							new_entity = crear_entidad("EBEN1", 342 + lugar[0], lugar[1], list_naves, 0, lugarnum)

						if tipo >= (probabilidad_tipo_nave_boss[valor - 1])[0] and tipo < (probabilidad_tipo_nave_boss[valor - 1])[1]:
							#Naves del tipo 2
							lugar = (ladoboss[valor - 1])[lugarnum]
							new_entity = crear_entidad("EBEN2", 342 + lugar[0], lugar[1], list_naves, 0, lugarnum)

						if tipo >= (probabilidad_tipo_nave_boss[valor - 1])[1] and tipo < (probabilidad_tipo_nave_boss[valor - 1])[2]:
							#Naves del tipo 3
							lugar = (ladoboss[valor - 1])[lugarnum]
							new_entity = crear_entidad("EBEN3", 342 + lugar[0], lugar[1], list_naves, 0, lugarnum)

						if tipo >= (probabilidad_tipo_nave_boss[valor - 1])[2] and tipo < (probabilidad_tipo_nave_boss[valor - 1])[3]:
							#Naves del tipo 4
							lugar = (ladoboss[valor - 1])[lugarnum]
							new_entity = crear_entidad("EBEN4", 342 + lugar[0], lugar[1], list_naves, 0, lugarnum)

						if tipo >= (probabilidad_tipo_nave_boss[valor - 1])[3] and tipo < (probabilidad_tipo_nave_boss[valor - 1])[4]:
							#Naves del tipo 5
							lugar = (ladoboss[valor - 1])[lugarnum]
							new_entity = crear_entidad("EBEN5", 342 + lugar[0], lugar[1], list_naves, 0, lugarnum)

						if tipo >= (probabilidad_tipo_nave_boss[valor - 1])[4] and tipo < (probabilidad_tipo_nave_boss[valor - 1])[5]:
							#Naves del tipo 6
							pass

						if tipo >= (probabilidad_tipo_nave_boss[valor - 1])[5] and tipo < (probabilidad_tipo_nave_boss[valor - 1])[6]:
							#Naves del tipo 7
							pass

						if tipo >= (probabilidad_tipo_nave_boss[valor - 1])[6] and tipo < (probabilidad_tipo_nave_boss[valor - 1])[7]:
							#Naves del tipo 8
							pass

						if tipo >= (probabilidad_tipo_nave_boss[valor - 1])[7] and tipo < (probabilidad_tipo_nave_boss[valor - 1])[8]:
							#Naves del tipo 9
							pass

						if tipo >= (probabilidad_tipo_nave_boss[valor - 1])[8] and tipo < (probabilidad_tipo_nave_boss[valor - 1])[9]:
							#Naves del tipo 10
							pass

						if new_entity[0] != False:
							#print("New")
							naves.append(new_entity[0])
							list_naves = new_entity[1]

						else:
							pass
							#print("Tried")

					else:
						print("nave")
						if tipo >= 0 and tipo < (probabilidad_tipo_nave_boss[valor - 1])[0]:
							#Naves del tipo 1
							lugar = (ladoboss[valor - 1])
							new_entity = crear_entidad("EBEN1", 342 + lugar[0], lugar[1], list_naves, 0)

						if tipo >= (probabilidad_tipo_nave_boss[valor - 1])[0] and tipo < (probabilidad_tipo_nave_boss[valor - 1])[1]:
							#Naves del tipo 2
							lugar = (ladoboss[valor - 1])
							new_entity = crear_entidad("EBEN2", 342 + lugar[0], lugar[1], list_naves, 0)

						if tipo >= (probabilidad_tipo_nave_boss[valor - 1])[1] and tipo < (probabilidad_tipo_nave_boss[valor - 1])[2]:
							#Naves del tipo 3
							lugar = (ladoboss[valor - 1])
							new_entity = crear_entidad("EBEN3", 342 + lugar[0], lugar[1], list_naves, 0)

						if tipo >= (probabilidad_tipo_nave_boss[valor - 1])[2] and tipo < (probabilidad_tipo_nave_boss[valor - 1])[3]:
							#Naves del tipo 4
							lugar = (ladoboss[valor - 1])
							new_entity = crear_entidad("EBEN4", 342 + lugar[0], lugar[1], list_naves, 0)

						if tipo >= (probabilidad_tipo_nave_boss[valor - 1])[3] and tipo < (probabilidad_tipo_nave_boss[valor - 1])[4]:
							#Naves del tipo 5
							lugar = (ladoboss[valor - 1])
							new_entity = crear_entidad("EBEN5", 342 + lugar[0], lugar[1], list_naves, 0)

						if tipo >= (probabilidad_tipo_nave_boss[valor - 1])[4] and tipo < (probabilidad_tipo_nave_boss[valor - 1])[5]:
							#Naves del tipo 6
							pass

						if tipo >= (probabilidad_tipo_nave_boss[valor - 1])[5] and tipo < (probabilidad_tipo_nave_boss[valor - 1])[6]:
							#Naves del tipo 7
							pass

						if tipo >= (probabilidad_tipo_nave_boss[valor - 1])[6] and tipo < (probabilidad_tipo_nave_boss[valor - 1])[7]:
							#Naves del tipo 8
							pass

						if tipo >= (probabilidad_tipo_nave_boss[valor - 1])[7] and tipo < (probabilidad_tipo_nave_boss[valor - 1])[8]:
							#Naves del tipo 9
							pass

						if tipo >= (probabilidad_tipo_nave_boss[valor - 1])[8] and tipo < (probabilidad_tipo_nave_boss[valor - 1])[9]:
							#Naves del tipo 10
							pass

						if new_entity[0] != False:
							#print("New")
							naves.append(new_entity[0])
							list_naves = new_entity[1]

						else:
							pass

				if new_disparo == 1:

					if valor == 1:

						pos_disp_inic = random.randrange(0, 4) #El numero 4 no entra en las posibilidades

						new_disparo = [Disparos_Boses[0], (posicionesx_de_cañones_bosses[0])[pos_disp_inic], (posicionesy_de_cañones_bosses[0])[pos_disp_inic], posbossx, 0, 0, 0]

					elif valor == 2:

						new_disparo = [Disparos_Boses[1], posicionesx_de_cañones_bosses[1], posicionesy_de_cañones_bosses[1], posbossx, random.randrange(400, 700), 0, 0]
						print(new_disparo)
						print(tamañobossy)

					elif valor == 3:

						pos_disp_inic = random.randrange(0, 2)

						new_disparo = [Disparos_Boses[0], (posicionesx_de_cañones_bosses[2])[pos_disp_inic], (posicionesy_de_cañones_bosses[2])[pos_disp_inic], posbossx, 0, random.randrange(300, 1000), 0]
					
					# [imag, posxinic, posxyinic, posbossxsalida, para el segundo disparo a que altura tiene que explotar, para disparo 3 la cantidad de px necesrios para explotar, cuenta de px para explotido de disparo boss 3]
					disparos_boss.append(new_disparo)

				for disparo_boss in disparos_boss: #Movimiento de los disparos del boss y deteccion de colisiones entre disparos y nave prin

					ventana.blit(Disparos_Bosses_negros[valor - 1], (disparo_boss[1] + disparo_boss[3], disparo_boss[2] + posbossy))

					mostrar_disp = True

					if disparo_boss[2] > alto:
						mostrar_disp = False
						aborrar.append(disparos_boss.index(disparo_boss))
						aborrar.sort()
						aborrar.reverse()

					if disparo_boss[1] + disparo_boss[3] + 8 > xn and disparo_boss[1] + disparo_boss[3] < xn + 42 and disparo_boss[2] + posbossy + 8 > yn and disparo_boss[2] + posbossy < yn + 26:
						disparado = True

						if disparo_boss[4] != 0: #Disparo del boss 2

							new_explosion_boss_2 = [disparo_boss[1] - 41  + disparo_boss[3], disparo_boss[2] - 39 + posbossy, 0]
							ExplosionesDeBoss2Activas.append(new_explosion_boss_2)

							if escudo == False:

								for mejora in mejoras_activadas:
									if mejora[0] == 11: #Detectado que ya hay veneno activa
										aborrar.append(mejoras_activadas.index(mejora))
										aborrar.sort()
										aborrar.reverse()

								for borrado in aborrar:
									mejoras_activadas.pop(borrado)

								aborrar = []
								mejora_activada_new = [11, Efectos[1], "Envenenado: ", Color_Efecto]
								mejoras_activadas.append(mejora_activada_new)

						if disparo_boss[5] != 0:

							new_explosion_boss_3 = [disparo_boss[1] - 41  + disparo_boss[3], disparo_boss[2] - 39 + posbossy, 0]
							ExplosionesDeBoss3Activas.append(new_explosion_boss_3)

						if xn + 14 > disparo_boss[1] + disparo_boss[3] and alaIzquierda == True and escudo == False: #14px primera ala
							mostrar_disp = False
							vida_alaIzquierda -= daño_disparo_bosses[valor - 1]

							if vida_alaIzquierda < 0:
								vida_alaIzquierda = 0

							aborrar.append(disparos_boss.index(disparo_boss))
							aborrar.sort()
							aborrar.reverse()

						elif xn + 28 < disparo_boss[1] + disparo_boss[3] and alaDerecha == True and escudo == False: #28px segunda ala
							mostrar_disp = False
							vida_alaDerecha -= daño_disparo_bosses[valor - 1]

							if vida_alaDerecha < 0:
								vida_alaDerecha = 0

							aborrar.append(disparos_boss.index(disparo_boss))
							aborrar.sort()
							aborrar.reverse()

						elif frontal == False and escudo == False: #Deteccion del motor
							mostrar_disp = False
							vida_motor -= daño_disparo_bosses[valor - 1]

							if vida_motor < 0:
								vida_motor = 0

							aborrar.append(disparos_boss.index(disparo_boss))
							aborrar.sort()
							aborrar.reverse()

						elif xn + 13 < disparo_boss[1] + disparo_boss[3] and xn + 29 > disparo_boss[1] + disparo_boss[3] and escudo == False: #Deteccion del frontal
							mostrar_disp = False
							vida_frontal -= daño_disparo_bosses[valor - 1]

							if vida_frontal < 0:
								vida_frontal = 0

							aborrar.append(disparos_boss.index(disparo_boss))
							aborrar.sort()
							aborrar.reverse()

						elif escudo == True:
							mostrar_disp = False
							escudo = False
							ventana.blit(Escudo_Negro, (round(xn) - 2, round(yn) - 2))
							aborrar.append(disparos_boss.index(disparo_boss))
							aborrar.sort()
							aborrar.reverse()

					elif disparo_boss[2] >= disparo_boss[4] and disparo_boss[4] != 0: #Ha llegado al punto de explosion
						mostrar_disp = False

						#print(comprovardistancia(xn, yn, disparo_boss[1] + disparo_boss[3], disparo_boss[2] + posbossy))

						if comprovardistancia(xn, yn, disparo_boss[1] + disparo_boss[3], disparo_boss[2] + posbossy) < 47 or comprovardistancia(xn + tamañox, yn, disparo_boss[1] + disparo_boss[3], disparo_boss[2] + posbossy) < 47 or comprovardistancia(xn + tamañox, yn + tamañoy, disparo_boss[1] + disparo_boss[3], disparo_boss[2] + posbossy) < 47 or comprovardistancia(xn, yn + tamañoy, disparo_boss[1] + disparo_boss[3], disparo_boss[2] + posbossy) < 47 and escudo == False: #La nave principal esta a la suficiente distancia como para ser envenenada.
							
							for mejora in mejoras_activadas:
								if mejora[0] == 11: #Detectado que ya hay veneno activa
									aborrar.append(mejoras_activadas.index(mejora))
									aborrar.sort()
									aborrar.reverse()

							for borrado in aborrar:
								mejoras_activadas.pop(borrado)

							aborrar = []

							mejora_activada_new = [11, Efectos[1], "Envenenado: ", Color_Efecto]
							mejoras_activadas.append(mejora_activada_new)

						#print(disparo_boss)

						new_explosion_boss_2 = [disparo_boss[1] - 41  + disparo_boss[3], disparo_boss[2] - 39 + posbossy, 0]
						ExplosionesDeBoss2Activas.append(new_explosion_boss_2)

						aborrar.append(disparos_boss.index(disparo_boss))
						aborrar.sort()
						aborrar.reverse()

					elif disparo_boss[6] >= disparo_boss[5] and disparo_boss[5] != 0:

						new_explosion_boss_3 = [disparo_boss[1] - 41  + disparo_boss[3], disparo_boss[2] - 39 + posbossy, 0]
						ExplosionesDeBoss3Activas.append(new_explosion_boss_3)

						aborrar.append(disparos_boss.index(disparo_boss))
						aborrar.sort()
						aborrar.reverse()

					if disparo_boss[5] != 0:
						#Zona para calcular el incremento de x y de y en los disparos del boss 3
						diferencia, motor_1, ladox, ladoy = calcular_fraccion_avance(xn, yn, disparo_boss[1] + disparo_boss[3], disparo_boss[2] + posbossy)

						if motor_1 == "x":
							xavanzado = (velocidad_disparo_boss*(200/FPS))/1.8
							yavanzado = xavanzado * diferencia

						elif motor_1 == "y":
							yavanzado = (velocidad_disparo_boss*(200/FPS))/1.8
							xavanzado = yavanzado * diferencia

						x_ant = disparo_boss[1]
						y_ant = disparo_boss[2]

						if ladox == "izq" and ladoy == "arr":
							disparo_boss[1] -= xavanzado
							disparo_boss[2] -= yavanzado

						elif ladox == "izq" and ladoy == "abj":
							disparo_boss[1] -= xavanzado
							disparo_boss[2] += yavanzado

						elif ladox == "dch" and ladoy == "arr":
							disparo_boss[1] += xavanzado
							disparo_boss[2] -= yavanzado

						elif ladox == "dch" and ladoy == "abj":
							disparo_boss[1] += xavanzado
							disparo_boss[2] += yavanzado

						elif ladox == None and ladoy == "arr":
							disparo_boss[2] -= yavanzado

						elif ladox == None and ladoy == "abj":
							disparo_boss[2] += yavanzado

						elif ladoy == None and ladox == "izq":
							disparo_boss[1] -= xavanzado

						elif ladoy == None and ladox == "dch":
							disparo_boss[1] += xavanzado

						if mostrar_disp == True:
							ventana.blit(disparo_boss[0], (disparo_boss[1] + disparo_boss[3], disparo_boss[2] + posbossy))
							dist = comprovardistancia(disparo_boss[1], disparo_boss[2], x_ant, y_ant)
							disparo_boss[6] += dist

					else:
						disparo_boss[2] += velocidad_disparo_boss*(200/FPS)

						if mostrar_disp == True:
							ventana.blit(disparo_boss[0], (disparo_boss[1] + disparo_boss[3], disparo_boss[2] + posbossy))

				for borrado in aborrar:
					disparos_boss.pop(borrado)

				aborrar = []

				for nave in naves:

					if nave.viva == True:

						if nave.posx < 950 - nave.tamañox and nave.posx > 330:
							ventana.blit(Naves_Negro[nave.tipo - 1], (round(nave.posx), round(nave.posy)))
							mix = nave.calculardisparo(Lv_act, FPS)

							if mix != "False":
								if mix[2] == 1:
									listdisparos_NE.append(mix[1])

								else:
									for new_disp in mix[1]:
										listdisparos_NE.append(new_disp)

						else:
							pass

						if nave.salidaboss == False and valor !=3:

							if nave.posxtogo == None:
								nave.posxytogoset(xn, yn)
								nave.radioinicset((math.sqrt((nave.posx - xn) ** 2 + (nave.posy - yn) ** 2))/2)
								nave.centroset(math.sqrt((xn - nave.posx) ** 2)/2 + nave.posx, math.sqrt((yn - nave.posy) ** 2)/2 + nave.posy)

							if round(nave.posy) + 2 >= round(nave.posytogo) and round(nave.posx) + 2 >= round(nave.posxtogo):
								nave.salidabossset(True)
								nave.posxytogoset(None, None)

							if nave.ladoboss == 0:

								try:
									if nave.pasado == True:
										x = 9/0

									else:
										newy = ((nave.radioinic ** 2 - (nave.centrox - (nave.posx - (1000/FPS)*nave.velocidad)) ** 2) ** (1/2))*-1
										trier = round(nave.centroy + newy)
										nave.actualizarpos(nave.posx - (1000/FPS)*nave.velocidad, nave.centroy + newy)

								except:
									nave.pasadoset(True)
									newy = ((nave.radioinic ** 2 - (nave.centrox - (nave.posx + (1000/FPS)*nave.velocidad)) ** 2) ** (1/2))
									nave.actualizarpos(nave.posx + (1000/FPS)*nave.velocidad, nave.centroy + newy)

							else:
								try:
									if nave.pasado == True:
										x = 9/0

									else:
										newy = ((nave.radioinic ** 2 - (nave.centrox - (nave.posx + (1000/FPS)*nave.velocidad)) ** 2) ** (1/2))*-1
										trier = round(nave.centroy + newy)
										nave.actualizarpos(nave.posx + (1000/FPS)*nave.velocidad, nave.centroy + newy)

								except:
									nave.pasadoset(True)
									newy = ((nave.radioinic ** 2 - (nave.centrox - (nave.posx - (1000/FPS)*nave.velocidad)) ** 2) ** (1/2))
									nave.actualizarpos(nave.posx - (1000/FPS)*nave.velocidad, nave.centroy + newy)

						elif nave.salidaboss == False:

							if nave.posx < 600:
								nave.actualizarpos(round(nave.posx + (700/FPS)*nave.velocidad), nave.posy)

							else:
								nave.salidabossset(True)

						else:
							if nave.posxtogo == None and nave.idavuelta == 0:
								nave.posxytogoset(random.randint(330, 950 - nave.tamañox), random.randint(360, 719 - nave.tamañoy))
								nave.idavueltaset(1)

							elif nave.posxtogo == None and nave.idavuelta == 1:
								nave.posxytogoset(xn, yn)
								nave.idavueltaset(0)

							diferencia, motor_1, ladox, ladoy = calcular_fraccion_avance(nave.posxtogo, nave.posytogo, nave.posx, nave.posy)

							if motor_1 == "x":
								xavanzado = (450/FPS)*0.3
								yavanzado = xavanzado * diferencia

							elif motor_1 == "y":
								yavanzado = (450/FPS)*0.3
								xavanzado = yavanzado * diferencia

							x_ant = nave.posx
							y_ant = nave.posy

							if ladox == "izq" and ladoy == "arr":
								nave.actualizarpos(x_ant - xavanzado, y_ant - yavanzado)

							elif ladox == "izq" and ladoy == "abj":
								nave.actualizarpos(x_ant - xavanzado, y_ant + yavanzado)

							elif ladox == "dch" and ladoy == "arr":
								nave.actualizarpos(x_ant + xavanzado, y_ant - yavanzado)

							elif ladox == "dch" and ladoy == "abj":
								nave.actualizarpos(x_ant + xavanzado, y_ant + yavanzado)

							elif ladox == None and ladoy == "arr":
								nave.actualizarpos(x_ant, y_ant - yavanzado)

							elif ladox == None and ladoy == "abj":
								nave.actualizarpos(x_ant, y_ant + yavanzado)

							elif ladoy == None and ladox == "izq":
								nave.actualizarpos(x_ant - xavanzado, y_ant)

							elif ladoy == None and ladox == "dch":
								nave.actualizarpos(x_ant + xavanzado, y_ant)

							if round(nave.posxtogo) == round(nave.posx) and round(nave.posytogo) == round(nave.posy):
								nave.posxytogoset(None, None)

						if nave.posx < 950 - nave.tamañox and nave.posx > 330:
							ventana.blit(nave.ImagenNave, (round(nave.posx), round(nave.posy)))

						#else:
							#ventana.blit(nave.ImagenNave, (round(nave.posx), round(nave.posy)))

						#pygame.draw.circle(ventana, blanco, (round(nave.centrox), round(nave.centroy)), round(nave.radioinic), 5)

					else:
						if nave.muerteprimera == True:

							list_naves.pop(nave.pos)
							list_naves.insert(nave.pos, 0)
							if nave.caida != False:
								nave.caidaset(False)
								navecayendo = False
							#explosion_sound.play()

							ventana.blit(Naves_Negro[nave.tipo - 1], (round(nave.posx), round(nave.posy)))

							naves_destruidas_a_explotar.append([nave.posx, nave.posy, nave.tipo, 1])

							nave.Muerteprimera()

			else:

				for nave in naves:

					if nave.viva == True:

						if nave.posx < 330 or nave.posx > 950 - nave.tamañox:
							pass

						else:
							ventana.blit(Naves_Negro[nave.tipo - 1], (round(nave.posx), round(nave.posy)))

						mix = nave.calculardisparo(Lv_act, FPS)

						if mix != "False":
							if mix[2] == 1:
								listdisparos_NE.append(mix[1])

							else:
								for new_disp in mix[1]:
									listdisparos_NE.append(new_disp)

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

						elif nave.posy < 600 and navecayendo != True and nave.esperando == False and nave.permanecer == False:

							value = random.randrange(1, round(5000/300) * (FPS + 1)) #Hay 4 tipos d caidas

							if value > 0 and value < round(1000/300) * (FPS + 1): #Recta diagonal hacia la nave
								xnavetoir = xn
								ynavetoir = alto
								nave.caidaset(1)
								navecayendo = True

							elif value > round(1000/300) * (FPS + 1) and value < round(2000/300) * (FPS + 1) and nave.posxinic > 350 + round(0.03125 * ancho) and nave.posxinic < 930 - round(0.03125 * ancho) - 18: #Ancho de la nave
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

							elif value > round(2000/300) * (FPS + 1) and value < round(3000/300) * (FPS + 1) and nave.posx < 960 - radio - round(0.03125 * ancho) and nave.posx > 320 + radio + round(0.03125 * ancho):
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

						if nave.posx < 330 or nave.posx > 950 - nave.tamañox:
							pass

						else:
							ventana.blit(nave.ImagenNave, (round(nave.posx), round(nave.posy)))

					else:
						if nave.muerteprimera == True:

							list_naves.pop(nave.pos)
							list_naves.insert(nave.pos, 0)
							if nave.caida != False:
								nave.caidaset(False)
								navecayendo = False
							#explosion_sound.play()

							ventana.blit(Naves_Negro[nave.tipo - 1], (nave.posx, nave.posy))

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
					salida, reintentar = crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

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

		for explosion in ExplosionesNuclearesActivas: #[posx, posy, counter]
			
			if explosion[2] == 0:
				ventana.blit(ExplosionesNucleares[explosion[2]], (explosion[0], explosion[1]))

			else:
				ventana.blit(ExplosionesNucleares_Negro[explosion[2] - 1], (explosion[0], explosion[1]))

				if explosion[2] > 11:
					aborrar.append(ExplosionesNuclearesActivas.index(explosion))
					aborrar.sort()
					aborrar.reverse()

				else:
					ventana.blit(ExplosionesNucleares[explosion[2]], (explosion[0], explosion[1]))

			counter_ant = explosion[2]

			explosion.pop(2)
			explosion.insert(2, counter_ant + 1)

		for borrado in aborrar:
			ExplosionesNuclearesActivas.pop(borrado)

		aborrar = []

		for explosion in ExplosionesDeBoss2Activas: #[posx, posy, counter]

			if explosion[2] == 0:
				ventana.blit(ExplosionesDisparoBoss2[explosion[2]], (explosion[0], explosion[1]))

			else:
				ventana.blit(ExplosionesNucleares_Negro[explosion[2] - 1], (explosion[0], explosion[1]))

				if explosion[2] > 11:
					aborrar.append(ExplosionesDeBoss2Activas.index(explosion))
					aborrar.sort()
					aborrar.reverse()

				else:
					ventana.blit(ExplosionesDisparoBoss2[explosion[2]], (explosion[0], explosion[1]))

			counter_ant = explosion[2]

			explosion.pop(2)
			explosion.insert(2, counter_ant + 1)

		for borrado in aborrar:
			ExplosionesDeBoss2Activas.pop(borrado)

		aborrar = []

		for explosion in ExplosionesDeBoss3Activas: #[posx, posy, counter]

			if explosion[2] == 0:
				ventana.blit(ExplosionesDisparoBoss3[explosion[2]], (explosion[0], explosion[1]))

			else:
				ventana.blit(ExplosionesNucleares_Negro[explosion[2] - 1], (explosion[0], explosion[1]))

				if explosion[2] > 11:
					aborrar.append(ExplosionesDeBoss3Activas.index(explosion))
					aborrar.sort()
					aborrar.reverse()

				else:
					ventana.blit(ExplosionesDisparoBoss3[explosion[2]], (explosion[0], explosion[1]))

			counter_ant = explosion[2]

			explosion.pop(2)
			explosion.insert(2, counter_ant + 1)

		for borrado in aborrar:
			ExplosionesDeBoss3Activas.pop(borrado)

		aborrar = []

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

				resultados = actualizar_pantalla_derecha_arriba(ventana, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, fpsactivos, infinito, segundostranscurridos, mejoras_activadas)

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

				if resultados[7] != False:

					for mejora_mostrada in resultados[7]:
						ventana.blit(mejora_mostrada[0], (mejora_mostrada[1], mejora_mostrada[2]))

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

				resultados = actualizar_pantalla_derecha_arriba(ventana, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, fpsactivos, infinito, segundostranscurridos, mejoras_activadas)

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

				if resultados[7] != False:

					for mejora_mostrada in resultados[7]:
						ventana.blit(mejora_mostrada[0], (mejora_mostrada[1], mejora_mostrada[2]))

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
					
				resultados = actualizar_pantalla_derecha_arriba(ventana, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, fpsactivos, infinito, segundostranscurridos, mejoras_activadas)

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

				if resultados[7] != False:

					for mejora_mostrada in resultados[7]:
						ventana.blit(mejora_mostrada[0], (mejora_mostrada[1], mejora_mostrada[2]))

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
					
				resultados = actualizar_pantalla_derecha_arriba(ventana, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, fpsactivos, infinito, segundostranscurridos, mejoras_activadas)

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

				if resultados[7] != False:

					for mejora_mostrada in resultados[7]:
						ventana.blit(mejora_mostrada[0], (mejora_mostrada[1], mejora_mostrada[2]))

				aborrar.append(monedas_en_pantalla.index(moneda))
				aborrar.sort()
				aborrar.reverse()

		for borrado in aborrar:
			ventana.blit(monedas_Negras_Imag[(monedas_en_pantalla[borrado])[2]], ((monedas_en_pantalla[borrado])[0], (monedas_en_pantalla[borrado])[1]))
			monedas_en_pantalla.pop(borrado)

		aborrar = []

		for disparo in listdisparos_NE: #Balas enemigas contra nave amiga

			if xn < disparo[0] + ancho_proyectiles[disparo[4] - 1] and xn + 42 > disparo[0] and yn < disparo[1] + alto_proyectiles[disparo[4] - 1] and yn + 26 > disparo[1]: #Comprueva si esta tocando la nave amiga
				disparado = True
				#print("Tocado", disparo[4])
				puntuacion -= 5
				if puntuacion < 0: puntuacion = 0

				if disparo[4] == 6:

					existente = False

					Multiplicador_Velocidad += 1

					if escudo == False:

						for mejora in mejoras_activadas:
							if mejora[0] == 9: #Detectado que ya hay lentitud activa
								existente == True
								aborrarlos.append(mejoras_activadas.index(mejora))
								aborrarlos.sort()
								aborrarlos.reverse()

						for borrado in aborrarlos:
							mejoras_activadas.pop(borrado)

						aborrarlos = []

					new_explosion_nuclear = [disparo[0] - 41, disparo[1] - 39, 0]
					ExplosionesNuclearesActivas.append(new_explosion_nuclear)

					if escudo == False:
						Velocidad_Nave = Velocidad_Nave/2
						mejora_activada_new = [9, Efectos[0], "Lentitud X" + str(Multiplicador_Velocidad) + ": ", Color_Efecto]
						mejoras_activadas.append(mejora_activada_new)
						#print("lentitud", disparo, listdisparos_NE)

					resultados = actualizar_pantalla_derecha_arriba(ventana, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, med, fpsactivos, infinito, segundostranscurridos, mejoras_activadas)

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

					if resultados[7] != False:

						for mejora_mostrada in resultados[7]: #[Texto, x, y]
							ventana.blit(mejora_mostrada[0], (mejora_mostrada[1], mejora_mostrada[2]))

				if xn + 14 > disparo[0] + ancho_proyectiles[disparo[4] - 1] and alaIzquierda == True and escudo == False and vida_alaIzquierda > 0: #14px primera ala
					vida_alaIzquierda -= dañoProyectiles[disparo[4] - 1]

					if vida_alaIzquierda < 0:
						vida_alaIzquierda = 0

					if vida_alaIzquierda == 0:
						resultados3 = actualizar_pantalla_izquierda_debajo(ventana, notificacion_ala)

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

					aborrar.append(listdisparos_NE.index(disparo))
					aborrar.sort()
					aborrar.reverse()

				elif xn + 28 < disparo[0] and alaDerecha == True and escudo == False and vida_alaDerecha > 0: #28px segunda ala
					vida_alaDerecha -= dañoProyectiles[disparo[4] - 1]

					if vida_alaDerecha < 0:
						vida_alaDerecha = 0

					if vida_alaDerecha == 0:
						resultados3 = actualizar_pantalla_izquierda_debajo(ventana, notificacion_ala)

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

					aborrar.append(listdisparos_NE.index(disparo))
					aborrar.sort()
					aborrar.reverse()

				elif frontal == False and escudo == False: #Deteccion del motor
					vida_motor -= dañoProyectiles[disparo[4] - 1]

					if vida_motor < 0:
						vida_motor = 0

					aborrar.append(listdisparos_NE.index(disparo))
					aborrar.sort()
					aborrar.reverse()

				elif escudo == False and vida_frontal > 0: #Deteccion del frontal
					vida_frontal -= dañoProyectiles[disparo[4] - 1]

					if vida_frontal < 0:
						vida_frontal = 0

					if vida_frontal == 0:
						resultados3 = actualizar_pantalla_izquierda_debajo(ventana, notificacion_frontal)

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

					aborrar.append(listdisparos_NE.index(disparo))
					aborrar.sort()
					aborrar.reverse()

				elif escudo == True:
					escudo = False
					ventana.blit(Escudo_Negro, (round(xn) - 2, round(yn) - 2))

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
					salida, reintentar = crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

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
					frontal_tocado = False
					ala_tocada = False

					if nave.posx + 4 > xn and nave.posx - 4 < xn + tamañox and nave.posy + 4 > yn and nave.posy  - 4 < yn + tamañoy: #Arriba izquierda
						#print(escudo, "1")
						untouched = False
						motor_destruido = False

						if nave.posx < xn + 14: #Ala izquierda
							if vida_alaIzquierda == 0:
								untouched = True

							else:
								ala_tocada = True

							if escudo != True: vida_alaIzquierda = 0

						elif nave.posx > xn + 28: #Ala derecha
							if vida_alaDerecha == 0:
								untouched = True

							else:
								ala_tocada = True

							if escudo != True: vida_alaDerecha = 0

						elif nave.posx > xn + 14 and nave.posx < xn + 28 and nave.posy < yn + 12 and escudo == False: #Frontal
							frontal_tocado = True
							vida_frontal = 0

						elif nave.posx > xn + 14 and nave.posx < xn + 28 and nave.posy < yn + 26:
							motor_destruido = True
							nave.recibirdañoEBA(dañocac)

							if escudo == True:
								viva = True
								escudo = False
								ventana.blit(Escudo_Negro, (round(xn) - 2, round(yn) - 2))

							else:
								vida_motor = 0

							disparado = True
							puntuacion -= 80

							if nave.caida == True:
								navecayendo = False
								nave.caidaset(False)

						if untouched == False and motor_destruido == False:
							print("tocado")

							viva, escudo = ejecutar_daño_CAC(escudo)

							disparado = True
							puntuacion -= 40

							if nave.caida == True:
								navecayendo = False
								nave.caidaset(False)

						if nave.caida == True and desactivar_caida_con_parte_imaginaria == True:
							navecayendo = False
							nave.caidaset(False)

						#print(frontal_tocado, escudo, viva, untouched, "1")

					elif nave.posx + nave.tamañox + 4 > xn and nave.posx + nave.tamañox  - 4 < xn + tamañox and nave.posy + 4 > yn and nave.posy  - 4 < yn + tamañoy: #Arriba derecha
						#print(escudo, "2")
						untouched = False
						motor_destruido = False

						if nave.posx + nave.tamañox < xn + 14: #Ala izquierda
							if vida_alaIzquierda == 0:
								untouched = True

							else:
								ala_tocada = True

							if escudo != True: vida_alaIzquierda = 0

						elif nave.posx + nave.tamañox > xn + 28: #Ala derecha
							if vida_alaDerecha == 0:
								untouched = True

							else:
								ala_tocada = True

							if escudo != True: vida_alaDerecha = 0

						elif nave.posx + nave.tamañox > xn + 14 and nave.posx + nave.tamañox < xn + 28 and nave.posy < yn + 12 and escudo == False: #Frontal
							frontal_tocado = True
							vida_frontal = 0

						elif nave.posx + nave.tamañox > xn + 14 and nave.posx + nave.tamañox < xn + 28 and nave.posy < yn + 26:
							motor_destruido = True
							nave.recibirdañoEBA(dañocac)

							if escudo == True:
								viva = True
								escudo = False
								ventana.blit(Escudo_Negro, (round(xn) - 2, round(yn) - 2))

							else:
								vida_motor = 0

							disparado = True
							puntuacion -= 80

							if nave.caida == True:
								navecayendo = False
								nave.caidaset(False)

						if untouched == False and motor_destruido == False:
							#print("tocado")

							viva, escudo = ejecutar_daño_CAC(escudo)
							disparado = True
							puntuacion -= 40

							if nave.caida == True:
								navecayendo = False
								nave.caidaset(False)

						if nave.caida == True and desactivar_caida_con_parte_imaginaria == True:
							navecayendo = False
							nave.caidaset(False)

						#print(frontal_tocado, escudo, viva, untouched, "2")

					elif nave.posx + nave.tamañox + 4 > xn and nave.posx + nave.tamañox  - 4 < xn + tamañox and nave.posy +  nave.tamañoy + 4 > yn and nave.posy + nave.tamañoy - 4 < yn + tamañoy: #Abajo derecha
						#print(escudo, "3")
						untouched = False
						motor_destruido = False

						if nave.posx + nave.tamañox < xn + 14: #Ala izquierda
							if vida_alaIzquierda == 0:
								untouched = True

							else:
								ala_tocada = True

							if escudo != True: vida_alaIzquierda = 0

						elif nave.posx + nave.tamañox > xn + 28: #Ala derecha
							if vida_alaDerecha == 0:
								untouched = True

							else:
								ala_tocada = True

							if escudo != True: vida_alaDerecha = 0

						elif nave.posx + nave.tamañox > xn + 14 and nave.posx + nave.tamañox < xn + 28 and nave.posy + nave.tamañoy < yn + 12 and escudo == False: #Frontal
							frontal_tocado = True
							vida_frontal = 0

						elif nave.posx + nave.tamañox > xn + 14 and nave.posx + nave.tamañox < xn + 28 and nave.posy + nave.tamañoy < yn + 26:
							motor_destruido = True
							nave.recibirdañoEBA(dañocac)

							if escudo == True:
								viva = True
								escudo = False
								ventana.blit(Escudo_Negro, (round(xn) - 2, round(yn) - 2))

							else:
								vida_motor = 0

							disparado = True
							puntuacion -= 80

							if nave.caida == True:
								navecayendo = False
								nave.caidaset(False)

						if untouched == False and motor_destruido == False:
							#print("tocado")

							viva, escudo = ejecutar_daño_CAC(escudo)
							disparado = True
							puntuacion -= 40

							if nave.caida == True:
								navecayendo = False
								nave.caidaset(False)

						if nave.caida == True and desactivar_caida_con_parte_imaginaria == True:
							navecayendo = False
							nave.caidaset(False)

						#print(frontal_tocado, escudo, viva, untouched, "3")

					elif nave.posx + 4 > xn and nave.posx  - 4 < xn + tamañox and nave.posy + nave.tamañoy + 4 > yn and nave.posy + nave.tamañoy - 4 < yn + tamañoy: #Abajo izquierda
						#print(escudo, "4")
						untouched = False
						motor_destruido = False

						if nave.posx < xn + 14: #Ala izquierda
							if vida_alaIzquierda == 0:
								untouched = True

							else:
								ala_tocada = True

							if escudo != True: vida_alaIzquierda = 0

						elif nave.posx > xn + 28: #Ala derecha
							if vida_alaDerecha == 0:
								untouched = True

							else:
								ala_tocada = True

							if escudo != True: vida_alaDerecha = 0

						elif nave.posx > xn + 14 and nave.posx < xn + 28 and nave.posy + nave.tamañoy < yn + 12 and escudo == False: #Frontal
							frontal_tocado = True
							vida_frontal = 0

						elif nave.posx > xn + 14 and nave.posx < xn + 28 and nave.posy < yn + 26:
							motor_destruido = True
							nave.recibirdañoEBA(dañocac)

							if escudo == True:
								viva = True
								escudo = False
								ventana.blit(Escudo_Negro, (round(xn) - 2, round(yn) - 2))

							else:
								vida_motor = 0

							disparado = True
							puntuacion -= 80

							if nave.caida == True:
								navecayendo = False
								nave.caidaset(False)

						if untouched == False and motor_destruido == False:
							#print("tocado")

							viva, escudo = ejecutar_daño_CAC(escudo)
							disparado = True
							puntuacion -= 40

							if nave.caida == True:
								navecayendo = False
								nave.caidaset(False)

						if nave.caida == True and desactivar_caida_con_parte_imaginaria == True:
							navecayendo = False
							nave.caidaset(False)

						#print(frontal_tocado, escudo, viva, untouched, "4", nave.posy, yn)

					if puntuacion < 0: puntuacion = 0

					if ala_tocada == True:
						resultados3 = actualizar_pantalla_izquierda_debajo(ventana, notificacion_ala)

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

					if frontal_tocado == True:
						resultados3 = actualizar_pantalla_izquierda_debajo(ventana, notificacion_frontal)

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

				else:
					pass

		if Naves_destruidas == Nº_Naves and boss_activo == False or viva == False and infinito == True and boss_activo == False: #Para comprovar que hayas ganado
			pygame.draw.rect(ventana, negro, (posxline1 + tamañoline, 0, 640 - tamañoline - 1, alto))
			pygame.display.update()

			if Lv_act != 5 and Lv_act != 10 and Lv_act != 15 and Lv_act != 20 and Lv_act != 25: #No hay boss
				if viva == True:
					#crear_texto_en_pantalla(ventana, "!GANASTE¡, este texto es temporal", 2, FPS)
					porcentaje_alcanzado_exportar = round((Naves_destruidas/Nº_Naves)*100)
					porcent_vida_alaIzquierda = vida_alaIzquierda/vida_alaIzquierda_org
					porcent_vida_alaDerecha = vida_alaDerecha/vida_alaDerecha_org
					porcent_vida_motor = vida_motor/vida_motor_org
					porcent_vida_frontal = vida_frontal/vida_frontal_org
					porcentaje_Medio_de_vida_exportar = (round((porcent_vida_alaIzquierda + porcent_vida_alaDerecha + porcent_vida_motor + porcent_vida_frontal)/4, 2))*100

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

					resultado = "¡Has ganado!"

					# --> NUEVO

					reintentar = ejecutar_pantalla_resultados(ventana, user_act[1], Lv_act, pantalla_act, puntuacion_total, monedas_totales, Naves_destruidas, segundostranscurridos, Monedas, puntuacion_exportar, resultado, Nº_Naves, estado_escudo, estado_alaizquierda, estado_aladerecha, estado_motor, estado_frontal, estado_final_nave, infinito, porcentaje_Medio_de_vida_exportar, porcentaje_alcanzado_exportar)

					victoria = True

					Exit_presionado = True
					###AQUI

				else:
					#crear_texto_en_pantalla(ventana, "¡PERDISTE!, este texto es temporal", 2, FPS)

					if infinito == False:
						porcentaje_alcanzado_exportar = round((Naves_destruidas/Nº_Naves)*100)

					else:
						porcentaje_alcanzado_exportar = 0

					porcentaje_Medio_de_vida_exportar = 0

					estado_alaizquierda = 2
					estado_aladerecha = 2
					estado_motor = 2
					estado_frontal = 2

					if escudo == True:
						puntuacion_exportar = puntuacion * 2
						estado_escudo = 0

					else:
						puntuacion_exportar = puntuacion
						estado_escudo = 2

					estado_final_nave = "destruida"

					resultado = "¡Has perdido!"

					# --> NUEVO

					reintentar = ejecutar_pantalla_resultados(ventana, user_act[1], Lv_act, pantalla_act, puntuacion_total, monedas_totales, Naves_destruidas, segundostranscurridos, Monedas, puntuacion_exportar, resultado, Nº_Naves, estado_escudo, estado_alaizquierda, estado_aladerecha, estado_motor, estado_frontal, estado_final_nave, infinito, porcentaje_Medio_de_vida_exportar, porcentaje_alcanzado_exportar)

					victoria = False
		
					Exit_presionado = True
					###AQUI

			else: #Hay boss
				if viva == True:

					ultimoseventos = []

					for disparo in listdisparos_NA: #Naves amigas
						ventana.blit(DisparoNegro, (disparo[0], disparo[1]))

					for disparo in listdisparos_NE: #Naves enemigas
						ventana.blit(DisparosNegros[disparo[4] - 1], (disparo[0], disparo[1]))

					listdisparos_NA = []
					listdisparos_NE = []

					primeravuelta = True
					vueltas = 0
					navecayendo = False

					ultimoseventos = []

					teclaizquierdapress = False
					tecladerechapress = False
					teclaabajopress = False
					teclaarribapress = False
					disparoAmigo = False

					print("Boss creandose")
					boss_activo = True
					ventana.blit(NavePrincipalNegro, (round(xn), round(yn)))
					xn = ancho/2 - 21
					yn = alto/4 * 3
					ventana.blit(Tipos_De_Naves_Prin[index_Nave_Prin], (xn, yn))
					pygame.display.update()
					AparicionesBossAct = AparicionesBosses[valor - 1]

					for i in AparicionesBossAct:
						ventana.blit(i, (posbossx, posbossy))
						pygame.display.update()
						time.sleep(0.09)

					ventana.blit(Borrador_ap_bosses, (posbossx, posbossy))

					ventana.blit(Bosses[valor - 1][escudo_boss], (posbossx, posbossy))
					pygame.display.update()

					crear_texto_en_pantalla(ventana, "Destruye " + str(naves_a_matar[valor - 1]) + " naves para poder disparar al boss", 2, FPS)

				else: #Jajaja pringado moriste junto a tu esperanza de llegar al boss
					#crear_texto_en_pantalla(ventana, "¡PERDISTE!, este texto es temporal", 2, FPS)

					if infinito == False:
						porcentaje_alcanzado_exportar = round((Naves_destruidas/Nº_Naves)*100)

					else:
						porcentaje_alcanzado_exportar = 0

					porcentaje_Medio_de_vida_exportar = 0

					estado_alaizquierda = 2
					estado_aladerecha = 2
					estado_motor = 2
					estado_frontal = 2

					if escudo == True:
						puntuacion_exportar = puntuacion * 2
						estado_escudo = 0

					else:
						puntuacion_exportar = puntuacion
						estado_escudo = 2

					estado_final_nave = "destruida"

					resultado = "¡Has perdido!"

					# --> NUEVO

					reintentar = ejecutar_pantalla_resultados(ventana, user_act[1], Lv_act, pantalla_act, puntuacion_total, monedas_totales, Naves_destruidas, segundostranscurridos, Monedas, puntuacion_exportar, resultado, Nº_Naves, estado_escudo, estado_alaizquierda, estado_aladerecha, estado_motor, estado_frontal, estado_final_nave, infinito, porcentaje_Medio_de_vida_exportar, porcentaje_alcanzado_exportar)

					victoria = False
		
					Exit_presionado = True
					###AQUI

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
					salida, reintentar = crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

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

		if boss_activo == True and escudo_boss == 0:

			for disparo in listdisparos_NA: #Balas amigas contra boss sin escudo

				if comprovartocandoboss(disparo, posbossx, posbossy, multiplier_boss):
					vida_boss_act -= daño_por_proyectil[tipodeproyectilamigo]
					print(vida_boss_act)
					aborrar.append(listdisparos_NA.index(disparo))
					aborrar.sort()
					aborrar.reverse()

		elif boss_activo == True and escudo_boss == 1:

			for disparo in listdisparos_NA: #Balas amigas contra boss con escudo

				if comprovartocandoboss(disparo, posbossx, posbossy, multiplier_boss):
					aborrar.append(listdisparos_NA.index(disparo))
					aborrar.sort()
					aborrar.reverse()

		for borrado in aborrar:
			pygame.draw.rect(ventana, negro, ((listdisparos_NA[borrado])[0], (listdisparos_NA[borrado])[1], 4, 16))
			listdisparos_NA.pop(borrado)

		aborrar = []

		for mejora in mejoras:

			tocado = False

			if mejora[2] > xn and mejora[2] < xn + nave_ancho and mejora[3] > yn and mejora[3] < yn + nave_alto:
				tocado = True

			elif mejora[2] > xn and mejora[2] < xn + nave_ancho and mejora[3] + alto_mejoras > yn and mejora[3] + alto_mejoras < yn + nave_alto:
				tocado = True

			elif mejora[2] + ancho_mejoras > xn and mejora[2] + ancho_mejoras < xn + nave_ancho and mejora[3] > yn and mejora[3] < yn + nave_alto:
				tocado = True

			elif mejora[2] + ancho_mejoras > xn and mejora[2] + ancho_mejoras < xn + nave_ancho and mejora[3] + alto_mejoras > yn and mejora[3] + alto_mejoras < yn + nave_alto:
				tocado = True

			if tocado == True:
				aborrar.append(mejoras.index(mejora))# [lado de pant, imag, posx, posy, posx_ir, posy_ir]
				aborrar.sort()
				aborrar.reverse()

				existe = False

				if mejora[6] == 0: #2 Disparos

					for mejora_activada in mejoras_activadas:
						if mejora_activada[0] == mejora[6]:
							existe = True
							mejora_activada.pop(1)
							mejora_activada.insert(1, (Upgrades[mejora[6]])[2])

					if existe == False:
						mejora_activada_new = [mejora[6], (Upgrades[mejora[6]])[2], "2 Disparos: ", Color_Mejora] #[Tipo, tiempo, texto_a_mostrar]
						mejoras_activadas.append(mejora_activada_new)

					if nºdisparos < 2:
						nºdisparos = 2

				elif mejora[6] == 1: #3 Disparos

					for mejora_activada in mejoras_activadas:
						if mejora_activada[0] == mejora[6]:
							existe = True
							mejora_activada.pop(1)
							mejora_activada.insert(1, (Upgrades[mejora[6]])[2])

					if existe == False:
						mejora_activada_new = [mejora[6], (Upgrades[mejora[6]])[2], "3 Disparos: ", Color_Mejora] #[[Upgrade_Image, porcentaje_aparicion sobre 100, tiempo activos], 0]
						mejoras_activadas.append(mejora_activada_new)

					if nºdisparos < 3:
						nºdisparos = 3

				elif mejora[6] == 2: #4 Disparos

					for mejora_activada in mejoras_activadas:
						if mejora_activada[0] == mejora[6]:
							existe = True
							mejora_activada.pop(1)
							mejora_activada.insert(1, (Upgrades[mejora[6]])[2])

					if existe == False:
						mejora_activada_new = [mejora[6], (Upgrades[mejora[6]])[2], "4 Disparos: ", Color_Mejora]
						mejoras_activadas.append(mejora_activada_new)

					if nºdisparos < 4:
						nºdisparos = 4

				elif mejora[6] == 3: #5 Disparos

					for mejora_activada in mejoras_activadas:
						if mejora_activada[0] == mejora[6]:
							existe = True
							mejora_activada.pop(1)
							mejora_activada.insert(1, (Upgrades[mejora[6]])[2])

					if existe == False:
						mejora_activada_new = [mejora[6], (Upgrades[mejora[6]])[2], "5 Disparos: ", Color_Mejora]
						mejoras_activadas.append(mejora_activada_new)

					if nºdisparos < 5:
						nºdisparos = 5

				elif mejora[6] == 4: #x2 velocidad

					for mejora_activada in mejoras_activadas:
						if mejora_activada[0] == mejora[6]:
							existe = True
							mejora_activada.pop(1)
							mejora_activada.insert(1, (Upgrades[mejora[6]])[2])

					if existe == False:
						mejora_activada_new = [mejora[6], (Upgrades[mejora[6]])[2], "Velocidad x2: ", Color_Mejora]
						mejoras_activadas.append(mejora_activada_new)

					if round(tiempo_de_diferencia_entre_disparos_org/2) < tiempo_de_diferencia_entre_disparos:
					
						tiempo_de_diferencia_entre_disparos = round(tiempo_de_diferencia_entre_disparos_org/2)

				elif mejora[6] == 5: #x3 velocidad

					for mejora_activada in mejoras_activadas:
						if mejora_activada[0] == mejora[6]:
							existe = True
							mejora_activada.pop(1)
							mejora_activada.insert(1, (Upgrades[mejora[6]])[2])

					if existe == False:
						mejora_activada_new = [mejora[6], (Upgrades[mejora[6]])[2], "Velocidad x3: ", Color_Mejora]
						mejoras_activadas.append(mejora_activada_new)

					if round(tiempo_de_diferencia_entre_disparos_org/3) < tiempo_de_diferencia_entre_disparos:

						tiempo_de_diferencia_entre_disparos = round(tiempo_de_diferencia_entre_disparos_org/3)

				elif mejora[6] == 6: #x4 velocidad

					for mejora_activada in mejoras_activadas:
						if mejora_activada[0] == mejora[6]:
							existe = True
							mejora_activada.pop(1)
							mejora_activada.insert(1, (Upgrades[mejora[6]])[2])

					if existe == False:
						mejora_activada_new = [mejora[6], (Upgrades[mejora[6]])[2], "Velocidada x4: ", Color_Mejora]
						mejoras_activadas.append(mejora_activada_new)

					tiempo_de_diferencia_entre_disparos = round(tiempo_de_diferencia_entre_disparos_org/4)

				elif mejora[6] == 7: #Escudo
					
					escudo = True
					disparado = True

				elif mejora[6] == 8: #Iman

					for mejora_activada in mejoras_activadas:
						if mejora_activada[0] == mejora[6]:
							existe = True
							mejora_activada.pop(1)
							mejora_activada.insert(1, (Upgrades[mejora[6]])[2])

					if existe == False:
						mejora_activada_new = [mejora[6], (Upgrades[mejora[6]])[2], "Iman: ", Color_Mejora]
						mejoras_activadas.append(mejora_activada_new)

					funcion_imantar = True

				elif mejora[6] == 9: #Recup Vida Se recuperara vida de la parte que menos tenga
					
					vidas_partes = [vida_alaDerecha, vida_alaIzquierda, vida_frontal, vida_motor]

					vidas_partes_org = vidas_partes.copy()

					vidas_partes.sort()

					indice = vidas_partes_org.index(vidas_partes[0])

					#print(vidas_partes, vidas_partes_org, indice)

					if indice == 0: #Ala derecha
						vida_alaDerecha += 5

						if vida_alaDerecha > vida_alaDerecha_org:
							vida_alaDerecha = vida_alaDerecha_org

						alaDerecha = True

						#print(vida_alaDerecha)

					elif indice == 1: #Ala izquierda
						vida_alaIzquierda += 5
						
						if vida_alaIzquierda > vida_alaIzquierda_org:
							vida_alaIzquierda = vida_alaIzquierda_org

						alaIzquierda = True

						#print(vida_alaIzquierda)

					elif indice == 2: #Frontal
						vida_frontal += 5
						
						if vida_frontal > vida_frontal_org:
							vida_frontal = vida_frontal_org

						frontal = True

						#print(vida_frontal)

					elif indice == 3: #Motor
						vida_motor += 5
						
						if vida_motor > vida_motor_org:
							vida_motor = vida_motor_org

						motor = True

						#print(vida_motor)

					tipos_de_vidas = [frontal, motor, alaDerecha, alaIzquierda]

					eleabuscar = []

					for vida in tipos_de_vidas:

						eleabuscar.append(vida)

					try:

						index_Nave_Prin = Data_Prin.index(eleabuscar)
						index_Escudo = Data_Escudos.index(eleabuscar)

					except:
						index_Nave_Prin = 8

					disparado = True

				else:
					print("Mejora no existente: ", mejora[6])

				resultados = actualizar_pantalla_derecha_arriba(ventana, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, med, fpsactivos, infinito, segundostranscurridos, mejoras_activadas)

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

				if resultados[7] != False:

					for mejora_mostrada in resultados[7]: #[Texto, x, y]
						ventana.blit(mejora_mostrada[0], (mejora_mostrada[1], mejora_mostrada[2]))

		for borrado in aborrar:
			ventana.blit(Upgrade_Negra, ((mejoras[borrado])[2], (mejoras[borrado])[3]))
			mejoras.pop(borrado)

		aborrar = []

		for disparo in listdisparos_NA: #Balas amigas contra naves enemigas

			dañada = False

			for nave in naves:

				if nave.posx < disparo[0] and nave.posx + 40 > disparo[0] + 2 and nave.posy < disparo[1] and nave.posy + 22 > disparo[1] and nave.viva == True and dañada == False:

					dañada = True
					puntuacion += 15
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
			txt2_AI, posxytxt2_AI = resultados4[11]
			txt3_AI, posxytxt3_AI = resultados4[12]
			txt4_AI, posxytxt4_AI = resultados4[13]
			txt5_AI, posxytxt5_AI = resultados4[14]
			txt6_AI, posxytxt6_AI = resultados4[15]

			if escudo: ventana.blit(Escudo, (posxControlador - 8, posyControlador - 8))

			caracteristicas = [vida_alaDerecha, vida_alaDerecha_org, vida_alaIzquierda, vida_alaIzquierda_org, vida_motor, vida_motor_org, vida_frontal, vida_frontal_org, alaDerecha, alaIzquierda, motor, frontal]

			if txt1_AI != ["", ""]: ventana.blit(txt1_AI, (posxytxt1_AI[0], posxytxt1_AI[1]))
			if txt2_AI != ["", ""]: ventana.blit(txt2_AI, (posxytxt2_AI[0], posxytxt2_AI[1]))
			if txt3_AI != ["", ""]: ventana.blit(txt3_AI, (posxytxt3_AI[0], posxytxt3_AI[1]))
			if txt4_AI != ["", ""]: ventana.blit(txt4_AI, (posxytxt4_AI[0], posxytxt4_AI[1]))
			if txt5_AI != ["", ""]: ventana.blit(txt5_AI, (posxytxt5_AI[0], posxytxt5_AI[1]))
			if txt6_AI != ["", ""]: ventana.blit(txt6_AI, (posxytxt6_AI[0], posxytxt6_AI[1]))
			ventana.blit(Nave_act_Controlador_De_Daños, (posxControlador, posyControlador))

			tipos_de_vidas = [frontal, motor, alaDerecha, alaIzquierda]

			eleabuscar = []

			for vida in tipos_de_vidas:

				eleabuscar.append(vida)

			try:

				index_Nave_Prin = Data_Prin.index(eleabuscar)
				index_Escudo = Data_Escudos.index(eleabuscar)

			except:
				index_Nave_Prin = 8

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
					salida, reintentar = crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

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

					if nave_a_explotar[2] == "Principal": #Moriste BUEYYY

						pygame.draw.rect(ventana, negro, (posxline1 + tamañoline, 0, 640 - tamañoline - 1, alto))
						pygame.display.update()

						#crear_texto_en_pantalla(ventana, "¡PERDISTE!, este texto es temporal", 2, FPS) #Poner aqui la direccion al la página de perdiste
						
						if infinito == False:
							if boss_activo == True:
								porcentaje_alcanzado_exportar = 80 + (20 - vida_boss_act/5)

							else:
								porcentaje_alcanzado_exportar = round((Naves_destruidas/Nº_Naves)*100)

						else:
							porcentaje_alcanzado_exportar = 0

						porcentaje_Medio_de_vida_exportar = 0

						estado_alaizquierda = 2
						estado_aladerecha = 2
						estado_motor = 2
						estado_frontal = 2

						if escudo == True:
							puntuacion_exportar = puntuacion * 2
							estado_escudo = 0

						else:
							puntuacion_exportar = puntuacion
							estado_escudo = 2

						estado_final_nave = "destruida"

						resultado = "¡Has perdido!"

						# --> NUEVO

						reintentar = ejecutar_pantalla_resultados(ventana, user_act[1], Lv_act, pantalla_act, puntuacion_total, monedas_totales, Naves_destruidas, segundostranscurridos, Monedas, puntuacion_exportar, resultado, Nº_Naves, estado_escudo, estado_alaizquierda, estado_aladerecha, estado_motor, estado_frontal, estado_final_nave, infinito, porcentaje_Medio_de_vida_exportar, porcentaje_alcanzado_exportar)

						victoria = False
			
						Exit_presionado = True
						###AQUI
						break

					else:

						if naves_destruidas_boss >= naves_a_matar[valor - 1] and escudo_desactivado == False:
							escudo_desactivandose = True
							escudo_desactivado = True
							escudo_boss = 0

						resultados = actualizar_pantalla_derecha_arriba(ventana, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, fpsactivos, infinito, segundostranscurridos, mejoras_activadas)

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

						if resultados[7] != False:

							for mejora_mostrada in resultados[7]:
								ventana.blit(mejora_mostrada[0], (mejora_mostrada[1], mejora_mostrada[2]))

				elif nave_a_explotar[3] == 1:

					Naves_destruidas += 1

					if boss_activo == True:
						naves_destruidas_boss += 1
					
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
					salida, reintentar = crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

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

			for mejora_activada in mejoras_activadas:
				tiempo_transcurrido = mejora_activada[1]

				mejora_activada.pop(1)
				mejora_activada.insert(1, tiempo_transcurrido - 1)

			for mejora_activada in mejoras_activadas:  #[Tipo, tiempo, texto_a_mostrar]

				if mejora_activada[1] < 0: #Ha terminado el tiempo de uso

					if mejora_activada[0] == 0: #2 disparos
						max_disp = 1
						for mejorac_activada in mejoras_activadas:

							if mejorac_activada[0] == 3 and max_disp < 5:
								max_disp = 5

							elif mejorac_activada[0] == 2 and max_disp < 4:
								max_disp = 4

							elif mejorac_activada[0] == 1 and max_disp < 3:
								max_disp = 3

						nºdisparos = max_disp

					elif mejora_activada[0] == 1: #3 disparos
						max_disp = 1
						for mejorac_activada in mejoras_activadas:

							if mejorac_activada[0] == 3 and max_disp < 5:
								max_disp = 5

							elif mejorac_activada[0] == 2 and max_disp < 4:
								max_disp = 4

							elif mejorac_activada[0] == 0:
								max_disp = 2

						nºdisparos = max_disp

					elif mejora_activada[0] == 2: #4 disparos
						max_disp = 1
						for mejorac_activada in mejoras_activadas:

							if mejorac_activada[0] == 3 and max_disp < 5:
								max_disp = 5

							elif mejorac_activada[0] == 1 and max_disp < 3:
								max_disp = 3

							elif mejorac_activada[0] == 0:
								max_disp = 2

						nºdisparos = max_disp
					elif mejora_activada[0] == 3: #5 disparos
						max_disp = 1
						for mejorac_activada in mejoras_activadas:

							if mejorac_activada[0] == 2 and max_disp < 4:
								max_disp = 4

							elif mejorac_activada[0] == 1 and max_disp < 3:
								max_disp = 3

							elif mejorac_activada[0] == 0:
								max_disp = 2

						nºdisparos = max_disp

					elif mejora_activada[0] == 4: #x2 velocidad
						max_vel = 1
						for mejorac_activada in mejoras_activadas:

							if mejorac_activada[0] == 6 and max_vel < 4:
								max_vel = 4

							elif mejorac_activada[0] == 5 and max_vel < 3:
								max_vel = 3

						tiempo_de_diferencia_entre_disparos = round(tiempo_de_diferencia_entre_disparos_org/max_vel)

					elif mejora_activada[0] == 5: #x3 velocidad
						max_vel = 1
						for mejorac_activada in mejoras_activadas:

							if mejorac_activada[0] == 6 and max_vel < 4:
								max_vel = 4

							elif mejorac_activada[0] == 4 and max_vel < 3:
								max_vel = 2

						tiempo_de_diferencia_entre_disparos = round(tiempo_de_diferencia_entre_disparos_org/max_vel)

					elif mejora_activada[0] == 6: #x4 velocidad
						max_vel = 1
						for mejorac_activada in mejoras_activadas:

							if mejorac_activada[0] == 5 and max_vel < 4:
								max_vel = 3

							elif mejorac_activada[0] == 4 and max_vel < 3:
								max_vel = 2

						tiempo_de_diferencia_entre_disparos = round(tiempo_de_diferencia_entre_disparos_org/max_vel)

					elif mejora_activada[0] == 8: #iman
						funcion_imantar = False

					elif mejora_activada[0] == 9: #Lentitud Nuclear
						Velocidad_Nave = Velocidad_Nave_Org
						Multiplicador_Velocidad = 0

					elif mejora_activada[0] == 11: #Envenenamiento
						pass

					#Hace lo de que tb aparezxa el efecto de lentitud por exp nucl en este apartado, 

					aborrar.append(mejoras_activadas.index(mejora_activada))
					aborrar.sort()
					aborrar.reverse()

				else: #Cuando aun siguen usandose

					if mejora_activada[0] == 11: #Envenenamiento
						if vida_alaDerecha > 0:
							vida_alaDerecha -= 1

						if vida_alaIzquierda > 0:
							vida_alaIzquierda -= 1

						if vida_motor > 0:
							vida_motor -= 1

						if vida_frontal > 0:
							vida_frontal -= 1

						disparado = True

			for borrado in aborrar:
				mejoras_activadas.pop(borrado)

			aborrar = []


			med = round(math.fsum(fpslist)/len(fpslist))

			fpslist = []

			segundostranscurridos += 1

			resultados = actualizar_pantalla_derecha_arriba(ventana, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, med, fpsactivos, infinito, segundostranscurridos, mejoras_activadas)

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

			if resultados[7] != False:

				for mejora_mostrada in resultados[7]: #[Texto, x, y]
					ventana.blit(mejora_mostrada[0], (mejora_mostrada[1], mejora_mostrada[2]))

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
					salida, reintentar = crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

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
			if escudo == True: ventana.blit(Escudo_Negro, (round(xn) - 2, round(yn) - 2))

			if xn > 330:

				xn -= (450/FPS)*Velocidad_Nave

			ventana.blit(Tipos_De_Naves_Prin[index_Nave_Prin], (round(xn), round(yn)))
			if escudo == True: ventana.blit(Escudos_Nave_Prin[index_Escudo], (round(xn) - 2, round(yn) - 2))

		if tecladerechapress == True and viva == True:

			ventana.blit(NavePrincipalNegro, (round(xn), round(yn)))
			if escudo == True: ventana.blit(Escudo_Negro, (round(xn) - 2, round(yn) - 2))

			if xn < 910:

				xn += (450/FPS)*Velocidad_Nave

			ventana.blit(Tipos_De_Naves_Prin[index_Nave_Prin], (round(xn), round(yn)))
			if escudo == True: ventana.blit(Escudos_Nave_Prin[index_Escudo], (round(xn) - 2, round(yn) - 2))

		if teclaabajopress == True and viva == True:

			ventana.blit(NavePrincipalNegro, (round(xn), round(yn)))
			if escudo == True: ventana.blit(Escudo_Negro, (round(xn) - 2, round(yn) - 2))

			if yn < 688:

				yn += (450/FPS)*Velocidad_Nave

			ventana.blit(Tipos_De_Naves_Prin[index_Nave_Prin], (round(xn), round(yn)))
			if escudo == True: ventana.blit(Escudos_Nave_Prin[index_Escudo], (round(xn) - 2, round(yn) - 2))

		if teclaarribapress == True and viva == True:

			ventana.blit(NavePrincipalNegro, (round(xn), round(yn)))
			if escudo == True: ventana.blit(Escudo_Negro, (round(xn) - 2, round(yn) - 2))

			if yn > 370:

				yn -= (450/FPS)*Velocidad_Nave

			ventana.blit(Tipos_De_Naves_Prin[index_Nave_Prin], (round(xn), round(yn)))
			if escudo == True: ventana.blit(Escudos_Nave_Prin[index_Escudo], (round(xn) - 2, round(yn) - 2))

		if teclaarribapress == False and teclaabajopress == False and tecladerechapress == False and teclaizquierdapress == False and primeravuelta == False and viva == True:

			ventana.blit(NavePrincipalNegro, (round(xn), round(yn)))
			if escudo == True: ventana.blit(Escudo_Negro, (round(xn) - 2, round(yn) - 2))

			if alaDerecha == False or alaIzquierda == False:
				multiplicador = Velocidad_Nave/2.5

			else:
				multiplicador = Velocidad_Nave/5

			if yn < 688:

				yn += (450/FPS)*multiplicador

			ventana.blit(Tipos_De_Naves_Prin[index_Nave_Prin], (round(xn), round(yn)))
			if escudo == True: ventana.blit(Escudos_Nave_Prin[index_Escudo], (round(xn) - 2, round(yn) - 2))

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

					disparoaañadir = [xn + 21, yn, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 2 and dispararya == True:

					disparoaañadir = [xn + 40, yn, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn, yn + 1, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 3 and dispararya == True:

					disparoaañadir = [xn + 40, yn, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn, yn + 1, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 21, yn - 1, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 4 and dispararya == True:

					disparoaañadir = [xn + 40, yn, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn, yn + 1, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 8, yn + 4, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 32, yn + 5, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 5 and dispararya == True:

					disparoaañadir = [xn + 40, yn, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn, yn + 1, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 8, yn + 4, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 32, yn + 5, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 21, yn - 1, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

			elif alaDerecha == False:

				if nºdisparos == 1 and dispararya == True:

					disparoaañadir = [xn + 21, yn, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 2 and dispararya == True:

					disparoaañadir = [xn + 21, yn, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn, yn + 1, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 3 and dispararya == True:

					disparoaañadir = [xn + 21, yn, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn, yn + 1, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 8, yn -1, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 4 and dispararya == True:

					disparoaañadir = [xn + 21, yn, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn, yn + 1, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 8, yn -1, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 5 and dispararya == True:

					disparoaañadir = [xn + 21, yn, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn, yn + 1, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 8, yn -1, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

			elif alaIzquierda == False:

				if nºdisparos == 1 and dispararya == True:

					disparoaañadir = [xn + 21, yn, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 2 and dispararya == True:

					disparoaañadir = [xn + 40, yn, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 21, yn, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 3 and dispararya == True:

					disparoaañadir = [xn + 40, yn, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 32, yn + 5, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 21, yn - 1, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 4 and dispararya == True:

					disparoaañadir = [xn + 40, yn, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 32, yn + 5, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 21, yn - 1, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 5 and dispararya == True:

					disparoaañadir = [xn + 40, yn, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 32, yn + 5, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 21, yn - 1, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

			elif frontal == False:

				if nºdisparos == 1 and dispararya == True:

					disparoaañadir = [xn + 32, yn + 5, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 2 and dispararya == True:

					disparoaañadir = [xn + 32, yn + 5, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 8, yn + 4, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 3 and dispararya == True:

					disparoaañadir = [xn + 40, yn, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 32, yn + 5, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 8, yn + 4, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 4 and dispararya == True:

					disparoaañadir = [xn + 40, yn, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn, yn + 1, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 8, yn + 4, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 32, yn + 5, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

				elif nºdisparos == 5 and dispararya == True:

					disparoaañadir = [xn + 40, yn, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn, yn + 1, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 8, yn + 4, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					disparoaañadir = [xn + 32, yn + 5, disparos[tipodeproyectilamigo], velocidad_de_disparo_amigo]
					listdisparos_NA.append(disparoaañadir)
					dispardoreciene = True
					dispararya = False

		### ACCIONES DE OBJETOS ### ACCIONES DE OBJETOS ### ACCIONES DE OBJETOS ### ACCIONES DE OBJETOS ### ACCIONES DE OBJETOS ###

		if fpsactivos == False and cambioFps == True: #Esconder los FPS
			cambioFps = False

			resultados = actualizar_pantalla_derecha_arriba(ventana, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, False, infinito, segundostranscurridos, mejoras_activadas)

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

			if resultados[7] != False:

				for mejora_mostrada in resultados[7]:
					ventana.blit(mejora_mostrada[0], (mejora_mostrada[1], mejora_mostrada[2]))

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
					salida, reintentar = crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

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

		if boss_activo == False:

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

		if list_naves.count(1) == 0 and Naves_destruidas != Nº_Naves and explotada == True and Exit_presionado == False and boss_activo == False: 

			print("Sig oleada")

			ultimoseventos = []

			if infinito == True:
				Nº_Naves += 20

			for disparo in listdisparos_NA: #Naves amigas
				
				ventana.blit(DisparoNegro, (disparo[0], disparo[1]))

			for disparo in listdisparos_NE: #Naves enemigas

				ventana.blit(DisparosNegros[disparo[4] - 1], (disparo[0], disparo[1]))

			ventana.blit(Barrera_Azul, (320, posybarrera))

			listdisparos_NA = []
			listdisparos_NE = []

			usados = []
			oleada += 1

			naves, list_naves, usados = crear_oleada(ventana, Lv_act, infinito, list_naves, usados, oleada, radio)

			for nave in naves:

				ventana.blit(nave.ImagenNave, (nave.posx, nave.posy))

				time.sleep(0.05)

				pygame.display.update()

			crear_texto_en_pantalla(ventana,"OLEADA Nº" + str(oleada), 0.5, FPS)

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
						salida, reintentar = crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

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

		if list_naves.count(1) == 0 and Naves_destruidas != Nº_Naves and explotada == True and Exit_presionado == False and boss_activo == False: 

			ultimoseventos = []

			if infinito == True:
				Nº_Naves += 20

			for disparo in listdisparos_NA: #Naves amigas
				
				ventana.blit(DisparoNegro, (disparo[0], disparo[1]))

			for disparo in listdisparos_NE: #Naves enemigas

				ventana.blit(DisparosNegros[disparo[4] - 1], (disparo[0], disparo[1]))

			listdisparos_NA = []
			listdisparos_NE = []

			usados = []
			oleada += 1

			naves, list_naves, usados = crear_oleada(ventana, Lv_act, infinito, list_naves, usados, oleada, radio)

			for nave in naves:

				ventana.blit(nave.ImagenNave, (nave.posx, nave.posy))

				time.sleep(0.05)

				pygame.display.update()

			crear_texto_en_pantalla(ventana,"OLEADA Nº" + str(oleada), 0.5, FPS)

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
						salida, reintentar = crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

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

	if salida == False:
		return victoria, reintentar

	else:
		return False, reintentar