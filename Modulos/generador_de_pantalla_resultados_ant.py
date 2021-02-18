"""

Este módulo muestra una pantalla tras una partida para mostrar los resultados.

"""

import pygame, sqlite3, time, math, random

from pygame.locals import *

from Modulos.basededatosnivelesfaciliter import *

from Modulos.generador_de_pantalla_seleccionLv import *

from Modulos.objetos_de_pantalla import *

from Modulos.basededatosnivelesfaciliter import *

def ejecutar_pantalla_resultados(ventana, usuario, nivel, pantalla, PuntuacionTotal, MonedasTotales, NavesDestruidas, Tiempo, MonedasNivel, PuntuacionNivel, Resultado, NavesTotales, Escudo, AlaIzquierda, AlaDerecha, Motor, Frontal, EstadoFinal, infinitopulsado, porcentaje_Medio_de_vida_exportar, porcentaje_alcanzado_exportar):
	"""

	Inclinación de las líneas: por cada 1y, 0,25x

	pygame.draw.line(ventana, colorline, (posxline1_, posyline1_), (posxline2_, posyline2_), tamañoline)

	posxline1_ = 0
	posxline2_ = ancho
	posyline1_ = 0
	posyline2_ = alto

	posxtxt = 0
	posytxt = 0

	def print_pantalla(texto, posx, posy, tamaño, color = (0, 0, 0), fuente = "Default", color_de_fondo = None)
	
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
	gris_claro = (150, 150, 150)
	verde = (0, 255, 0)
	rosa = (255, 0, 188)
	verde_claro = [100, 255, 0]

	colores_seleccion = [blanco, rojo, amarillo, azul, verde, rosa, verde_claro]

	colorline = blanco
	colortxt = blanco
	colorfondo = negro

	tamañoline = round(0.00234375 * ancho)

	tamañotxtE = 70 #ENORMEE
	tamañotxtG = 55 #GRANDE
	tamañotxtM = 40 #MeDiAnO
	tamañotxtP = 25 #pequeño
	tamañotxtD = 15 #diminutoo

	tamañotxt2 = round(0.0234375 * ancho)
	tamañopolygon = round(0.00190625 * ancho)
	errordebotgeneral = round(0.00390625 * ancho)

	pygame.mouse.set_visible(True)

	### ========== POSICIONES DE LAS LÍNEAS ========== ###

	posxline1_arriba = 0
	posxline2_arriba = ancho
	posyline1_arriba = 140
	posyline2_arriba = 140

	posxline1_abajo = 0
	posxline2_abajo = ancho
	posyline1_abajo = 580
	posyline2_abajo = 580

	posxline1_cruzada = 345
	posxline2_cruzada = 455
	posyline1_cruzada = 140
	posyline2_cruzada = 580

	posxline1_pequeñaup = 623
	posxline2_pequeñaup = 683
	posyline1_pequeñaup = 0
	posyline2_pequeñaup = 240

	posxline1_pequeñabajo = 375
	posxline2_pequeñabajo = 410
	posyline1_pequeñabajo = 580
	posyline2_pequeñabajo = alto

	posxline1_titulos = 0
	posxline2_titulos = ancho
	posyline1_titulos = 240
	posyline2_titulos = 240

	posxline1_pequeñabajo2 = 768
	posxline2_pequeñabajo2 = 803
	posyline1_pequeñabajo2 = 580
	posyline2_pequeñabajo2 = alto

	### ========== POSICIONES DE LOS TÍTULOS ========== ###

	posxtxt1 = 30
	posytxt1 = 35

	posxtxt2 = 25
	posytxt2 = 167

	posxtxt3 = 700
	posytxt3 = 167

	posxtxt4 = 700
	posytxt4 = 25
	posxtxt5 = 700
	posytxt5 = 75
	posxtxt6 = 900
	posytxt6 = 75

	posxtxt7 = 25
	posytxt7 = 610
	posxtxt8 = 405
	posytxt8 = 610

	posxtxt9 = 405
	posytxt9 = 250
	posxtxt10 = 422.5
	posytxt10 = 320
	posxtxt11 = 440
	posytxt11 = 390
	posxtxt12 = 457.5
	posytxt12 = 460
	posxtxt13 = 475
	posytxt13 = 530

	posxtxt14 = 25
	posytxt14 = 250
	posxtxt15 = 25
	posytxt15 = 305
	posxtxt16 = 25
	posytxt16 = 360
	posxtxt17 = 25
	posytxt17 = 415
	posxtxt18 = 25
	posytxt18 = 470

	### ========== POSICIONES DE LA INFORMACIÓN ========== ###

	posxtxt19 = 960
	posytxt19 = 25
	posxtxt20 = 800
	posytxt20 = 75
	posxtxt21 = 1045
	posytxt21 = 75

	posxtxt22 = 50
	posytxt22 = 645
	posxtxt23 = 440
	posytxt23 = 645

	posxtxt24 = 605
	posytxt24 = 250
	posxtxt25 = 530
	posytxt25 = 320
	posxtxt26 = 645
	posytxt26 = 395
	posxtxt27 = 680
	posytxt27 = 460
	posxtxt28 = 740
	posytxt28 = 530

	posxtxt29 = 365
	posytxt29 = 157

	posxtxt30 = 50
	posytxt30 = 250
	posxtxt31 = 50
	posytxt31 = 305
	posxtxt32 = 50
	posytxt32 = 360
	posxtxt33 = 50
	posytxt33 = 415
	posxtxt34 = 50
	posytxt34 = 470
	posxtxt35 = 25
	posytxt35 = 525

	def generar_fondo(ventana):

		pygame.draw.line(ventana, colorline, (posxline1_arriba, posyline1_arriba), (posxline2_arriba, posyline2_arriba), tamañoline)
		pygame.draw.line(ventana, colorline, (posxline1_abajo, posyline1_abajo), (posxline2_abajo, posyline2_abajo), tamañoline)
		pygame.draw.line(ventana, colorline, (posxline1_cruzada, posyline1_cruzada), (posxline2_cruzada, posyline2_cruzada), tamañoline)
		pygame.draw.line(ventana, colorline, (posxline1_pequeñaup, posyline1_pequeñaup), (posxline2_pequeñaup, posyline2_pequeñaup), tamañoline)
		pygame.draw.line(ventana, colorline, (posxline1_pequeñabajo, posyline1_pequeñabajo), (posxline2_pequeñabajo, posyline2_pequeñabajo), tamañoline)
		pygame.draw.line(ventana, colorline, (posxline1_titulos, posyline1_titulos), (posxline2_titulos, posyline2_titulos), tamañoline)
		pygame.draw.line(ventana, colorline, (posxline1_pequeñabajo2, posyline1_pequeñabajo2), (posxline2_pequeñabajo2, posyline2_pequeñabajo2), tamañoline)

	def generar_titulos(ventana):
		
		txt1, posxytxt1 = print_pantalla("RESULTADOS", posxtxt1, posytxt1, tamañotxtE, colortxt, fuente)
		txt2, posxytxt2 = print_pantalla("RÉCORDS", posxtxt2, posytxt2, tamañotxtG, colortxt, fuente)
		txt3, posxytxt3 = print_pantalla("INFORMACIÓN", posxtxt3, posytxt3, tamañotxtG, colortxt, fuente)
		txt4, posxytxt4 = print_pantalla("Usuario actual: ", posxtxt4, posytxt4, tamañotxtM, colortxt, fuente) #user_act[1]
		txt5, posxytxt5 = print_pantalla("Nivel", posxtxt5, posytxt5, tamañotxtM, colortxt, fuente) #Lv_act
		txt6, posxytxt6 = print_pantalla("Pantalla", posxtxt6, posytxt6, tamañotxtM, colortxt, fuente) #pantalla_act
		txt7, posxytxt7 = print_pantalla("Puntuación total", posxtxt7, posytxt7, tamañotxtP, colortxt, fuente) #puntuacion_total
		txt8, posxytxt8 = print_pantalla("Monedas totales", posxtxt8, posytxt8, tamañotxtP, colortxt, fuente) #monedas_totales
		txt9, posxytxt9 = print_pantalla("· Naves destruidas:", posxtxt9, posytxt9, tamañotxtP, colortxt, fuente) #Naves_destruidas
		txt10, posxytxt10 = print_pantalla("· Tiempo:", posxtxt10, posytxt10, tamañotxtP, colortxt, fuente) #segundostranscurridos
		txt11, posxytxt11 = print_pantalla("· Estado de la nave:", posxtxt11, posytxt11, tamañotxtP, colortxt, fuente)
		txt12, posxytxt12 = print_pantalla("· Monedas recogidas:", posxtxt12, posytxt12, tamañotxtP, colortxt, fuente) #Monedas
		txt13, posxytxt13 = print_pantalla("PUNTUACIÓN DEL NIVEL:", posxtxt13, posytxt13, tamañotxtP, colortxt, fuente) #puntuacion_exportar
		txt14, posxytxt14 = print_pantalla("1.", posxtxt14, posytxt14, tamañotxtP, colortxt, fuente)
		txt15, posxytxt15 = print_pantalla("2.", posxtxt15, posytxt15, tamañotxtP, colortxt, fuente)
		txt16, posxytxt16 = print_pantalla("3.", posxtxt16, posytxt16, tamañotxtP, colortxt, fuente)
		txt17, posxytxt17 = print_pantalla("4.", posxtxt17, posytxt17, tamañotxtP, colortxt, fuente)
		txt18, posxytxt18 = print_pantalla("5.", posxtxt18, posytxt18, tamañotxtP, colortxt, fuente)

		return((txt1, posxytxt1), (txt2, posxytxt2), (txt3, posxytxt3), (txt4, posxytxt4), (txt5, posxytxt5), (txt6, posxytxt6), (txt7, posxytxt7), (txt8, posxytxt8), (txt9, posxytxt9), (txt10, posxytxt10), (txt11, posxytxt11), (txt12, posxytxt12), (txt13, posxytxt13), (txt14, posxytxt14), (txt15, posxytxt15), (txt16, posxytxt16), (txt17, posxytxt17), (txt18, posxytxt18))

	def generar_informacion(ventana, usuario, nivel, pantalla, PuntuacionTotal, MonedasTotales, NavesDestruidas, Tiempo, MonedasNivel, PuntuacionNivel, Resultado, NavesTotales, Escudo, AlaIzquierda, AlaDerecha, Motor, Frontal, EstadoFinal):

		data_nivel = extraerdatos(usuario, nivel)

		records = [0, 0, 0, 0, 0, 0]

		colorecord1 = colortxt
		colorecord2 = colortxt
		colorecord3 = colortxt
		colorecord4 = colortxt
		colorecord5 = colortxt
		colorecordx = gris_claro

		for data in data_nivel:
			records.append(data[0])

		records.append(PuntuacionNivel)

		records.sort(reverse = True)

		#print(records)

		Record1 = records[0]
		Record1 = str(Record1)
		#print(Record1)
		if records[1] != 0:
			Record2 = records[1]
			Record2 = str(Record2)
			#print(Record2)
			if records[2] != 0:
				Record3 = records[2]
				Record3 = str(Record3)
				#print(Record3)
				if records[3] != 0:
					Record4 = records[3]
					Record4 = str(Record4)
					#print(Record4)
					if records[4] != 0:
						Record5 = records[4]
						Record5 = str(Record5)
						#print(Record5)
						Recordx = "-: -----"
					else:
						Record5 = "-----"
						Recordx = "-: -----"
				else:
					Record4 = "-----"
					Record5 = "-----"
					Recordx = "-: -----"
			else:
				Record3 = "-----"
				Record4 = "-----"
				Record5 = "-----"
				Recordx = "-: -----"
		else:
			Record2 = "-----"
			Record3 = "-----"
			Record4 = "-----"
			Record5 = "-----"
			Recordx = "-: -----"

		i = True

		if records[0] == PuntuacionNivel:
			colorecord1 = amarillo
		elif records[1] == PuntuacionNivel:
			colorecord2 = amarillo
		elif records[2] == PuntuacionNivel:
			colorecord3 = amarillo
		elif records[3] == PuntuacionNivel:
			colorecord4 = amarillo
		elif records[4] == PuntuacionNivel:
			colorecord5 = amarillo
		'''else:
			for elemento in records:
				if i == True:
					if elemento == PuntuacionNivel:
						PuntuacionNivelStr = str(PuntuacionNivel)
						recordx = "-:"+PuntuacionNivelStr
						colorecordx = amarillo
						i = False'''

		if EstadoFinal == "destruida":
			EstadoFinalNave = "Nave destruida"

		else:
			if AlaIzquierda == 1 or AlaIzquierda == 2 or AlaDerecha == 1 or AlaDerecha == 2 or Motor == 1 or Motor == 2 or Frontal == 1 or Frontal == 2:
				if Escudo == 0:
					EstadoFinalNave = "Con escudo"

				else:
					EstadoFinalNave = "Sin escudo"
					
				if AlaIzquierda == 1:
					EstadoFinalNave = EstadoFinalNave+", Ala izquierda dañada"

				elif AlaIzquierda == 2:
					EstadoFinalNave = EstadoFinalNave+", Ala izquierda destruida"

				if AlaDerecha == 1:
					EstadoFinalNave = EstadoFinalNave+", Ala derecha dañada"

				elif AlaDerecha == 2:
					EstadoFinalNave = EstadoFinalNave+", Ala derecha destruida"

				if Motor == 1:
					EstadoFinalNave = EstadoFinalNave+", Motor dañado"

				elif Motor == 2:
					EstadoFinalNave = EstadoFinalNave+", Motor destruido"

				if Frontal == 1:
					EstadoFinalNave = EstadoFinalNave+", Parte frontal dañada"

				elif Frontal == 2:
					EstadoFinalNave = EstadoFinalNave+", Parte frontal destruida"

			else:
				if Escudo == 0:
					EstadoFinalNave = "Con escudo"

				else:
					EstadoFinalNave = "Sin escudo"

		EstadoFinalNave = EstadoFinalNave+"."

		Minutos = int(Tiempo/60)
		Segundos = int(Tiempo%60)

		txt19, posxytxt19 = print_pantalla(usuario, posxtxt19, posytxt19, tamañotxtM, colortxt, fuente)
		txt20, posxytxt20 = print_pantalla(str(nivel), posxtxt20, posytxt20, tamañotxtM, colortxt, fuente)
		txt21, posxytxt21 = print_pantalla(str(pantalla), posxtxt21, posytxt21, tamañotxtM, colortxt, fuente)
		txt22, posxytxt22 = print_pantalla(str(PuntuacionTotal), posxtxt22, posytxt22, tamañotxtM, colortxt, fuente)
		txt23, posxytxt23 = print_pantalla(str(MonedasTotales + MonedasNivel), posxtxt23, posytxt23, tamañotxtM, colortxt, fuente)
		txt24, posxytxt24 = print_pantalla(str(NavesDestruidas) + " de " + str(NavesTotales), posxtxt24, posytxt24, tamañotxtP, colortxt, fuente)
		txt25, posxytxt25 = print_pantalla(str(Minutos) + " minuto(s) y " + str(Segundos) + " segundo(s)", posxtxt25, posytxt25, tamañotxtP, colortxt, fuente)
		txt26, posxytxt26 = print_pantalla(EstadoFinalNave, posxtxt26, posytxt26, tamañotxtD, colortxt, fuente)
		txt27, posxytxt27 = print_pantalla(str(MonedasNivel), posxtxt27, posytxt27, tamañotxtP, colortxt, fuente)
		txt28, posxytxt28 = print_pantalla(str(PuntuacionNivel), posxtxt28, posytxt28, tamañotxtP, colortxt, fuente)
		txt29, posxytxt29 = print_pantalla(Resultado, posxtxt29, posytxt29, tamañotxtG, colortxt, fuente)
		txt30, posxytxt30 = print_pantalla(Record1, posxtxt30, posytxt30, tamañotxtP, colorecord1, fuente)
		txt31, posxytxt31 = print_pantalla(Record2, posxtxt31, posytxt31, tamañotxtP, colorecord2, fuente)
		txt32, posxytxt32 = print_pantalla(Record3, posxtxt32, posytxt32, tamañotxtP, colorecord3, fuente)
		txt33, posxytxt33 = print_pantalla(Record4, posxtxt33, posytxt33, tamañotxtP, colorecord4, fuente)
		txt34, posxytxt34 = print_pantalla(Record5, posxtxt34, posytxt34, tamañotxtP, colorecord5, fuente)
		'''txt35, posxytxt35 = print_pantalla(Recordx, posxtxt35, posytxt35, tamañotxtP, colorecordx, fuente)'''

		return((txt19, posxytxt19), (txt20, posxytxt20), (txt21, posxytxt21), (txt22, posxytxt22), (txt23, posxytxt23), (txt24, posxytxt24), (txt25, posxytxt25), (txt26, posxytxt26), (txt27, posxytxt27), (txt28, posxytxt28), (txt29, posxytxt29), (txt30, posxytxt30), (txt31, posxytxt31), (txt32, posxytxt32), (txt33, posxytxt33), (txt34, posxytxt34))

	ventana.fill(negro)

	generar_fondo(ventana)

	output1 = generar_titulos(ventana)

	txt1, posxytxt1 = output1[0]
	txt2, posxytxt2 = output1[1]
	txt3, posxytxt3 = output1[2]
	txt4, posxytxt4 = output1[3]
	txt5, posxytxt5 = output1[4]
	txt6, posxytxt6 = output1[5]
	txt7, posxytxt7 = output1[6]
	txt8, posxytxt8 = output1[7]
	txt9, posxytxt9 = output1[8]
	txt10, posxytxt10 = output1[9]
	txt11, posxytxt11 = output1[10]
	txt12, posxytxt12 = output1[11]
	txt13, posxytxt13 = output1[12]
	txt14, posxytxt14 = output1[13]
	txt15, posxytxt15 = output1[14]
	txt16, posxytxt16 = output1[15]
	txt17, posxytxt17 = output1[16]
	txt18, posxytxt18 = output1[17]

	output2 = generar_informacion(ventana, usuario, nivel, pantalla, PuntuacionTotal, MonedasTotales, NavesDestruidas, Tiempo, MonedasNivel, PuntuacionNivel, Resultado, NavesTotales, Escudo, AlaIzquierda, AlaDerecha, Motor, Frontal, EstadoFinal)

	txt19, posxytxt19 = output2[0]
	txt20, posxytxt20 = output2[1]
	txt21, posxytxt21 = output2[2]
	txt22, posxytxt22 = output2[3]
	txt23, posxytxt23 = output2[4]
	txt24, posxytxt24 = output2[5]
	txt25, posxytxt25 = output2[6]
	txt26, posxytxt26 = output2[7]
	txt27, posxytxt27 = output2[8]
	txt28, posxytxt28 = output2[9]
	txt29, posxytxt29 = output2[10]
	txt30, posxytxt30 = output2[11]
	txt31, posxytxt31 = output2[12]
	txt32, posxytxt32 = output2[13]
	txt33, posxytxt33 = output2[14]
	txt34, posxytxt34 = output2[15]
	'''txt35, posxytxt35 = outputi[16]'''

	if txt1 != ["", ""]: ventana.blit(txt1, (posxytxt1[0], posxytxt1[1]))
	if txt2 != ["", ""]: ventana.blit(txt2, (posxytxt2[0], posxytxt2[1]))
	if txt3 != ["", ""]: ventana.blit(txt3, (posxytxt3[0], posxytxt3[1]))
	if txt4 != ["", ""]: ventana.blit(txt4, (posxytxt4[0], posxytxt4[1]))
	if txt5 != ["", ""]: ventana.blit(txt5, (posxytxt5[0], posxytxt5[1]))
	if txt6 != ["", ""]: ventana.blit(txt6, (posxytxt6[0], posxytxt6[1]))
	if txt7 != ["", ""]: ventana.blit(txt7, (posxytxt7[0], posxytxt7[1]))
	if txt8 != ["", ""]: ventana.blit(txt8, (posxytxt8[0], posxytxt8[1]))
	if txt9 != ["", ""]: ventana.blit(txt9, (posxytxt9[0], posxytxt9[1]))
	if txt10 != ["", ""]: ventana.blit(txt10, (posxytxt10[0], posxytxt10[1]))
	if txt11 != ["", ""]: ventana.blit(txt11, (posxytxt11[0], posxytxt11[1]))
	if txt12 != ["", ""]: ventana.blit(txt12, (posxytxt12[0], posxytxt12[1]))
	if txt13 != ["", ""]: ventana.blit(txt13, (posxytxt13[0], posxytxt13[1]))
	if txt14 != ["", ""]: ventana.blit(txt14, (posxytxt14[0], posxytxt14[1]))
	if txt15 != ["", ""]: ventana.blit(txt15, (posxytxt15[0], posxytxt15[1]))
	if txt16 != ["", ""]: ventana.blit(txt16, (posxytxt16[0], posxytxt16[1]))
	if txt17 != ["", ""]: ventana.blit(txt17, (posxytxt17[0], posxytxt17[1]))
	if txt18 != ["", ""]: ventana.blit(txt18, (posxytxt18[0], posxytxt18[1]))
	if txt19 != ["", ""]: ventana.blit(txt19, (posxytxt19[0], posxytxt19[1]))
	if txt20 != ["", ""]: ventana.blit(txt20, (posxytxt20[0], posxytxt20[1]))
	if txt21 != ["", ""]: ventana.blit(txt21, (posxytxt21[0], posxytxt21[1]))
	if txt22 != ["", ""]: ventana.blit(txt22, (posxytxt22[0], posxytxt22[1]))
	if txt23 != ["", ""]: ventana.blit(txt23, (posxytxt23[0], posxytxt23[1]))
	if txt24 != ["", ""]: ventana.blit(txt24, (posxytxt24[0], posxytxt24[1]))
	if txt25 != ["", ""]: ventana.blit(txt25, (posxytxt25[0], posxytxt25[1]))
	if txt26 != ["", ""]: ventana.blit(txt26, (posxytxt26[0], posxytxt26[1]))
	if txt27 != ["", ""]: ventana.blit(txt27, (posxytxt27[0], posxytxt27[1]))
	if txt28 != ["", ""]: ventana.blit(txt28, (posxytxt28[0], posxytxt28[1]))
	if txt29 != ["", ""]: ventana.blit(txt29, (posxytxt29[0], posxytxt29[1]))
	if txt30 != ["", ""]: ventana.blit(txt30, (posxytxt30[0], posxytxt30[1]))
	if txt31 != ["", ""]: ventana.blit(txt31, (posxytxt31[0], posxytxt31[1]))
	if txt32 != ["", ""]: ventana.blit(txt32, (posxytxt32[0], posxytxt32[1]))
	if txt33 != ["", ""]: ventana.blit(txt33, (posxytxt33[0], posxytxt33[1]))
	if txt34 != ["", ""]: ventana.blit(txt34, (posxytxt34[0], posxytxt34[1]))
	'''if txt35 != ["", ""]: ventana.blit(txt35, (posxytxt35[0], posxytxt35[1]))'''

	pygame.display.update()

	bot1 = crear_boton3(ventana, 860, 600, 925, 630, "Salir", tamañotxt2, tamañopolygon, errordebotgeneral, blanco, fuente, blanco)
	posesxybot1, posesxy2bot1 = bot1[1]
	bot2 = crear_boton3(ventana, 860, 640, 1000, 670, "Reintentar", tamañotxt2, tamañopolygon, errordebotgeneral, blanco, fuente, blanco)
	posesxybot2, posesxy2bot2 = bot2[1]
	bot3 = crear_boton3(ventana, 860, 600, 925, 630, "Salir", tamañotxt2, tamañopolygon, errordebotgeneral, gris_fondo, fuente, gris_fondo)
	posesxybot3, posesxy2bot3 = bot3[1]
	bot4 = crear_boton3(ventana, 860, 640, 1000, 670, "Reintentar", tamañotxt2, tamañopolygon, errordebotgeneral, gris_fondo, fuente, gris_fondo)
	posesxybot4, posesxy2bot4 = bot4[1]

	terminado = False

	Bucle_Terminado = False

	Reintentar = False

	while Bucle_Terminado == False:

		ratonx, ratony = pygame.mouse.get_pos()

		for evento in pygame.event.get():

			if bot1 != ["", ""] and ratonx > posesxybot1[0] and ratony > posesxybot1[1] and ratonx < posesxy2bot1[0] and ratony < posesxy2bot1[1]:

				if evento.type == MOUSEBUTTONDOWN:

					Bucle_Terminado = True

			elif bot2 != ["", ""] and ratonx > posesxybot2[0] and ratony > posesxybot2[1] and ratonx < posesxy2bot2[0] and ratony < posesxy2bot2[1]:

				if evento.type == MOUSEBUTTONDOWN:

					Bucle_Terminado = True
					Reintentar = True

		if terminado == False:
			
			ventana.blit(bot3[0], (posesxybot3[0], posesxybot3[1]))
			ventana.blit(bot4[0], (posesxybot4[0], posesxybot4[1]))
			pygame.display.update()

			if infinitopulsado == True:
				insertardatosniveles((PuntuacionNivel, NavesDestruidas, porcentaje_alcanzado_exportar, porcentaje_Medio_de_vida_exportar, Tiempo), usuario, nivel + 25)
				ordenardbniveles(usuario, nivel + 25)

			else:
				insertardatosniveles((PuntuacionNivel, NavesDestruidas, porcentaje_alcanzado_exportar, porcentaje_Medio_de_vida_exportar, Tiempo), usuario, nivel)
				ordenardbniveles(usuario, nivel)

			"""data_niveles = []

			toca = 1

			while toca < 31:

				data_nivel = extraerdatos(usuario, toca)

				data_niveles.append(data_nivel)

				toca += 1"""

			ultimoidentificador = ultimoident("Records", "monedas")

			datos_a_insertar_monedas = (usuario, MonedasNivel, ultimoidentificador +1)

			insertardatos("Records", datos_a_insertar_monedas, "Datos insertados correctamente", "Hubo un error al insertar los datos", "monedas")		

			terminado = True

			ventana.blit(bot1[0], (posesxybot1[0], posesxybot1[1]))
			ventana.blit(bot2[0], (posesxybot2[0], posesxybot2[1]))
			pygame.display.update()

	return Reintentar