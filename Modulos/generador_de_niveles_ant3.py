import pygame

from Modulos.clasificador import *

from Modulos.creador_de_entidades import *

"""

Lvo = nivel obligatorio
Lvsf = nivel sin fin / uno por pantalla
Lvof = nivel opcional de final
Mnpo = maximo de naves por oleada
LvoP = nivel obligatorio / proyectil
Flvsf = funcion de niveles sin fin
EaFlvsf = elementos añadidos en la formula de niveles sin fin
sdlvsf = sucesion de dificultad de niveles sin fin
MefdpupLvsf = maximo de elementos de la formula de parametros a utilizar por nivel sin fin
Ceflvsf = cantidad de elementos en la formula de niveles sin fin

"""

def crear_oleada(ventana, nivel, infinito, list_naves, usados, oleada, radio):

	"""
	Crea las oleadas correspondientes a cada nivel aqui se modifican las posiciones iniciales de cada nave.
	
	### INFORMACION DE CADA NIVEL ###

	Lv1: Nº Naves: 15, Nº Naves Tipo1: 15, Nº Oleadas: 1
	Lv2: Nº Naves: 20, Nº Naves Tipo1: 18, Nº Naves Tipo2: 2, Nº Oleadas: 1
	Lv3: Nº Naves: 32, Nº Naves Tipo1: 25, Nº Naves Tipo2: 7, Nº Oleadas: 2
	Lv4:
	Lv5:

	"""

	#Generacion de niveles obligatorios

	Lvo_List1_5 = [(15), (18, 2), (25, 7), (20, 10, 5), (10, 10, 10)] #Colocacion de naves por Lvo del lv 1 al 5
	Lvo_List6_10 = [(15, 8, 8, 5), (30, 10, 5, 5), (20, 20, 10, 8), (20, 20, 12, 10), (15, 16, 15, 5, 5)] #Colocacion de naves por Lvo del lv 6 al 10
	Lvo_List11_15 = [(18, 18, 18, 10, 8), (15, 15, 20, 15, 10), (10, 15, 20, 20, 12), (0, 19, 23, 19, 14, 5), (5, 17, 22, 22, 11, 8)] #Colocacion de naves por Lvo del lv 11 al 15
	Lvo_List16_20 = [(2, 11, 25, 26, 16, 10), (0, 15, 25, 20, 12, 23, 4), (16, 17, 18, 15, 15, 20, 8), (7, 15, 20, 15, 20, 24, 25, 4), (5, 15, 15, 19, 18, 22, 20, 16)] #Colocacion de naves por Lvo del lv 16 al 20
	Lvo_List21_25 = [(10, 25, 20, 18, 17, 19, 15, 16), (15, 20, 20, 18, 17, 20, 20, 14, 6), (5, 20, 20, 20, 20, 20, 21, 20, 14), (17, 19, 20, 20, 20, 19, 18, 17, 16, 4), (17, 18, 18, 18, 18, 19, 19, 18, 18, 17)] #Colocacion de naves por Lvo del lv 21 al 25
	tipoN_txt_List = ["EBEN1", "EBEN2", "EBEN3", "EBEN4", "EBEN5", "EBEN6", "EBEN7", "EBEN8", "EBEN9", "EBEN10"]#Los diferentes tipos de clases que se pueden crear

	posicionesx = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]

	formacionLv1 = [(340, 80, 1), (500, 80, 1), (740, 80, 1), (900, 80, 1), (380, 124, 1), (460, 124, 1), (780, 124, 1), (860, 124, 1), (420, 168, 1), (500, 168, 1), (740, 168, 1), (820, 168, 1), (580, 212, 1), (660, 212, 1), (620, 256, 1)] #El orden es de arriba-derecha a abajo-izquierda (dando prioridad a una misma fila)

	formacionLv2 = [(360, 80, 2), (560, 80, 1), (680, 80, 1), (880, 80, 2), (440, 124, 1), (800, 124, 1), (360, 168, 1), (480, 168, 1), (760, 168, 1), (880, 168, 1), (440, 212, 1), (520, 212, 1), (720, 212, 1), (800, 212, 1), (400, 256, 1), (560, 256, 1), (680, 256, 1), (840, 256, 1), (560, 300, 1), (680, 300, 1)]

	formacionLv3_Oleada1 = [(380, 80, 2), (860, 80, 2), (340, 124, 2), (420, 124, 1), (820, 124, 1), (900, 124, 2), (340, 168, 1), (460, 168, 1), (540, 168, 1), (700, 168, 1), (780, 168, 1), (900, 168, 1), (380, 212, 1), (500, 212, 1), (620, 212, 1), (740, 212, 1), (860, 212, 1)]

	formacionLv3_Oleada2 = [(340, 80, 2), (900, 80, 2), (380, 124, 1), (460, 124, 1), (620, 124, 2), (780, 124, 1), (860, 124, 1), (340, 168, 1), (500, 168, 1), (580, 168, 1), (660, 168, 1), (740, 168, 1), (900, 168, 1), (580, 212, 1), (660, 212, 1)]

	formacionLv4_Oleada1 = [(620, 80, 1), (340, 124, 1), (540, 124, 1), (620, 124, 1), (700, 124, 1), (900, 124, 1), (380, 168, 1), (500, 168, 1), (580, 168, 1), (660, 168, 1), (740, 168, 1), (860, 168, 1), (380, 212, 1), (460, 212, 1), (780, 212, 1), (860, 212, 1), (340, 256, 1), (500, 256, 1), (740, 256, 1), (900, 256, 1)]

	formacionLv4_Oleada2 = [(100, 100, 1), (100, 100, 1)]

	#Generacion de niveles opcionales del final

	#Lvof_List = [(), (), (), (), ()] #Colocacion de naves del Lvof

	#Posicion de eventos en el mapa

	Lvo_New_list = [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1] #Si se estrena un nuevo tipo de arma en un Lvo determinado
	Lvo_List = [(0, 0, 1, 0, 0), (0, 0, 0, 1, 0), (0, 0, 0, 1, 0), (0, 0, 0, 1, 0), (0, 1, 0, 0, 0)] #En que posicion de niveles esta el nivel sin fin

	#Posicion de aparicion de nuevas armas en Lv a lo que respecta

	LvoP_list = [(1), (0, 0, 1), (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)] #En que orden van apareciendo las armas

	#Aparicion de bosses en diferentes Lv

	Lvo_Boss_List = [0, 0, 0, 0, (1, 0, 0, 0, 0), 0, 0, 0, 0, (0, 1, 0, 0, 0), 0, 0, 0, 0, (0, 0, 1, 0, 0), 0, 0, 0, 0, (0, 0, 0, 1, 0), 0, 0, 0, 0, (0, 0, 0, 0, 1)] #Numero de bosses por Lvo
	Lvsf_Boss_List = [0, 0, 0, 0, 0] #Numero de boses por Lvsf
	Lvof_Boss_List = [(2, 0, 0, 0, 0), (0, 2, 0, 0, 0), (0, 0, 2, 0, 0), (0, 0, 0, 2, 0), (0, 0, 0, 0, 2)] #Numero de bosses por Lvof

	#Formulas de niveles sin fin

	EaFlvsf_List = [1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8]
	Flvsf_List = [1, 2, 4, 6, 9, 12, 16, 21, 26, 32, 38, 45, 52, 60] #Tabien llamados fdp = formula de parametros
	MefdpupLvsf_List = [60, 45, 32, 16, 9]
	Ceflvsf_var = 14

	#Otras variables y listas

	Mnpo = 20 #Habra 20 naves como maximo en la pantalla a la vez los boses cuentan como 5 naves

	terminado = False

	navesoutput = []

	while terminado == False:

		if nivel == 1:

			for nave in formacionLv1:

				output = crear_entidad(tipoN_txt_List[nave[2]- 1], nave[0], nave[1], list_naves, radio)

				if output[0] != False:

					list_naves = output[1]

					navesoutput.append(output[0])

					usados.append(nave[2])

			terminado = True

		if nivel == 2:

			for nave in formacionLv2:

				output = crear_entidad(tipoN_txt_List[nave[2]- 1], nave[0], nave[1], list_naves, radio)

				if output[0] != False:

					list_naves = output[1]

					navesoutput.append(output[0])

					usados.append(nave[2])

			terminado = True

		if nivel == 3 and oleada == 1:

			for nave in formacionLv3_Oleada1:

				output = crear_entidad(tipoN_txt_List[nave[2]- 1], nave[0], nave[1], list_naves, radio)

				if output[0] != False:

					list_naves = output[1]

					navesoutput.append(output[0])

					usados.append(nave[2])

			terminado = True

		if nivel == 3 and oleada == 2:

			for nave in formacionLv3_Oleada2:

				output = crear_entidad(tipoN_txt_List[nave[2]- 1], nave[0], nave[1], list_naves, radio)

				if output[0] != False:

					list_naves = output[1]

					navesoutput.append(output[0])

					usados.append(nave[2])

			terminado = True

		if nivel == 4 and oleada == 1:

			for nave in formacionLv4_Oleada1:

				output = crear_entidad(tipoN_txt_List[nave[2]- 1], nave[0], nave[1], list_naves, radio)

				if output[0] != False:

					list_naves = output[1]

					navesoutput.append(output[0])

					usados.append(nave[2])

			terminado = True

		if nivel == 4 and oleada == 2:

			for nave in formacionLv4_Oleada2:

				output = crear_entidad(tipoN_txt_List[nave[2]- 1], nave[0], nave[1], list_naves, radio)

				if output[0] != False:

					list_naves = output[1]

					navesoutput.append(output[0])

					usados.append(nave[2])

			terminado = True

	print(list_naves)

	return (navesoutput, list_naves, usados)