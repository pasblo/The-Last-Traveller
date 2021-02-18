import pygame

import sys

from Modulos.objetos_de_pantalla import *

from pygame.locals import *

from Modulos.user import *

from Modulos.cifrador import *

from Modulos.clasificador import SoundObj, BGMObj

from Modulos.sqlite3faciliter import *

from Modulos.sqlite3igualador import *

from Modulos.generador_de_pantalla_ajustes import *

from Modulos.basededatosajustesfaciliter import *

from Modulos.generador_de_pantalla_seleccionLv import *

from Modulos.basededatosnivelesfaciliter import *

import time

def Executepantalla1(ventana, user_act, ancho, alto):

    def calcularx(letras, ancho, modo_seguro = False):

        longit = 0

        for letraact in letras:

            if modo_seguro == True:
                letraact = "*"

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

    imagen_fondo_seleccion_pantalla_alpha = pygame.image.load("Imagenes/imagen_fondo_seleccion_pantalla_1.jpg").convert()
    imagen_fondo_seleccion_pantalla_2_alpha = pygame.image.load("Imagenes/imagen_fondo_seleccion_pantalla_2.jpg").convert()
    imagen_fondo_seleccion_pantalla_3_alpha = pygame.image.load("Imagenes/imagen_fondo_seleccion_pantalla_3_prueva.jpg").convert()

    imagenes_de_fondo_seleccion_pantallas = [imagen_fondo_seleccion_pantalla_alpha, imagen_fondo_seleccion_pantalla_2_alpha, imagen_fondo_seleccion_pantalla_3_alpha]

    imagen_de_fondo_alpha = pygame.image.load("Imagenes/fondo.png").convert()

    imagen_de_fondo = pygame.transform.scale(imagen_de_fondo_alpha, (ancho, alto))

    tipodeletra = "Calibri"

    toca = 1

    data_niveles = []

    if user_act[1] != "None":

        for x in range(30):
            ordenardbniveles(user_act[1], x + 1)

        while toca < 31:

            data_nivel = extraerdatos(user_act[1], toca)

            data_niveles.append(data_nivel)

            toca += 1

    #Botones principales

    posx1comenzar = round(0.37 * ancho) #Caracteristicas del boton comenzar
    posx2comenzar = round(0.6335 * ancho)
    posy1comenzar = round(0.66 * alto)
    posy2comenzar = round(0.76 * alto)
    tamañocomenzar = round(0.053571 * ancho) #0.053571 #0.044

    posx1ajus = round(0.8371 * ancho) #Caracteristicas del boton ajustes de usuario
    posx2ajus = round(0.984 * ancho)
    posy1ajus = round(0.02 * alto)
    posy2ajus = round(0.05 * alto)
    tamañoajus = round(0.015625 * ancho)

    posx1logandcre = round(0.7971 * ancho) #Caracteristicas del boton logear y crear
    posx2logandcre = round(0.984 * ancho)
    posy1logandcre = round(0.02 * alto)
    posy2logandcre = round(0.05 * alto)
    tamañologandcre = round(0.015625 * ancho) #0.015625

    posx1ajustes = round(0.9 * ancho) #Carcteristicas de boton de ajustes generales
    posy1ajustes = round(0.86 * alto)
    posx2ajustes = round(0.94 * ancho)
    posy2ajustes = round(0.92 * alto)

    user_comp = user_act

    #Textos principales

    if user_comp[0] == True: #Caracteristicas del texto1
        posxtxt1 = round(0.775375 * ancho) - calcularx(user_comp[1], ancho)

    else:
        posxtxt1 = None

    posytxt1 = round(0.0125 * ancho)
    tamañotxt1 = round(0.015625 * ancho)

    #Otros principales

    posy1rect1 = round(0.0328125 * ancho) #Caracteristicas del rectangulo1
    posy2rect1 = round(0.13825 * ancho)
    diferenciaentrelos2 = round(0.00234375 * ancho)

    #Botones secundarios

    posy1bot3 = round(0.0484375 * ancho) #Caracteristicas del bot3
    posy2bot3 = round(0.066406 * ancho)
    tamañobot3 = round(0.015625 * ancho)

    posy1bot4 = round(0.06796 * ancho) #Caracteristicas del bot4
    posy2bot4 = round(0.08593 * ancho)
    tamañobot4 = round(0.015625 * ancho)

    posy1bot5 = round(0.0875 * ancho) #Caracteristicas del bot5
    posy2bot5 = round(0.10546 * ancho)
    tamañobot5 = round(0.015625 * ancho)

    posy1bot6 = round(0.10703125 * ancho) #Caracteristicas de bot6
    posy2bot6 = round(0.125 * ancho)
    tamañobot6 = round(0.015625 * ancho)

    Portadax = 320
    Portaday = 180

    #Textos secundarios

    #Otros secundarios

    tamañotxtgeneralconsola = round(0.0234375 * ancho)


    rojo = (255, 0, 0)

    blanco = (255, 255, 255)

    negro = (0, 0, 0)

    verde = (0, 255, 0)

    azul = (0, 0, 255)
    """
    ventana.fill(blanco)

    pygame.display.update()

    ndcat = 0 #ndcat = numero de cancion a tocar

    ventana.fill(negro)

    txt1 = print_pantalla("Loading...", 550, 335, 40, blanco, tipodeletra)

    posxytxt1 = txt1[1]

    ventana.blit(txt1[0], (posxytxt1[0], posxytxt1[1]))

    pygame.display.update()

    time.sleep(3)"""

    musicadefondo1 = BGMObj("CancionFondo1", False, 0, 10)

    musicasdefondo = [musicadefondo1]

    ajustes = extraer_ajustes()

    vol_general = int(ajustes[4])
    vol_musica = int(ajustes[6])

    musicasdefondo[0].play(25)

    musicasdefondo[0].setVolume((vol_musica * vol_general)/1000)

    botytxt1 = crear_boton("COMENZAR", posx1comenzar, posy1comenzar, posx2comenzar, posy2comenzar, tamañocomenzar, ventana, negro, tipodeletra, blanco)
    rectangulo1 = botytxt1[1]
    posesxybot1 = rectangulo1[1]
    posesxy2bot1 = rectangulo1[2]

    if user_comp[0] == False:
        botytxt2 = crear_boton("LOGGEAR/CREAR USUARIO", posx1logandcre, posy1logandcre, posx2logandcre, posy2logandcre, tamañologandcre, ventana, negro, tipodeletra, blanco)
        rectangulo2 = botytxt2[1]
        posesxybot2 = rectangulo2[1]
        posesxy2bot2 = rectangulo2[2]
        txt1 = None

    else:
        botytxt2 = crear_boton("AJUSTES DE USUARIO", posx1ajus, posy1ajus, posx2ajus, posy2ajus, tamañoajus, ventana, negro, tipodeletra, blanco)
        rectangulo2 = botytxt2[1]
        posesxybot2 = rectangulo2[1]
        posesxy2bot2 = rectangulo2[2]
        txt1 = print_pantalla("Usuario: " + user_comp[1], posxtxt1, posytxt1, tamañotxt1, blanco, tipodeletra)
        posxytxt1 = txt1[1]

    bot7_alpha = pygame.image.load("Imagenes/ajustes.svg")

    bot7 = pygame.transform.scale(bot7_alpha, (posx2ajustes - posx1ajustes, posy2ajustes - posy1ajustes))

    ImagenInsetCoins_alpha = pygame.image.load("Imagenes/Insert_Coins/Insert_Coins.png")
    ImagenInsetCoins = pygame.transform.scale(ImagenInsetCoins_alpha, (272, 28)) #68 X 7 ha sido multiplicado por 4

    Portada_alpha = pygame.image.load("Imagenes/TheLastTraveller.png")
    Portada = pygame.transform.scale(Portada_alpha, (615, 250))

    ratonx = 0
    ratony = 0

    accion = ""

    eventopant = None

    eventopantant = 0

    tiempo_de_error = 0.1

    primera_vuelta = True

    sucedio_accion = False

    while True:

            sucedio_accion = False

            for evento in pygame.event.get():

                if user_comp[0] == True: #Caracteristicas del texto1
                    posxtxt1 = round(0.775375 * ancho) - calcularx(user_comp[1], ancho)

                else:
                    posxtxt1 = None

                posytxt1 = round(0.0125 * ancho)
                tamañotxt1 = round(0.015625 * ancho)

                sucedio_accion = False

                ratonx, ratony = pygame.mouse.get_pos()

                if evento.type == QUIT:
                    print("Juego terminado")
                    pygame.quit()
                    raise KeyError

                if evento.type == KEYDOWN:

                    if evento.key == 282: #Cambiar a tamaño default

                        actualizar_dato("ancho", 1280)
                        actualizar_dato("alto", 720)

                        ajustes = extraer_ajustes()

                        ancho = int(ajustes[0])

                        alto = int(ajustes[1])

                        imagen_de_fondo = pygame.transform.scale(imagen_de_fondo_alpha, (ancho, alto))

                        pantalla_comp = ajustes[2]

                        if pantalla_comp == "True":
                            try:
                                pygame.display.set_mode((ancho, alto), pygame.FULLSCREEN)
                            except:
                                pass

                        else:
                            try:
                                pygame.display.set_mode((ancho, alto))
                            except:
                                pass

                        #Botones principales

                        posx1comenzar = round(0.37 * ancho) #Caracteristicas del boton comenzar
                        posx2comenzar = round(0.6335 * ancho)
                        posy1comenzar = round(0.66 * alto)
                        posy2comenzar = round(0.76 * alto)
                        tamañocomenzar = round(0.053571 * ancho) #0.053571 #0.044

                        posx1ajus = round(0.8371 * ancho) #Caracteristicas del boton ajustes de usuario
                        posx2ajus = round(0.984 * ancho)
                        posy1ajus = round(0.02 * alto)
                        posy2ajus = round(0.05 * alto)
                        tamañoajus = round(0.015625 * ancho)

                        posx1logandcre = round(0.7971 * ancho) #Caracteristicas del boton logear y crear
                        posx2logandcre = round(0.984 * ancho)
                        posy1logandcre = round(0.02 * alto)
                        posy2logandcre = round(0.05 * alto)
                        tamañologandcre = round(0.015625 * ancho) #0.015625

                        posx1ajustes = round(0.9 * ancho) #Carcteristicas de boton de ajustes generales
                        posy1ajustes = round(0.86 * alto)
                        posx2ajustes = round(0.94 * ancho)
                        posy2ajustes = round(0.92 * alto)

                        user_comp = user_act

                        #Textos principales

                        if user_comp[0] == True: #Caracteristicas del texto1
                            posxtxt1 = round(0.775375 * ancho) - calcularx(user_comp[1], ancho)

                        else:
                            posxtxt1 = None

                        posytxt1 = round(0.0125 * ancho)
                        tamañotxt1 = round(0.015625 * ancho)

                        #Otros principales

                        posy1rect1 = round(0.0328125 * ancho) #Caracteristicas del rectangulo1
                        posy2rect1 = round(0.13825 * ancho)
                        diferenciaentrelos2 = round(0.00234375 * ancho)

                        #Botones secundarios

                        posy1bot3 = round(0.0484375 * ancho) #Caracteristicas del bot3
                        posy2bot3 = round(0.066406 * ancho)
                        tamañobot3 = round(0.015625 * ancho)

                        posy1bot4 = round(0.06796 * ancho) #Caracteristicas del bot4
                        posy2bot4 = round(0.08593 * ancho)
                        tamañobot4 = round(0.015625 * ancho)

                        posy1bot5 = round(0.0875 * ancho) #Caracteristicas del bot5
                        posy2bot5 = round(0.10546 * ancho)
                        tamañobot5 = round(0.015625 * ancho)

                        posy1bot6 = round(0.10703125 * ancho) #Caracteristicas de bot6
                        posy2bot6 = round(0.125 * ancho)
                        tamañobot6 = round(0.015625 * ancho)

                        #Textos secundarios

                        #Otros secundarios

                        tamañotxtgeneralconsola = round(0.0234375 * ancho)
                        
                        botytxt1 = crear_boton("COMENZAR", posx1comenzar, posy1comenzar, posx2comenzar, posy2comenzar, tamañocomenzar, ventana, negro, tipodeletra, blanco)
                        rectangulo1 = botytxt1[1]
                        posesxybot1 = rectangulo1[1]
                        posesxy2bot1 = rectangulo1[2]

                        if user_comp[0] == False:
                            botytxt2 = crear_boton("LOGGEAR/CREAR USUARIO", posx1logandcre, posy1logandcre, posx2logandcre, posy2logandcre, tamañologandcre, ventana, negro, tipodeletra, blanco)
                            rectangulo2 = botytxt2[1]
                            posesxybot2 = rectangulo2[1]
                            posesxy2bot2 = rectangulo2[2]
                            txt1 = None

                        else:
                            botytxt2 = crear_boton("AJUSTES DE USUARIO", posx1ajus, posy1ajus, posx2ajus, posy2ajus, tamañoajus, ventana, negro, tipodeletra, blanco)
                            rectangulo2 = botytxt2[1]
                            posesxybot2 = rectangulo2[1]
                            posesxy2bot2 = rectangulo2[2]
                            txt1 = print_pantalla("Usuario: " + user_comp[1], posxtxt1, posytxt1, tamañotxt1, blanco, tipodeletra)
                            posxytxt1 = txt1[1]

                        bot7_alpha = pygame.image.load("Imagenes/ajustes.svg")

                        bot7 = pygame.transform.scale(bot7_alpha, (posx2ajustes - posx1ajustes, posy2ajustes - posy1ajustes))

                        ventana.blit(botytxt1[0], (posesxybot1[0], posesxybot1[1]))
                        ventana.blit(botytxt2[0], (posesxybot2[0], posesxybot2[1]))
                        if txt1 != None: ventana.blit(txt1[0], (posxytxt1[0], posxytxt1[1]))
                        ventana.blit(bot7, (posx1ajustes, posy1ajustes))
                        pygame.display.update()

                    elif evento.key == 285:
                        print("Juego terminado")
                        pygame.quit()
                        raise KeyError

                    elif evento.key == 27:

                        pantalla_comp = False
                        try:
                            pygame.display.set_mode((ancho, alto))
                        except:
                            pass

                        actualizar_dato("pantcomp", pantalla_comp)

                        ventana.blit(imagen_de_fondo, (0, 0))
                        ventana.blit(ImagenInsetCoins, (504, 10))
                        ventana.blit(Portada, (Portadax, Portaday))
                        pygame.display.update()

                        botytxt1 = crear_boton("COMENZAR", posx1comenzar, posy1comenzar, posx2comenzar, posy2comenzar, tamañocomenzar, ventana, negro, tipodeletra, blanco)

                        if user_comp[0] == False:
                            botytxt2 = crear_boton("LOGGEAR/CREAR USUARIO", posx1logandcre, posy1logandcre, posx2logandcre, posy2logandcre, tamañologandcre, ventana, negro, tipodeletra, blanco)
                            rectangulo2 = botytxt2[1]
                            posesxybot2 = rectangulo2[1]
                            posesxy2bot2 = rectangulo2[2]
                            txt1 = None

                        else:
                            botytxt2 = crear_boton("AJUSTES DE USUARIO", posx1ajus, posy1ajus, posx2ajus, posy2ajus, tamañoajus, ventana, negro, tipodeletra, blanco)
                            rectangulo2 = botytxt2[1]
                            posesxybot2 = rectangulo2[1]
                            posesxy2bot2 = rectangulo2[2]
                            txt1 = print_pantalla("Usuario: " + user_comp[1], posxtxt1, posytxt1, tamañotxt1, blanco, tipodeletra)
                            posxytxt1 = txt1[1]

                        eventopantant = eventopant
                        eventopant = None

                    elif evento.key == 292:

                        pantalla_comp = True
                        try:
                            pygame.display.set_mode((ancho, alto), pygame.FULLSCREEN)
                        except:
                            pass

                        actualizar_dato("pantcomp", pantalla_comp)

                        ventana.blit(imagen_de_fondo, (0, 0))
                        ventana.blit(ImagenInsetCoins, (504, 10))
                        ventana.blit(Portada, (Portadax, Portaday))
                        pygame.display.update()
                        botytxt1 = crear_boton("COMENZAR", posx1comenzar, posy1comenzar, posx2comenzar, posy2comenzar, tamañocomenzar, ventana, negro, tipodeletra, blanco)

                        if user_act[0] == False:
                            botytxt2 = crear_boton("LOGGEAR/CREAR USUARIO", posx1logandcre, posy1logandcre, posx2logandcre, posy2logandcre, tamañologandcre, ventana, negro, tipodeletra, blanco)
                            rectangulo2 = botytxt2[1]
                            posesxybot2 = rectangulo2[1]
                            posesxy2bot2 = rectangulo2[2]
                            txt1 = None

                        else:
                            botytxt2 = crear_boton("AJUSTES DE USUARIO", posx1ajus, posy1ajus, posx2ajus, posy2ajus, tamañoajus, ventana, negro, tipodeletra, blanco)
                            rectangulo2 = botytxt2[1]
                            posesxybot2 = rectangulo2[1]
                            posesxy2bot2 = rectangulo2[2]
                            txt1 = print_pantalla("Usuario: " + user_comp[1], posxtxt1, posytxt1, tamañotxt1, blanco, tipodeletra)
                            posxytxt1 = txt1[1]

                        eventopantant = eventopant
                        eventopant = None

                if ratonx > posesxybot1[0] and ratony > posesxybot1[1] and ratonx < posesxy2bot1[0] and ratony < posesxy2bot1[1]:
                    
                    if evento.type == MOUSEBUTTONDOWN:
                        print("Boton 1 pulsado")
                        botytxt1 = crear_boton("COMENZAR", posx1comenzar, posy1comenzar, posx2comenzar, posy2comenzar, tamañocomenzar, ventana, negro, tipodeletra, blanco)
                        accion = "start"
                        sucedio_accion = True
                        eventopantant = eventopant
                        eventopant = 1

                    else:
                        botytxt1 = crear_boton("COMENZAR", posx1comenzar, posy1comenzar, posx2comenzar, posy2comenzar, tamañocomenzar, ventana, blanco, tipodeletra, negro)
                        eventopantant = eventopant
                        eventopant = 2

                else:
                    botytxt1 = crear_boton("COMENZAR", posx1comenzar, posy1comenzar, posx2comenzar, posy2comenzar, tamañocomenzar, ventana, negro, tipodeletra, blanco)
                    eventopantant = eventopant
                    eventopant = None

                if ratonx > posesxybot2[0] and ratony > posesxybot2[1] and ratonx < posesxy2bot2[0] and ratony < posesxy2bot2[1]:

                    if evento.type == MOUSEBUTTONDOWN:
                        print("Boton 2 pulsado")

                        if user_comp[0] == False:
                            botytxt2 = crear_boton("LOGGEAR/CREAR USUARIO", posx1logandcre, posy1logandcre, posx2logandcre, posy2logandcre, tamañologandcre, ventana, negro, tipodeletra, blanco)
                            rectangulo2 = botytxt2[1]
                            posesxybot2 = rectangulo2[1]
                            posesxy2bot2 = rectangulo2[2]
                            accion = "col"
                            sucedio_accion = True
                            txt1 = None
                            

                        else:
                            botytxt2 = crear_boton("AJUSTES DE USUARIO", posx1ajus, posy1ajus, posx2ajus, posy2ajus, tamañoajus, ventana, negro, tipodeletra, blanco)
                            rectangulo2 = botytxt2[1]
                            posesxybot2 = rectangulo2[1]
                            posesxy2bot2 = rectangulo2[2]
                            accion = "ajustesuser"
                            sucedio_accion = True
                            txt1 = print_pantalla("Usuario: " + user_comp[1], posxtxt1, posytxt1, tamañotxt1, blanco, tipodeletra)
                            posxytxt1 = txt1[1]

                        eventopantant = eventopant

                        eventopant = 3

                    else:

                        if user_comp[0] == False:
                            botytxt2 = crear_boton("LOGGEAR/CREAR USUARIO", posx1logandcre, posy1logandcre, posx2logandcre, posy2logandcre, tamañologandcre, ventana, blanco, tipodeletra, negro)
                            rectangulo2 = botytxt2[1]
                            posesxybot2 = rectangulo2[1]
                            posesxy2bot2 = rectangulo2[2]
                            txt1 = None
                            
                        else:
                            botytxt2 = crear_boton("AJUSTES DE USUARIO", posx1ajus, posy1ajus, posx2ajus, posy2ajus, tamañoajus, ventana, blanco, tipodeletra, negro)
                            rectangulo2 = botytxt2[1]
                            posesxybot2 = rectangulo2[1]
                            posesxy2bot2 = rectangulo2[2]
                            txt1 = print_pantalla("Usuario: " + user_comp[1], posxtxt1, posytxt1, tamañotxt1, blanco, tipodeletra)
                            posxytxt1 = txt1[1]

                        eventopantant = eventopant

                        eventopant = 4

                else:
                    if user_comp[0] == False:
                        botytxt2 = crear_boton("LOGGEAR/CREAR USUARIO", posx1logandcre, posy1logandcre, posx2logandcre, posy2logandcre, tamañologandcre, ventana, negro, tipodeletra, blanco)
                        rectangulo2 = botytxt2[1]
                        posesxybot2 = rectangulo2[1]
                        posesxy2bot2 = rectangulo2[2]
                        txt1 = None
                            

                    else:
                        botytxt2 = crear_boton("AJUSTES DE USUARIO", posx1ajus, posy1ajus, posx2ajus, posy2ajus, tamañoajus, ventana, negro, tipodeletra, blanco)
                        rectangulo2 = botytxt2[1]
                        posesxybot2 = rectangulo2[1]
                        posesxy2bot2 = rectangulo2[2]
                        txt1 = print_pantalla("Usuario: " + user_comp[1], posxtxt1, posytxt1, tamañotxt1, blanco, tipodeletra)
                        posxytxt1 = txt1[1]

                    eventopantant = eventopant

                    eventopant = None

                if ratonx > posx1ajustes and ratony > posy1ajustes and ratonx < posx2ajustes and ratony < posy2ajustes:

                    if evento.type == MOUSEBUTTONDOWN:
                        print("Boton 7 pulsado")
                        sucedio_accion = True
                        accion = "ajustes"

                        posx1ajustes = round(0.9 * ancho)
                        posy1ajustes = round(0.86 * alto)
                        posx2ajustes = round(0.94 * ancho)
                        posy2ajustes = round(0.92 * alto)

                        bot7 = pygame.transform.scale(bot7_alpha, (posx2ajustes - posx1ajustes, posy2ajustes - posy1ajustes))

                        eventopantant = eventopant

                        eventopant = 5

                    else:
                        posx1ajustes = round(0.89 * ancho)
                        posy1ajustes = round(0.85 * alto)
                        posx2ajustes = round(0.95 * ancho)
                        posy2ajustes = round(0.93 * alto)

                        bot7 = pygame.transform.scale(bot7_alpha, (posx2ajustes - posx1ajustes, posy2ajustes - posy1ajustes))

                        eventopantant = eventopant


                else:
                    posx1ajustes = round(0.9 * ancho)
                    posy1ajustes = round(0.86 * alto)
                    posx2ajustes = round(0.94 * ancho)
                    posy2ajustes = round(0.92 * alto)

                    bot7 = pygame.transform.scale(bot7_alpha, (posx2ajustes - posx1ajustes, posy2ajustes - posy1ajustes))

                    eventopantant = eventopant

                    eventopant = None

                if eventopant != eventopantant or eventopant == None:
                    pass

                    #pygame.draw.rect(ventana, azul, (posx1ajustes - round(0.01015625 * ancho), posy1ajustes - round(0.0138888 * alto), posx2ajustes + round(0.0078125 * ancho), posy2ajustes + round(0.0138888 * alto)))

                    #pygame.display.update()

                    ventana.blit(botytxt1[0], (posesxybot1[0], posesxybot1[1]))
                    ventana.blit(botytxt2[0], (posesxybot2[0], posesxybot2[1]))
                    if txt1 != None: ventana.blit(txt1[0], (posxytxt1[0], posxytxt1[1]))
                    ventana.blit(bot7, (posx1ajustes, posy1ajustes))
                    ventana.blit(ImagenInsetCoins, (504, 10))
                    ventana.blit(Portada, (Portadax, Portaday))
                    pygame.display.update()
                    ventana.blit(imagen_de_fondo, (0, 0))

            if sucedio_accion == True:

                if accion == "start":

                    EjecutarSeleccionLv(ventana, user_comp, musicasdefondo, imagenes_de_fondo_seleccion_pantallas, data_niveles)

                    ajustes = extraer_ajustes()

                    ancho = int(ajustes[0])
                    alto = int(ajustes[1])
                    pantalla_comp_ext = ajustes[2]

                    imagen_de_fondo = pygame.transform.scale(imagen_de_fondo_alpha, (ancho, alto))

                    posx1comenzar = round(0.37 * ancho) #Caracteristicas del boton comenzar
                    posx2comenzar = round(0.6335 * ancho)
                    posy1comenzar = round(0.66 * alto)
                    posy2comenzar = round(0.76 * alto)
                    tamañocomenzar = round(0.053571 * ancho) #0.053571 #0.044

                    posx1ajus = round(0.8371 * ancho) #Caracteristicas del boton ajustes de usuario
                    posx2ajus = round(0.984 * ancho)
                    posy1ajus = round(0.02 * alto)
                    posy2ajus = round(0.05 * alto)
                    tamañoajus = round(0.015625 * ancho)

                    posx1logandcre = round(0.7971 * ancho) #Caracteristicas del boton logear y crear
                    posx2logandcre = round(0.984 * ancho)
                    posy1logandcre = round(0.02 * alto)
                    posy2logandcre = round(0.05 * alto)
                    tamañologandcre = round(0.015625 * ancho) #0.015625

                    posx1ajustes = round(0.9 * ancho) #Carcteristicas de boton de ajustes generales
                    posy1ajustes = round(0.86 * alto)
                    posx2ajustes = round(0.94 * ancho)
                    posy2ajustes = round(0.92 * alto)

                    #Textos principales

                    if user_comp[0] == True: #Caracteristicas del texto1
                        posxtxt1 = round(0.775375 * ancho) - calcularx(user_comp[1], ancho)

                    else:
                        posxtxt1 = None

                    posytxt1 = round(0.0125 * ancho)
                    tamañotxt1 = round(0.015625 * ancho)

                    #Otros principales

                    posy1rect1 = round(0.0328125 * ancho) #Caracteristicas del rectangulo1
                    posy2rect1 = round(0.13825 * ancho)
                    diferenciaentrelos2 = round(0.00234375 * ancho)

                    #Botones secundarios

                    posy1bot3 = round(0.0484375 * ancho) #Caracteristicas del bot3
                    posy2bot3 = round(0.066406 * ancho)
                    tamañobot3 = round(0.015625 * ancho)

                    posy1bot4 = round(0.06796 * ancho) #Caracteristicas del bot4
                    posy2bot4 = round(0.08593 * ancho)
                    tamañobot4 = round(0.015625 * ancho)

                    posy1bot5 = round(0.0875 * ancho) #Caracteristicas del bot5
                    posy2bot5 = round(0.10546 * ancho)
                    tamañobot5 = round(0.015625 * ancho)

                    posy1bot6 = round(0.10703125 * ancho) #Caracteristicas de bot6
                    posy2bot6 = round(0.125 * ancho)
                    tamañobot6 = round(0.015625 * ancho)

                    #Textos secundarios

                    #Otros secundarios

                    tamañotxtgeneralconsola = round(0.0234375 * ancho)

                    if pantalla_comp_ext == "True":

                        pantalla_comp = True
                        try:

                            pygame.display.set_mode((ancho, alto), pygame.FULLSCREEN)

                        except:
                            pass
                        actualizar_dato("pantcomp", pantalla_comp)
                        
                        botytxt1 = crear_boton("COMENZAR", posx1comenzar, posy1comenzar, posx2comenzar, posy2comenzar, tamañocomenzar, ventana, negro, tipodeletra, blanco)
                        rectangulo1 = botytxt1[1]
                        posesxybot1 = rectangulo1[1]
                        posesxy2bot1 = rectangulo1[2]

                        if user_act[0] == False:
                            botytxt2 = crear_boton("LOGGEAR/CREAR USUARIO", posx1logandcre, posy1logandcre, posx2logandcre, posy2logandcre, tamañologandcre, ventana, negro, tipodeletra, blanco)
                            rectangulo2 = botytxt2[1]
                            posesxybot2 = rectangulo2[1]
                            posesxy2bot2 = rectangulo2[2]
                            txt1 = None

                        else:
                            botytxt2 = crear_boton("AJUSTES DE USUARIO", posx1ajus, posy1ajus, posx2ajus, posy2ajus, tamañoajus, ventana, negro, tipodeletra, blanco)
                            rectangulo2 = botytxt2[1]
                            posesxybot2 = rectangulo2[1]
                            posesxy2bot2 = rectangulo2[2]
                            txt1 = print_pantalla("Usuario: " + user_comp[1], posxtxt1, posytxt1, tamañotxt1, blanco, tipodeletra)
                            posxytxt1 = txt1[1]

                    else:

                        pantalla_comp = False
                        try:
                            pygame.display.set_mode((ancho, alto))

                        except:
                            pass

                        actualizar_dato("pantcomp", pantalla_comp)

                        ventana.blit(imagen_de_fondo, (0, 0))
                        pygame.display.update()
                        botytxt1 = crear_boton("COMENZAR", posx1comenzar, posy1comenzar, posx2comenzar, posy2comenzar, tamañocomenzar, ventana, negro, tipodeletra, blanco)
                        rectangulo1 = botytxt1[1]
                        posesxybot1 = rectangulo1[1]
                        posesxy2bot1 = rectangulo1[2]

                        if user_comp[0] == False:
                            botytxt2 = crear_boton("LOGGEAR/CREAR USUARIO", posx1logandcre, posy1logandcre, posx2logandcre, posy2logandcre, tamañologandcre, ventana, negro, tipodeletra, blanco)
                            rectangulo2 = botytxt2[1]
                            posesxybot2 = rectangulo2[1]
                            posesxy2bot2 = rectangulo2[2]
                            txt1 = None

                        else:
                            botytxt2 = crear_boton("AJUSTES DE USUARIO", posx1ajus, posy1ajus, posx2ajus, posy2ajus, tamañoajus, ventana, negro, tipodeletra, blanco)
                            rectangulo2 = botytxt2[1]
                            posesxybot2 = rectangulo2[1]
                            posesxy2bot2 = rectangulo2[2]
                            txt1 = print_pantalla("Usuario: " + user_comp[1], posxtxt1, posytxt1, tamañotxt1, blanco, tipodeletra)
                            posxytxt1 = txt1[1]

                elif accion == "ajustes":

                    musicasdefondo[0].pause()

                    Ejecutarajustes(ventana, user_comp, ancho, alto)

                    ajustes = extraer_ajustes()

                    vol_general = int(ajustes[4])
                    vol_musica = int(ajustes[6])

                    musicasdefondo[0].setVolume((vol_general * vol_musica)/1000)

                    vol_act = musicasdefondo[0].getVolume()

                    musicasdefondo[0].unpause()

                    ajustes = extraer_ajustes()

                    ancho = int(ajustes[0])
                    alto = int(ajustes[1])
                    pantalla_comp_ext = ajustes[2]

                    imagen_de_fondo = pygame.transform.scale(imagen_de_fondo_alpha, (ancho, alto))

                    posx1comenzar = round(0.37 * ancho) #Caracteristicas del boton comenzar
                    posx2comenzar = round(0.6335 * ancho)
                    posy1comenzar = round(0.66 * alto)
                    posy2comenzar = round(0.76 * alto)
                    tamañocomenzar = round(0.053571 * ancho) #0.053571 #0.044

                    posx1ajus = round(0.8371 * ancho) #Caracteristicas del boton ajustes de usuario
                    posx2ajus = round(0.984 * ancho)
                    posy1ajus = round(0.02 * alto)
                    posy2ajus = round(0.05 * alto)
                    tamañoajus = round(0.015625 * ancho)

                    posx1logandcre = round(0.7971 * ancho) #Caracteristicas del boton logear y crear
                    posx2logandcre = round(0.984 * ancho)
                    posy1logandcre = round(0.02 * alto)
                    posy2logandcre = round(0.05 * alto)
                    tamañologandcre = round(0.015625 * ancho) #0.015625

                    posx1ajustes = round(0.9 * ancho) #Carcteristicas de boton de ajustes generales
                    posy1ajustes = round(0.86 * alto)
                    posx2ajustes = round(0.94 * ancho)
                    posy2ajustes = round(0.92 * alto)

                    user_comp

                    #Textos principales

                    if user_comp[0] == True: #Caracteristicas del texto1
                        posxtxt1 = round(0.775375 * ancho) - calcularx(user_comp[1], ancho)

                    else:
                        posxtxt1 = None

                    posytxt1 = round(0.0125 * ancho)
                    tamañotxt1 = round(0.015625 * ancho)

                    #Otros principales

                    posy1rect1 = round(0.0328125 * ancho) #Caracteristicas del rectangulo1
                    posy2rect1 = round(0.13825 * ancho)
                    diferenciaentrelos2 = round(0.00234375 * ancho)

                    #Botones secundarios

                    posy1bot3 = round(0.0484375 * ancho) #Caracteristicas del bot3
                    posy2bot3 = round(0.066406 * ancho)
                    tamañobot3 = round(0.015625 * ancho)

                    posy1bot4 = round(0.06796 * ancho) #Caracteristicas del bot4
                    posy2bot4 = round(0.08593 * ancho)
                    tamañobot4 = round(0.015625 * ancho)

                    posy1bot5 = round(0.0875 * ancho) #Caracteristicas del bot5
                    posy2bot5 = round(0.10546 * ancho)
                    tamañobot5 = round(0.015625 * ancho)

                    posy1bot6 = round(0.10703125 * ancho) #Caracteristicas de bot6
                    posy2bot6 = round(0.125 * ancho)
                    tamañobot6 = round(0.015625 * ancho)

                    #Textos secundarios

                    #Otros secundarios

                    tamañotxtgeneralconsola = round(0.0234375 * ancho)

                    if pantalla_comp_ext == "True":

                        pantalla_comp = True
                        try:

                            pygame.display.set_mode((ancho, alto), pygame.FULLSCREEN)

                        except:
                            pass
                        actualizar_dato("pantcomp", pantalla_comp)
                        
                        botytxt1 = crear_boton("COMENZAR", posx1comenzar, posy1comenzar, posx2comenzar, posy2comenzar, tamañocomenzar, ventana, negro, tipodeletra, blanco)
                        rectangulo1 = botytxt1[1]
                        posesxybot1 = rectangulo1[1]
                        posesxy2bot1 = rectangulo1[2]

                        if user_act[0] == False:
                            botytxt2 = crear_boton("LOGGEAR/CREAR USUARIO", posx1logandcre, posy1logandcre, posx2logandcre, posy2logandcre, tamañologandcre, ventana, negro, tipodeletra, blanco)
                            rectangulo2 = botytxt2[1]
                            posesxybot2 = rectangulo2[1]
                            posesxy2bot2 = rectangulo2[2]
                            txt1 = None

                        else:
                            botytxt2 = crear_boton("AJUSTES DE USUARIO", posx1ajus, posy1ajus, posx2ajus, posy2ajus, tamañoajus, ventana, negro, tipodeletra, blanco)
                            rectangulo2 = botytxt2[1]
                            posesxybot2 = rectangulo2[1]
                            posesxy2bot2 = rectangulo2[2]
                            txt1 = print_pantalla("Usuario: " + user_comp[1], posxtxt1, posytxt1, tamañotxt1, blanco, tipodeletra)
                            posxytxt1 = txt1[1]

                    else:

                        pantalla_comp = False
                        try:
                            pygame.display.set_mode((ancho, alto))

                        except:
                            pass

                        actualizar_dato("pantcomp", pantalla_comp)

                        ventana.blit(imagen_de_fondo, (0, 0))
                        pygame.display.update()
                        botytxt1 = crear_boton("COMENZAR", posx1comenzar, posy1comenzar, posx2comenzar, posy2comenzar, tamañocomenzar, ventana, negro, tipodeletra, blanco)
                        rectangulo1 = botytxt1[1]
                        posesxybot1 = rectangulo1[1]
                        posesxy2bot1 = rectangulo1[2]

                        if user_comp[0] == False:
                            botytxt2 = crear_boton("LOGGEAR/CREAR USUARIO", posx1logandcre, posy1logandcre, posx2logandcre, posy2logandcre, tamañologandcre, ventana, negro, tipodeletra, blanco)
                            rectangulo2 = botytxt2[1]
                            posesxybot2 = rectangulo2[1]
                            posesxy2bot2 = rectangulo2[2]
                            txt1 = None

                        else:
                            botytxt2 = crear_boton("AJUSTES DE USUARIO", posx1ajus, posy1ajus, posx2ajus, posy2ajus, tamañoajus, ventana, negro, tipodeletra, blanco)
                            rectangulo2 = botytxt2[1]
                            posesxybot2 = rectangulo2[1]
                            posesxy2bot2 = rectangulo2[2]
                            txt1 = print_pantalla("Usuario: " + user_comp[1], posxtxt1, posytxt1, tamañotxt1, blanco, tipodeletra)
                            posxytxt1 = txt1[1]

                elif accion == "col":

                    ventana.fill(negro)

                    terminargen = False

                    while terminargen == False:

                        letras = str("")
                        intro = False

                        while intro == False:
                            conj1 = preguntar(letras, tipodeletra, "Indique 'c' si quiere crear un usuario o 'l' si quiere loggearse", 0, ventana, round(0.01953125 * ancho), 43, (alto, ancho))
                            letras = conj1[1]
                            intro = conj1[0]

                        if letras == "/Exit":
                            terminal = False
                            terminargen = True

                        else:
                            terminal = True

                            crearologgear = letras

                            if crearologgear == "c":
                                intro = False
                                letras = str("")
                                terminado = False

                                while terminado == False:

                                    while intro == False:
                                        conj1 = preguntar(letras, tipodeletra, "Indique su nombre de usuario minimo 3 chr", 1.5, ventana, round(0.078125 * ancho), 16, (alto, ancho), 3)
                                        letras = conj1[1]
                                        intro = conj1[0]

                                    if letras == "/Exit":
                                        terminal = False
                                        terminado = True
                                        terminargen = True

                                    else:

                                        if not obtenerdato("Datos", "cuentas", letras, 1): terminado = True

                                        else:
                                            print("Ese usuario ya existe")
                                            letraslist = []
                                            letraslist.extend(letras)
                                            xtoerrase = calcularx(letraslist, ancho)
                                            rectangulo = pygame.draw.rect(ventana, negro, (round(0.021875 * ancho), round(0.09375 * ancho), xtoerrase, round(0.15625 * ancho)))
                                            pygame.display.update()
                                            letras = str("")
                                            miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                            miTexto2 = miFuente2.render("Ese usuario ya existe", 0, rojo)
                                            posxtgo = calcularx(letras, ancho)
                                            ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.09765625 * ancho)))
                                            pygame.display.update()
                                            time.sleep(1)
                                            miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                            miTexto2 = miFuente2.render("Ese usuario ya existe", 0, negro)
                                            ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.09765625 * ancho)))
                                            pygame.display.update()
                                            intro = False

                                if terminal == True:

                                    nombredeusuario = letras

                                    intro = False
                                    letras = str("")
                                    terminado = False

                                    while terminado == False:

                                        while intro == False:
                                            conj1 = preguntar(letras, tipodeletra, "Indique su contraseña minimo 5 chr (Solo numeros positivos)", 3, ventana, round(0.13671875 * ancho), 16, (alto, ancho), 5, True)
                                            letras = conj1[1]
                                            intro = conj1[0]

                                        if letras == "/Exit":
                                            terminal = False
                                            terminado = True
                                            terminargen = True

                                        else:

                                            try:
                                                x = int(letras)

                                                if int(letras) < 0:
                                                    print(hola)

                                            except:
                                                print("La contraseña introducida no es valida")
                                                letraslist = []
                                                letraslist.extend(letras)
                                                xtoerrase = calcularx(letraslist, ancho, True)
                                                rectangulo = pygame.draw.rect(ventana, negro, (round(0.021875 * ancho), round(0.15234375 * ancho), xtoerrase, round(0.15625 * ancho)))
                                                pygame.display.update()
                                                letras = str("")
                                                miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                miTexto2 = miFuente2.render("Tienen que ser numeros positivos", 0, rojo)
                                                posxtgo = calcularx(letras, ancho)
                                                ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.15625 * ancho)))
                                                pygame.display.update()
                                                time.sleep(1)
                                                miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                miTexto2 = miFuente2.render("Tienen que ser numeros positivos", 0, negro)
                                                ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.15625 * ancho)))
                                                pygame.display.update()
                                                intro = False

                                            else:
                                                terminado = True

                                    if terminal == True:

                                        contraseña = letras

                                        intro = False
                                        letras = str("")

                                        while intro == False:
                                            conj1 = preguntar(letras, tipodeletra, "Indique su correo electronico minimo 5 chr (Este correo no podra ser cambiado)", 4.5, ventana, round(0.1953125 * ancho), 43, (alto, ancho), 5)
                                            letras = conj1[1]
                                            intro = conj1[0]

                                        if letras == "/Exit":
                                            terminal = False
                                            terminargen = True

                                        else:
                                            correo = letras

                                            intro = False
                                            letras = str("")
                                            terminado = False

                                            while terminado == False:

                                                while intro == False:
                                                    conj1 = preguntar(letras, tipodeletra, "Indique su fecha de nacimiento estructura: 01-01-2001", 6, ventana, round(0.25390625 * ancho), 10, (alto, ancho))
                                                    letras = conj1[1]
                                                    intro = conj1[0]

                                                if letras == "/Exit":
                                                    terminal = False
                                                    terminado = True
                                                    terminargen = True

                                                else:
                                                    if len(letras) == 10:

                                                        nacimientolist = []

                                                        nacimientolist.extend(letras)

                                                        x = 0

                                                        jota = 0

                                                        error = False

                                                        for letra in nacimientolist:

                                                            x = x +1

                                                            try:
                                                                jota = int(letra) + 1

                                                            except:
                                                                integer = 0 #Si no es numero

                                                            else:
                                                                integer = 1 #Si es numero

                                                            if x == 1 and integer == 1:
                                                                pass

                                                            elif x == 2 and integer == 1:
                                                                pass

                                                            elif x == 3 and letra == "-":
                                                                pass

                                                            elif x == 4 and integer == 1:
                                                                pass

                                                            elif x == 5 and integer == 1:
                                                                pass

                                                            elif x == 6 and letra == "-":
                                                                pass

                                                            elif x == 7 and integer == 1:
                                                                pass

                                                            elif x == 8 and integer == 1:
                                                                pass

                                                            elif x == 9 and integer == 1:
                                                                pass

                                                            elif x == 10 and integer == 1:
                                                                pass

                                                            else:
                                                                error = True

                                                        if error == False:
                                                            terminado = True

                                                            fecha_de_nacimiento = letras

                                                            cont_cifrada = cifrar_contraseña(contraseña)

                                                            comp2 = loggearocrear(False, nombredeusuario, cont_cifrada, "c", fecha_de_nacimiento, correo)

                                                            ultimoidentificador = ultimoident("Records", "records")

                                                            datos_a_insertar = (nombredeusuario, 0, ultimoidentificador +1)

                                                            ultimoidentificador = ultimoident("Records", "monedas")

                                                            datos_a_insertar_monedas = (nombredeusuario, 0, ultimoidentificador +1)

                                                            insertardatos("Records", datos_a_insertar_monedas, "Datos insertados correctamente", "Hubo un error al insertar los datos", "monedas")

                                                            insertardatos("Records", datos_a_insertar, "Datos insertados correctamente", "Hubo un error al insertar los datos")

                                                            comprovarigualdad("Records", "records", 0)

                                                            ordenarDBrespectoaotraDB("Records", "records", 0)

                                                            crearbasededatosniveles(nombredeusuario)

                                                            user_comp = [True, nombredeusuario]

                                                            print("Loggeado como", nombredeusuario)

                                                            toca = 1

                                                            data_niveles = []

                                                            if user_comp[0] == True:

                                                                for x in range(30):
                                                                    ordenardbniveles(user_act[1], x + 1)

                                                                while toca < 31:

                                                                    data_nivel = extraerdatos(nombredeusuario, toca)

                                                                    data_niveles.append(data_nivel)

                                                                    toca += 1

                                                            terminargen = True

                                                            ventana.blit(imagen_de_fondo, (0, 0))
                                                            ventana.blit(ImagenInsetCoins, (504, 10))
                                                            ventana.blit(Portada, (Portadax, Portaday))
                                                            ventana.blit(botytxt1[0], (posesxybot1[0], posesxybot1[1]))
                                                            ventana.blit(botytxt2[0], (posesxybot2[0], posesxybot2[1]))
                                                            if txt1 != None: ventana.blit(txt1[0], (posxytxt1[0], posxytxt1[1]))
                                                            ventana.blit(bot7, (posx1ajustes, posy1ajustes))

                                                            pygame.display.update()

                                                            sucedio_accion = False

                                                        else:
                                                            print("La sintaxis no es correcta")
                                                            letraslist = []
                                                            letraslist.extend(letras)
                                                            xtoerrase = calcularx(letraslist, ancho)
                                                            rectangulo = pygame.draw.rect(ventana, negro, (round(0.021875 * ancho), round(0.26953125 * ancho), xtoerrase, round(0.15625 * ancho)))
                                                            pygame.display.update()
                                                            letras = str("")
                                                            miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                            miTexto2 = miFuente2.render("La sintaxis no es correcta", 0, rojo)
                                                            ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.2734375 * ancho)))
                                                            pygame.display.update()
                                                            time.sleep(1)
                                                            miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                            miTexto2 = miFuente2.render("La sintaxis no es correcta", 0, negro)
                                                            ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.2734375 * ancho)))
                                                            pygame.display.update()
                                                            intro = False

                            elif crearologgear == "l":
                                intro = False
                                letras = str("")
                                terminado = False

                                while terminado == False:

                                    while intro == False:
                                        conj1 = preguntar(letras, tipodeletra, "Indique su nombre de usuario", 1.5, ventana, round(0.078125 * ancho), 16, (alto, ancho), 3)
                                        letras = conj1[1]
                                        intro = conj1[0]

                                    if letras == "/Exit":
                                        terminal = False
                                        terminado = True
                                        terminargen = True

                                    elif obtenerdato("Datos", "cuentas", letras, 1): terminado = True

                                    else:
                                        print("Ese usuario no existe")
                                        letraslist = []
                                        letraslist.extend(letras)
                                        xtoerrase = calcularx(letraslist, ancho)
                                        rectangulo = pygame.draw.rect(ventana, negro, (round(0.021875 * ancho), round(0.09375 * ancho), xtoerrase, round(0.15625 * ancho)))
                                        pygame.display.update()
                                        letras = str("")
                                        miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                        miTexto2 = miFuente2.render("Ese usuario no existe", 0, rojo)
                                        posxtgo = calcularx(letras, ancho)
                                        ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.09765625 * ancho)))
                                        pygame.display.update()
                                        time.sleep(1)
                                        miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                        miTexto2 = miFuente2.render("Ese usuario no existe", 0, negro)
                                        ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.09765625 * ancho)))
                                        pygame.display.update()
                                        intro = False

                                if terminal == True:

                                    nombredeusuario = letras

                                    listadodeuser = obtenerdato("Datos", "cuentas", letras, 1)

                                    intro = False
                                    letras = str("")
                                    terminado = False
                                    terminado2 = False

                                    while terminado == False:

                                            while intro == False:
                                                conj1 = preguntar(letras, tipodeletra, "Indique su contraseña minimo 5 chr (Solo numeros positivos)", 3, ventana, round(0.13671875 * ancho), 16, (alto, ancho), 5, True)
                                                letras = conj1[1]
                                                intro = conj1[0]

                                            if letras == "/Exit":
                                                terminal = False
                                                terminado = True
                                                terminargen = True

                                            else:

                                                try:
                                                    x = int(letras)

                                                    if int(letras) < 0:
                                                        print(hola)

                                                except:
                                                    print("La contraseña introducida no es valida")
                                                    letraslist = []
                                                    letraslist.extend(letras)
                                                    xtoerrase = calcularx(letraslist, ancho, True)
                                                    rectangulo = pygame.draw.rect(ventana, negro, (round(0.021875 * ancho), round(0.15234375 * ancho), xtoerrase, round(0.15625 * ancho)))
                                                    pygame.display.update()
                                                    letras = str("")
                                                    miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                    miTexto2 = miFuente2.render("Tienen que ser numeros positivos", 0, rojo)
                                                    posxtgo = calcularx(letras, ancho)
                                                    ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.15625 * ancho)))
                                                    pygame.display.update()
                                                    time.sleep(1)
                                                    miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                    miTexto2 = miFuente2.render("Tienen que ser numeros positivos", 0, negro)
                                                    ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.15625 * ancho)))
                                                    pygame.display.update()
                                                    intro = False

                                                else:

                                                    contraseñadescifrada = descifrar_contraseña(listadodeuser[3], letras[0])

                                                    if contraseñadescifrada == letras:
                                                        terminado = True

                                                        contraseña = letras

                                                        user_comp = [True, nombredeusuario]

                                                        ventana.fill(negro)

                                                        print("Loggeado como", nombredeusuario)

                                                        toca = 1

                                                        data_niveles = []

                                                        if user_comp[0] == True:

                                                            for x in range(30):
                                                                ordenardbniveles(user_act[1], x + 1)

                                                            while toca < 31:

                                                                data_nivel = extraerdatos(nombredeusuario, toca)

                                                                data_niveles.append(data_nivel)

                                                                toca += 1

                                                        terminargen = True

                                                        ventana.blit(imagen_de_fondo, (0, 0))
                                                        ventana.blit(ImagenInsetCoins, (504, 10))
                                                        ventana.blit(Portada, (Portadax, Portaday))
                                                        ventana.blit(botytxt1[0], (posesxybot1[0], posesxybot1[1]))
                                                        ventana.blit(botytxt2[0], (posesxybot2[0], posesxybot2[1]))
                                                        if txt1 != None: ventana.blit(txt1[0], (posxytxt1[0], posxytxt1[1]))
                                                        ventana.blit(bot7, (posx1ajustes, posy1ajustes))
                                                        pygame.display.update()

                                                        sucedio_accion = False

                                                    else:
                                                        print("La contraseña introducida es incorrecta")
                                                        letraslist = []
                                                        letraslist.extend(letras)
                                                        xtoerrase = calcularx(letraslist, ancho)
                                                        rectangulo = pygame.draw.rect(ventana, negro, (round(0.021875 * ancho), round(0.15234375 * ancho), xtoerrase, round(0.15625 * ancho)))
                                                        pygame.display.update()
                                                        letras = str("")
                                                        miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                        miTexto2 = miFuente2.render("No es la contraseña de ese usuario", 0, rojo)
                                                        posxtgo = calcularx(letras, ancho)
                                                        ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.15625 * ancho)))
                                                        pygame.display.update()
                                                        time.sleep(1)
                                                        miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                        miTexto2 = miFuente2.render("No es la contraseña de ese usuario", 0, negro)
                                                        ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.15625 * ancho)))
                                                        pygame.display.update()
                                                        intro = False

                            elif terminal == True:
                                print("Ese caracter no esta definido")
                                letraslist = []
                                letraslist.extend(letras)
                                xtoerrase = calcularx(letraslist, ancho)
                                rectangulo = pygame.draw.rect(ventana, negro, (round(0.021875 * ancho), round(0.03515625 * ancho), xtoerrase, round(0.15625 * ancho)))
                                pygame.display.update()
                                letras = str("")
                                miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                miTexto2 = miFuente2.render("Ese caracter no esta definido", 0, rojo)
                                posxtgo = calcularx(letras, ancho)
                                ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.03515625 * ancho)))
                                pygame.display.update()
                                time.sleep(1)
                                miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                miTexto2 = miFuente2.render("Ese caracter no esta definido", 0, negro)
                                ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.03515625 * ancho)))
                                pygame.display.update()
                                intro = False
                                terminado = False

                    if terminal == False:

                        user_comp = [False, "nombredeusuario"]
                        print("Loggeo cancelado")
                        ventana.blit(imagen_de_fondo, (0, 0))
                        ventana.blit(ImagenInsetCoins, (504, 10))
                        ventana.blit(Portada, (Portadax, Portaday))
                        pygame.display.update()

                elif accion == "ajustesuser":
                    var_cont = False

                    abierto = False

                    def configuracion_intro(user_comp, ventana, alto, ancho, tipodeletra, postxtant1, posx1comenzar, posx2comenzar, posy1comenzar, posy2comenzar, tamañocomenzar, posx1ajus, posx2ajus, posy1ajus, posy2ajus, tamañoajus, posxtxt1, posytxt1, tamañotxt1, posxytxt1):

                            botytxt1 = crear_boton("COMENZAR", posx1comenzar, posy1comenzar, posx2comenzar, posy2comenzar, tamañocomenzar, ventana, (0, 0, 0), tipodeletra, (255, 255, 255))
                            rectangulo1 = botytxt1[1]
                            posesxybot1 = rectangulo1[1]
                            posesxy2bot1 = rectangulo1[2]
                            ventana.blit(botytxt1[0], (posesxybot1[0], posesxybot1[1])) 
                            pygame.display.update()

                            if user_comp[0] == False:
                                botytxt2 = crear_boton("LOGGEAR/CREAR USUARIO", posx1logandcre, posy1logandcre, posx2logandcre, posy2logandcre, tamañologandcre, ventana, (0, 0, 0), tipodeletra, (255, 255, 255))
                                rectangulo2 = botytxt2[1]
                                posesxybot2 = rectangulo2[1]
                                posesxy2bot2 = rectangulo2[2]
                                txt1 = None

                            else:
                                botytxt2 = crear_boton("AJUSTES DE USUARIO", posx1ajus, posy1ajus, posx2ajus, posy2ajus, tamañoajus, ventana, (0, 0, 0), tipodeletra, (255, 255, 255))
                                rectangulo2 = botytxt2[1]
                                posesxybot2 = rectangulo2[1]
                                posesxy2bot2 = rectangulo2[2]
                                txt1 = print_pantalla("Usuario: " + user_comp[1], posxtxt1, posytxt1, tamañotxt1, (255, 255, 255), tipodeletra)
                                posxytxt1 = postxtant1

                            if user_comp[0] == True: ventana.blit(txt1[0], (posxytxt1[0], posxytxt1[1]))
                            ventana.blit(botytxt2[0], (posesxybot2[0], posesxybot2[1])) 
                            pygame.display.update()


                    def dibujar_caja(ventana, posx, posy, posxtogo, posytogo):
                        caja1 = pygame.draw.rect(ventana, negro, ((posx, posy),(posxtogo - posx, posytogo - posy)), 3)
                        relleno_caja1 = pygame.draw.rect(ventana, blanco, ((posx + diferenciaentrelos2, posy + round(0.0015625 * ancho)),(posxtogo - posx - round(0.00390625 * ancho), posytogo - posy - round(0.003125 * ancho))))
                        pygame.display.update()
                        return [caja1, relleno_caja1]

                    if abierto == True:
                        pass


                    else:

                        dibujar_caja(ventana, posx1ajus, posy1rect1, posx2ajus, posy2rect1)
                        botytxt3 = crear_boton2(ventana, posx1ajus + diferenciaentrelos2, posy1bot3, posx2ajus - diferenciaentrelos2, posy2bot3, "Cambiar datos", tamañobot3, negro, tipodeletra, blanco)
                        rectangulo3 = botytxt3[1]
                        posesxybot3 = rectangulo3[1]
                        posesxy2bot3 = rectangulo3[2]

                        botytxt4 = crear_boton2(ventana, posx1ajus + diferenciaentrelos2, posy1bot4, posx2ajus - diferenciaentrelos2, posy2bot4, "Borrar usuario", tamañobot4, negro, tipodeletra, blanco)
                        rectangulo4 = botytxt4[1]
                        posesxybot4 = rectangulo4[1]
                        posesxy2bot4 = rectangulo4[2]

                        botytxt5 = crear_boton2(ventana, posx1ajus + diferenciaentrelos2, posy1bot5, posx2ajus - diferenciaentrelos2, posy2bot5, "Mostrar datos", tamañobot5, negro, tipodeletra, blanco)
                        rectangulo5 = botytxt5[1]
                        posesxybot5 = rectangulo5[1]
                        posesxy2bot5 = rectangulo5[2]

                        botytxt6 = crear_boton2(ventana, posx1ajus + diferenciaentrelos2, posy1bot6, posx2ajus - diferenciaentrelos2, posy2bot6, "Salir del usuario", tamañobot6, negro, tipodeletra, blanco)
                        rectangulo6 = botytxt6[1]
                        posesxybot6 = rectangulo6[1]
                        posesxy2bot6 = rectangulo6[2]

                        ratonx, ratony = pygame.mouse.get_pos()

                        vuelta = False

                        while vuelta == False:
                            accion2 = ""

                            for evento in pygame.event.get():

                                if evento.type == QUIT:
                                    print("Juego terminado")
                                    pygame.quit()
                                    raise KeyError

                                if evento.type == KEYDOWN:

                                    if evento.key == 285:
                                        print("Juego terminado")
                                        pygame.quit()
                                        raise KeyError

                                    elif evento.key == 27:

                                        pantalla_comp = True
                                        try:
                                            pygame.display.set_mode((ancho, alto))

                                        except:
                                            pass

                                        actualizar_dato("pantcomp", pantalla_comp)
                                            
                                        ventana.blit(imagen_de_fondo, (0, 0))
                                        ventana.blit(ImagenInsetCoins, (504, 10))
                                        ventana.blit(Portada, (Portadax, Portaday))
                                        pygame.display.update()
                                        botytxt1 = crear_boton("COMENZAR", posx1comenzar, posy1comenzar, posx2comenzar, posy2comenzar, tamañocomenzar, ventana, (0, 0, 0), tipodeletra, (255, 255, 255))
                                        rectangulo1 = botytxt1[1]
                                        posesxybot1 = rectangulo1[1]
                                        posesxy2bot1 = rectangulo1[2]

                                        if user_comp[0] == False:
                                            botytxt2 = crear_boton("LOGGEAR/CREAR USUARIO", posx1logandcre, posy1logandcre, posx2logandcre, posy2logandcre, tamañologandcre, ventana, negro, tipodeletra, blanco)
                                            rectangulo2 = botytxt2[1]
                                            posesxybot2 = rectangulo2[1]
                                            posesxy2bot2 = rectangulo2[2]
                                            txt1 = None

                                        else:
                                            botytxt2 = crear_boton("AJUSTES DE USUARIO", posx1ajus, posy1ajus, posx2ajus, posy2ajus, tamañoajus, ventana, negro, tipodeletra, blanco)
                                            rectangulo2 = botytxt2[1]
                                            posesxybot2 = rectangulo2[1]
                                            posesxy2bot2 = rectangulo2[2]
                                            txt1 = print_pantalla("Usuario: " + user_comp[1], posxtxt1, posytxt1, tamañotxt1, blanco, tipodeletra)
                                            posxytxt1 = txt1[1]

                                        ventana.blit(txt1[0], (posxytxt1[0], posxytxt1[1]))
                                        ventana.blit(botytxt1[0], (posesxybot1[0], posesxybot1[1])) 
                                        ventana.blit(botytxt2[0], (posesxybot2[0], posesxybot2[1])) 
                                        dibujar_caja(ventana, posx1ajus, posy1rect1, posx2ajus, posy2rect1)
                                        pygame.display.update()

                                    
                                    elif evento.key == 292:

                                        pantalla_comp = False
                                        try:
                                            pygame.display.set_mode((ancho, alto), pygame.FULLSCREEN)

                                        except:
                                            pass

                                        actualizar_dato("pantcomp", pantalla_comp)

                                        ventana.blit(imagen_de_fondo, (0, 0))
                                        ventana.blit(ImagenInsetCoins, (504, 10))
                                        ventana.blit(Portada, (Portadax, Portaday))
                                        pygame.display.update()
                                        botytxt1 = crear_boton("COMENZAR", posx1comenzar, posy1comenzar, posx2comenzar, posy2comenzar, tamañocomenzar, ventana, (0, 0, 0), tipodeletra, (255, 255, 255))
                                        rectangulo1 = botytxt1[1]
                                        posesxybot1 = rectangulo1[1]
                                        posesxy2bot1 = rectangulo1[2]

                                        if user_act[0] == False:
                                            botytxt2 = crear_boton("LOGGEAR/CREAR USUARIO", posx1logandcre, posy1logandcre, posx2logandcre, posy2logandcre, tamañologandcre, ventana, negro, tipodeletra, blanco)
                                            rectangulo2 = botytxt2[1]
                                            posesxybot2 = rectangulo2[1]
                                            posesxy2bot2 = rectangulo2[2]
                                            txt1 = None

                                        else:
                                            botytxt2 = crear_boton("AJUSTES DE USUARIO", posx1ajus, posy1ajus, posx2ajus, posy2ajus, tamañoajus, ventana, negro, tipodeletra, blanco)
                                            rectangulo2 = botytxt2[1]
                                            posesxybot2 = rectangulo2[1]
                                            posesxy2bot2 = rectangulo2[2]
                                            txt1 = print_pantalla("Usuario: " + user_act[1], posxtxt1, posytxt1, tamañotxt1, blanco, tipodeletra)
                                            posxytxt1 = txt1[1]

                                        ventana.blit(txt1[0], (posxytxt1[0], posxytxt1[1]))
                                        ventana.blit(botytxt1[0], (posesxybot1[0], posesxybot1[1])) 
                                        ventana.blit(botytxt2[0], (posesxybot2[0], posesxybot2[1])) 
                                        dibujar_caja(ventana, posx1ajus, posy1rect1, posx2ajus, posy2rect1)
                                        pygame.display.update()


                                if evento.type == MOUSEBUTTONDOWN:

                                    if ratonx > posesxybot3[0] and ratony > posesxybot3[1] and ratonx < posesxy2bot3[0] and ratony < posesxy2bot3[1]:
                                        botytxt3 = crear_boton2(ventana,  posx1ajus + diferenciaentrelos2, posy1bot3, posx2ajus - diferenciaentrelos2, posy2bot3, "Cambiar datos", tamañobot3, negro, tipodeletra, blanco)
                                        rectangulo3 = botytxt3[1]
                                        posesxybot3 = rectangulo3[1]
                                        posesxy2bot3 = rectangulo3[2]
                                        print("Boton 3 pulsado")
                                        accion2 = "cambiar datos"


                                    elif ratonx > posesxybot4[0] and ratony > posesxybot4[1] and ratonx < posesxy2bot4[0] and ratony < posesxy2bot4[1]:
                                        botytxt4 = crear_boton2(ventana, posx1ajus + diferenciaentrelos2, posy1bot4, posx2ajus - diferenciaentrelos2, posy2bot4, "Borrar usuario", tamañobot4, negro, tipodeletra, blanco)
                                        rectangulo4 = botytxt4[1]
                                        posesxybot4 = rectangulo4[1]
                                        posesxy2bot4 = rectangulo4[2]
                                        print("Boton 4 pulsado")
                                        accion2 = "borrar usuario"

                                    elif ratonx > posesxybot5[0] and ratony > posesxybot5[1] and ratonx < posesxy2bot5[0] and ratony < posesxy2bot5[1]:
                                        botytxt5 = crear_boton2(ventana, posx1ajus + diferenciaentrelos2, posy1bot5, posx2ajus - diferenciaentrelos2, posy2bot5, "Mostrar datos", tamañobot5, negro, tipodeletra, blanco)
                                        rectangulo5 = botytxt5[1]
                                        posesxybot5 = rectangulo5[1]
                                        posesxy2bot5 = rectangulo5[2]
                                        print("Boton 5 pulsado")
                                        accion2 = "mostrar datos"

                                    elif ratonx > posesxybot6[0] and ratony > posesxybot6[1] and ratonx < posesxy2bot6[0] and ratony < posesxy2bot6[1]:
                                        botytxt6 = crear_boton2(ventana, posx1ajus + diferenciaentrelos2, posy1bot6, posx2ajus - diferenciaentrelos2, posy2bot6, "Salir del usuario", tamañobot6, negro, tipodeletra, blanco)
                                        rectangulo6 = botytxt6[1]
                                        posesxybot6 = rectangulo6[1]
                                        posesxy2bot6 = rectangulo6[2]
                                        print("Boton 6 pulsado")
                                        accion2 = "salir del usuario"

                                    elif  ratonx > posx1ajus and ratony > posy1rect1 and ratonx < posx2ajus and ratony < posy2rect1:
                                        pass

                                    else:
                                        configuracion_intro(user_comp, ventana, alto, ancho, tipodeletra, posxytxt1, posx1comenzar, posx2comenzar, posy1comenzar, posy2comenzar, tamañocomenzar, posx1ajus, posx2ajus, posy1ajus, posy2ajus, tamañoajus, posxtxt1, posytxt1, tamañotxt1, posxytxt1)
                                        vuelta = True
                                        pygame.display.update()
                                        ratonx, ratony = pygame.mouse.get_pos()

                                else:

                                    if ratonx > posesxybot3[0] and ratony > posesxybot3[1] and ratonx < posesxy2bot3[0] and ratony < posesxy2bot3[1]:
                                        botytxt3 = crear_boton2(ventana, posx1ajus + diferenciaentrelos2, posy1bot3, posx2ajus - diferenciaentrelos2, posy2bot3, "Cambiar datos", tamañobot3, blanco, tipodeletra, negro)
                                        rectangulo3 = botytxt3[1]
                                        posesxybot3 = rectangulo3[1]
                                        posesxy2bot3 = rectangulo3[2]

                                    elif ratonx > posesxybot4[0] and ratony > posesxybot4[1] and ratonx < posesxy2bot4[0] and ratony < posesxy2bot4[1]:
                                        botytxt4 = crear_boton2(ventana, posx1ajus + diferenciaentrelos2, posy1bot4, posx2ajus - diferenciaentrelos2, posy2bot4, "Borrar usuario", tamañobot4, blanco, tipodeletra, negro)
                                        rectangulo4 = botytxt4[1]
                                        posesxybot4 = rectangulo4[1]
                                        posesxy2bot4 = rectangulo4[2]

                                    elif ratonx > posesxybot5[0] and ratony > posesxybot5[1] and ratonx < posesxy2bot5[0] and ratony < posesxy2bot5[1]:
                                        botytxt5 = crear_boton2(ventana, posx1ajus + diferenciaentrelos2, posy1bot5, posx2ajus - diferenciaentrelos2, posy2bot5, "Mostrar datos", tamañobot5, blanco, tipodeletra, negro)
                                        rectangulo5 = botytxt5[1]
                                        posesxybot5 = rectangulo5[1]
                                        posesxy2bot5 = rectangulo5[2]

                                    elif ratonx > posesxybot6[0] and ratony > posesxybot6[1] and ratonx < posesxy2bot6[0] and ratony < posesxy2bot6[1]:
                                        botytxt6 = crear_boton2(ventana, posx1ajus + diferenciaentrelos2, posy1bot6, posx2ajus - diferenciaentrelos2, posy2bot6, "Salir del usuario", tamañobot6, blanco, tipodeletra, negro)
                                        rectangulo6 = botytxt6[1]
                                        posesxybot6 = rectangulo6[1]
                                        posesxy2bot6 = rectangulo6[2]

                                    else:
                                        botytxt3 = crear_boton2(ventana, posx1ajus + diferenciaentrelos2, posy1bot3, posx2ajus - diferenciaentrelos2, posy2bot3, "Cambiar datos", tamañobot3, negro, tipodeletra, blanco)
                                        rectangulo3 = botytxt3[1]
                                        posesxybot3 = rectangulo3[1]
                                        posesxy2bot3 = rectangulo3[2]

                                        botytxt4 = crear_boton2(ventana, posx1ajus + diferenciaentrelos2, posy1bot4, posx2ajus - diferenciaentrelos2, posy2bot4, "Borrar usuario", tamañobot4, negro, tipodeletra, blanco)
                                        rectangulo4 = botytxt4[1]
                                        posesxybot4 = rectangulo4[1]
                                        posesxy2bot4 = rectangulo4[2]

                                        botytxt5 = crear_boton2(ventana, posx1ajus + diferenciaentrelos2, posy1bot5, posx2ajus - diferenciaentrelos2, posy2bot5, "Mostrar datos", tamañobot5, negro, tipodeletra, blanco)
                                        rectangulo5 = botytxt5[1]
                                        posesxybot5 = rectangulo5[1]
                                        posesxy2bot5 = rectangulo5[2]

                                        botytxt6 = crear_boton2(ventana, posx1ajus + diferenciaentrelos2, posy1bot6, posx2ajus - diferenciaentrelos2, posy2bot6, "Salir del usuario", tamañobot6, negro, tipodeletra, blanco)
                                        rectangulo6 = botytxt6[1]
                                        posesxybot6 = rectangulo6[1]
                                        posesxy2bot6 = rectangulo6[2]

                                if var_cont == False:
                                    configuracion_intro(user_comp, ventana, alto, ancho, tipodeletra, posxytxt1, posx1comenzar, posx2comenzar, posy1comenzar, posy2comenzar, tamañocomenzar, posx1ajus, posx2ajus, posy1ajus, posy2ajus, tamañoajus, posxtxt1, posytxt1, tamañotxt1, posxytxt1)
                                    var_cont = True

                                ratonx, ratony = pygame.mouse.get_pos()
                                if vuelta == False: ventana.blit(botytxt3[0], (posesxybot3[0], posesxybot3[1])) 
                                if vuelta == False: ventana.blit(botytxt4[0], (posesxybot4[0], posesxybot4[1])) 
                                if vuelta == False: ventana.blit(botytxt5[0], (posesxybot5[0], posesxybot5[1]))
                                if vuelta == False: ventana.blit(botytxt6[0], (posesxybot6[0], posesxybot6[1]))
                                ventana.blit(bot7, (posx1ajustes, posy1ajustes))
                                ventana.blit(ImagenInsetCoins, (504, 10))
                                ventana.blit(Portada, (Portadax, Portaday))
                                pygame.display.update()

                                if accion2 == "cambiar datos":
                                    ventana.fill(negro)

                                    terminargen = False

                                    terminal = True

                                    while terminargen == False:
                                        letras = str("")
                                        intro = False

                                        while intro == False:
                                            conj1 = preguntar(letras, tipodeletra, "Indique el elemento que quiere cambiar: contraseña o fecha de nacimiento", 0, ventana, round(0.01953125 * ancho), 43, (alto, ancho))
                                            letras = conj1[1]
                                            intro = conj1[0]

                                        if letras == "/Exit":
                                            terminal = False
                                            terminargen = True

                                        else:
                                            if letras == "contraseña":
                                                letras = str("")
                                                intro = False
                                                cuenta_act = obtenerdato("Datos", "cuentas", user_comp[1], 1)
                                                contraseñacifrada_act = cuenta_act[3]
                                                terminado = False

                                                while terminado == False:

                                                    while intro == False:
                                                        conj1 = preguntar(letras, tipodeletra, "Indique la antigua contraseña", 1.5, ventana, round(0.078125 * ancho), 16, (alto, ancho), 5, True)
                                                        letras = conj1[1]
                                                        intro = conj1[0]

                                                    if letras == "/Exit":
                                                        terminal = False
                                                        terminado = True
                                                        terminargen = True

                                                    else:
                                                        contdes = descifrar_contraseña(contraseñacifrada_act, letras[0])

                                                        if contdes == letras:
                                                            terminado = True

                                                        else:
                                                            print("Esa contraseña no es correcta")
                                                            letraslist = []
                                                            letraslist.extend(letras)
                                                            xtoerrase = calcularx(letraslist, ancho)
                                                            rectangulo = pygame.draw.rect(ventana, negro, (round(0.021875 * ancho), round(0.09375 * ancho), xtoerrase, round(0.15625 * ancho)))
                                                            pygame.display.update()
                                                            letras = str("")
                                                            miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                            miTexto2 = miFuente2.render("Esa contraseña no es correcta", 0, rojo)
                                                            posxtgo = calcularx(letras, ancho)
                                                            ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.09765625 * ancho)))
                                                            pygame.display.update()
                                                            time.sleep(1)
                                                            miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                            miTexto2 = miFuente2.render("Esa contraseña no es correcta", 0, negro)
                                                            ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.09765625 * ancho)))
                                                            pygame.display.update()
                                                            intro = False

                                                letras = str("")
                                                intro = False
                                                terminado = False

                                                if terminal == True:

                                                    while terminado == False:

                                                        while intro == False:
                                                            conj1 = preguntar(letras, tipodeletra, "Indique su nueva contraseña minimo 5 chr (Solo numeros positivos)", 3, ventana, round(0.13671875 * ancho), 16, (alto, ancho), 5, True)
                                                            letras = conj1[1]
                                                            intro = conj1[0]

                                                        if letras == "/Exit":
                                                            terminal = False
                                                            terminado = True
                                                            terminargen = True

                                                        else:

                                                            try:
                                                                x = int(letras)

                                                                if int(letras) < 0:
                                                                    print(hola)

                                                            except:
                                                                print("La contraseña introducida no es valida")
                                                                letraslist = []
                                                                letraslist.extend(letras)
                                                                xtoerrase = calcularx(letraslist, ancho)
                                                                rectangulo = pygame.draw.rect(ventana, negro, (round(0.021875 * ancho), round(0.15234375 * ancho), xtoerrase, round(0.15625 * ancho)))
                                                                pygame.display.update()
                                                                letras = str("")
                                                                miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                                miTexto2 = miFuente2.render("Tienen que ser numeros positivos", 0, rojo)
                                                                posxtgo = calcularx(letras, ancho)
                                                                ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.15625 * ancho)))
                                                                pygame.display.update()
                                                                time.sleep(1)
                                                                miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                                miTexto2 = miFuente2.render("Tienen que ser numeros positivos", 0, negro)
                                                                ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.15625 * ancho)))
                                                                pygame.display.update()
                                                                intro = False

                                                            else:

                                                                terminado = True

                                                                terminargen = True

                                                                print("Contraseña cambiada con exito")

                                                                nueva_contraseña = cifrar_contraseña(letras)

                                                                cambiarele("Datos", "cuentas", "contraseña", nueva_contraseña, 1, cuenta_act[1])

                                                                sucedio_accion = False
                                                else:
                                                    pass

                                            elif letras == "fecha de nacimiento":
                                                letras = str("")
                                                intro = False
                                                cuenta_act = obtenerdato("Datos", "cuentas", user_comp[1], 1)
                                                fecha_de_nacimiento_act = cuenta_act[4]
                                                terminado = False

                                                while terminado == False:

                                                    while intro == False:
                                                        conj1 = preguntar(letras, tipodeletra, "Indique la nueva fecha de nacimiento, la anterior era: " + fecha_de_nacimiento_act, 1.5, ventana, round(0.078125 * ancho), 10, (alto, ancho))
                                                        letras = conj1[1]
                                                        intro = conj1[0]

                                                    if letras == "/Exit":
                                                        terminal = False
                                                        terminargen = True
                                                        terminado = True

                                                    else:
                                                        if len(letras) == 10:

                                                            nacimientolist = []

                                                            nacimientolist.extend(letras)

                                                            x = 0

                                                            jota = 0

                                                            error = False

                                                            for letra in nacimientolist:

                                                                x = x +1

                                                                try:
                                                                    jota = int(letra) + 1

                                                                except:
                                                                    integer = 0 #Si no es numero

                                                                else:
                                                                    integer = 1 #Si es numero

                                                                if x == 1 and integer == 1:
                                                                    pass

                                                                elif x == 2 and integer == 1:
                                                                    pass

                                                                elif x == 3 and letra == "-":
                                                                    pass

                                                                elif x == 4 and integer == 1:
                                                                    pass

                                                                elif x == 5 and integer == 1:
                                                                    pass

                                                                elif x == 6 and letra == "-":
                                                                    pass

                                                                elif x == 7 and integer == 1:
                                                                    pass

                                                                elif x == 8 and integer == 1:
                                                                    pass

                                                                elif x == 9 and integer == 1:
                                                                    pass

                                                                elif x == 10 and integer == 1:
                                                                    pass

                                                                else:
                                                                    error = True

                                                            if error == False:

                                                                terminado = True

                                                                terminargen = True

                                                                print("Fecha de nacimiento cambiada con exito")

                                                                nueva_fecha_de_nacimiento = letras

                                                                cambiarele("Datos", "cuentas", "fecha_de_nacimiento", nueva_fecha_de_nacimiento, 1, cuenta_act[1])

                                                                sucedio_accion = False

                                                            else:
                                                                print("La sintaxis no es correcta")
                                                                letraslist = []
                                                                letraslist.extend(letras)
                                                                xtoerrase = calcularx(letraslist, ancho)
                                                                rectangulo = pygame.draw.rect(ventana, negro, (round(0.021875 * ancho), round(0.09765625 * ancho), xtoerrase, round(0.15625 * ancho)))
                                                                pygame.display.update()
                                                                letras = str("")
                                                                miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                                miTexto2 = miFuente2.render("La sintaxis no es correcta", 0, rojo)
                                                                ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.09765625 * ancho)))
                                                                pygame.display.update()
                                                                time.sleep(1)
                                                                miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                                miTexto2 = miFuente2.render("La sintaxis no es correcta", 0, negro)
                                                                ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.09765625 * ancho)))
                                                                pygame.display.update()
                                                                intro = False
                                                        else:
                                                            print("La sintaxis no es correcta")
                                                            letraslist = []
                                                            letraslist.extend(letras)
                                                            xtoerrase = calcularx(letraslist, ancho)
                                                            rectangulo = pygame.draw.rect(ventana, negro, (round(0.021875 * ancho), round(0.09765625 * ancho), xtoerrase, round(0.15625 * ancho)))
                                                            pygame.display.update()
                                                            letras = str("")
                                                            miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                            miTexto2 = miFuente2.render("La sintaxis no es correcta", 0, rojo)
                                                            ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.09765625 * ancho)))
                                                            pygame.display.update()
                                                            time.sleep(1)
                                                            miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                            miTexto2 = miFuente2.render("La sintaxis no es correcta", 0, negro)
                                                            ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.09765625 * ancho)))
                                                            pygame.display.update()
                                                            intro = False

                                            elif terminal == True:
                                                print("Ese caracter no esta definido")
                                                letraslist = []
                                                letraslist.extend(letras)
                                                xtoerrase = calcularx(letraslist, ancho)
                                                rectangulo = pygame.draw.rect(ventana, negro, (round(0.021875 * ancho), round(0.03515625 * ancho), xtoerrase, round(0.15625 * ancho)))
                                                pygame.display.update()
                                                letras = str("")
                                                miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                miTexto2 = miFuente2.render("Ese caracter no esta definido", 0, rojo)
                                                posxtgo = calcularx(letras, ancho)
                                                ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.03515625 * ancho)))
                                                pygame.display.update()
                                                time.sleep(1)
                                                miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                miTexto2 = miFuente2.render("Ese caracter no esta definido", 0, negro)
                                                ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.03515625 * ancho)))
                                                pygame.display.update()
                                                intro = False
                                                terminado = False
                                                
                                    configuracion_intro(user_comp, ventana, alto, ancho, tipodeletra, posxytxt1, posx1comenzar, posx2comenzar, posy1comenzar, posy2comenzar, tamañocomenzar, posx1ajus, posx2ajus, posy1ajus, posy2ajus, tamañoajus, posxtxt1, posytxt1, tamañotxt1, posxytxt1)
                                    vuelta = True
                                    ventana.blit(imagen_de_fondo, (0, 0))
                                    ventana.blit(ImagenInsetCoins, (504, 10))
                                    ventana.blit(Portada, (Portadax, Portaday))
                                    ventana.blit(botytxt1[0], (posesxybot1[0], posesxybot1[1]))
                                    ventana.blit(botytxt2[0], (posesxybot2[0], posesxybot2[1]))
                                    if txt1 != None: ventana.blit(txt1[0], (posxytxt1[0], posxytxt1[1]))
                                    ventana.blit(bot7, (posx1ajustes, posy1ajustes))
                                    pygame.display.update()
                                    ratonx, ratony = pygame.mouse.get_pos()

                                elif accion2 == "borrar usuario":
                                    ventana.fill(negro)

                                    terminargen = False

                                    terminal = True

                                    while terminargen == False:
                                        letras = str("")
                                        intro = False

                                        while intro == False:
                                            conj1 = preguntar(letras, tipodeletra, "ATENCION ESTA A PUNTO DE BORRAR SU USARIO, ESTA SEGURO DE QUE QUIERE HACERLO si o no", 0, ventana, round(0.01953125 * ancho), 43, (alto, ancho))
                                            letras = conj1[1]
                                            intro = conj1[0]

                                        if letras == "/Exit":
                                            terminal = False
                                            terminargen = True

                                        else:
                                            if letras == "si":
                                                letras = str("")
                                                intro = False
                                                cuenta_act = obtenerdato("Datos", "cuentas", user_comp[1], 1)
                                                contraseñacifrada_act = cuenta_act[3]
                                                terminado = False

                                                while terminado == False:

                                                    while intro == False:
                                                        conj1 = preguntar(letras, tipodeletra, "Indique su contraseña", 1.5, ventana, round(0.078125 * ancho), 16, (alto, ancho), 5, True)
                                                        letras = conj1[1]
                                                        intro = conj1[0]

                                                    if letras == "/Exit":
                                                        terminal = False
                                                        terminado = True
                                                        terminargen = True

                                                    else:
                                                        contdes = descifrar_contraseña(contraseñacifrada_act, letras[0])

                                                        if contdes == letras:
                                                            terminado = True
                                                            print("Usuario borrado con exito")

                                                            #print("\nDatos inicio\n")

                                                            #printbasededatos()

                                                            #printbasededatos("all", "Records", "records")

                                                            print("\nborrar datos\n")

                                                            borrardatos("Datos", "cuentas", user_comp[1])

                                                            borrardatos("Records", "records", user_comp[1])

                                                            #printbasededatos()

                                                            #printbasededatos("all", "Records", "records")

                                                            print("\nComprovar indice de datos\n")

                                                            comprovarindice("Datos", "cuentas")

                                                            #printbasededatos()

                                                            #printbasededatos("all", "Records", "records")

                                                            print("\nComprovar indice de Records\n")

                                                            comprovarindice("Records", "records", 2)

                                                            #printbasededatos()

                                                            #printbasededatos("all", "Records", "records")

                                                            print("\nComprovar la igualdad de las dos bases de datos\n")

                                                            comprovarigualdad("Records", "records", 0)

                                                            #printbasededatos()

                                                            #printbasededatos("all", "Records", "records")

                                                            print("\nOrdenar la base de datos datos respecto a la base de datos records\n")

                                                            ordenarDBrespectoaotraDB("Records", "records", 0)

                                                            #printbasededatos()

                                                            #printbasededatos("all", "Records", "records")

                                                            print("")

                                                            borardbniveles(user_comp[1])

                                                            user_comp = [False, "None"]

                                                            data_niveles = []

                                                            ventana.blit(imagen_de_fondo, (0, 0))
                                                            ventana.blit(ImagenInsetCoins, (504, 10))
                                                            ventana.blit(Portada, (Portadax, Portaday))
                                                            ventana.blit(botytxt1[0], (posesxybot1[0], posesxybot1[1]))
                                                            ventana.blit(botytxt2[0], (posesxybot2[0], posesxybot2[1]))
                                                            if txt1 != None: ventana.blit(txt1[0], (posxytxt1[0], posxytxt1[1]))
                                                            ventana.blit(bot7, (posx1ajustes, posy1ajustes))
                                                            pygame.display.update()
                                                            sucedio_accion = False

                                                            terminargen = True

                                                        else:
                                                            print("Esa contraseña no es correcta")
                                                            letraslist = []
                                                            letraslist.extend(letras)
                                                            xtoerrase = calcularx(letraslist, ancho)
                                                            rectangulo = pygame.draw.rect(ventana, negro, (round(0.021875 * ancho), round(0.09975 * ancho), xtoerrase, round(0.15625 * ancho)))
                                                            pygame.display.update()
                                                            letras = str("")
                                                            miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                            miTexto2 = miFuente2.render("Esa contraseña no es correcta", 0, rojo)
                                                            posxtgo = calcularx(letras, ancho)
                                                            ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.09765625 * ancho)))
                                                            pygame.display.update()
                                                            time.sleep(1)
                                                            miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                            miTexto2 = miFuente2.render("Esa contraseña no es correcta", 0, negro)
                                                            ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.09765625 * ancho)))
                                                            pygame.display.update()
                                                            intro = False

                                            elif letras == "no":
                                                configuracion_intro(user_comp, ventana, alto, ancho, tipodeletra, posxytxt1, posx1comenzar, posx2comenzar, posy1comenzar, posy2comenzar, tamañocomenzar, posx1ajus, posx2ajus, posy1ajus, posy2ajus, tamañoajus, posxtxt1, posytxt1, tamañotxt1, posxytxt1)
                                                vuelta = True
                                                terminargen = True
                                                pygame.display.update()
                                                ratonx, ratony = pygame.mouse.get_pos()

                                            elif terminal == True:
                                                print("Ese caracter no esta definido")
                                                letraslist = []
                                                letraslist.extend(letras)
                                                xtoerrase = calcularx(letraslist, ancho)
                                                rectangulo = pygame.draw.rect(ventana, negro, (round(0.021875 * ancho), round(0.03515625 * ancho), xtoerrase, round(0.15625 * ancho)))
                                                pygame.display.update()
                                                letras = str("")
                                                miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                miTexto2 = miFuente2.render("Ese caracter no esta definido", 0, rojo)
                                                posxtgo = calcularx(letras, ancho)
                                                ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.03515625 * ancho)))
                                                pygame.display.update()
                                                time.sleep(1)
                                                miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                miTexto2 = miFuente2.render("Ese caracter no esta definido", 0, negro)
                                                ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.03515625 * ancho)))
                                                pygame.display.update()
                                                intro = False

                                    configuracion_intro(user_comp, ventana, alto, ancho, tipodeletra, posxytxt1, posx1comenzar, posx2comenzar, posy1comenzar, posy2comenzar, tamañocomenzar, posx1ajus, posx2ajus, posy1ajus, posy2ajus, tamañoajus, posxtxt1, posytxt1, tamañotxt1, posxytxt1)
                                    vuelta = True
                                    ventana.blit(imagen_de_fondo, (0, 0))
                                    ventana.blit(ImagenInsetCoins, (504, 10))
                                    ventana.blit(Portada, (Portadax, Portaday))
                                    ventana.blit(botytxt1[0], (posesxybot1[0], posesxybot1[1]))
                                    ventana.blit(botytxt2[0], (posesxybot2[0], posesxybot2[1]))
                                    if txt1 != None: ventana.blit(txt1[0], (posxytxt1[0], posxytxt1[1]))
                                    ventana.blit(bot7, (posx1ajustes, posy1ajustes))
                                    pygame.display.update()
                                    pygame.display.update()
                                    sucedio_accion = False
                                    ratonx, ratony = pygame.mouse.get_pos()

                                elif accion2 == "mostrar datos":
                                    ventana.fill(negro)

                                    terminargen = False

                                    terminal = True

                                    terminado = False

                                    while terminargen == False:
                                        letras = str("")
                                        intro = False

                                        cuenta_act = obtenerdato("Datos", "cuentas", user_comp[1], 1)
                                        contraseñacifrada_act = cuenta_act[3]

                                        while terminado == False:
                                            letras = str("")
                                            intro = False

                                            while intro == False:
                                                conj1 = preguntar(letras, tipodeletra, "Introduzca su contraseña para poder observar los datos de su cuenta", 0, ventana, round(0.01953125 * ancho), 43, (alto, ancho), 0, True)
                                                letras = conj1[1]
                                                intro = conj1[0]

                                            if letras == "/Exit":
                                                terminal = False
                                                terminargen = True
                                                terminado = True

                                            else:
                                                contdes = descifrar_contraseña(contraseñacifrada_act, letras[0])

                                                if contdes == letras:
                                                    terminado = True

                                                else:
                                                    print("Esa contraseña no es correcta")
                                                    letraslist = []
                                                    letraslist.extend(letras)
                                                    xtoerrase = calcularx(letraslist, ancho)
                                                    rectangulo = pygame.draw.rect(ventana, negro, (round(0.021875 * ancho), round(0.03515625 * ancho), xtoerrase, round(0.15625 * ancho)))
                                                    pygame.display.update()
                                                    letras = str("")
                                                    miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                    miTexto2 = miFuente2.render("Esa contraseña no es correcta", 0, rojo)
                                                    posxtgo = calcularx(letras, ancho)
                                                    ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.03515625 * ancho)))
                                                    pygame.display.update()
                                                    time.sleep(1)
                                                    miFuente2 = pygame.font.SysFont(tipodeletra, tamañotxtgeneralconsola)
                                                    miTexto2 = miFuente2.render("Esa contraseña no es correcta", 0, negro)
                                                    ventana.blit(miTexto2, (round(0.021875 * ancho), round(0.03515625 * ancho)))
                                                    pygame.display.update()
                                                    intro = False
                                        
                                        if terminal == True:

                                            print("Datos mostrados con exito")

                                            textoaescribir = obtenerdato("Datos", "cuentas", user_comp[1])

                                            texto_de_antes = ["Estas loggeado en el usuario nº: ", "Tu nombre de usuario es: ", "Tu correo electronio es: ", "Tu contraseña es: ", "Tu fecha de nacimiento es: ", "Esta cuenta se creo el: "]
                                            posicion = 1.5
                                            volver = False
                                            numero_de_resultado = 0

                                            for parte in textoaescribir:
                                                if numero_de_resultado == 3:
                                                    parte = contdes

                                                if numero_de_resultado == 0:
                                                     escribir_en_terminal(str(texto_de_antes[numero_de_resultado]) + str(parte) + " de este ordenador", tipodeletra, posicion, ventana, ancho, alto)

                                                else:
                                                    escribir_en_terminal(str(texto_de_antes[numero_de_resultado]) + str(parte), tipodeletra, posicion, ventana, ancho, alto)
                                                
                                                posicion = posicion + 1
                                                numero_de_resultado = numero_de_resultado + 1

                                            escribir_en_terminal("Para volver a la pantalla anterior pulse intro", tipodeletra, posicion, ventana, ancho, alto)

                                            while volver == False:

                                                for evento in pygame.event.get():

                                                    if evento.type == QUIT:
                                                        print("Juego terminado")
                                                        pygame.quit()
                                                        raise KeyError

                                                    if evento.type == KEYDOWN:

                                                        if evento.key == 285:
                                                            print("Juego terminado")
                                                            pygame.quit()
                                                            raise KeyError
                                                        elif evento.key == 13:
                                                            volver = True
                                                            terminargen = True

                                    configuracion_intro(user_comp, ventana, alto, ancho, tipodeletra, posxytxt1, posx1comenzar, posx2comenzar, posy1comenzar, posy2comenzar, tamañocomenzar, posx1ajus, posx2ajus, posy1ajus, posy2ajus, tamañoajus, posxtxt1, posytxt1, tamañotxt1, posxytxt1)
                                    vuelta = True
                                    pygame.display.update()

                                    sucedio_accion = False

                                    ratonx, ratony = pygame.mouse.get_pos()

                                elif accion2 == "salir del usuario":

                                    user_comp = [False, "None"]

                                    data_niveles = []

                                    vuelta = True

                                    print("Salida de usuario ejecutada con exito")

                                    ventana.blit(imagen_de_fondo, (0, 0))
                                    ventana.blit(ImagenInsetCoins, (504, 10))
                                    ventana.blit(Portada, (Portadax, Portaday))
                                    ventana.blit(botytxt1[0], (posesxybot1[0], posesxybot1[1]))
                                    ventana.blit(botytxt2[0], (posesxybot2[0], posesxybot2[1]))
                                    if txt1 != None: ventana.blit(txt1[0], (posxytxt1[0], posxytxt1[1]))
                                    ventana.blit(bot7, (posx1ajustes, posy1ajustes))
                                    pygame.display.update()

                                    sucedio_accion = False

                                accion2 = ""

                        ventana.blit(imagen_de_fondo, (0, 0))
                        ventana.blit(ImagenInsetCoins, (504, 10))
                        ventana.blit(Portada, (Portadax, Portaday))
                        ventana.blit(botytxt1[0], (posesxybot1[0], posesxybot1[1]))
                        ventana.blit(botytxt2[0], (posesxybot2[0], posesxybot2[1]))
                        if txt1 != None: ventana.blit(txt1[0], (posxytxt1[0], posxytxt1[1]))
                        ventana.blit(bot7, (posx1ajustes, posy1ajustes))
                        pygame.display.update()

            accion = ""