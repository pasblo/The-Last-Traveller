import pygame

from Modulos.basededatosajustesfaciliter import *

from datetime import datetime

from Modulos.objetos_de_pantalla import *

from pygame.locals import *

def crearrecuadroemergente(ventana, fpsactivos, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, Mostrar):

	pygame.mouse.set_visible(True)

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

	posx1rect = round(0.3125 * ancho)
	posy1rect = round(0.33333333333333333333333333333333 * alto)
	posx2rect = round(0.6875 * ancho)
	posy2rect = round(0.66666666666666666666666666666667 * alto)

	posytxt_derecha_ariba = round(0.03472222222222222222222222222222 * alto)

	tamañoline = round(0.00234375 * ancho)
	tamañotxt1 = round(0.0234375 * ancho)

	posxline1 = round(0.25 * ancho)

	posy2rec1 = round(0.5 * alto)

	posx1bot2 = round(0.359375 * ancho)#460
	posy1bot2 = round(0.48611111111111111111111111111111 * alto)#412, 350
	posx2bot2 = round(0.640625 * ancho)#820
	posy2bot2 = round(0.52222222222222222222222222222222 * alto)#438, 376

	posx1bot3 = round(0.359375 * ancho)#460
	posy1bot3 = round(0.53611111111111111111111111111111 * alto)#364, 386
	posx2bot3 = round(0.640625 * ancho)#820
	posy2bot3 = round(0.57222222222222222222222222222222 * alto)#390, 412

	posx1bot4 = round(0.359375 * ancho)#460
	posy1bot4 = round(0.58611111111111111111111111111111 * alto)#422
	posx2bot4 = round(0.640625 * ancho)#820
	posy2bot4 = round(0.62222222222222222222222222222222 * alto)#448
	#Se llevan 26
	colortxt = blanco

	diferencia = round(0.0078125 * ancho)

	def actualizar_pantalla_derecha_arriba(ventana, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, Mostrar):

		pygame.draw.rect(ventana, negro, (0, 0, posxline1 - tamañoline + round(0.0015625 * ancho), posy2rec1 - tamañoline + round(0.0015625 * ancho)))

		txt1_AD, posxytxt1_AD = print_pantalla("Nivel: " + str(Lv_act), 0, posytxt_derecha_ariba * 0, tamañotxt1, colortxt, fuente)
		txt2_AD, posxytxt2_AD = print_pantalla("Porcentaje: " + str(porcentaje) + "%", 0, posytxt_derecha_ariba * 1, tamañotxt1, colortxt, fuente)
		txt3_AD, posxytxt3_AD = print_pantalla("Naves destruidas: " + str(Naves_destruidas), 0, posytxt_derecha_ariba * 2, tamañotxt1, colortxt, fuente)
		txt4_AD, posxytxt4_AD = print_pantalla("Naves totales: " + str(Nº_Naves), 0, posytxt_derecha_ariba * 3, tamañotxt1, colortxt, fuente)
		txt5_AD, posxytxt5_AD = print_pantalla("Monedas recogidas: " + str(Monedas), 0, posytxt_derecha_ariba * 4, tamañotxt1, colortxt, fuente) #A partir de aqui se pondran las mejoras compadas en la tienda
		
		if Mostrar == True:

			txt6_AD, posxytxt6_AD = print_pantalla("FPS: " + str(FPS), 0, posytxt_derecha_ariba * 5, tamañotxt1, colortxt, fuente)

		else:
			txt6_AD = ["", ""]
			posxytxt6_AD = ""

		return((txt1_AD, posxytxt1_AD), (txt2_AD, posxytxt2_AD), (txt3_AD, posxytxt3_AD), (txt4_AD, posxytxt4_AD), (txt5_AD, posxytxt5_AD), (txt6_AD, posxytxt6_AD))

	pygame.draw.rect(ventana, blanco, (posx1rect, posy1rect, posx2rect - posx1rect, posy2rect - posy1rect))

	pygame.draw.rect(ventana, negro, (posx1rect + diferencia, posy1rect + diferencia * 3, posx2rect - posx1rect - diferencia*2, posy2rect - posy1rect - diferencia*4))

	txt1, posxytxt1 = print_pantalla("Pausa", posx1rect + diferencia/2, posy1rect, tamañotxt1, negro, fuente)

	txt2, posxytxt2 = print_pantalla("Si sales de este nivel tu puntuacion y", posx1rect + diferencia * 1.5, posy1rect + diferencia * 4, tamañotxt1, blanco, fuente)

	txt3, posxytxt3 = print_pantalla("monedas obtenidas no se guardaran.", posx1rect + diferencia * 1.5, posy1rect + diferencia * 7, tamañotxt1, blanco, fuente)

	bot1 = crear_boton2(ventana, round(0.6328125 * ancho), posy1rect + round(0.0015625 * ancho), posx2rect - round(0.0015625 * ancho), posy1rect + diferencia *3 - round(0.0015625 * ancho), "   X", tamañotxt1, negro, fuente, blanco)
	rectangulo1 = bot1[1]
	posesxybot1 = rectangulo1[1]
	posesxy2bot1 = rectangulo1[2]

	bot2 = crear_boton2(ventana, posx1bot2, posy1bot2, posx2bot2, posy2bot2, "               Continuar", tamañotxt1, negro, fuente, blanco)
	rectangulo2 = bot2[1]
	posesxybot2 = rectangulo2[1]
	posesxy2bot2 = rectangulo2[2]

	bot3 = crear_boton2(ventana, posx1bot3, posy1bot3, posx2bot3, posy2bot3, "               Reintentar", tamañotxt1, negro, fuente, blanco)
	rectangulo3 = bot3[1]
	posesxybot3 = rectangulo3[1]
	posesxy2bot3 = rectangulo3[2]

	bot4 = crear_boton2(ventana, posx1bot4, posy1bot4, posx2bot4, posy2bot4, "Volver a la pantalla anterior", tamañotxt1, negro, fuente, blanco)
	rectangulo4 = bot4[1]
	posesxybot4 = rectangulo4[1]
	posesxy2bot4 = rectangulo4[2]

	ventana.blit(txt1, (posxytxt1[0], posxytxt1[1]))
	ventana.blit(txt2, (posxytxt2[0], posxytxt2[1]))
	ventana.blit(txt3, (posxytxt3[0], posxytxt3[1]))

	ventana.blit(bot1[0], (posesxybot1[0], posesxybot1[1]))
	ventana.blit(bot2[0], (posesxybot2[0], posesxybot2[1]))
	ventana.blit(bot3[0], (posesxybot3[0], posesxybot3[1]))
	ventana.blit(bot4[0], (posesxybot4[0], posesxybot4[1]))

	pygame.display.update()

	Exit_presionado = False

	second = datetime.now().second

	counter = 0

	while Exit_presionado != True:

		for evento in pygame.event.get():
			ratonx, ratony = pygame.mouse.get_pos()

			if evento.type == QUIT:
				print("Juego terminado")
				Exit_presionado = True
				#time.sleep(1)
				pygame.quit()
				raise KeyError

			elif evento.type == KEYDOWN:

				if evento.key == 285: #F4 = para cerrar el programa; hecho
					print("Juego terminado")
					Exit_presionado = True
					#time.sleep(1)
					pygame.quit()
					raise KeyError

				elif evento.key == 27: #ESC = para salir de la pantalla; crear recuadro emergente
					Exit_presionado = True

			if ratonx > round(0.6328125 * ancho) and ratony > posy1rect + round(0.0015625 * ancho) and ratonx < posx2rect - round(0.0015625 * ancho) and ratony < posy1rect + diferencia *3:

				if evento.type == MOUSEBUTTONDOWN:
					bot1 = crear_boton2(ventana, round(0.6328125 * ancho), posy1rect + round(0.0015625 * ancho), posx2rect - round(0.0015625 * ancho), posy1rect + diferencia *3 - round(0.0015625 * ancho), "   X", tamañotxt1, negro, fuente, blanco)
					rectangulo1 = bot1[1]
					posesxybot1 = rectangulo1[1]
					posesxy2bot1 = rectangulo1[2]

					ventana.blit(bot1[0], (posesxybot1[0], posesxybot1[1]))
					pygame.display.update()
					Exit_presionado = True

				else:
					bot1 = crear_boton2(ventana, round(0.6328125 * ancho), posy1rect + round(0.0015625 * ancho), posx2rect - round(0.0015625 * ancho), posy1rect + diferencia *3 - round(0.0015625 * ancho), "   X", tamañotxt1, blanco, fuente, rojo)
					rectangulo1 = bot1[1]
					posesxybot1 = rectangulo1[1]
					posesxy2bot1 = rectangulo1[2]
					
					ventana.blit(bot1[0], (posesxybot1[0], posesxybot1[1])) 
					pygame.display.update()

			else:
				bot1 = crear_boton2(ventana, round(0.6328125 * ancho), posy1rect + round(0.0015625 * ancho), posx2rect - round(0.0015625 * ancho), posy1rect + diferencia *3 - round(0.0015625 * ancho), "   X", tamañotxt1, negro, fuente, blanco)
				rectangulo1 = bot1[1]
				posesxybot1 = rectangulo1[1]
				posesxy2bot1 = rectangulo1[2]

				ventana.blit(bot1[0], (posesxybot1[0], posesxybot1[1])) 
				pygame.display.update()

			if ratonx > posx1bot2 and ratony > posy1bot2 and ratonx < posx2bot2 and ratony < posy2bot2:

				if evento.type == MOUSEBUTTONDOWN:
					Exit_presionado = True

			if ratonx > posx1bot3 and ratony > posy1bot3 and ratonx < posx2bot3 and ratony < posy2bot3:

				if evento.type == MOUSEBUTTONDOWN:
					return True, True

			if ratonx > posx1bot4 and ratony > posy1bot4 and ratonx < posx2bot4 and ratony < posy2bot4:

				if evento.type == MOUSEBUTTONDOWN:
					return True, False

		if fpsactivos == True:

			antsecond = second
			second = datetime.now().second

			if antsecond < second:

				FPS = counter
				counter = 0

				#if FPS > MaxFPS:
					#MaxFPS = FPS
					#print("Maximos FPS alcanzados: " + str(MaxFPS))

				resultados = actualizar_pantalla_derecha_arriba(ventana, user_act, Lv_act, demo, Nº_Naves, porcentaje, Naves_destruidas, Monedas, FPS, True)

				txt1_AD, posxytxt1_AD = resultados[0]
				txt2_AD, posxytxt2_AD = resultados[1]
				txt3_AD, posxytxt3_AD = resultados[2]
				txt4_AD, posxytxt4_AD = resultados[3]
				txt5_AD, posxytxt5_AD = resultados[4]
				txt6_AD, posxytxt6_AD = resultados[5]

				if txt1_AD != ["", ""]: ventana.blit(txt1_AD, (posxytxt1_AD[0], posxytxt1_AD[1]))
				if txt2_AD != ["", ""]: ventana.blit(txt2_AD, (posxytxt2_AD[0], posxytxt2_AD[1]))
				if txt3_AD != ["", ""]: ventana.blit(txt3_AD, (posxytxt3_AD[0], posxytxt3_AD[1]))
				if txt4_AD != ["", ""]: ventana.blit(txt4_AD, (posxytxt4_AD[0], posxytxt4_AD[1]))
				if txt5_AD != ["", ""]: ventana.blit(txt5_AD, (posxytxt5_AD[0], posxytxt5_AD[1]))
				if txt6_AD != ["", ""]: ventana.blit(txt6_AD, (posxytxt6_AD[0], posxytxt6_AD[1]))

				pygame.display.update()

			counter += 1

	return False, False