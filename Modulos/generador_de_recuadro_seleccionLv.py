import pygame

from pygame.locals import *

from Modulos.basededatosajustesfaciliter import *

def crear_recuadro_seleccionLv(ventana, Lv_act, pantalla_act, demo = False, animacionlineas = False):

	blanco = (255, 255, 255)
	negro = (0, 0, 0) # = sin desbloquear
	rojo = (255, 0, 0) # = siguienteLv a completar	
	amarillo = (255, 255, 0) # = Lv actual
	azul = (0, 0, 255) # = Lv pasado
	verde = (0, 255, 0) # = Lv Infinito

	ajustes = extraer_ajustes()
		
	ancho = int(ajustes[0])
	alto = int(ajustes[1])

	tamañocirculo = round(0.0078125 * ancho)

	pant1 = [(round(0.24375 * ancho), round(0.52777777777777777777777777777778 * alto), 1, 0), (round(0.390625 * ancho), round(0.34722222222222222222222222222222 * alto), 2, 0), (round(0.53125 * ancho), round(0.41944444444444444444444444444444 * alto), 3, 0), (640, 480, 4, 0), (770, 480, 5, 0), (885, 250, 6, 1)]

	pant2 = [(260, 170, 6, 0), (390, 300, 7, 0), (680, 360, 8, 0), (815, 275, 9, 0), (1040, 320, 10, 0), (400, 500, 11, 1)]

	pant3 = [(315, 310, 11, 0), (520, 350, 12, 0), (700, 200, 13, 0), (770, 550, 14, 0), (1000, 360, 15, 0), (400, 550, 16, 1)]

	pant4 = [(100, 500, 16, 0), (200, 500, 17, 0), (300, 500, 18, 0), (400, 500, 19, 0), (500, 500, 20, 0), (600, 600, 21, 1)]

	pant5 = [(100, 600, 21, 0), (200, 600, 22, 0), (300, 600, 23, 0), (400, 600, 24, 0), (500, 600, 25, 0), (600, 700, 26, 1)]

	pants = [pant1, pant2, pant3, pant4, pant5]

	def dibujar_lineas(ventana, Lv_act, pantalla_act, animacionlineas, pants):

		ajustes = extraer_ajustes()
		
		ancho = int(ajustes[0])
		alto = int(ajustes[1])

		nivel_necesario_paraInf = [3, 8, 14, 19, 22]

		pygame.draw.line(ventana, negro, (round(0.15625 * ancho), round(0.5 * alto)), (((pants[pantalla_act - 1])[0])[0], ((pants[pantalla_act - 1])[0])[1]), round(0.00390625 * ancho))

		if Lv_act > nivel_necesario_paraInf[pantalla_act - 1] -1:
			pygame.draw.line(ventana, negro, (((pants[pantalla_act - 1])[nivel_necesario_paraInf[pantalla_act -1] - (pantalla_act -1) * 5 -1])[0], ((pants[pantalla_act - 1])[nivel_necesario_paraInf[pantalla_act -1] - (pantalla_act - 1) * 5 -1])[1]), (((pants[pantalla_act - 1])[5])[0], ((pants[pantalla_act - 1])[5])[1]), round(0.00390625 * ancho))

		if Lv_act > 0:

			if Lv_act > pantalla_act * 5:

				repeat = 5

			else:
				repeat = Lv_act - (pantalla_act -1) * 5

			for i in range(repeat):

				i += 1

				if i == 5:
					pygame.draw.line(ventana, negro, (((pants[pantalla_act - 1])[i - 1])[0], ((pants[pantalla_act - 1])[i - 1])[1]), (round(0.84375 * ancho), round(0.5 * alto)), round(0.00390625 * ancho))

				else:
					pygame.draw.line(ventana, negro, (((pants[pantalla_act - 1])[i - 1])[0], ((pants[pantalla_act - 1])[i - 1])[1]), (((pants[pantalla_act - 1])[i])[0], ((pants[pantalla_act - 1])[i])[1]), round(0.00390625 * ancho))

	def dibujar_Lvs(ventana, pantalla, listpos, tamañocirculo, Lv_act):

		for element in listpos:

			if element[3] == 1:
				pygame.draw.circle(ventana, verde, (element[0], element[1]), tamañocirculo)

			elif element[2] < Lv_act and element[3] == 0: #azul
				pygame.draw.circle(ventana, azul, (element[0], element[1]), tamañocirculo)

			elif element[2] == Lv_act and element[3] == 0: #amarillo
				pygame.draw.circle(ventana, amarillo, (element[0], element[1]), tamañocirculo)

			elif element[2] == Lv_act + 1 and element[3] == 0: #rojo
				pygame.draw.circle(ventana, rojo, (element[0], element[1]), tamañocirculo)

			else: #negro
				pygame.draw.circle(ventana, negro, (element[0], element[1]), tamañocirculo)

	if demo == True:
		pass

	else:
		if pantalla_act == 1:
			dibujar_lineas(ventana, Lv_act, pantalla_act, animacionlineas, pants)
			dibujar_Lvs(ventana, pantalla_act, pant1, tamañocirculo, Lv_act)
			return (pant1[0], pant1[1], pant1[2], pant1[3], pant1[4], pant1[5], tamañocirculo)

		elif pantalla_act == 2:
			dibujar_lineas(ventana, Lv_act, pantalla_act, animacionlineas, pants)
			dibujar_Lvs(ventana, pantalla_act, pant2, tamañocirculo, Lv_act)
			return (pant2[0], pant2[1], pant2[2], pant2[3], pant2[4], pant2[5], tamañocirculo)

		elif pantalla_act == 3:
			dibujar_lineas(ventana, Lv_act, pantalla_act, animacionlineas, pants)
			dibujar_Lvs(ventana, pantalla_act, pant3, tamañocirculo, Lv_act)
			return (pant3[0], pant3[1], pant3[2], pant3[3], pant3[4], pant3[5], tamañocirculo)

		elif pantalla_act == 4:
			dibujar_lineas(ventana, Lv_act, pantalla_act, animacionlineas, pants)
			dibujar_Lvs(ventana, pantalla_act, pant4, tamañocirculo, Lv_act)
			return (pant4[0], pant4[1], pant4[2], pant4[3], pant4[4], pant4[5], tamañocirculo)

		elif pantalla_act == 5:
			dibujar_lineas(ventana, Lv_act, pantalla_act, animacionlineas, pants)
			dibujar_Lvs(ventana, pantalla_act, pant5, tamañocirculo, Lv_act)
			return (pant5[0], pant5[1], pant5[2], pant5[3], pant5[4], pant5[5], tamañocirculo)
