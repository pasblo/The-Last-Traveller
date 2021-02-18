import pygame

import sys

import random

from Modulos.generador_de_pantalla_ajustes import *

from Modulos.generador_de_recuadro_seleccionLv import *

from Modulos.generador_de_pantalla_juego import *

from Modulos.basededatosnivelesfaciliter import *

from Modulos.objetos_de_pantalla import *

from Modulos.generador_de_pantalla_controles import *

from pygame.locals import *

def EjecutarSeleccionLv(ventana, user_act):

	def calcularx(letras, ancho):

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

	# ========================================= NIVELES INFINITOS =============================================      MAX CHAR POR LINEA 64

	Lv1Inf_L1 = "(?/?/?): Ha habido una fuga en el combustible de la estación de comunicaciones, este"
	Lv1Inf_L2 = "ha provocado una explosión que me ha enviado muy lejos de allí, y por la mala"
	Lv1Inf_L3 = "suerte que tengo he ido a caer cerca de un agujero negro. No se que dia es por"
	Lv1Inf_L4 = "que llevo aquí mucho tiempo, ya que el agujero negro crea un bucle temporal"
	Lv1Inf_L5 = "donde estoy, el otro problema es que también vino conmigo una flota enemiga."

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

	# ========================================= NIVELES FINITOS =============================================      MAX CHAR POR LINEA 64 +-

	Lv1_L1 = "(21/3/2134): Llevo muchos años en una misión de exploración de otros"
	Lv1_L2 = "mundos y de descubrimiento de nuevas especies, hoy me toca un dia"
	Lv1_L3 = "rutinario de investigacion de unos asteroides que llevan emitiendo"
	Lv1_L4 = "ondas desconocidas desde hace varios meses y espero que se"
	Lv1_L5 = "trate de algo interesante porque llevo 2 meses observandolo."

	lista_textos_Lv1 = (Lv1_L1, Lv1_L2, Lv1_L3, Lv1_L4, Lv1_L5) #Nivel 1

	Lv2_L1 = "(5/4/2134): Desde que observé esas naves enemigas y me hicieron una"
	Lv2_L2 = "emboscada he estado escondido en este planeta por 2 semanas y no he"
	Lv2_L3 = "recibido ninguna transmisión del centro de control, pienso que"
	Lv2_L4 = "puede ser la densa atmosfera, pero no estoy seguro, voy a salir"
	Lv2_L5 = "de este planeta a investigar. Espero que no haya pasado nada." # Mensaje que recibes de S.O.S. de tu especie

	lista_textos_Lv2 = (Lv2_L1, Lv2_L2, Lv2_L3, Lv2_L4, Lv2_L5) #Nivel 2

	Lv3_L1 = "(6/4/2134): No se que puedo hacer, pero ya que soy el último en"
	Lv3_L2 = "libertad tendré que arreglarmelas solo. He estado pensando en un"
	Lv3_L3 = "plan: Conseguir entrar en la base de comunicaciones del enemigo"
	Lv3_L4 = "para obtener mas informacion sobre mi posicion y mis ventajas, pero"
	Lv3_L5 = "no va a ser un trbajo fácil ya que esa base esta muy bien protegida."

	lista_textos_Lv3 = (Lv3_L1, Lv3_L2, Lv3_L3, Lv3_L4, Lv3_L5) #Nivel 3

	Lv4_L1 = "(20/4/2134): Desde que salí de la base de comunicaciones he"
	Lv4_L2 = "estado arreglando los motores de curvatura para poder llegar al"
	Lv4_L3 = "sistema donde se encuentra el agujero de gusano, para poder llegar"
	Lv4_L4 = "a mi universo, el problema es que va a resultar muy complicado entrar"
	Lv4_L5 = "sin que me detecten."

	lista_textos_Lv4 = (Lv4_L1, Lv4_L2, Lv4_L3, Lv4_L4, Lv4_L5) #Nivel 4

	Lv5_L1 = "(25/4/2134): Acabo de salir de la hipervelocidad y he recibido un mensaje"
	Lv5_L2 = "del planeta tierra, en él que decian que se habían intentado escapar pero"
	Lv5_L3 = "no lo habían conseguido por que están muy bien vigilados y probablemente"
	Lv5_L4 = "este sea el último mensaje que me enviarán ya que dentro de poco los"
	Lv5_L5 = "invasores descubrirán la frecuencia de onda. Intentaré llegar rápido."

	lista_textos_Lv5 = (Lv5_L1, Lv5_L2, Lv5_L3, Lv5_L4, Lv5_L5) #Nivel 5

	Lv6_L1 = "(26/4/2134): La nave que me encontre ayer era enorme, estoy seguro de que"
	Lv6_L2 = "tendrán mas naves como esa o mayores, la verdad es que tuve bastante suerte "
	Lv6_L3 = "al poder destruirla. He tenido un grave problema con los motores de hipervelocidad"
	Lv6_L4 = "y no he podido arreglarlos así que ahora tendre que viajar mucho mas despacio, "
	Lv6_L5 = "espero tener algo con lo que divertirme." #Empezar el 6 con musica como si la estuviera escuchando

	lista_textos_Lv6 = (Lv6_L1, Lv6_L2, Lv6_L3, Lv6_L4, Lv6_L5) #Nivel 6

	Lv7_L1 = "(28/4/2134): El ataque de ayer me dejó destrozado creo que no voy a poder"
	Lv7_L2 = "continuar. Me fallan los motores, el soporte vital... Según mi nave no"
	Lv7_L3 = "me quedan mas de dos horas de vida, y tengo un 99,8%" + " de probabilidad de"
	Lv7_L4 = "muerte. Bueno pués en este tiempo no se me ha ocurrido otra idea más"
	Lv7_L5 = "que ponerme a escribir en mi diario de abordo y ver una película."

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
	verde = (0, 255, 0) # = Lv Infinito

	tamañoline = round(0.00234375 * ancho)

	posyline1 = round(0.16666666666666666666666666666667 * alto)
	posyline2 = round(0.83333333333333333333333333333333 * alto)

	posxline3 = round(0.15625 * ancho)
	posxline4 = round(0.84375 * ancho)

	posxflecha1 = round(0.078125 * ancho)
	posyflecha1 = round(0.5 * alto)
	posx1flecha1 = posxflecha1 - round(0.025 * ancho)
	posy1flecha1 = posyflecha1 - round(0.04444444444444444444444444444444 * alto)
	posx2flecha1 = posxflecha1 + round(0.025 * ancho)
	posy2flecha1 = posyflecha1 + round(0.04444444444444444444444444444444 * alto)

	posxflecha2 = round(0.921875 * ancho)
	posyflecha2 = round(0.5 * alto)
	posx1flecha2 = posxflecha2 - round(0.025 * ancho)
	posy1flecha2 = posyflecha2 - round(0.04444444444444444444444444444444 * alto)
	posx2flecha2 = posxflecha2 + round(0.025 * ancho)
	posy2flecha2 = posyflecha2 + round(0.04444444444444444444444444444444 * alto)

	tamañotxt1 = round(0.03125 * ancho)

	posytxt2 = round(0.04166666666666666666666666666667 * alto) #30
	posxtxt3 = round(0.4296875 * ancho)

	posytxt30 = round(0.08333333333333333333333333333333 * alto)

	posxtxt5678 = round(0.4375 * ancho)
	posytxt5 = 0
	posytxt6 = round(0.04166666666666666666666666666667 * alto)
	posytxt7 = round(0.08333333333333333333333333333333 * alto)
	posytxt8 = round(0.125 * alto)

	errordebotgeneral = round(0.00390625 * ancho)
	tamañopolygon = round(0.00190625 * ancho)
	posx1botat = round(0.015625 * ancho)
	posy1botat = round(0.9305555 * alto)
	posx2botat = round(0.234375 * ancho)
	posy2botat = round(0.9722222 * alto)
	tamañotxt2 = round(0.0234375 * ancho)
	tamañotxt3 = round(0.018 * ancho)

	posx1botaj = round(0.015625 * ancho)
	posy1botaj = round(0.855 * alto)
	posx2botaj = round(0.1041875 * ancho)
	posy2botaj = round(0.89666666667 * alto)

	tamañocirculo = round(0.0078125 * ancho)
	posxcirclegen = round(0.4296875 * ancho)
	posycircle1 = round(0.02083333333333333333333333333333 * alto)
	posycircle2 = round(0.0625 * alto)
	posycircle3 = round(0.10416666666666666666666666666667 * alto)
	posycircle4 = round(0.14583333333333333333333333333333 * alto)
	posxcircle5 = round(0.6546875 * ancho)

	posxtxt91011121314 = round(0.25 * ancho)
	posytxt9 = round(0.8375 * alto)
	posytxt10 = round(0.86805555555555555555555555555556 * alto)
	posytxt11 = round(0.89861111111111111111111111111111 * alto)
	posytxt12 = round(0.92916666666666666666666666666667 * alto)
	posytxt13 = round(0.95972222222222222222222222222222 * alto)

	posxtxt14151617 = round(0.84765625 * ancho)
	posytxt14 = round(0.17361111111111111111111111111111 * alto)
	posytxt15 = round(0.20833333333333333333333333333333 * alto)
	posytxt16 = round(0.24305555555555555555555555555556 * alto)
	posytxt17 = round(0.27777777777777777777777777777778 * alto)
	posytxt26 = round(0.3125 * alto)
	posytxt27 = round(0.34722222222222222222222222222222 * alto)

	posxtxt18 = round(0.6640625 * ancho)

	posx1bot5 = round(0.859375 * ancho)
	posy1bot5 = round(0.76388888888888888888888888888889 * alto)
	posx2bot5 = round(0.98046875 * ancho)
	posy2bot5 = round(0.80972222222222222222222222222222 * alto)

	posytxt20 = round(0.60833333333333333333333333333333 * alto) #438
	posytxt21 = round(0.67777777777777777777777777777778 * alto) #488
	posytxt22 = round(0.7125 * alto)
	posytxt23 = round(0.74722222222222222222222222222222 * alto)
	posytxt24 = round(0.78194444444444444444444444444444 * alto)
	posytxt25 = round(0.64305555555555555555555555555556 * alto)
	posytxt28 = round(0.36527777777777777777777777777778 * alto)
	posytxt29 = round(0.4 * alto)

	posx1botcont = round(0.109375 * ancho)
	posy1botcont = round(0.855 * alto)
	posx2botcont = round(0.234375 * ancho)
	posy2botcont = round(0.89666666667 * alto)

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

	if user_act[1] != "None":

		nivel_act = 25

	else:
		nivel_act = 0

	toca = 1

	data_niveles = []

	insertardatosniveles((5000, 14, 100, 1, 250), user_act[1], 1)
	'''insertardatosniveles((56, 14, 100, 1, 278), user_act[1], 2)
	insertardatosniveles((45, 14, 100, 1, 278), user_act[1], 3)
	insertardatosniveles((560, 14, 100, 1, 278), user_act[1], 4)
	insertardatosniveles((5678, 14, 100, 1, 278), user_act[1], 5)
	insertardatosniveles((43, 14, 100, 1, 278), user_act[1], 6)
	insertardatosniveles((1, 14, 100, 1, 278), user_act[1], 7)
	insertardatosniveles((56, 14, 100, 1, 278), user_act[1], 8)
	insertardatosniveles((45, 14, 100, 1, 278), user_act[1], 9)
	insertardatosniveles((560, 14, 100, 1, 278), user_act[1], 10)
	insertardatosniveles((5678, 14, 100, 1, 278), user_act[1], 11)
	insertardatosniveles((43, 14, 100, 1, 278), user_act[1], 12)
	insertardatosniveles((1, 14, 100, 1, 278), user_act[1], 13)
	insertardatosniveles((56, 14, 100, 1, 278), user_act[1], 14)
	insertardatosniveles((45, 14, 100, 1, 278), user_act[1], 15)
	insertardatosniveles((560, 14, 100, 1, 278), user_act[1], 16)
	insertardatosniveles((5678, 14, 100, 1, 278), user_act[1], 17)
	insertardatosniveles((43, 14, 100, 1, 278), user_act[1], 18)
	insertardatosniveles((1, 14, 100, 1, 278), user_act[1], 19)
	insertardatosniveles((56, 14, 100, 1, 278), user_act[1], 20)
	insertardatosniveles((45, 14, 100, 1, 278), user_act[1], 21)
	insertardatosniveles((560, 14, 100, 1, 278), user_act[1], 22)
	insertardatosniveles((5678, 14, 100, 1, 278), user_act[1], 23)
	insertardatosniveles((43, 14, 100, 1, 278), user_act[1], 24)
	insertardatosniveles((1, 14, 100, 1, 278), user_act[1], 25)
	insertardatosniveles((56, 14, 100, 1, 278), user_act[1], 26)
	insertardatosniveles((45, 14, 100, 1, 278), user_act[1], 27)
	insertardatosniveles((560, 14, 100, 1, 278), user_act[1], 28)
	insertardatosniveles((5678, 14, 100, 1, 278), user_act[1], 29)
	insertardatosniveles((43, 14, 100, 1, 278), user_act[1], 30)'''

	ordenardbniveles(user_act[1], 1)

	if user_act[1] != "None":

		while toca < 31:

			data_nivel = extraerdatos(user_act[1], toca)

			data_niveles.append(data_nivel)

			toca += 1

	caracteristicasfondo = [tamañoline, posyline1, posyline2, posxline3, posxline4, tamañotxt1, posytxt2, errordebotgeneral, tamañopolygon, posx1botat, posy1botat, posx2botat, posy2botat, tamañotxt2, posxtxt3, tamañocirculo, posxcirclegen, posycircle1, posycircle2, posycircle3, posycircle4, posxtxt5678, posytxt5, posytxt6, posytxt7, posytxt8, posxtxt18, posxcircle5, posytxt30]

	navestotales = [15, 20, 30, 25, 30, 36, 50, 58, 62, 56, 72, 75, 77, 80, 85, 90, 99, 109, 130, 130, 140, 150, 160, 170, 180]

	nivel_necesario_paraInf = [3, 9, 14, 19, 22]

	dificultades = ["Muy fácil", "Muy fácil", "Fácil", "Fácil", "Fácil", "Facil", "Normal", "Normal", "Normal", "Normal", "Normal", "Media", "Media", "Media", "Media", "Alta", "Alta", "Alta", "Dificil", "Dificil", "Dificil", "Muy Dificil", "Muy Dificil", "Muy Dificil", "Imposible"]

	caracteristicas_panelInfo = [posxtxt91011121314, posytxt9, posytxt10, posytxt11, posytxt12, posytxt13, lista_textos, lista_textos_LvsInfinitos, posxtxt14151617, posytxt14, posytxt15, posytxt16, posytxt17, navestotales, posytxt20, posytxt21, posytxt22, posytxt23, posytxt24, posytxt25, data_niveles, posytxt26, posytxt27, dificultades, posytxt28, posytxt29]

	ventana.fill(gris_fondo)

	imagen_fondo_seleccion_pantalla_alpha = pygame.image.load("Imagenes/imagen_fondo_seleccion_pantalla.jpg").convert()

	pantlenx = round(0.6875 * ancho) #880

	pantleny = round(0.66666666666666666666666666666667 * alto) #480

	imagen_fondo_seleccion_pantalla = pygame.transform.scale(imagen_fondo_seleccion_pantalla_alpha, (pantlenx, pantleny))

	frases_de_carga = ["Los controles rapidos como F11 en el juego no funcionan, excepto el F4.", "Al salir de un nivel sin haberlo acabado tu puntuacion no se guardará, pero tus monedas si.", "Intenta conseguir el mayor numero de monedas, luego te servirán para mejorar tu nave.", "Juega los niveles infinitos para aumentar tu puntuación."]

	if user_act[1] != "None":

		PuntuacionTotal = calculartotalpuntuacion(user_act[1])

		actualizarpuntuacion(PuntuacionTotal, user_act[1])

		punt_act = obtenerdato("Records", "records", user_act[1], 0)

		#monedas_act = obtenerdato("Records", "monedas", user_act[1], 0)

	else:
		punt_act = 0

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
		posytxt6 = caracteristicas[23]
		posytxt7 = caracteristicas[24]
		posytxt8 = caracteristicas[25]
		posxtxt18 = caracteristicas[26]
		posxcircle5 = caracteristicas[27]
		posytxt30 = caracteristicas[28]

		pygame.draw.line(ventana, negro, (0, posyline1), (ancho, posyline1), tamañoline)
		pygame.draw.line(ventana, negro, (0, posyline2), (ancho, posyline2), tamañoline)
		pygame.draw.line(ventana, negro, (posxline3, posyline1), (posxline3, posyline2), tamañoline)
		pygame.draw.line(ventana, negro, (posxline4, posyline1), (posxline4, posyline2), tamañoline)
		pygame.draw.line(ventana, negro, (posx2botat + round(0.0078125 * ancho), posyline2), (posx2botat + round(0.0078125 * ancho), alto), tamañoline)

		flecha_derecha = pygame.image.load("Imagenes/flecha_derecha.png")
		flecha_izquierda = pygame.image.load("Imagenes/flecha_izquierda.png")

		bot3 = pygame.transform.scale(flecha_derecha, (posx2flecha1 - posx1flecha1, posy2flecha1 - posy1flecha1))
		bot4 = pygame.transform.scale(flecha_izquierda, (posx2flecha2 - posx1flecha2, posy2flecha2 - posy1flecha2))

		if user_act[1] == "None":
			txt1, posxytxt1 = print_pantalla("Jugador actual: None", 0, 0, tamañotxt1, negro, fuente_act)
			txt2, posxytxt2 = print_pantalla("Puntuacion actual: None", 0, posytxt2, tamañotxt1, negro, fuente_act)
			txt30, posxytxt30 = print_pantalla("Monedas: None", 0, posytxt30, tamañotxt1, negro, fuente_act)
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
			txt18 = ["", ""]
			posxytxt18 = ("", "")

		else:
			txt1, posxytxt1 = print_pantalla("Jugador actual: " + user_act[1], 0, 0, tamañotxt1, negro, fuente_act)
			txt2, posxytxt2 = print_pantalla("Puntuacion actual: " + str(punt_act[1]), 0, posytxt2, tamañotxt1, negro, fuente_act)
			txt30, posxytxt30 = print_pantalla("Monedas: 0", 0, posytxt30, tamañotxt1, negro, fuente_act)
			txt3 = None
			posxytxt3 = (None, None)
			txt4 = None
			posxytxt4 = (None, None)
			pygame.draw.circle(ventana, azul, (posxcirclegen, posycircle1), tamañocirculo)
			pygame.draw.circle(ventana, amarillo, (posxcirclegen, posycircle2), tamañocirculo)
			pygame.draw.circle(ventana, rojo, (posxcirclegen, posycircle3), tamañocirculo)
			pygame.draw.circle(ventana, negro, (posxcirclegen, posycircle4), tamañocirculo)
			pygame.draw.circle(ventana, verde, (posxcircle5, posycircle4), tamañocirculo)
			txt5, posxytxt5 = print_pantalla("--> Nivel completado", posxtxt5678, posytxt5, tamañotxt2, negro, fuente_act)
			txt6, posxytxt6 = print_pantalla("--> Último nivel completado", posxtxt5678, posytxt6, tamañotxt2, negro, fuente_act)
			txt7, posxytxt7 = print_pantalla("--> Siguiente nivel a completar", posxtxt5678, posytxt7, tamañotxt2, negro, fuente_act)
			txt8, posxytxt8 = print_pantalla("--> Nivel bloqueado", posxtxt5678, posytxt8, tamañotxt2, negro, fuente_act)
			txt18, posxytxt18 = print_pantalla("--> Nivel Infinito", posxtxt18, posytxt8, tamañotxt2, negro, fuente_act)

		bot1 = crear_boton3(ventana, posx1botat, posy1botat, posx2botat, posy2botat, "<-- Pantalla anterior", tamañotxt2, tamañopolygon, errordebotgeneral, negro, fuente_act, negro)

		bot2 = crear_boton3(ventana, posx1botaj, posy1botaj, posx2botaj, posy2botaj, "AJUSTES", tamañotxt2, tamañopolygon, errordebotgeneral, negro, fuente_act, negro)

		bot6 = crear_boton3(ventana, posx1botcont, posy1botcont, posx2botcont, posy2botcont, "CONTROLES", tamañotxt2, tamañopolygon, errordebotgeneral, negro, fuente_act, negro)

		posesxybot1, posesxy2bot1 = bot1[1]

		posesxybot2, posesxy2bot2 = bot2[1]

		posesxybot6, posesxy2bot6 = bot6[1]

		return(bot3, bot4, (txt1, posxytxt1), (txt2, posxytxt2), (posesxybot1, posesxy2bot1, bot1[0]), (txt3, posxytxt3), (txt4, posxytxt4), (posesxybot2, posesxy2bot2, bot2[0]), (txt5, posxytxt5), (txt6, posxytxt6), (txt7, posxytxt7), (txt8, posxytxt8), (txt18, posxytxt18), (txt30, posxytxt30), (posesxybot6, posesxy2bot6, bot6[0]))

	def generar_panel_informativo(caracteristicas_panelInfo, Lv_act, pantalla_act, demo, infinito, posible):

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
		navestotales = caracteristicas_panelInfo[13]
		posytxt20 = caracteristicas_panelInfo[14]
		posytxt21 = caracteristicas_panelInfo[15]
		posytxt22 = caracteristicas_panelInfo[16]
		posytxt23 = caracteristicas_panelInfo[17]
		posytxt24 = caracteristicas_panelInfo[18]
		posytxt25 = caracteristicas_panelInfo[19]
		data_niveles = caracteristicas_panelInfo[20]
		posytxt26 = caracteristicas_panelInfo[21]
		posytxt27 = caracteristicas_panelInfo[22]
		dificultades = caracteristicas_panelInfo[23]
		posytxt28 = caracteristicas_panelInfo[24]
		posytxt29 = caracteristicas_panelInfo[25]

		print(data_niveles)

		if demo != True:

			if infinito == True:
				data_de_Lv_act = data_niveles[Lv_act + 25]

			else:
				data_de_Lv_act = data_niveles[Lv_act]

		ajustes = extraer_ajustes()
		
		ancho = int(ajustes[0])
		alto = int(ajustes[1])
		fuente_act = ajustes[3]

		if demo != True:

			if data_de_Lv_act == []:
				puntuacion = 0
				kills = 0
				porcentaje = "0"
				muertes = 0
				tiempo = "0.0"

			else:
				print(data_de_Lv_act)
				puntuacion = (data_de_Lv_act[0])[0]
				kills = (data_de_Lv_act[0])[1]
				porcentaje = (data_de_Lv_act[0])[2]
				muertes = (data_de_Lv_act[0])[3]
				tiempo = (data_de_Lv_act[0])[4]

			if Lv_act == 4 or Lv_act == 9 or Lv_act == 14 or Lv_act == 19 or Lv_act == 24:
				boss = True

			else:
				boss = False

		if demo == True:
			txt9, posxytxt9 = print_pantalla( "Estas en la version demo para poder jugar todos los niveles", posxtxt91011121314, posytxt9, tamañotxt2, negro, fuente_act) # Max 64 char
			txt10, posxytxt10 = print_pantalla( "tiene que registrarse como usuario. Para ello vaya a ventana", posxtxt91011121314, posytxt10, tamañotxt2, negro, fuente_act) # Max 64 char
			txt11, posxytxt11 = print_pantalla( "principal y pulse al boton LOGEAR/CREAR USUARIO, y siga las", posxtxt91011121314, posytxt11, tamañotxt2, negro, fuente_act) # Max 64 char
			txt12, posxytxt12 = print_pantalla( "instrucciones indicadas.", posxtxt91011121314, posytxt12, tamañotxt2, negro, fuente_act) # Max 64 char
			txt13, posxytxt13 = print_pantalla( "", posxtxt91011121314, posytxt13, tamañotxt2, negro, fuente_act) # Max 64 char
			txt14 = ["", ""]
			posxytxt14 = ""
			txt15 = ["", ""]
			posxytxt15 = ""
			txt16 = ["", ""]
			posxytxt16 = ""
			txt17 = ["", ""]
			posxytxt17 = ""
			txt20 = ["", ""]
			posxytxt20 = ""
			txt21 = ["", ""]
			posxytxt21 = ""
			txt22 = ["", ""]
			posxytxt22 = ""
			txt23 = ["", ""]
			posxytxt23 = ""
			txt24 = ["", ""]
			posxytxt24 = ""
			txt25 = ["", ""]
			posxytxt25 = ""
			txt26 = ["", ""]
			posxytxt26 = ""
			txt27 = ["", ""]
			posxytxt27 = ""
			txt28 = ["", ""]
			posxytxt28 = ""
			txt29 = ["", ""]
			posxytxt29 = ""

		elif infinito == True:

			if posible == True:
				txt9, posxytxt9 = print_pantalla((lista_textos_LvsInfinitos[Lv_act])[0], posxtxt91011121314, posytxt9, tamañotxt3, negro, fuente_act) # Max 64 char
				txt10, posxytxt10 = print_pantalla((lista_textos_LvsInfinitos[Lv_act])[1], posxtxt91011121314, posytxt10, tamañotxt3, negro, fuente_act) # Max 64 char
				txt11, posxytxt11 = print_pantalla((lista_textos_LvsInfinitos[Lv_act])[2], posxtxt91011121314, posytxt11, tamañotxt3, negro, fuente_act) # Max 64 char
				txt12, posxytxt12 = print_pantalla((lista_textos_LvsInfinitos[Lv_act])[3], posxtxt91011121314, posytxt12, tamañotxt3, negro, fuente_act) # Max 64 char
				txt13, posxytxt13 = print_pantalla((lista_textos_LvsInfinitos[Lv_act])[4], posxtxt91011121314, posytxt13, tamañotxt3, negro, fuente_act) # Max 64 char
				txt14, posxytxt14 = print_pantalla("Nivel actual: " + str(Lv_act + 1), posxtxt1415, posytxt14, tamañotxt2, negro, fuente_act)
				txt15, posxytxt15 = print_pantalla("Infinito: True", posxtxt14151617, posytxt15, tamañotxt2, negro, fuente_act)
				txt16, posxytxt16 = print_pantalla("Boss: False", posxtxt14151617, posytxt16, tamañotxt2, negro, fuente_act)
				txt17, posxytxt17 = print_pantalla("Nº Naves: ∞", posxtxt14151617, posytxt17, tamañotxt2, negro, fuente_act)
				txt20, posxytxt20 = print_pantalla("Puntuacion: ", 0, posytxt20, tamañotxt2, negro, fuente_act)
				txt21, posxytxt21 = print_pantalla("Kills: " + str(kills), 0, posytxt21, tamañotxt2, negro, fuente_act)
				txt22, posxytxt22 = print_pantalla("%Llegado: " + str(porcentaje) + "%", 0, posytxt22, tamañotxt2, negro, fuente_act)
				txt23, posxytxt23 = print_pantalla("Muertes: " + str(muertes), 0, posytxt23, tamañotxt2, negro, fuente_act)
				txt24, posxytxt24 = print_pantalla("Tiempo: " + str(tiempo), 0, posytxt24, tamañotxt2, negro, fuente_act)
				txt25, posxytxt25 = print_pantalla(str(puntuacion), 0, posytxt25, tamañotxt2, negro, fuente_act)
				txt26, posxytxt26 = print_pantalla("Dificultad: ∞", posxtxt14151617, posytxt26, tamañotxt2, negro, fuente_act)
				txt27 = ["", ""]
				posxytxt27 = ""
				txt28, posxytxt28 = print_pantalla("Mejores", 0, posytxt28, tamañotxt2, negro, fuente_act)
				txt29, posxytxt29 = print_pantalla("estadisticas:", 0, posytxt29, tamañotxt2, negro, fuente_act)

			else:
				txt9 = ["", ""]
				posxytxt9 = ""
				txt10 = ["", ""]
				posxytxt10 = ""
				txt11, posxytxt11 = print_pantalla("         ==========INFORMACION DE NIVEL NO DISPONIBLE==========", posxtxt91011121314, posytxt11, tamañotxt2, negro, fuente_act) # Max 64 char
				txt12 = ["", ""]
				posxytxt12 = ""
				txt13 = ["", ""]
				posxytxt13 = ""
				txt14, posxytxt14 = print_pantalla("Nivel actual: ¿?", posxtxt1415, posytxt14, tamañotxt2, negro, fuente_act)
				txt15, posxytxt15 = print_pantalla("Infinito: True", posxtxt14151617, posytxt15, tamañotxt2, negro, fuente_act)
				txt16, posxytxt16 = print_pantalla("Boss: ¿?", posxtxt14151617, posytxt16, tamañotxt2, negro, fuente_act)
				txt17, posxytxt17 = print_pantalla("Nº Naves: ¿?", posxtxt14151617, posytxt17, tamañotxt2, negro, fuente_act)
				txt20, posxytxt20 = print_pantalla("Puntuacion: ", 0, posytxt20, tamañotxt2, negro, fuente_act)
				txt21, posxytxt21 = print_pantalla("Kills: ", 0, posytxt21, tamañotxt2, negro, fuente_act)
				txt22, posxytxt22 = print_pantalla("%Llegado: ", 0, posytxt22, tamañotxt2, negro, fuente_act)
				txt23, posxytxt23 = print_pantalla("Muertes: ", 0, posytxt23, tamañotxt2, negro, fuente_act)
				txt24, posxytxt24 = print_pantalla("Tiempo: ", 0, posytxt24, tamañotxt2, negro, fuente_act)
				txt25, posxytxt25 = print_pantalla("", 0, posytxt25, tamañotxt2, negro, fuente_act)
				txt26, posxytxt26 = print_pantalla("Dificultad: ¿?", posxtxt14151617, posytxt26, tamañotxt2, negro, fuente_act)
				txt27 = ["", ""]
				posxytxt27 = ""
				txt28, posxytxt28 = print_pantalla("Mejores", 0, posytxt28, tamañotxt2, negro, fuente_act)
				txt29, posxytxt29 = print_pantalla("estadisticas:", 0, posytxt29, tamañotxt2, negro, fuente_act)

		else:

			if posible == True:
				numero_de_naves_de_Lv_act = navestotales[Lv_act]

				txt9, posxytxt9 = print_pantalla((lista_textos[Lv_act])[0], posxtxt91011121314, posytxt9, tamañotxt3, negro, fuente_act) # Max 64 char
				txt10, posxytxt10 = print_pantalla((lista_textos[Lv_act])[1], posxtxt91011121314, posytxt10, tamañotxt3, negro, fuente_act) # Max 64 char
				txt11, posxytxt11 = print_pantalla((lista_textos[Lv_act])[2], posxtxt91011121314, posytxt11, tamañotxt3, negro, fuente_act) # Max 64 char
				txt12, posxytxt12 = print_pantalla((lista_textos[Lv_act])[3], posxtxt91011121314, posytxt12, tamañotxt3, negro, fuente_act) # Max 64 char
				txt13, posxytxt13 = print_pantalla((lista_textos[Lv_act])[4], posxtxt91011121314, posytxt13, tamañotxt3, negro, fuente_act) # Max 64 char
				txt14, posxytxt14 = print_pantalla("Nivel actual: " + str(Lv_act + 1), posxtxt14151617, posytxt14, tamañotxt2, negro, fuente_act)
				txt15, posxytxt15 = print_pantalla("Infinito: False", posxtxt14151617, posytxt15, tamañotxt2, negro, fuente_act)
				txt16, posxytxt16 = print_pantalla("Boss: " + str(boss), posxtxt14151617, posytxt16, tamañotxt2, negro, fuente_act)
				txt17, posxytxt17 = print_pantalla("Nº Naves: " + str(numero_de_naves_de_Lv_act), posxtxt14151617, posytxt17, tamañotxt2, negro, fuente_act)
				txt20, posxytxt20 = print_pantalla("Puntuacion: ", 0, posytxt20, tamañotxt2, negro, fuente_act)
				txt21, posxytxt21 = print_pantalla("Kills: " + str(kills), 0, posytxt21, tamañotxt2, negro, fuente_act)
				txt22, posxytxt22 = print_pantalla("%Llegado: " + str(porcentaje) + "%", 0, posytxt22, tamañotxt2, negro, fuente_act)
				txt23, posxytxt23 = print_pantalla("Muertes: " + str(muertes), 0, posytxt23, tamañotxt2, negro, fuente_act)
				txt24, posxytxt24 = print_pantalla("Tiempo: " + str(tiempo), 0, posytxt24, tamañotxt2, negro, fuente_act)
				txt25, posxytxt25 = print_pantalla(str(puntuacion), 0, posytxt25, tamañotxt2, negro, fuente_act)
				txt26, posxytxt26 = print_pantalla("Dificultad: ", posxtxt14151617, posytxt26, tamañotxt2, negro, fuente_act)
				txt27, posxytxt27 = print_pantalla(dificultades[Lv_act], posxtxt14151617, posytxt27, tamañotxt2, negro, fuente_act)
				txt28, posxytxt28 = print_pantalla("Mejores", 0, posytxt28, tamañotxt2, negro, fuente_act)
				txt29, posxytxt29 = print_pantalla("estadisticas:", 0, posytxt29, tamañotxt2, negro, fuente_act)

			else:
				txt9 = ["", ""]
				posxytxt9 = ""
				txt10 = ["", ""]
				posxytxt10 = ""
				txt11, posxytxt11 = print_pantalla("         ==========INFORMACION DE NIVEL NO DISPONIBLE==========", posxtxt91011121314, posytxt11, tamañotxt2, negro, fuente_act) # Max 64 char
				txt12 = ["", ""]
				posxytxt12 = ""
				txt13 = ["", ""]
				posxytxt13 = ""
				txt14, posxytxt14 = print_pantalla("Nivel actual: ¿?", posxtxt1415, posytxt14, tamañotxt2, negro, fuente_act)
				txt15, posxytxt15 = print_pantalla("Infinito: False", posxtxt14151617, posytxt15, tamañotxt2, negro, fuente_act)
				txt16, posxytxt16 = print_pantalla("Boss: ¿?", posxtxt14151617, posytxt16, tamañotxt2, negro, fuente_act)
				txt17, posxytxt17 = print_pantalla("Nº Naves: ¿?", posxtxt14151617, posytxt17, tamañotxt2, negro, fuente_act)
				txt20, posxytxt20 = print_pantalla("Puntuacion: ", 0, posytxt20, tamañotxt2, negro, fuente_act)
				txt21, posxytxt21 = print_pantalla("Kills: ", 0, posytxt21, tamañotxt2, negro, fuente_act)
				txt22, posxytxt22 = print_pantalla("%Llegado: ", 0, posytxt22, tamañotxt2, negro, fuente_act)
				txt23, posxytxt23 = print_pantalla("Muertes: ", 0, posytxt23, tamañotxt2, negro, fuente_act)
				txt24, posxytxt24 = print_pantalla("Tiempo: ", 0, posytxt24, tamañotxt2, negro, fuente_act)
				txt25, posxytxt25 = print_pantalla("", 0, posytxt25, tamañotxt2, negro, fuente_act)
				txt26, posxytxt26 = print_pantalla("Dificultad: ¿?", posxtxt14151617, posytxt26, tamañotxt2, negro, fuente_act)
				txt27 = ["", ""]
				posxytxt27 = ""
				txt28, posxytxt28 = print_pantalla("Mejores", 0, posytxt28, tamañotxt2, negro, fuente_act)
				txt29, posxytxt29 = print_pantalla("estadisticas:", 0, posytxt29, tamañotxt2, negro, fuente_act)


		return((txt9, posxytxt9), (txt10, posxytxt10), (txt11, posxytxt11), (txt12, posxytxt12), (txt13, posxytxt13), (txt14, posxytxt14), (txt15, posxytxt15), (txt16, posxytxt16), (txt17, posxytxt17), (txt20, posxytxt20), (txt21, posxytxt21), (txt22, posxytxt22), (txt23, posxytxt23), (txt24, posxytxt24), (txt25, posxytxt25), (txt26, posxytxt26), (txt27, posxytxt27), (txt28, posxytxt28), (txt29, posxytxt29))


	Exit_presionado = False

	bot5 = ["", ""]

	posimagx = round(0.15625 * ancho) #200
	posimagy = round(0.16666666666666666666666666666667 *alto) #120

	ventana.blit(imagen_fondo_seleccion_pantalla, (posimagx, posimagy))

	pygame.display.update()

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
	txt18, posxytxt18 = results1[12]
	txt30, posxytxt30 = results1[13]
	posesxybot6, posesxy2bot6, botonreturn6 = results1[14]

	punto1, punto2, punto3, punto4, punto5, punto6, sumgen = crear_recuadro_seleccionLv(ventana, nivel_act, pantalla_act)

	ajustes = extraer_ajustes()

	fuente_act = ajustes[3]

	if user_act[1] == "None":                                                                                  #=============PROHIBIR ELECCION DE NIVELES CON DEMO============
		output = generar_panel_informativo(caracteristicas_panelInfo, 0, 0, True, False, True)

		txt9, posxytxt9 = output[0]
		txt10, posxytxt10 = output[1]
		txt11, posxytxt11 = output[2]
		txt12, posxytxt12 = output[3]
		txt13, posxytxt13 = output[4]
		txt14, posxytxt14 = print_pantalla("Nivel actual: 1", posxtxt14151617, posytxt14, tamañotxt2, negro, fuente_act)
		txt15, posxytxt15 = output[6]
		txt16, posxytxt16 = output[7]
		txt17, posxytxt17 = output[8]
		txt20, posxytxt20 = output[9]
		txt21, posxytxt21 = output[10]
		txt22, posxytxt22 = output[11]
		txt23, posxytxt23 = output[12]
		txt24, posxytxt24 = output[13]
		txt25, posxytxt25 = output[14]
		txt26, posxytxt26 = output[15]
		txt27, posxytxt27 = output[16]
		txt28, posxytxt28 = output[17]
		txt29, posxytxt29 = output[18]
		txt19, posxytxt19 = print_pantalla("Pantalla: " + str(pantalla_act), 0, posytxt14, tamañotxt2, negro, fuente_act)

	else:
		txt9 = ["", ""]
		txt10 = ["", ""]
		txt11, posxytxt11 = print_pantalla("                            ==========DIARIO PERSONAL==========", posxtxt91011121314, posytxt11, tamañotxt2, negro, fuente_act) # Max 64 char
		txt12 = ["", ""]
		txt13 = ["", ""]
		txt14, posxytxt14 = print_pantalla("Nivel actual: ", posxtxt14151617, posytxt14, tamañotxt2, negro, fuente_act)
		txt15, posxytxt15 = print_pantalla("Infinito: ", posxtxt14151617, posytxt15, tamañotxt2, negro, fuente_act)
		txt16, posxytxt16 = print_pantalla("Boss: ", posxtxt14151617, posytxt16, tamañotxt2, negro, fuente_act)
		txt17, posxytxt17 = print_pantalla("Nº Naves: ", posxtxt14151617, posytxt17, tamañotxt2, negro, fuente_act)
		txt19, posxytxt19 = print_pantalla("Pantalla: " + str(pantalla_act), 0, posytxt14, tamañotxt2, negro, fuente_act)
		txt20, posxytxt20 = print_pantalla("Puntuacion: ", 0, posytxt20, tamañotxt2, negro, fuente_act)
		txt21, posxytxt21 = print_pantalla("Kills: ", 0, posytxt21, tamañotxt2, negro, fuente_act)
		txt22, posxytxt22 = print_pantalla("%Llegado: ", 0, posytxt22, tamañotxt2, negro, fuente_act)
		txt23, posxytxt23 = print_pantalla("Muertes: ", 0, posytxt23, tamañotxt2, negro, fuente_act)
		txt24, posxytxt24 = print_pantalla("Tiempo: ", 0, posytxt24, tamañotxt2, negro, fuente_act)
		txt25, posxytxt25 = print_pantalla("", 0, posytxt25, tamañotxt2, negro, fuente_act)
		txt26, posxytxt26 = print_pantalla("Dificultad: ", posxtxt14151617, posytxt26, tamañotxt2, negro, fuente_act)
		txt27, posxytxt27 = print_pantalla("", posxtxt14151617, posytxt27, tamañotxt2, negro, fuente_act)
		txt28, posxytxt28 = print_pantalla("Mejores", 0, posytxt28, tamañotxt2, negro, fuente_act)
		txt29, posxytxt29 = print_pantalla("estadisticas:", 0, posytxt29, tamañotxt2, negro, fuente_act)


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
	ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
	ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))
	ventana.blit(botonreturn6, (posesxybot6[0], posesxybot6[1]))

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

				elif evento.key == 27:

					bot5 = ["", ""]

					ajustes = extraer_ajustes()
			
					ancho = int(ajustes[0])
					alto = int(ajustes[1])

					fuente_act = ajustes[3]

					try:
						pygame.display.set_mode((ancho, alto))
					except:
						pass

					actualizar_dato("pantcomp", False)

					ventana.fill(gris_fondo)

					txt9 = ["", ""]
					txt10 = ["", ""]
					txt11, posxytxt11 = print_pantalla("                            ==========DIARIO PERSONAL==========", posxtxt91011121314, posytxt11, tamañotxt2, negro, fuente_act) # Max 64 char
					txt12 = ["", ""]
					txt13 = ["", ""]
					txt14, posxytxt14 = print_pantalla("Nivel actual: ", posxtxt14151617, posytxt14, tamañotxt2, negro, fuente_act)
					txt15, posxytxt15 = print_pantalla("Infinito: ", posxtxt14151617, posytxt15, tamañotxt2, negro, fuente_act)
					txt16, posxytxt16 = print_pantalla("Boss: ", posxtxt14151617, posytxt16, tamañotxt2, negro, fuente_act)
					txt17, posxytxt17 = print_pantalla("Nº Naves: ", posxtxt14151617, posytxt17, tamañotxt2, negro, fuente_act)
					txt19, posxytxt19 = print_pantalla("Pantalla: " + str(pantalla_act), 0, posytxt14, tamañotxt2, negro, fuente_act)
					txt20, posxytxt20 = print_pantalla("Puntuacion: ", 0, posytxt20, tamañotxt2, negro, fuente_act)
					txt21, posxytxt21 = print_pantalla("Kills: ", 0, posytxt21, tamañotxt2, negro, fuente_act)
					txt22, posxytxt22 = print_pantalla("%Llegado: ", 0, posytxt22, tamañotxt2, negro, fuente_act)
					txt23, posxytxt23 = print_pantalla("Muertes: ", 0, posytxt23, tamañotxt2, negro, fuente_act)
					txt24, posxytxt24 = print_pantalla("Tiempo: ", 0, posytxt24, tamañotxt2, negro, fuente_act)
					txt25, posxytxt25 = print_pantalla("", 0, posytxt25, tamañotxt2, negro, fuente_act)
					txt26, posxytxt26 = print_pantalla("Dificultad: ", posxtxt14151617, posytxt26, tamañotxt2, negro, fuente_act)
					txt27, posxytxt27 = print_pantalla("", posxtxt14151617, posytxt27, tamañotxt2, negro, fuente_act)
					txt28, posxytxt28 = print_pantalla("Mejores", 0, posytxt28, tamañotxt2, negro, fuente_act)
					txt29, posxytxt29 = print_pantalla("estadisticas:", 0, posytxt29, tamañotxt2, negro, fuente_act)

					ventana.blit(imagen_fondo_seleccion_pantalla, (posimagx, posimagy))

					pygame.display.update()

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
					txt18, posxytxt18 = results1[12]
					txt30, posxytxt30 = results1[13]
					posesxybot6, posesxy2bot6, botonreturn6 = results1[14]

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
					ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
					ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))
					ventana.blit(botonreturn6, (posesxybot6[0], posesxybot6[1]))

					pygame.display.update()

				elif evento.key == 292:

					bot5 = ["", ""]

					ajustes = extraer_ajustes()
			
					ancho = int(ajustes[0])
					alto = int(ajustes[1])

					fuente_act = ajustes[3]

					try:
						pygame.display.set_mode((ancho, alto), pygame.FULLSCREEN)
					except:
						pass

					actualizar_dato("pantcomp", True)

					ventana.fill(gris_fondo)

					txt9 = ["", ""]
					txt10 = ["", ""]
					txt11, posxytxt11 = print_pantalla("                            ==========DIARIO PERSONAL==========", posxtxt91011121314, posytxt11, tamañotxt2, negro, fuente_act) # Max 64 char
					txt12 = ["", ""]
					txt13 = ["", ""]
					txt14, posxytxt14 = print_pantalla("Nivel actual: ", posxtxt14151617, posytxt14, tamañotxt2, negro, fuente_act)
					txt15, posxytxt15 = print_pantalla("Infinito: ", posxtxt14151617, posytxt15, tamañotxt2, negro, fuente_act)
					txt16, posxytxt16 = print_pantalla("Boss: ", posxtxt14151617, posytxt16, tamañotxt2, negro, fuente_act)
					txt17, posxytxt17 = print_pantalla("Nº Naves: ", posxtxt14151617, posytxt17, tamañotxt2, negro, fuente_act)
					txt19, posxytxt19 = print_pantalla("Pantalla: " + str(pantalla_act), 0, posytxt14, tamañotxt2, negro, fuente_act)
					txt20, posxytxt20 = print_pantalla("Puntuacion: ", 0, posytxt20, tamañotxt2, negro, fuente_act)
					txt21, posxytxt21 = print_pantalla("Kills: ", 0, posytxt21, tamañotxt2, negro, fuente_act)
					txt22, posxytxt22 = print_pantalla("%Llegado: ", 0, posytxt22, tamañotxt2, negro, fuente_act)
					txt23, posxytxt23 = print_pantalla("Muertes: ", 0, posytxt23, tamañotxt2, negro, fuente_act)
					txt24, posxytxt24 = print_pantalla("Tiempo: ", 0, posytxt24, tamañotxt2, negro, fuente_act)
					txt25, posxytxt25 = print_pantalla("", 0, posytxt25, tamañotxt2, negro, fuente_act)
					txt26, posxytxt26 = print_pantalla("Dificultad: ", posxtxt14151617, posytxt26, tamañotxt2, negro, fuente_act)
					txt27, posxytxt27 = print_pantalla("", posxtxt14151617, posytxt27, tamañotxt2, negro, fuente_act)
					txt28, posxytxt28 = print_pantalla("Mejores", 0, posytxt28, tamañotxt2, negro, fuente_act)
					txt29, posxytxt29 = print_pantalla("estadisticas:", 0, posytxt29, tamañotxt2, negro, fuente_act)

					ventana.blit(imagen_fondo_seleccion_pantalla, (posimagx, posimagy))

					pygame.display.update()

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
					txt18, posxytxt18 = results1[12]
					txt30, posxytxt30 = results1[13]
					posesxybot6, posesxy2bot6, botonreturn6 = results1[14]

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
					ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
					ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))
					ventana.blit(botonreturn6, (posesxybot6[0], posesxybot6[1]))

					pygame.display.update()

			elif ratonx > punto1[0] - sumgen and ratony > punto1[1] - sumgen and ratonx < punto1[0] + sumgen and ratony < punto1[1] + sumgen:

				if evento.type == MOUSEBUTTONDOWN:
					print("Nivel: " + str(5 * (pantalla_act - 1) + 1))

					ventana.fill(gris_fondo)

					if nivel_act < (5 * (pantalla_act - 1)):
						bot5 = ["",""]
						posible = False

					elif nivel_act >= (5 * (pantalla_act - 1)):
						bot5 = crear_boton3(ventana, posx1bot5, posy1bot5, posx2bot5, posy2bot5, "COMENZAR", tamañotxt2, tamañopolygon, errordebotgeneral, negro, fuente_act, negro)
						posesxybot5, posesxy2bot5 = bot5[1]
						posible = True

					if user_act[1] != "None":
						Demo = False

					else:
						Demo = True

					nivelpulsado = 5 * (pantalla_act - 1) + 1
					infinitopulsado = False

					output = generar_panel_informativo(caracteristicas_panelInfo, 5 * (pantalla_act - 1), pantalla_act, Demo, False, posible)

					if Demo == True and pantalla_act == 1:

						txt9, posxytxt9 = output[0]
						txt10, posxytxt10 = output[1]
						txt11, posxytxt11 = output[2]
						txt12, posxytxt12 = output[3]
						txt13, posxytxt13 = output[4]
						txt14, posxytxt14 = print_pantalla("Nivel actual: 1", posxtxt14151617, posytxt14, tamañotxt2, negro, fuente_act)
						txt15, posxytxt15 = print_pantalla("Infinito: False", posxtxt14151617, posytxt15, tamañotxt2, negro, fuente_act)
						txt16, posxytxt16 = print_pantalla("Boss: False", posxtxt14151617, posytxt16, tamañotxt2, negro, fuente_act)
						txt17, posxytxt17 = print_pantalla("Nº Naves: 15", posxtxt14151617, posytxt17, tamañotxt2, negro, fuente_act)
						txt20, posxytxt20 = print_pantalla("Puntuacion: ", 0, posytxt20, tamañotxt2, negro, fuente_act)
						txt21, posxytxt21 = print_pantalla("Kills: 0", 0, posytxt21, tamañotxt2, negro, fuente_act)
						txt22, posxytxt22 = print_pantalla("%Llegado: 0%", 0, posytxt22, tamañotxt2, negro, fuente_act)
						txt23, posxytxt23 = print_pantalla("Muertes: 0", 0, posytxt23, tamañotxt2, negro, fuente_act)
						txt24, posxytxt24 = print_pantalla("Tiempo: 0.0", 0, posytxt24, tamañotxt2, negro, fuente_act)
						txt25, posxytxt25 = print_pantalla(str(0), 0, posytxt25, tamañotxt2, negro, fuente_act)
						txt26, posxytxt26 = print_pantalla("Dificultad: ", posxtxt14151617, posytxt26, tamañotxt2, negro, fuente_act)
						txt27, posxytxt27 = print_pantalla("Muy Fácil", posxtxt14151617, posytxt27, tamañotxt2, negro, fuente_act)
						txt28, posxytxt28 = print_pantalla("Mejores", 0, posytxt28, tamañotxt2, negro, fuente_act)
						txt29, posxytxt29 = print_pantalla("estadisticas:", 0, posytxt29, tamañotxt2, negro, fuente_act)

					else:

						txt9, posxytxt9 = output[0]
						txt10, posxytxt10 = output[1]
						txt11, posxytxt11 = output[2]
						txt12, posxytxt12 = output[3]
						txt13, posxytxt13 = output[4]
						txt14, posxytxt14 = output[5]
						txt15, posxytxt15 = output[6]
						txt16, posxytxt16 = output[7]
						txt17, posxytxt17 = output[8]
						txt20, posxytxt20 = output[9]
						txt21, posxytxt21 = output[10]
						txt22, posxytxt22 = output[11]
						txt23, posxytxt23 = output[12]
						txt24, posxytxt24 = output[13]
						txt25, posxytxt25 = output[14]
						txt26, posxytxt26 = output[15]
						txt27, posxytxt27 = output[16]
						txt28, posxytxt28 = output[17]
						txt29, posxytxt29 = output[18]

					posimagx = round(0.15625 * ancho) #200
					posimagy = round(0.16666666666666666666666666666667 *alto) #120

					ventana.blit(imagen_fondo_seleccion_pantalla, (posimagx, posimagy))

					pygame.display.update()

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
					txt18, posxytxt18 = results1[12]
					txt30, posxytxt30 = results1[13]
					posesxybot6, posesxy2bot6, botonreturn6 = results1[14]

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
					ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
					ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))
					ventana.blit(botonreturn6, (posesxybot6[0], posesxybot6[1]))
					if bot5 != ["", ""]: ventana.blit(bot5[0], (posesxybot5[0], posesxybot5[1]))

					pygame.display.update()

			elif user_act[1] != "None" and ratonx > punto2[0] - sumgen and ratony > punto2[1] - sumgen and ratonx < punto2[0] + sumgen and ratony < punto2[1] + sumgen:

				if evento.type == MOUSEBUTTONDOWN:
					print("Nivel: " + str(5 * (pantalla_act - 1) + 2))

					ventana.fill(gris_fondo)

					if nivel_act < (5 * (pantalla_act - 1) + 1):
						bot5 = ["",""]
						posible = False

					elif nivel_act >= (5 * (pantalla_act - 1) + 1):
						bot5 = crear_boton3(ventana, posx1bot5, posy1bot5, posx2bot5, posy2bot5, "COMENZAR", tamañotxt2, tamañopolygon, errordebotgeneral, negro, fuente_act, negro)
						posesxybot5, posesxy2bot5 = bot5[1]
						posible = True

					nivelpulsado = 5 * (pantalla_act - 1) + 2
					infinitopulsado = False

					output = generar_panel_informativo(caracteristicas_panelInfo, 5 * (pantalla_act - 1) + 1, pantalla_act, False, False, posible)

					txt9, posxytxt9 = output[0]
					txt10, posxytxt10 = output[1]
					txt11, posxytxt11 = output[2]
					txt12, posxytxt12 = output[3]
					txt13, posxytxt13 = output[4]
					txt14, posxytxt14 = output[5]
					txt15, posxytxt15 = output[6]
					txt16, posxytxt16 = output[7]
					txt17, posxytxt17 = output[8]
					txt20, posxytxt20 = output[9]
					txt21, posxytxt21 = output[10]
					txt22, posxytxt22 = output[11]
					txt23, posxytxt23 = output[12]
					txt24, posxytxt24 = output[13]
					txt25, posxytxt25 = output[14]
					txt26, posxytxt26 = output[15]
					txt27, posxytxt27 = output[16]
					txt28, posxytxt28 = output[17]
					txt29, posxytxt29 = output[18]

					posimagx = round(0.15625 * ancho) #200
					posimagy = round(0.16666666666666666666666666666667 *alto) #120

					ventana.blit(imagen_fondo_seleccion_pantalla, (posimagx, posimagy))

					pygame.display.update()

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
					txt18, posxytxt18 = results1[12]
					txt30, posxytxt30 = results1[13]
					posesxybot6, posesxy2bot6, botonreturn6 = results1[14]

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
					ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
					ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))
					ventana.blit(botonreturn6, (posesxybot6[0], posesxybot6[1]))
					if bot5 != ["", ""]: ventana.blit(bot5[0], (posesxybot5[0], posesxybot5[1]))

					pygame.display.update()

			elif user_act[1] != "None" and ratonx > punto3[0] - sumgen and ratony > punto3[1] - sumgen and ratonx < punto3[0] + sumgen and ratony < punto3[1] + sumgen:

				if evento.type == MOUSEBUTTONDOWN:
					print("Nivel: " + str(5 * (pantalla_act - 1) + 3))

					ventana.fill(gris_fondo)

					if nivel_act < (5 * (pantalla_act - 1) + 2):
						bot5 = ["",""]
						posible = False

					elif nivel_act >= (5 * (pantalla_act - 1) + 2):
						bot5 = crear_boton3(ventana, posx1bot5, posy1bot5, posx2bot5, posy2bot5, "COMENZAR", tamañotxt2, tamañopolygon, errordebotgeneral, negro, fuente_act, negro)
						posesxybot5, posesxy2bot5 = bot5[1]
						posible = True

					nivelpulsado = 5 * (pantalla_act - 1) + 3
					infinitopulsado = False

					output = generar_panel_informativo(caracteristicas_panelInfo, 5 * (pantalla_act - 1) + 2, pantalla_act, False, False, posible)

					txt9, posxytxt9 = output[0]
					txt10, posxytxt10 = output[1]
					txt11, posxytxt11 = output[2]
					txt12, posxytxt12 = output[3]
					txt13, posxytxt13 = output[4]
					txt14, posxytxt14 = output[5]
					txt15, posxytxt15 = output[6]
					txt16, posxytxt16 = output[7]
					txt17, posxytxt17 = output[8]
					txt20, posxytxt20 = output[9]
					txt21, posxytxt21 = output[10]
					txt22, posxytxt22 = output[11]
					txt23, posxytxt23 = output[12]
					txt24, posxytxt24 = output[13]
					txt25, posxytxt25 = output[14]
					txt26, posxytxt26 = output[15]
					txt27, posxytxt27 = output[16]
					txt28, posxytxt28 = output[17]
					txt29, posxytxt29 = output[18]

					posimagx = round(0.15625 * ancho) #200
					posimagy = round(0.16666666666666666666666666666667 *alto) #120

					ventana.blit(imagen_fondo_seleccion_pantalla, (posimagx, posimagy))

					pygame.display.update()

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
					txt18, posxytxt18 = results1[12]
					txt30, posxytxt30 = results1[13]
					posesxybot6, posesxy2bot6, botonreturn6 = results1[14]

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
					ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
					ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))
					ventana.blit(botonreturn6, (posesxybot6[0], posesxybot6[1]))
					if bot5 != ["", ""]: ventana.blit(bot5[0], (posesxybot5[0], posesxybot5[1]))

					pygame.display.update()

			elif user_act[1] != "None" and ratonx > punto4[0] - sumgen and ratony > punto4[1] - sumgen and ratonx < punto4[0] + sumgen and ratony < punto4[1] + sumgen:

				if evento.type == MOUSEBUTTONDOWN:
					print("Nivel: " + str(5 * (pantalla_act - 1) + 4))

					ventana.fill(gris_fondo)

					if nivel_act < (5 * (pantalla_act - 1) + 3):
						bot5 = ["",""]
						posible = False

					elif nivel_act >= (5 * (pantalla_act - 1) + 3):
						bot5 = crear_boton3(ventana, posx1bot5, posy1bot5, posx2bot5, posy2bot5, "COMENZAR", tamañotxt2, tamañopolygon, errordebotgeneral, negro, fuente_act, negro)
						posesxybot5, posesxy2bot5 = bot5[1]
						posible = True

					nivelpulsado = 5 * (pantalla_act - 1) + 4
					infinitopulsado = False

					output = generar_panel_informativo(caracteristicas_panelInfo, 5 * (pantalla_act - 1) + 3, pantalla_act, False, False, posible)

					txt9, posxytxt9 = output[0]
					txt10, posxytxt10 = output[1]
					txt11, posxytxt11 = output[2]
					txt12, posxytxt12 = output[3]
					txt13, posxytxt13 = output[4]
					txt14, posxytxt14 = output[5]
					txt15, posxytxt15 = output[6]
					txt16, posxytxt16 = output[7]
					txt17, posxytxt17 = output[8]
					txt20, posxytxt20 = output[9]
					txt21, posxytxt21 = output[10]
					txt22, posxytxt22 = output[11]
					txt23, posxytxt23 = output[12]
					txt24, posxytxt24 = output[13]
					txt25, posxytxt25 = output[14]
					txt26, posxytxt26 = output[15]
					txt27, posxytxt27 = output[16]
					txt28, posxytxt28 = output[17]
					txt29, posxytxt29 = output[18]

					posimagx = round(0.15625 * ancho) #200
					posimagy = round(0.16666666666666666666666666666667 *alto) #120

					ventana.blit(imagen_fondo_seleccion_pantalla, (posimagx, posimagy))

					pygame.display.update()

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
					txt18, posxytxt18 = results1[12]
					txt30, posxytxt30 = results1[13]
					posesxybot6, posesxy2bot6, botonreturn6 = results1[14]

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
					ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
					ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))
					ventana.blit(botonreturn6, (posesxybot6[0], posesxybot6[1]))
					if bot5 != ["", ""]: ventana.blit(bot5[0], (posesxybot5[0], posesxybot5[1]))

					pygame.display.update()

			elif user_act[1] != "None" and ratonx > punto5[0] - sumgen and ratony > punto5[1] - sumgen and ratonx < punto5[0] + sumgen and ratony < punto5[1] + sumgen:

				if evento.type == MOUSEBUTTONDOWN:
					print("Nivel: " + str(5 * (pantalla_act - 1) + 5))

					ventana.fill(gris_fondo)

					if nivel_act < (5 * (pantalla_act - 1) + 4):
						bot5 = ["",""]
						posible = False

					elif nivel_act >= (5 * (pantalla_act - 1) + 4):
						bot5 = crear_boton3(ventana, posx1bot5, posy1bot5, posx2bot5, posy2bot5, "COMENZAR", tamañotxt2, tamañopolygon, errordebotgeneral, negro, fuente_act, negro)
						posesxybot5, posesxy2bot5 = bot5[1]
						posible = True

					nivelpulsado = 5 * (pantalla_act - 1) + 5
					infinitopulsado = False

					output = generar_panel_informativo(caracteristicas_panelInfo, 5 * (pantalla_act - 1) + 4, pantalla_act, False, False, posible)

					txt9, posxytxt9 = output[0]
					txt10, posxytxt10 = output[1]
					txt11, posxytxt11 = output[2]
					txt12, posxytxt12 = output[3]
					txt13, posxytxt13 = output[4]
					txt14, posxytxt14 = output[5]
					txt15, posxytxt15 = output[6]
					txt16, posxytxt16 = output[7]
					txt17, posxytxt17 = output[8]
					txt20, posxytxt20 = output[9]
					txt21, posxytxt21 = output[10]
					txt22, posxytxt22 = output[11]
					txt23, posxytxt23 = output[12]
					txt24, posxytxt24 = output[13]
					txt25, posxytxt25 = output[14]
					txt26, posxytxt26 = output[15]
					txt27, posxytxt27 = output[16]
					txt28, posxytxt28 = output[17]
					txt29, posxytxt29 = output[18]

					posimagx = round(0.15625 * ancho) #200
					posimagy = round(0.16666666666666666666666666666667 *alto) #120

					ventana.blit(imagen_fondo_seleccion_pantalla, (posimagx, posimagy))

					pygame.display.update()

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
					txt18, posxytxt18 = results1[12]
					txt30, posxytxt30 = results1[13]
					posesxybot6, posesxy2bot6, botonreturn6 = results1[14]

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
					ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
					ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))
					ventana.blit(botonreturn6, (posesxybot6[0], posesxybot6[1]))
					if bot5 != ["", ""]: ventana.blit(bot5[0], (posesxybot5[0], posesxybot5[1]))

					pygame.display.update()

			elif user_act[1] != "None" and ratonx > punto6[0] - sumgen and ratony > punto6[1] - sumgen and ratonx < punto6[0] + sumgen and ratony < punto6[1] + sumgen:

				if evento.type == MOUSEBUTTONDOWN:

					print("Nivel Infinito: " + str(pantalla_act))

					ventana.fill(gris_fondo)

					if nivel_necesario_paraInf[pantalla_act - 1] <= nivel_act:
						bot5 = crear_boton3(ventana, posx1bot5, posy1bot5, posx2bot5, posy2bot5, "COMENZAR", tamañotxt2, tamañopolygon, errordebotgeneral, negro, fuente_act, negro)
						posesxybot5, posesxy2bot5 = bot5[1]
						posible = True

					else:
						bot5 = ["", ""]
						posible = False

					nivelpulsado = pantalla_act
					infinitopulsado = True

					output = generar_panel_informativo(caracteristicas_panelInfo, pantalla_act - 1, pantalla_act, False, True, posible)

					txt9, posxytxt9 = output[0]
					txt10, posxytxt10 = output[1]
					txt11, posxytxt11 = output[2]
					txt12, posxytxt12 = output[3]
					txt13, posxytxt13 = output[4]
					txt14, posxytxt14 = output[5]
					txt15, posxytxt15 = output[6]
					txt16, posxytxt16 = output[7]
					txt17, posxytxt17 = output[8]
					txt20, posxytxt20 = output[9]
					txt21, posxytxt21 = output[10]
					txt22, posxytxt22 = output[11]
					txt23, posxytxt23 = output[12]
					txt24, posxytxt24 = output[13]
					txt25, posxytxt25 = output[14]
					txt26, posxytxt26 = output[15]
					txt27, posxytxt27 = output[16]
					txt28, posxytxt28 = output[17]
					txt29, posxytxt29 = output[18]

					posimagx = round(0.15625 * ancho) #200
					posimagy = round(0.16666666666666666666666666666667 *alto) #120

					ventana.blit(imagen_fondo_seleccion_pantalla, (posimagx, posimagy))

					pygame.display.update()

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
					txt18, posxytxt18 = results1[12]
					txt30, posxytxt30 = results1[13]
					posesxybot6, posesxy2bot6, botonreturn6 = results1[14]

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
					ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
					ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))
					ventana.blit(botonreturn6, (posesxybot6[0], posesxybot6[1]))
					if bot5 != ["", ""]: ventana.blit(bot5[0], (posesxybot5[0], posesxybot5[1]))

					pygame.display.update()

			elif ratonx > posx1flecha1 and ratony > posy1flecha1 and ratonx < posx2flecha1 and ratony < posy2flecha1:

				if evento.type == MOUSEBUTTONDOWN and pantalla_act != 1:

					bot5 = ["", ""]

					if pantalla_act > 1:
						pantalla_act -= 1

					print("Pantalla: " + str(pantalla_act))

					if user_act[1] == "None":                                                                                  #=============PROHIBIR ELECCION DE NIVELES CON DEMO============
						output = generar_panel_informativo(caracteristicas_panelInfo, 0, 0, True, False, True)

						txt9, posxytxt9 = output[0]
						txt10, posxytxt10 = output[1]
						txt11, posxytxt11 = output[2]
						txt12, posxytxt12 = output[3]
						txt13, posxytxt13 = output[4]
						txt14, posxytxt14 = print_pantalla("Nivel actual: 1", posxtxt14151617, posytxt14, tamañotxt2, negro, fuente_act)
						txt15, posxytxt15 = output[6]
						txt16, posxytxt16 = output[7]
						txt17, posxytxt17 = output[8]
						txt20, posxytxt20 = output[9]
						txt21, posxytxt21 = output[10]
						txt22, posxytxt22 = output[11]
						txt23, posxytxt23 = output[12]
						txt24, posxytxt24 = output[13]
						txt25, posxytxt25 = output[14]
						txt26, posxytxt26 = output[15]
						txt27, posxytxt27 = output[16]
						txt28, posxytxt28 = output[17]
						txt29, posxytxt29 = output[18]
						txt19, posxytxt19 = print_pantalla("Pantalla: " + str(pantalla_act), 0, posytxt14, tamañotxt2, negro, fuente_act)

					else:

						txt9 = ["", ""]
						txt10 = ["", ""]
						txt11, posxytxt11 = print_pantalla("                            ==========DIARIO PERSONAL==========", posxtxt91011121314, posytxt11, tamañotxt2, negro, fuente_act) # Max 64 char
						txt12 = ["", ""]
						txt13 = ["", ""]
						txt14, posxytxt14 = print_pantalla("Nivel actual: ", posxtxt14151617, posytxt14, tamañotxt2, negro, fuente_act)
						txt15, posxytxt15 = print_pantalla("Infinito: ", posxtxt14151617, posytxt15, tamañotxt2, negro, fuente_act)
						txt16, posxytxt16 = print_pantalla("Boss: ", posxtxt14151617, posytxt16, tamañotxt2, negro, fuente_act)
						txt17, posxytxt17 = print_pantalla("Nº Naves: ", posxtxt14151617, posytxt17, tamañotxt2, negro, fuente_act)
						txt19, posxytxt19 = print_pantalla("Pantalla: " + str(pantalla_act), 0, posytxt14, tamañotxt2, negro, fuente_act)
						txt20, posxytxt20 = print_pantalla("Puntuacion: ", 0, posytxt20, tamañotxt2, negro, fuente_act)
						txt21, posxytxt21 = print_pantalla("Kills: ", 0, posytxt21, tamañotxt2, negro, fuente_act)
						txt22, posxytxt22 = print_pantalla("%Llegado: ", 0, posytxt22, tamañotxt2, negro, fuente_act)
						txt23, posxytxt23 = print_pantalla("Muertes: ", 0, posytxt23, tamañotxt2, negro, fuente_act)
						txt24, posxytxt24 = print_pantalla("Tiempo: ", 0, posytxt24, tamañotxt2, negro, fuente_act)
						txt25, posxytxt25 = print_pantalla("", 0, posytxt25, tamañotxt2, negro, fuente_act)
						txt26, posxytxt26 = print_pantalla("Dificultad: ", posxtxt14151617, posytxt26, tamañotxt2, negro, fuente_act)
						txt27, posxytxt27 = print_pantalla("", posxtxt14151617, posytxt27, tamañotxt2, negro, fuente_act)
						txt28, posxytxt28 = print_pantalla("Mejores", 0, posytxt28, tamañotxt2, negro, fuente_act)
						txt29, posxytxt29 = print_pantalla("estadisticas:", 0, posytxt29, tamañotxt2, negro, fuente_act)

					ventana.fill(gris_fondo)

					posimagx = round(0.15625 * ancho) #200
					posimagy = round(0.16666666666666666666666666666667 *alto) #120

					ventana.blit(imagen_fondo_seleccion_pantalla, (posimagx, posimagy))

					pygame.display.update()

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
					txt18, posxytxt18 = results1[12]
					txt30, posxytxt30 = results1[13]
					posesxybot6, posesxy2bot6, botonreturn6 = results1[14]

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
					ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
					ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))
					ventana.blit(botonreturn6, (posesxybot6[0], posesxybot6[1]))

					pygame.display.update()

			elif ratonx > posx1flecha2 and ratony > posy1flecha2 and ratonx < posx2flecha2 and ratony < posy2flecha2:

				if evento.type == MOUSEBUTTONDOWN and pantalla_act != 5 and user_act[1] != "None":

					bot5 = ["", ""]

					if pantalla_act < 5:
						pantalla_act += 1

					print("Pantalla: " + str(pantalla_act))

					if user_act[1] == "None":                                                                                  #=============PROHIBIR ELECCION DE NIVELES CON DEMO============
						output = generar_panel_informativo(caracteristicas_panelInfo, 0, 0, True, False, True)

						txt9, posxytxt9 = output[0]
						txt10, posxytxt10 = output[1]
						txt11, posxytxt11 = output[2]
						txt12, posxytxt12 = output[3]
						txt13, posxytxt13 = output[4]
						txt14, posxytxt14 = print_pantalla("Nivel actual: 1", posxtxt14151617, posytxt14, tamañotxt2, negro, fuente_act)
						txt15, posxytxt15 = output[6]
						txt16, posxytxt16 = output[7]
						txt17, posxytxt17 = output[8]
						txt20, posxytxt20 = output[9]
						txt21, posxytxt21 = output[10]
						txt22, posxytxt22 = output[11]
						txt23, posxytxt23 = output[12]
						txt24, posxytxt24 = output[13]
						txt25, posxytxt25 = output[14]
						txt26, posxytxt26 = output[15]
						txt27, posxytxt27 = output[16]
						txt28, posxytxt28 = output[17]
						txt29, posxytxt29 = output[18]
						txt19, posxytxt19 = print_pantalla("Pantalla: " + str(pantalla_act), 0, posytxt14, tamañotxt2, negro, fuente_act)

					else:

						txt9 = ["", ""]
						txt10 = ["", ""]
						txt11, posxytxt11 = print_pantalla("                            ==========DIARIO PERSONAL==========", posxtxt91011121314, posytxt11, tamañotxt2, negro, fuente_act) # Max 64 char
						txt12 = ["", ""]
						txt13 = ["", ""]
						txt14, posxytxt14 = print_pantalla("Nivel actual: ", posxtxt14151617, posytxt14, tamañotxt2, negro, fuente_act)
						txt15, posxytxt15 = print_pantalla("Infinito: ", posxtxt14151617, posytxt15, tamañotxt2, negro, fuente_act)
						txt16, posxytxt16 = print_pantalla("Boss: ", posxtxt14151617, posytxt16, tamañotxt2, negro, fuente_act)
						txt17, posxytxt17 = print_pantalla("Nº Naves: ", posxtxt14151617, posytxt17, tamañotxt2, negro, fuente_act)
						txt19, posxytxt19 = print_pantalla("Pantalla: " + str(pantalla_act), 0, posytxt14, tamañotxt2, negro, fuente_act)
						txt20, posxytxt20 = print_pantalla("Puntuacion: ", 0, posytxt20, tamañotxt2, negro, fuente_act)
						txt21, posxytxt21 = print_pantalla("Kills: ", 0, posytxt21, tamañotxt2, negro, fuente_act)
						txt22, posxytxt22 = print_pantalla("%Llegado: ", 0, posytxt22, tamañotxt2, negro, fuente_act)
						txt23, posxytxt23 = print_pantalla("Muertes: ", 0, posytxt23, tamañotxt2, negro, fuente_act)
						txt24, posxytxt24 = print_pantalla("Tiempo: ", 0, posytxt24, tamañotxt2, negro, fuente_act)
						txt25, posxytxt25 = print_pantalla("", 0, posytxt25, tamañotxt2, negro, fuente_act)
						txt26, posxytxt26 = print_pantalla("Dificultad: ", posxtxt14151617, posytxt26, tamañotxt2, negro, fuente_act)
						txt27, posxytxt27 = print_pantalla("", posxtxt14151617, posytxt27, tamañotxt2, negro, fuente_act)
						txt28, posxytxt28 = print_pantalla("Mejores", 0, posytxt28, tamañotxt2, negro, fuente_act)
						txt29, posxytxt29 = print_pantalla("estadisticas:", 0, posytxt29, tamañotxt2, negro, fuente_act)

					ventana.fill(gris_fondo)

					posimagx = round(0.15625 * ancho) #200
					posimagy = round(0.16666666666666666666666666666667 *alto) #120

					ventana.blit(imagen_fondo_seleccion_pantalla, (posimagx, posimagy))

					pygame.display.update()

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
					txt18, posxytxt18 = results1[12]
					txt30, posxytxt30 = results1[13]
					posesxybot6, posesxy2bot6, botonreturn6 = results1[14]

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
					ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
					ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))
					ventana.blit(botonreturn6, (posesxybot6[0], posesxybot6[1]))

					pygame.display.update()

			elif ratonx > posesxybot1[0] -  errordebotgeneral and ratony > posesxybot1[1] - errordebotgeneral and ratonx < posesxy2bot1[0] and ratony < posesxy2bot1[1]:

				if evento.type == MOUSEBUTTONDOWN:

					Exit_presionado = True

			elif bot5 != ["", ""] and ratonx > posx1bot5 -  errordebotgeneral and ratony > posy1bot5 - errordebotgeneral and ratonx < posx2bot5 and ratony < posy2bot5:

				if evento.type == MOUSEBUTTONDOWN:

					print("Boton comenzar pulsado Comenzando...")

					ventana.fill(negro)

					num = random.randrange(len(frases_de_carga) +1)

					frase = frases_de_carga[num - 1]

					lista = []

					lista.extend(frase)

					if user_act[1] == None:
						demo = True

					else:
						demo = False

					ajustes = extraer_ajustes()

					ancho = int(ajustes[0])
					alto = int(ajustes[1])

					txtx_1 = calcularx(frase, ancho)

					txt_1, posxytxt_1 = print_pantalla(frase, (ancho - txtx_1)/2, round(0.60416666666666666666666666666667 * alto), tamañotxt2, blanco, fuente_act)
					ventana.blit(txt_1, (posxytxt_1[0], posxytxt_1[1]))
					pygame.display.update()

					num = 0

					dire = "Imagenes/Barra/Barra0.png" #Copiar desde aquí
					barra_alpha = pygame.image.load(dire)
					barra = pygame.transform.scale(barra_alpha, (round(0.2265625 * ancho), round(0.20833333333333333333333333333333 * alto)))
					ventana.fill(negro)
					ventana.blit(barra, (round(0.38671875 * ancho), round(0.39583333333333333333333333333333 * alto)))
					ventana.blit(txt_1, (posxytxt_1[0], posxytxt_1[1]))
					pygame.display.update() #Hasta aqui

					ejecutar_juego(ventana, user_act, nivelpulsado, infinitopulsado, pantalla_act, demo, navestotales[nivelpulsado - 1], txt_1, posxytxt_1)

					pygame.mouse.set_visible(True)

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
					txt18, posxytxt18 = results1[12]
					txt30, posxytxt30 = results1[13]
					posesxybot6, posesxy2bot6, botonreturn6 = results1[14]

					txt9 = ["", ""]
					txt10 = ["", ""]
					txt11, posxytxt11 = print_pantalla("                            ==========DIARIO PERSONAL==========", posxtxt91011121314, posytxt11, tamañotxt2, negro, fuente_act) # Max 64 char
					txt12 = ["", ""]
					txt13 = ["", ""]
					txt14, posxytxt14 = print_pantalla("Nivel actual: ", posxtxt14151617, posytxt14, tamañotxt2, negro, fuente_act)
					txt15, posxytxt15 = print_pantalla("Infinito: ", posxtxt14151617, posytxt15, tamañotxt2, negro, fuente_act)
					txt16, posxytxt16 = print_pantalla("Boss: ", posxtxt14151617, posytxt16, tamañotxt2, negro, fuente_act)
					txt17, posxytxt17 = print_pantalla("Nº Naves: ", posxtxt14151617, posytxt17, tamañotxt2, negro, fuente_act)
					txt19, posxytxt19 = print_pantalla("Pantalla: " + str(pantalla_act), 0, posytxt14, tamañotxt2, negro, fuente_act)
					txt20, posxytxt20 = print_pantalla("Puntuacion: ", 0, posytxt20, tamañotxt2, negro, fuente_act)
					txt21, posxytxt21 = print_pantalla("Kills: ", 0, posytxt21, tamañotxt2, negro, fuente_act)
					txt22, posxytxt22 = print_pantalla("%Llegado: ", 0, posytxt22, tamañotxt2, negro, fuente_act)
					txt23, posxytxt23 = print_pantalla("Muertes: ", 0, posytxt23, tamañotxt2, negro, fuente_act)
					txt24, posxytxt24 = print_pantalla("Tiempo: ", 0, posytxt24, tamañotxt2, negro, fuente_act)
					txt25, posxytxt25 = print_pantalla("", 0, posytxt25, tamañotxt2, negro, fuente_act)
					txt26, posxytxt26 = print_pantalla("Dificultad: ", posxtxt14151617, posytxt26, tamañotxt2, negro, fuente_act)
					txt27, posxytxt27 = print_pantalla("", posxtxt14151617, posytxt27, tamañotxt2, negro, fuente_act)
					txt28, posxytxt28 = print_pantalla("Mejores", 0, posytxt28, tamañotxt2, negro, fuente_act)
					txt29, posxytxt29 = print_pantalla("estadisticas:", 0, posytxt29, tamañotxt2, negro, fuente_act)

					pantlenx = round(0.6875 * ancho) #880

					pantleny = round(0.66666666666666666666666666666667 * alto) #480

					imagen_fondo_seleccion_pantalla = pygame.transform.scale(imagen_fondo_seleccion_pantalla_alpha, (pantlenx, pantleny))

					posimagx = round(0.15625 * ancho) #200
					posimagy = round(0.16666666666666666666666666666667 *alto) #120

					ventana.blit(imagen_fondo_seleccion_pantalla, (posimagx, posimagy))

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
					ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
					ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))
					ventana.blit(botonreturn6, (posesxybot6[0], posesxybot6[1]))

					pygame.display.update()

			elif ratonx > posesxybot6[0] -  errordebotgeneral and ratony > posesxybot6[1] - errordebotgeneral and ratonx < posesxy2bot6[0] and ratony < posesxy2bot6[1]:

				if evento.type == MOUSEBUTTONDOWN:

					print("Boton Controles pulsado")

					ventana.fill(negro)

					generarpantallacontroles(ventana)

					ajustes = extraer_ajustes()

					ancho = int(ajustes[0])
					alto = int(ajustes[1])

					tamañoline = round(0.00234375 * ancho)

					posyline1 = round(0.16666666666666666666666666666667 * alto)
					posyline2 = round(0.83333333333333333333333333333333 * alto)

					posxline3 = round(0.15625 * ancho)
					posxline4 = round(0.84375 * ancho)

					posxflecha1 = round(0.078125 * ancho)
					posyflecha1 = round(0.5 * alto)
					posx1flecha1 = posxflecha1 - round(0.025 * ancho)
					posy1flecha1 = posyflecha1 - round(0.04444444444444444444444444444444 * alto)
					posx2flecha1 = posxflecha1 + round(0.025 * ancho)
					posy2flecha1 = posyflecha1 + round(0.04444444444444444444444444444444 * alto)

					posxflecha2 = round(0.921875 * ancho)
					posyflecha2 = round(0.5 * alto)
					posx1flecha2 = posxflecha2 - round(0.025 * ancho)
					posy1flecha2 = posyflecha2 - round(0.04444444444444444444444444444444 * alto)
					posx2flecha2 = posxflecha2 + round(0.025 * ancho)
					posy2flecha2 = posyflecha2 + round(0.04444444444444444444444444444444 * alto)

					tamañotxt1 = round(0.03125 * ancho)

					posytxt2 = round(0.06944444444444444444444444444444 * alto)
					posxtxt3 = round(0.4296875 * ancho)

					posxtxt5678 = round(0.4375 * ancho)
					posytxt5 = 0
					posytxt6 = round(0.04166666666666666666666666666667 * alto)
					posytxt7 = round(0.08333333333333333333333333333333 * alto)
					posytxt8 = round(0.125 * alto)

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

					tamañocirculo = round(0.0078125 * ancho)
					posxcirclegen = round(0.4296875 * ancho)
					posycircle1 = round(0.02083333333333333333333333333333 * alto)
					posycircle2 = round(0.0625 * alto)
					posycircle3 = round(0.10416666666666666666666666666667 * alto)
					posycircle4 = round(0.14583333333333333333333333333333 * alto)
					posxcircle5 = round(0.6546875 * ancho)

					posxtxt91011121314 = round(0.25 * ancho)
					posytxt9 = round(0.8375 * alto)
					posytxt10 = round(0.86805555555555555555555555555556 * alto)
					posytxt11 = round(0.89861111111111111111111111111111 * alto)
					posytxt12 = round(0.92916666666666666666666666666667 * alto)
					posytxt13 = round(0.95972222222222222222222222222222 * alto)

					posxtxt14151617 = round(0.84765625 * ancho)
					posytxt14 = round(0.17361111111111111111111111111111 * alto)
					posytxt15 = round(0.20833333333333333333333333333333 * alto)
					posytxt16 = round(0.24305555555555555555555555555556 * alto)
					posytxt17 = round(0.27777777777777777777777777777778 * alto)
					posytxt26 = round(0.3125 * alto)
					posytxt27 = round(0.34722222222222222222222222222222 * alto)

					posxtxt18 = round(0.6640625 * ancho)

					posx1bot5 = round(0.859375 * ancho)
					posy1bot5 = round(0.76388888888888888888888888888889 * alto)
					posx2bot5 = round(0.98046875 * ancho)
					posy2bot5 = round(0.80972222222222222222222222222222 * alto)

					posytxt20 = round(0.60833333333333333333333333333333 * alto)
					posytxt21 = round(0.67777777777777777777777777777778 * alto)
					posytxt22 = round(0.7125 * alto)
					posytxt23 = round(0.74722222222222222222222222222222 * alto)
					posytxt24 = round(0.78194444444444444444444444444444 * alto)
					posytxt25 = round(0.64305555555555555555555555555556 * alto)
					posytxt28 = round(0.36527777777777777777777777777778 * alto)
					posytxt29 = round(0.4 * alto)

					posx1botcont = round(0.109375 * ancho)
					posy1botcont = round(0.855 * alto)
					posx2botcont = round(0.234375 * ancho)
					posy2botcont = round(0.89666666667 * alto)

					caracteristicasfondo = [tamañoline, posyline1, posyline2, posxline3, posxline4, tamañotxt1, posytxt2, errordebotgeneral, tamañopolygon, posx1botat, posy1botat, posx2botat, posy2botat, tamañotxt2, posxtxt3, tamañocirculo, posxcirclegen, posycircle1, posycircle2, posycircle3, posycircle4, posxtxt5678, posytxt5, posytxt6, posytxt7, posytxt8, posxtxt18, posxcircle5, posytxt30]

					caracteristicas_panelInfo = [posxtxt91011121314, posytxt9, posytxt10, posytxt11, posytxt12, posytxt13, lista_textos, lista_textos_LvsInfinitos, posxtxt14151617, posytxt14, posytxt15, posytxt16, posytxt17, navestotales, posytxt20, posytxt21, posytxt22, posytxt23, posytxt24, posytxt25, data_niveles, posytxt26, posytxt27, dificultades, posytxt28, posytxt29]

					ventana.fill(gris_fondo)

					txt9 = ["", ""]
					txt10 = ["", ""]
					txt11, posxytxt11 = print_pantalla("                            ==========DIARIO PERSONAL==========", posxtxt91011121314, posytxt11, tamañotxt2, negro, fuente_act) # Max 64 char
					txt12 = ["", ""]
					txt13 = ["", ""]
					txt14, posxytxt14 = print_pantalla("Nivel actual: ", posxtxt14151617, posytxt14, tamañotxt2, negro, fuente_act)
					txt15, posxytxt15 = print_pantalla("Infinito: ", posxtxt14151617, posytxt15, tamañotxt2, negro, fuente_act)
					txt16, posxytxt16 = print_pantalla("Boss: ", posxtxt14151617, posytxt16, tamañotxt2, negro, fuente_act)
					txt17, posxytxt17 = print_pantalla("Nº Naves: ", posxtxt14151617, posytxt17, tamañotxt2, negro, fuente_act)
					txt19, posxytxt19 = print_pantalla("Pantalla: " + str(pantalla_act), 0, posytxt14, tamañotxt2, negro, fuente_act)
					txt20, posxytxt20 = print_pantalla("Puntuacion: ", 0, posytxt20, tamañotxt2, negro, fuente_act)
					txt21, posxytxt21 = print_pantalla("Kills: ", 0, posytxt21, tamañotxt2, negro, fuente_act)
					txt22, posxytxt22 = print_pantalla("%Llegado: ", 0, posytxt22, tamañotxt2, negro, fuente_act)
					txt23, posxytxt23 = print_pantalla("Muertes: ", 0, posytxt23, tamañotxt2, negro, fuente_act)
					txt24, posxytxt24 = print_pantalla("Tiempo: ", 0, posytxt24, tamañotxt2, negro, fuente_act)
					txt25, posxytxt25 = print_pantalla("", 0, posytxt25, tamañotxt2, negro, fuente_act)
					txt26, posxytxt26 = print_pantalla("Dificultad: ", posxtxt14151617, posytxt26, tamañotxt2, negro, fuente_act)
					txt27, posxytxt27 = print_pantalla("", posxtxt14151617, posytxt27, tamañotxt2, negro, fuente_act)
					txt28, posxytxt28 = print_pantalla("Mejores", 0, posytxt28, tamañotxt2, negro, fuente_act)
					txt29, posxytxt29 = print_pantalla("estadisticas:", 0, posytxt29, tamañotxt2, negro, fuente_act)

					pantlenx = round(0.6875 * ancho) #880

					pantleny = round(0.66666666666666666666666666666667 * alto) #480

					imagen_fondo_seleccion_pantalla = pygame.transform.scale(imagen_fondo_seleccion_pantalla_alpha, (pantlenx, pantleny))

					posimagx = round(0.15625 * ancho) #200
					posimagy = round(0.16666666666666666666666666666667 *alto) #120

					ventana.blit(imagen_fondo_seleccion_pantalla, (posimagx, posimagy))

					pygame.display.update()

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
					txt18, posxytxt18 = results1[12]
					txt30, posxytxt30 = results1[13]
					posesxybot6, posesxy2bot6, botonreturn6 = results1[14]

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
					ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
					ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))
					ventana.blit(botonreturn6, (posesxybot6[0], posesxybot6[1]))

					pygame.display.update()

			elif ratonx > posesxybot2[0] -  errordebotgeneral and ratony > posesxybot2[1] - errordebotgeneral and ratonx < posesxy2bot2[0] and ratony < posesxy2bot2[1]:

				if evento.type == MOUSEBUTTONDOWN:

					bot5 = ["", ""]

					ajustes = extraer_ajustes()

					ancho = int(ajustes[0])
					alto = int(ajustes[1])

					Ejecutarajustes(ventana, user_act, ancho, alto)

					ajustes = extraer_ajustes()

					ancho = int(ajustes[0])
					alto = int(ajustes[1])

					tamañoline = round(0.00234375 * ancho)

					posyline1 = round(0.16666666666666666666666666666667 * alto)
					posyline2 = round(0.83333333333333333333333333333333 * alto)

					posxline3 = round(0.15625 * ancho)
					posxline4 = round(0.84375 * ancho)

					posxflecha1 = round(0.078125 * ancho)
					posyflecha1 = round(0.5 * alto)
					posx1flecha1 = posxflecha1 - round(0.025 * ancho)
					posy1flecha1 = posyflecha1 - round(0.04444444444444444444444444444444 * alto)
					posx2flecha1 = posxflecha1 + round(0.025 * ancho)
					posy2flecha1 = posyflecha1 + round(0.04444444444444444444444444444444 * alto)

					posxflecha2 = round(0.921875 * ancho)
					posyflecha2 = round(0.5 * alto)
					posx1flecha2 = posxflecha2 - round(0.025 * ancho)
					posy1flecha2 = posyflecha2 - round(0.04444444444444444444444444444444 * alto)
					posx2flecha2 = posxflecha2 + round(0.025 * ancho)
					posy2flecha2 = posyflecha2 + round(0.04444444444444444444444444444444 * alto)

					tamañotxt1 = round(0.03125 * ancho)

					posytxt2 = round(0.06944444444444444444444444444444 * alto)
					posxtxt3 = round(0.4296875 * ancho)

					posxtxt5678 = round(0.4375 * ancho)
					posytxt5 = 0
					posytxt6 = round(0.04166666666666666666666666666667 * alto)
					posytxt7 = round(0.08333333333333333333333333333333 * alto)
					posytxt8 = round(0.125 * alto)

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

					tamañocirculo = round(0.0078125 * ancho)
					posxcirclegen = round(0.4296875 * ancho)
					posycircle1 = round(0.02083333333333333333333333333333 * alto)
					posycircle2 = round(0.0625 * alto)
					posycircle3 = round(0.10416666666666666666666666666667 * alto)
					posycircle4 = round(0.14583333333333333333333333333333 * alto)
					posxcircle5 = round(0.6546875 * ancho)

					posxtxt91011121314 = round(0.25 * ancho)
					posytxt9 = round(0.8375 * alto)
					posytxt10 = round(0.86805555555555555555555555555556 * alto)
					posytxt11 = round(0.89861111111111111111111111111111 * alto)
					posytxt12 = round(0.92916666666666666666666666666667 * alto)
					posytxt13 = round(0.95972222222222222222222222222222 * alto)

					posxtxt14151617 = round(0.84765625 * ancho)
					posytxt14 = round(0.17361111111111111111111111111111 * alto)
					posytxt15 = round(0.20833333333333333333333333333333 * alto)
					posytxt16 = round(0.24305555555555555555555555555556 * alto)
					posytxt17 = round(0.27777777777777777777777777777778 * alto)
					posytxt26 = round(0.3125 * alto)
					posytxt27 = round(0.34722222222222222222222222222222 * alto)

					posxtxt18 = round(0.6640625 * ancho)

					posx1bot5 = round(0.859375 * ancho)
					posy1bot5 = round(0.76388888888888888888888888888889 * alto)
					posx2bot5 = round(0.98046875 * ancho)
					posy2bot5 = round(0.80972222222222222222222222222222 * alto)

					posytxt20 = round(0.60833333333333333333333333333333 * alto)
					posytxt21 = round(0.67777777777777777777777777777778 * alto)
					posytxt22 = round(0.7125 * alto)
					posytxt23 = round(0.74722222222222222222222222222222 * alto)
					posytxt24 = round(0.78194444444444444444444444444444 * alto)
					posytxt25 = round(0.64305555555555555555555555555556 * alto)
					posytxt28 = round(0.36527777777777777777777777777778 * alto)
					posytxt29 = round(0.4 * alto)

					posx1botcont = round(0.109375 * ancho)
					posy1botcont = round(0.855 * alto)
					posx2botcont = round(0.234375 * ancho)
					posy2botcont = round(0.89666666667 * alto)

					caracteristicasfondo = [tamañoline, posyline1, posyline2, posxline3, posxline4, tamañotxt1, posytxt2, errordebotgeneral, tamañopolygon, posx1botat, posy1botat, posx2botat, posy2botat, tamañotxt2, posxtxt3, tamañocirculo, posxcirclegen, posycircle1, posycircle2, posycircle3, posycircle4, posxtxt5678, posytxt5, posytxt6, posytxt7, posytxt8, posxtxt18, posxcircle5, posytxt30]

					caracteristicas_panelInfo = [posxtxt91011121314, posytxt9, posytxt10, posytxt11, posytxt12, posytxt13, lista_textos, lista_textos_LvsInfinitos, posxtxt14151617, posytxt14, posytxt15, posytxt16, posytxt17, navestotales, posytxt20, posytxt21, posytxt22, posytxt23, posytxt24, posytxt25, data_niveles, posytxt26, posytxt27, dificultades, posytxt28, posytxt29]

					ventana.fill(gris_fondo)

					txt9 = ["", ""]
					txt10 = ["", ""]
					txt11, posxytxt11 = print_pantalla("                            ==========DIARIO PERSONAL==========", posxtxt91011121314, posytxt11, tamañotxt2, negro, fuente_act) # Max 64 char
					txt12 = ["", ""]
					txt13 = ["", ""]
					txt14, posxytxt14 = print_pantalla("Nivel actual: ", posxtxt14151617, posytxt14, tamañotxt2, negro, fuente_act)
					txt15, posxytxt15 = print_pantalla("Infinito: ", posxtxt14151617, posytxt15, tamañotxt2, negro, fuente_act)
					txt16, posxytxt16 = print_pantalla("Boss: ", posxtxt14151617, posytxt16, tamañotxt2, negro, fuente_act)
					txt17, posxytxt17 = print_pantalla("Nº Naves: ", posxtxt14151617, posytxt17, tamañotxt2, negro, fuente_act)
					txt19, posxytxt19 = print_pantalla("Pantalla: " + str(pantalla_act), 0, posytxt14, tamañotxt2, negro, fuente_act)
					txt20, posxytxt20 = print_pantalla("Puntuacion: ", 0, posytxt20, tamañotxt2, negro, fuente_act)
					txt21, posxytxt21 = print_pantalla("Kills: ", 0, posytxt21, tamañotxt2, negro, fuente_act)
					txt22, posxytxt22 = print_pantalla("%Llegado: ", 0, posytxt22, tamañotxt2, negro, fuente_act)
					txt23, posxytxt23 = print_pantalla("Muertes: ", 0, posytxt23, tamañotxt2, negro, fuente_act)
					txt24, posxytxt24 = print_pantalla("Tiempo: ", 0, posytxt24, tamañotxt2, negro, fuente_act)
					txt25, posxytxt25 = print_pantalla("", 0, posytxt25, tamañotxt2, negro, fuente_act)
					txt26, posxytxt26 = print_pantalla("Dificultad: ", posxtxt14151617, posytxt26, tamañotxt2, negro, fuente_act)
					txt27, posxytxt27 = print_pantalla("", posxtxt14151617, posytxt27, tamañotxt2, negro, fuente_act)
					txt28, posxytxt28 = print_pantalla("Mejores", 0, posytxt28, tamañotxt2, negro, fuente_act)
					txt29, posxytxt29 = print_pantalla("estadisticas:", 0, posytxt29, tamañotxt2, negro, fuente_act)

					pantlenx = round(0.6875 * ancho) #880

					pantleny = round(0.66666666666666666666666666666667 * alto) #480

					imagen_fondo_seleccion_pantalla = pygame.transform.scale(imagen_fondo_seleccion_pantalla_alpha, (pantlenx, pantleny))

					posimagx = round(0.15625 * ancho) #200
					posimagy = round(0.16666666666666666666666666666667 *alto) #120

					ventana.blit(imagen_fondo_seleccion_pantalla, (posimagx, posimagy))

					pygame.display.update()

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
					txt18, posxytxt18 = results1[12]
					txt30, posxytxt30 = results1[13]
					posesxybot6, posesxy2bot6, botonreturn6 = results1[14]

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
					ventana.blit(botonreturn, (posesxybot1[0], posesxybot1[1]))
					ventana.blit(botonreturn2, (posesxybot2[0], posesxybot2[1]))
					ventana.blit(botonreturn6, (posesxybot6[0], posesxybot6[1]))

					pygame.display.update()