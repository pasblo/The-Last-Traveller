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

	Lvo_List1_5 = [(15), (18, 2), (25, 7), (20, 10, 5), (16, 12, 12)] #Colocacion de naves por Lvo del lv 1 al 5
	Lvo_List6_10 = [(15, 8, 8, 5), (30, 10, 5, 5), (20, 20, 10, 8), (20, 20, 12, 10), (15, 16, 15, 5, 5)] #Colocacion de naves por Lvo del lv 6 al 10
	Lvo_List11_15 = [(18, 18, 18, 10, 8), (15, 15, 20, 15, 10), (10, 15, 20, 20, 12), (0, 19, 23, 19, 14, 5), (5, 17, 22, 22, 11, 8)] #Colocacion de naves por Lvo del lv 11 al 15
	Lvo_List16_20 = [(2, 11, 25, 26, 16, 10), (0, 15, 25, 20, 12, 23, 4), (16, 17, 18, 15, 15, 20, 8), (7, 15, 20, 15, 20, 24, 25, 4), (5, 15, 15, 19, 18, 22, 20, 16)] #Colocacion de naves por Lvo del lv 16 al 20
	Lvo_List21_25 = [(10, 25, 20, 18, 17, 19, 15, 16), (15, 20, 20, 18, 17, 20, 20, 14, 6), (5, 20, 20, 20, 20, 20, 21, 20, 14), (17, 19, 20, 20, 20, 19, 18, 17, 16, 4), (17, 18, 18, 18, 18, 19, 19, 18, 18, 17)] #Colocacion de naves por Lvo del lv 21 al 25
	tipoN_txt_List = ["EBEN1", "EBEN2", "EBEN3", "EBEN4", "EBEN5", "EBEN6", "EBEN7", "EBEN8", "EBEN9", "EBEN10"]#Los diferentes tipos de clases que se pueden crear

	posicionesx = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]

	#Generacion de niveles finitos

	formacionLv1 = [(340, 80, 1), (500, 80, 1), (740, 80, 1), (900, 80, 1), (380, 124, 1), (460, 124, 1), (780, 124, 1), (860, 124, 1), (420, 168, 1), (500, 168, 1), (740, 168, 1), (820, 168, 1), (580, 212, 1), (660, 212, 1), (620, 256, 1)] #El orden es de arriba-derecha a abajo-izquierda (dando prioridad a una misma fila)

	formacionLv2 = [(360, 80, 2), (560, 80, 1), (680, 80, 1), (880, 80, 2), (440, 124, 1), (800, 124, 1), (360, 168, 1), (480, 168, 1), (760, 168, 1), (880, 168, 1), (440, 212, 1), (520, 212, 1), (720, 212, 1), (800, 212, 1), (400, 256, 1), (560, 256, 1), (680, 256, 1), (840, 256, 1), (560, 300, 1), (680, 300, 1)]

	formacionLv3_Oleada1 = [(380, 80, 2), (860, 80, 2), (340, 124, 2), (420, 124, 1), (820, 124, 1), (900, 124, 2), (340, 168, 1), (460, 168, 1), (540, 168, 1), (700, 168, 1), (780, 168, 1), (900, 168, 1), (380, 212, 1), (500, 212, 1), (620, 212, 1), (740, 212, 1), (860, 212, 1)]

	formacionLv3_Oleada2 = [(340, 80, 2), (900, 80, 2), (380, 124, 1), (460, 124, 1), (620, 124, 2), (780, 124, 1), (860, 124, 1), (340, 168, 1), (500, 168, 1), (580, 168, 1), (660, 168, 1), (740, 168, 1), (900, 168, 1), (580, 212, 1), (660, 212, 1)]

	formacionLv4_Oleada1 = [(620, 80, 3), (340, 124, 2), (540, 124, 2), (620, 124, 1), (700, 124, 2), (900, 124, 2), (380, 168, 1), (500, 168, 1), (580, 168, 1), (660, 168, 1), (740, 168, 1), (860, 168, 1), (380, 212, 1), (460, 212, 1), (780, 212, 1), (860, 212, 1), (340, 256, 1), (500, 256, 1), (740, 256, 1), (900, 256, 1)]

	formacionLv4_Oleada2 = [(540, 80, 2), (620, 80, 2), (700, 80, 2), (380, 124, 3), (580, 124, 3), (660, 124, 3), (860, 124, 3), (540, 168, 2), (620, 168, 2), (700, 168, 2), (540, 212, 1), (700, 212, 1), (580, 256, 1), (660, 256, 1), (620, 300, 1)]

	formacionLv5_Oleada1 = [(460, 80, 2), (540, 80, 2), (620, 80, 3), (700, 80, 2), (780, 80, 2), (340, 124, 3), (900, 124, 3), (500, 168, 2), (740, 168, 2), (340, 212, 3), (620, 212, 1), (900, 212, 3), (420, 256, 1), (580, 256, 1), (660, 256, 1), (820, 256, 1), (340, 300, 1), (540, 300, 1), (700, 300, 1), (900, 300, 1)]

	formacionLv5_Oleada2 = [(340, 80, 3), (540, 80, 1), (700, 80, 1), (900, 80, 3), (420, 124, 1), (580, 124, 1), (660, 124, 1), (820, 124, 1), (340, 168, 3), (620, 168, 1), (900, 168, 3), (500, 212, 2), (740, 212, 2), (340, 256, 3), (900, 256, 3), (460, 300, 2), (540, 300, 2), (620, 300, 3), (700, 300, 2), (780, 300, 2)]

	formaciones = [(formacionLv1, 0), (formacionLv2, 0), (formacionLv3_Oleada1, formacionLv3_Oleada2), (formacionLv4_Oleada1, formacionLv4_Oleada2), (formacionLv5_Oleada1, formacionLv5_Oleada2)]
	#Generacion de niveles infinitos

	#Posiciones de naves opcionales Lvsf (se hace cada uno con su probabilidad y se coge el mayor) (En la primera oleada todas las naves son de Lv1) (suma/resta 2 por oleada)

	opcion1_Lvsf1 = [[340, 80, (100, 20, 0), (0, 50, 100), (2, 2, 2)], [620, 80, (100, 50, 0), (0, 80, 100), (2, 2, 2)], [900, 80, (100, 20, 0), (0, 50, 100), (2, 2, 2)], [420, 124, (100, 10, 0), (0, 90, 100), (2, 2, 2)], [580, 124, (100, 10, 0), (0, 90, 100), (2, 2, 2)], [660, 124, (100, 10, 0), (0, 90, 100), (2, 2, 2)], [820, 124, (100, 10, 0), (0, 90, 100), (2, 2, 2)], [380, 168, (100, 5, 0), (0, 95, 100), (2, 2, 2)], [500, 168, (100, 15, 0), (0, 100, 100), (2, 2, 2)], [620, 168, (100, 20, 0), (0, 95, 100), (2, 2, 2)], [740, 168, (100, 15, 0), (0, 95, 100), (2, 2, 2)], [860, 168, (100, 5, 0), (0, 95, 100), (2, 2, 2)], [460, 212, (100, 5, 0), (0, 95, 100), (2, 2, 2)], [540, 212, (100, 10, 0), (0, 80, 100), (2, 2, 2)], [700, 212, (100, 10, 0), (0, 80, 100), (2, 2, 2)], [780, 212, (100, 5, 0), (0, 95, 100), (2, 2, 2)], [340, 256, (100, 20, 0), (0, 50, 100), (2, 2, 2)], [420, 256, (100, 15, 0), (0, 90, 100), (2, 2, 2)], [820, 256, (100, 15, 0), (0, 90, 100), (2, 2, 2)], [900, 256, (100, 20, 0), (0, 50, 100), (2, 2, 2)]] #(posx, posy, (probabilidades_minimas.osea inicio), (probabilidades_maximas.osea final), (subidas))
	opcion2_Lvsf1 = [[500, 80, (100, 20, 0), (0, 50, 100), (2, 2, 2)], [580, 80, (100, 20, 5), (0, 90, 100), (2, 2, 2)], [660, 80, (100, 20, 5), (0, 90, 100), (2, 2, 2)], [740, 80, (100, 20, 0), (0, 50, 100), (2, 2, 2)], [460, 124, (100, 10, 0), (0, 100, 100), (2, 2, 2)], [540, 124, (100, 20, 5), (0, 90, 100), (2, 2, 2)], [700, 124, (100, 20, 5), (0, 90, 100), (2, 2, 2)], [780, 124, (100, 10, 0), (0, 100, 100), (2, 2, 2)], [340, 168, (100, 20, 5), (0, 80, 100), (2, 2, 2)], [420, 168, (100, 0, 0), (0, 100, 100), (2, 2, 2)], [500, 168, (100, 15, 0), (0, 90, 100), (2, 2, 2)], [740, 168, (100, 15, 0), (0, 90, 100), (2, 2, 2)], [820, 168, (100, 0, 0), (0, 100, 100), (2, 2, 2)], [900, 168, (100, 10, 0), (0, 100, 100), (2, 2, 2)], [380, 212, (100, 10, 0), (0, 90, 100), (2, 2, 2)], [460, 212, (100, 20, 0), (0, 80, 100), (2, 2, 2)], [780, 212, (100, 20, 0), (0, 80, 100), (2, 2, 2)], [860, 212, (100, 10, 0), (0, 90, 100), (2, 2, 2)], [340, 256, (100, 30, 5), (0, 100, 100), (2, 2, 2)], [900, 256, (100, 30, 5), (0, 100, 100), (2, 2, 2)]]
	opcion3_Lvsf1 = [[360, 80, (94, 20, 6), (0, 20, 100), (2, 2, 2)], [560, 80, (100, 20, 0), (0, 80, 100), (2, 2, 2)], [680, 80, (100, 20, 0), (0, 80, 100), (2, 2, 2)], [880, 80, (94, 20, 6), (0, 20, 100), (2, 2, 2)], [400, 124, (98, 40, 2), (0, 90, 100), (2, 2, 2)], [520, 124, (94, 20, 6), (0, 20, 100), (2, 2, 2)], [720, 124, (94, 20, 6), (0, 20, 100), (2, 2, 2)], [840, 124, (98, 40, 2), (0, 90, 100), (2, 2, 2)], [360, 168, (94, 20, 6), (0, 20, 100), (2, 2, 2)], [560, 168, (100, 20, 0), (0, 80, 100), (2, 2, 2)], [680, 168, (100, 20, 0), (0, 80, 100), (2, 2, 2)], [880, 168, (94, 20, 6), (0, 20, 100), (2, 2, 2)], [400, 212, (98, 40, 2), (0, 90, 100), (2, 2, 2)], [840, 212, (98, 40, 2), (0, 90, 100), (2, 2, 2)], [360, 256, (94, 20, 6), (0, 20, 100), (2, 2, 2)], [480, 256, (98, 40, 2), (0, 90, 100), (2, 2, 2)], [760, 256, (98, 40, 2), (0, 90, 100), (2, 2, 2)], [880, 256, (94, 20, 6), (0, 20, 100), (2, 2, 2)], [400, 300, (98, 40, 2), (0, 90, 100), (2, 2, 2)], [840, 300, (98, 40, 2), (0, 90, 100), (2, 2, 2)]]
	opcion4_Lvsf1 = []
	opcion5_Lvsf1 = []

	oleadasLvsf1 = [opcion1_Lvsf1, opcion2_Lvsf1, opcion3_Lvsf1, opcion4_Lvsf1, opcion5_Lvsf1]
	formacionesLvsf = [oleadasLvsf1, 0]
	#Posicion de eventos en el mapa

	Lvo_New_list = [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1] #Si se estrena un nuevo tipo de arma en un Lvo determinado
	Lvo_List = [(0, 0, 1, 0, 0), (0, 0, 0, 1, 0), (0, 0, 0, 1, 0), (0, 0, 0, 1, 0), (0, 1, 0, 0, 0)] #En que posicion de niveles esta el nivel sin fin

	#Posicion de aparicion de nuevas armas en Lv a lo que respecta

	LvoP_list = [(1), (0, 0, 1), (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)] #En que orden van apareciendo las armas

	#Aparicion de bosses en diferentes Lv

	Lvo_Boss_List = [0, 0, 0, 0, (1, 0, 0, 0, 0), 0, 0, 0, 0, (0, 1, 0, 0, 0), 0, 0, 0, 0, (0, 0, 1, 0, 0), 0, 0, 0, 0, (0, 0, 0, 1, 0), 0, 0, 0, 0, (0, 0, 0, 0, 1)] #Numero de bosses por Lvo

	#Formulas de niveles sin fin

	EaFlvsf_List = [1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8]
	Flvsf_List = [1, 2, 4, 6, 9, 12, 16, 21, 26, 32, 38, 45, 52, 60] #Tabien llamados fdp = formula de parametros
	MefdpupLvsf_List = [60, 45, 32, 16, 9]
	Ceflvsf_var = 14

	#Otras variables y listas

	terminado = False

	navesoutput = []

	while terminado == False:

		if infinito == False:

			nivel_a_usar = formaciones[nivel - 1]

			oleada_a_usar = nivel_a_usar[oleada - 1]

			for nave in oleada_a_usar:

				output = crear_entidad(tipoN_txt_List[nave[2]- 1], nave[0], nave[1], list_naves, radio)

				if output[0] != False:

					list_naves = output[1]

					navesoutput.append(output[0])

					usados.append(nave[2])

			terminado = True

		if infinito == True: #(posx, posy, (probabilidades_minimas.osea inicio), (probabilidades_maximas.osea final), (paso))
			nivelinfinito_a_usar = formacionesLvsf[nivel - 1]
			oleada_Nº = random.randrange(0, 3)
			oleada_a_ejecutar = nivelinfinito_a_usar[oleada_Nº]

			if oleada == 1:

				for nave in oleada_a_ejecutar:

					output = crear_entidad("EBEN1", nave[0], nave[1], list_naves, radio)

					if output[0] != False:

						list_naves = output[1]

						navesoutput.append(output[0])

						usados.append(nave[2])

				terminado = True

			else:

				for nave in oleada_a_ejecutar:
					encontrado = False
					signos = []

					for x in nave[2]:

						if x > (nave[3])[(nave[2]).index(x)]:
							signos.append(-1)

						else:
							signos.append(1)

					while encontrado == False:

						ha_tocado = []

						for x in nave[2]:

							if signos[(nave[2]).index(x)] == -1:

								if x+(oleada*(nave[4])[(nave[2]).index(x)])*signos[(nave[2]).index(x)] <= (nave[3])[(nave[2]).index(x)]: #Si ya se ha llegado al limite establecido
									if (nave[3])[(nave[2]).index(x)] > random.randrange(0, 100):
										ha_tocado.append((nave[2]).index(x))

								else:
									if x+(oleada*(nave[4])[(nave[2]).index(x)])*signos[(nave[2]).index(x)] > random.randrange(0, 100):
										ha_tocado.append((nave[2]).index(x))

							else:

								if x+(oleada*(nave[4])[(nave[2]).index(x)])*signos[(nave[2]).index(x)] >= (nave[3])[(nave[2]).index(x)]: #Si ya se ha llegado al limite establecido
									if (nave[3])[(nave[2]).index(x)] > random.randrange(0, 100):
										ha_tocado.append((nave[2]).index(x))

								else:
									if x+(oleada*(nave[4])[(nave[2]).index(x)])*signos[(nave[2]).index(x)] > random.randrange(0, 100):
										ha_tocado.append((nave[2]).index(x))

						if ha_tocado != []:
							ha_tocado.reverse()
							nivel_a_usar = ha_tocado[0]
							encontrado = True

					output = crear_entidad(tipoN_txt_List[nivel_a_usar], nave[0], nave[1], list_naves, radio)

					if output[0] != False:

						list_naves = output[1]

						navesoutput.append(output[0])

						usados.append(nave[2])

				terminado = True

	return (navesoutput, list_naves, usados)