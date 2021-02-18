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

def Crear_oleada(nivel, list_naves, pantalla, numero_de_oleada = 1, Lvo = False, Lvsf = False, Lvof = False):

	#Musica
	
	Canciones_Fondo_List = []
	Canciones_Lvs_List = []
	Cancion_Final_var = ""

	#Generacion de niveles obligatorios

	Lvo_List1_5 = [(5, 1, 1), (18, 2), (25, 5), (10, 10, 5), (10, 10, 10)] #Colocacion de naves por Lvo del lv 1 al 5
	Lvo_List6_10 = [(15, 8, 8, 5), (30, 10, 5, 5), (20, 20, 10, 8), (20, 20, 12, 10), (15, 16, 15, 5, 5)] #Colocacion de naves por Lvo del lv 6 al 10
	Lvo_List11_15 = [(18, 18, 18, 10, 8), (15, 15, 20, 15, 10), (10, 15, 20, 20, 12), (0, 20, 24, 20, 15, 5)] #Colocacion de naves por Lvo del lv 11 al 15
	Lvo_List16_20 = [(), (), (), (), ()] #Colocacion de naves por Lvo del lv 16 al 20
	Lvo_List21_25 = [(), (), (), (), ()] #Colocacion de naves por Lvo del lv 21 al 25
	tipoN_txt_List = ["EBEN1", "EBEN2", "EBEN3", "EBEN4", "EBEN5", "EBEN6", "EBEN7", "EBEN8", "EBEN9", "EBEN10"]#Los diferentes tipos de clases que se pueden crear

	posicionesx = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]

	#Generacion de niveles opcionales del final

	Lvof_List = [(), (), (), (), ()] #Colocacion de naves del Lvof

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

	naves_creadas = []
	tipo = 0
	y = 0

	if Lvo == True and Lvsf == False and Lvof == False:

		if numero_de_oleada > 0:

			if nivel <= 5:
				Lv_act = Lvo_List1_5[nivel-1]
				print(Lv_act)
				conj_de_naves = 0

				for number in list(Lv_act):

					conj_de_naves = conj_de_naves + number

				print(conj_de_naves)

				if conj_de_naves <= Mnpo:

					for list_act in list(Lv_act):
						print(list_act)
						pos = list_act
						x = 0

						while x < pos:
							if Lv_act[0] > 0:

								conj = crear_entidad(tipoN_txt_List[tipo], posicionesx[x + y], 0, list_naves, pantalla)
								list_naves = conj[1]
								naves_creadas.append(conj[0])

							x = x +1
						y = x + y

						tipo = tipo +1
							
					return (naves_creadas, list_naves)


				else:
					pass


			elif nivel > 5 and nivel <= 10:
				Lv_act = Lvo_List6_10[nivel-6]
				print(Lv_act)

			elif nivel > 10 and nivel <= 15:
				Lv_act = Lvo_List11_15[nivel-11]
				print(Lv_act)

			elif nivel > 15 and nivel <= 20:
				Lv_act = Lvo_List16_20[nivel-16]
				print(Lv_act)

			elif nivel > 20 and nivel <= 25:
				Lv_act = Lvo_List21_25[nivel-21]
				print(Lv_act)

			else:
				print("El nivel maximo es 25, introduzca un valor dentro de ese limite")

		else:
			print("No existe una oleada menor a cero")

	elif Lvsf == True and Lvo == False and Lvof == False:
		pass

	elif Lvof == True and Lvo == False and Lvsf == False:
		pass

	else:
		print("Ninguno se llama asi")
	
	#return (Nave1, Nave2, Nave3, Nave4, Nave5, Nave6, Nave7, Nave8, Nave9, Nave10, Nave11, Nave12, Nave13, Nave14, Nave15, Nave16, Nave17, Nave18, Nave19, Nave20)
