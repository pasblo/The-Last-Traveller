import pygame

from Modulos.basededatosmejorasfaciliter import *

from Modulos.generador_de_pantalla_seleccionLv import *

def EjecutarTienda(ventana, user_act):

	### ========== DATOS ========== ###

	monedas = obtenerdato("Records", "monedas", user_act[1], 0)

	datos_nave_prin_alpha = extraerdatosmejoras(user_act[1])# [Proteccion, Daño, Velocidad, Escudo]

	datos_nave_prin = list(datos_nave_prin_alpha[0])

	#print(datos_nave_prin)

	### ========== AJUSTES ========== ###

	ajustes = extraer_ajustes()

	ancho = int(ajustes[0])
	alto = int(ajustes[1])
	fuente = ajustes[3]

	vol_general = int(ajustes[4])
	vol_efectos = int(ajustes[5])
	vol_musica = int(ajustes[6])

	### ========== COLORES ========== ###

	blanco = (255, 255, 255)
	negro = (0, 0, 0)
	gris = (200, 200, 200)
	rojo = (255, 0, 0)
	verde = (0, 255, 0)

	### ========== TAMAÑOS ========== ###

	tamañotxt1 = round(0.03906 * ancho)
	tamañotxtgeneral = round(0.0234375 * ancho)
	tamañotxt2 = 20
	tamañopolygon = round(0.00190625 * ancho)
	tamañoline = round(0.00190625 * ancho) #Caracteristicas generales de las lineas

	tamañoxrecuadro = 320
	tamañoyrecuadro = 120

	### ========== POSICIONES ========== ###

	posxtxt1 = round(0.0078125 * ancho)
	posytxt1 = round(0.0078125 * alto)

	posxtxt2 = 200
	posytxt2 = round(0.0078125 * alto)

	posxtxt3 = 900
	posytxt3 = round(0.0078125 * alto)

	posxline4 = 320
	posxline5 = 640
	posxline6 = 960

	posyline7 = 180
	posyline8 = 300
	posyline9 = 420
	posyline10 = 540
	posyline11 = 660

	posxtxt7 = 640
	posytxt7 = 683
	errordebotat = round(0.00390625 * ancho)

	posx1botsalida = round(0.015625 * ancho)
	posy1botsalida = round(0.9305555 * alto)
	posx2botsalida = round(0.234375 * ancho)
	posy2botsalida = round(0.9722222 * alto)

	### ========== LINEAS ========== ###

	posyline1 = round(0.08333333 * alto) #Caracteristicas de linea 1

	posxline2 = 190

	posxline3 = 890

	### ========== SE CREAN LAS FUNCIONES ========= ###

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

	def generarfondo():
		pygame.draw.line(ventana, blanco, (0, posyline1), (ancho, posyline1), tamañoline)
		pygame.draw.line(ventana, blanco, (posxline2, 0), (posxline2, posyline1), tamañoline)
		pygame.draw.line(ventana, blanco, (posxline3, 0), (posxline3, posyline1), tamañoline)

		pygame.draw.line(ventana, negro, (posxline4, posyline1 + tamañoline), (posxline4, alto), tamañoline)
		pygame.draw.line(ventana, negro, (posxline5, posyline1 + tamañoline), (posxline5, alto), tamañoline)
		pygame.draw.line(ventana, negro, (posxline6, posyline1 + tamañoline), (posxline6, alto), tamañoline)

		pygame.draw.line(ventana, negro, (0, posyline7), (ancho, posyline7), tamañoline)
		pygame.draw.line(ventana, negro, (0, posyline8), (ancho, posyline8), tamañoline)
		pygame.draw.line(ventana, negro, (0, posyline9), (ancho, posyline9), tamañoline)
		pygame.draw.line(ventana, negro, (0, posyline10), (ancho, posyline10), tamañoline)
		pygame.draw.line(ventana, negro, (0, posyline11), (ancho, posyline11), tamañoline)

	def generar_compras():

		ultimo_dato = len(datos_nave_prin) - 1
		Linea = 0

		txts4 = []
		txts5 = []
		txts6 = []
		recuadros = []

		for dato in datos_nave_prin:

			#print(datos_nave_prin, dato, ultimo_dato)

			Linea = 0

			if datos_nave_prin.index(dato) < ultimo_dato:

				Coste = (Compras_Orden[datos_nave_prin.index(dato)])[0]
				Niveles = (Compras_Orden[datos_nave_prin.index(dato)])[1]
				Total = (Compras_Orden[datos_nave_prin.index(dato)])[2]
				Texto = (Compras_Orden[datos_nave_prin.index(dato)])[3]

				#print(Coste, Niveles, Total, Texto)

				#print(Coste, Niveles, Total, Texto)

				try:
					Nivel_Compra = Niveles.index(dato) + 1

				except:
					Nivel_Compra = 0

				#print(Nivel_Compra)

				if Nivel_Compra == Total: #Nivel maximo conseguido

					Texto_Arriba = str(Texto) + str(dato)
					Texto_Enmedio = "Nivel: " + str(Total)
					Texto_Abajo = "Coste: None"
					color = gris

				elif Total == 1 and dato == Total: #Nivel maximo conseguido en mejoras de solo 1 compra

					Texto_Arriba = str(Texto) + "True"
					Texto_Enmedio = "Nivel: " + str(Total)
					Texto_Abajo = "Coste: None"
					color = gris

				else: # Aun qudan niveles por desbloquear

					try:
						Coste_act = Coste[Nivel_Compra]
						Niveles_act = Niveles[Nivel_Compra]

					except: #Es una compra de un solo objeto
						Coste_act = Coste
						Niveles_act = Niveles

					if Total == 1:
						Texto_Arriba = str(Texto) + "False"

					else:
						Texto_Arriba = str(Texto) + str(dato)

					Texto_Enmedio = "Nivel: " + str(Nivel_Compra)
					Texto_Abajo = "Coste: " + str(Coste_act)

					if Coste_act <= monedas[1]:
						color = verde

					else:
						color = rojo

				Numero_Recuadro = datos_nave_prin.index(dato)

				posxrecuadro = 320 * Numero_Recuadro

				if posxrecuadro >= 1280: #Sig Linea
					Linea += 1
					posxrecuadro = 320 * (Numero_Recuadro - Linea*4)

				posyrecuadro = Linea * 120 + 60

				pygame.draw.rect(ventana, color, (posxrecuadro, posyrecuadro, tamañoxrecuadro, tamañoyrecuadro))

				posxtextoarriba = posxrecuadro + (tamañoxrecuadro - calcularx(Texto_Arriba))/2
				posytextoarriba = posyrecuadro + 10

				posxtextoenmedio = posxrecuadro + (tamañoxrecuadro - calcularx(Texto_Enmedio))/2
				posytextoenmedio = posyrecuadro + (tamañoyrecuadro - tamañotxtgeneral)/2

				posxtextoabajo = posxrecuadro + (tamañoxrecuadro - calcularx(Texto_Abajo))/2
				posytextoabajo = posyrecuadro + tamañoyrecuadro - 10 - tamañotxtgeneral

				txt4 = print_pantalla(Texto_Arriba, posxtextoarriba, posytextoarriba, tamañotxtgeneral, negro, fuente)
				txt5 = print_pantalla(Texto_Enmedio, posxtextoenmedio, posytextoenmedio, tamañotxtgeneral, negro, fuente)
				txt6 = print_pantalla(Texto_Abajo, posxtextoabajo, posytextoabajo, tamañotxtgeneral, negro, fuente)

				txts4.append(txt4)
				txts5.append(txt5)
				txts6.append(txt6)

				recuadro_act = [posxrecuadro, posyrecuadro, posxrecuadro + tamañoxrecuadro, posyrecuadro + tamañoyrecuadro, Numero_Recuadro]

				#print(recuadro_act)

				recuadros.append(recuadro_act)

		return(txts4, txts5, txts6, recuadros)

	### ========== SE CREA LA PANTALLA ========== ###

	ventana.fill(negro)

	txt1, posxytxt1 = print_pantalla("Tienda:", posxtxt1, posytxt1, tamañotxt1, blanco, fuente)

	txt2, posxytxt2 = print_pantalla("Usuario: " + str(user_act[1]), posxtxt2, posytxt2, tamañotxt1, blanco, fuente)

	txt3, posxytxt3 = print_pantalla("Monedas: " + str(monedas[1]), posxtxt3, posytxt3, tamañotxt1, blanco, fuente)

	txt7, posxytxt7 = print_pantalla("Pulsa en el recuadro de cada mejora para subirla al siguiente nivel", posxtxt7, posytxt7, tamañotxt2, blanco, fuente)

	botsalida = crear_boton3(ventana, posx1botsalida, posy1botsalida, posx2botsalida, posy2botsalida, "<-- Pantalla anterior", tamañotxtgeneral, tamañopolygon, errordebotat, blanco, fuente, blanco)

	posesxybotsalida, posesxy2botsalida = botsalida[1]

	### ========== VARIABLES ========== ###

	Exit_Presionado = False

	Proteccion_Coste = [10, 20, 30, 50, 80, 150, 230, 300, 450, 700]

	Proteccion_Niveles = [15, 20, 25, 30, 35, 40, 45, 50, 55, 65] #10

	Daño_Coste = [15, 30, 50, 90, 150, 220, 290, 400, 580, 850]

	Daño_Niveles = [8, 11, 13, 16, 19, 26, 32, 39, 48, 60] # 5

	Velocidad_Coste = [15, 35, 60, 100, 180, 240, 320, 440, 600, 900]

	Velocidad_Niveles = [0.525, 0.55, 0.575, 0.6, 0.625, 0.65, 0.675, 0.7, 0.75, 0.8] #0.5

	Escudo_Coste = 1000

	Aparicion_Disparo_Coste = [100, 300, 800, 1500, 3000]

	Aparicion_Disparo_Niveles = [440000, 430000, 420000, 410000, 400000]

	Velocidad_Disparo_Coste = [20, 80, 120, 190, 280, 400, 550, 750, 1000, 1500]

	Velocidad_Disparo_Niveles = [1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5]

	Compras_Orden = [[Proteccion_Coste, Proteccion_Niveles, 10, "Proteccion: "], [Daño_Coste, Daño_Niveles, 10, "Daño: "], [Velocidad_Coste, Velocidad_Niveles, 10, "Velocidad: "], [Escudo_Coste, 0, 1, "Escudo: "], [Aparicion_Disparo_Coste, Aparicion_Disparo_Niveles, 5, "Frecuencia disp: "], [Velocidad_Disparo_Coste, Velocidad_Disparo_Niveles, 10, "Velocidad disparos: "]]

	### ========== SE LLAMAN A LAS FUNCIONES ========== ###

	valores = generar_compras()

	txts4 = valores[0]
	txts5 = valores[1]
	txts6 = valores[2]
	recuadros = valores[3]

	generarfondo()

	### ========== SE ACTUALIZA POR PRIMERA VEZ LA PANTALLA ========== ###

	ventana.blit(txt1, posxytxt1)
	ventana.blit(txt2, posxytxt2)
	ventana.blit(txt3, posxytxt3)
	ventana.blit(txt7, posxytxt7)

	for txt4 in txts4:
		ventana.blit(txt4[0], txt4[1])

	for txt5 in txts5:
		ventana.blit(txt5[0], txt5[1])

	for txt6 in txts6:
		ventana.blit(txt6[0], txt6[1])

	ventana.blit(botsalida[0], (posesxybotsalida[0], posesxybotsalida[1]))

	pygame.display.update()

	### ========== BUCLE PRINCIPAL ========== ###

	while Exit_Presionado == False:

		for evento in pygame.event.get():

			ratonx, ratony = pygame.mouse.get_pos()

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

			elif evento.type == MOUSEBUTTONDOWN:

				salir = False

				while salir == False:

					for evento in pygame.event.get():
						if evento.type == MOUSEBUTTONUP:
							salir = True

				if ratonx > posx1botsalida and ratony > posy1botsalida and ratonx < posx2botsalida and ratony < posy2botsalida:
					print("Presionado")
					Exit_Presionado = True

				for recuadro in recuadros:

					if ratonx > recuadro[0] and ratony > recuadro[1] and ratonx < recuadro[2] and ratony < recuadro[3]:

							print("Pulsado boton: " + str(recuadro[4]))

							Coste = (Compras_Orden[recuadro[4]])[0]
							Niveles = (Compras_Orden[recuadro[4]])[1]
							Total = (Compras_Orden[recuadro[4]])[2]

							try:
								Nivel_Compra = Niveles.index(datos_nave_prin[recuadro[4]]) + 1

							except:
								Nivel_Compra = 0

							if Nivel_Compra == Total or Total == Niveles: #Nivel maximo conseguido
								pass
								
							else: # Aun qudan niveles por desbloquear

								try:

									Coste_act = Coste[Nivel_Compra]

								except:
									Coste_act = Coste

								if Coste_act <= monedas[1]:

									ultimoidentificador = ultimoident("Records", "monedas")

									datos_a_insertar_monedas = (user_act[1], Coste_act, ultimoidentificador +1)

									insertardatos("Records", datos_a_insertar_monedas, "Datos insertados correctamente", "Hubo un error al insertar los datos", "monedas", True)

									if recuadro[4] == 0:
										datos_a_intercambiar = [Niveles[Nivel_Compra], datos_nave_prin[1], datos_nave_prin[2], datos_nave_prin[3], datos_nave_prin[4], datos_nave_prin[5], 1]

									elif recuadro[4] == 1:
										datos_a_intercambiar = [datos_nave_prin[0], Niveles[Nivel_Compra], datos_nave_prin[2], datos_nave_prin[3], datos_nave_prin[4], datos_nave_prin[5], 1]

									elif recuadro[4] == 2:
										datos_a_intercambiar = [datos_nave_prin[0], datos_nave_prin[1], Niveles[Nivel_Compra], datos_nave_prin[3], datos_nave_prin[4], datos_nave_prin[5], 1]

									elif recuadro[4] == 3:
										datos_a_intercambiar = [datos_nave_prin[0], datos_nave_prin[1], datos_nave_prin[2], 1, datos_nave_prin[4], datos_nave_prin[5], 1]

									elif recuadro[4] == 4:
										datos_a_intercambiar = [datos_nave_prin[0], datos_nave_prin[1], datos_nave_prin[2], datos_nave_prin[3], Niveles[Nivel_Compra], datos_nave_prin[5], 1]

									elif recuadro[4] == 5:
										datos_a_intercambiar = [datos_nave_prin[0], datos_nave_prin[1], datos_nave_prin[2], datos_nave_prin[3], datos_nave_prin[4], Niveles[Nivel_Compra], 1]
									
									intercambiardatosmejoras(user_act[1], datos_a_intercambiar)

									monedas = obtenerdato("Records", "monedas", user_act[1], 0)

									datos_nave_prin_alpha = extraerdatosmejoras(user_act[1])# [Proteccion, Daño, Velocidad, Escudo]

									datos_nave_prin = list(datos_nave_prin_alpha[0])

									ventana.fill(negro)

									valores = generar_compras()

									txts4 = valores[0]
									txts5 = valores[1]
									txts6 = valores[2]
									recuadros = valores[3]

									generarfondo()

									txt1, posxytxt1 = print_pantalla("Tienda:", posxtxt1, posytxt1, tamañotxt1, blanco, fuente)

									txt2, posxytxt2 = print_pantalla("Usuario: " + str(user_act[1]), posxtxt2, posytxt2, tamañotxt1, blanco, fuente)

									txt3, posxytxt3 = print_pantalla("Monedas: " + str(monedas[1]), posxtxt3, posytxt3, tamañotxt1, blanco, fuente)

									txt7, posxytxt7 = print_pantalla("Pulsa en el recuadro de cada mejora para subirla al siguiente nivel", posxtxt7, posytxt7, tamañotxt2, blanco, fuente)

									botsalida = crear_boton3(ventana, posx1botsalida, posy1botsalida, posx2botsalida, posy2botsalida, "<-- Pantalla anterior", tamañotxtgeneral, tamañopolygon, errordebotat, blanco, fuente, blanco)

									posesxybotsalida, posesxy2botsalida = botsalida[1]

									ventana.blit(txt1, posxytxt1)
									ventana.blit(txt2, posxytxt2)
									ventana.blit(txt3, posxytxt3)
									ventana.blit(txt7, posxytxt7)

									for txt4 in txts4:
										ventana.blit(txt4[0], txt4[1])

									for txt5 in txts5:
										ventana.blit(txt5[0], txt5[1])

									for txt6 in txts6:
										ventana.blit(txt6[0], txt6[1])

									ventana.blit(botsalida[0], (posesxybotsalida[0], posesxybotsalida[1]))

									pygame.display.update()

		pygame.display.update()