import pygame

from pygame.locals import *

from Modulos.objetos_de_pantalla import *

from Modulos.sqlite3igualador import *

from Modulos.basededatosajustesfaciliter import *

import time

pygame.init()

existe = comprovarexistencia()

if existe == False:

    datosiniciales = [("ancho", 1280), ("alto", 720), ("pantcomp", "False"), ("fuentegen", "Calibri"), ("Volgen", 10), ("Volefect", 100), ("Volmusic", 100), ("Effectyanimations", "True"), ("Scroll", "True"), ("MaxFPS", 501), ("VSync", "True"), ("Usuario", "None")]

    crearbasededatosajustes(datosiniciales)

from Modulos.generador_de_pantallas import *

from Modulos.clasificador import *

ajustes = extraer_ajustes()

ancho = ajustes[0]
alto = ajustes[1]
pantalla_comp = ajustes[2]

font = ajustes[3]

if pantalla_comp == "True":
    try:
        ventana = pygame.display.set_mode((int(ancho), int(alto)), pygame.FULLSCREEN)

    except:
        print("Hubo un error al generar la pantalla y se pusieron estas medidas debug")
        actualizar_dato("ancho", 1280)
        actualizar_dato("alto", 720)
        ventana = pygame.display.set_mode((int(ancho), int(alto)), pygame.FULLSCREEN)

else:
    try:
        ventana = pygame.display.set_mode((int(ancho), int(alto)))

    except:
        print("Hubo un error al generar la pantalla y se pusieron estas medidas debug")
        actualizar_dato("ancho", 1280)
        actualizar_dato("alto", 720)
        ventana = pygame.display.set_mode((int(ancho), int(alto)))

icono_alpha=pygame.image.load("Imagenes/NaveIcono.png")
icono = pygame.transform.scale(icono_alpha, (32, 32))
pygame.display.set_icon(icono)

imagen_de_carga_alpha = pygame.image.load("Imagenes/Loading.gif").convert()
imagen_de_carga = pygame.transform.scale(imagen_de_carga_alpha, (int(int(ancho)/9), int(int(alto)/9)))
ventana.blit(imagen_de_carga, (int(int(ancho)/9 * 4), int(int(alto)/9 * 4)))
pygame.display.update()

pygame.display.set_caption("The Last Traveller")
sql1 = """
CREATE TABLE IF NOT EXISTS cuentas(
ident INTEGER NOT NULL,
usuario VARCHAR(50) NOT NULL,
correo_electronico VARCHAR(50) NOT NULL,
contraseña VARCHAR NOT NULL,
fecha_de_nacimiento VARCHAR(50) NOT NULL,
fecha_de_creacion DATE NOT NULL)"""

crearbasededatos(sql1, "Datos")

sql2 = """
CREATE TABLE IF NOT EXISTS records(
usuario VARCHAR(50) NOT NULL,
record INTEGER NOT NULL,
ident INTEGER NOT NULL)"""

sql3 = """
CREATE TABLE IF NOT EXISTS monedas(
usuario VARCHAR(50) NOT NULL,
monedas INTEGER NOT NULL,
ident INTEGER NOT NULL)"""

crearbasededatos(sql2, "Records", 2, sql3)

comprovarigualdad("Records", "records", 0)

ordenarDBrespectoaotraDB("Records", "records", 0)

ajustes = extraer_ajustes()

user_alpha = ajustes[11]

existe = obtenerdato("Datos", "cuentas", user_alpha)

if existe == False:
    actualizar_dato("Usuario", "None")
    print("Se ha desguardado el usuario")

ajustes = extraer_ajustes()

user = ajustes[11]

if user != "None":
    user_act = [True, user]

else:
    user_act = [False, user]
         
Executepantalla1(ventana, user_act, int(ancho), int(alto))
