#!/usr/bin/python3

from Modulos.cifrador import *

import pygame

from pygame.locals import *

import pygame.image

import sys

import os

import random

import math

from time import sleep

from Modulos.basededatosajustesfaciliter import *

#import trosnoth.data.music as music
#from trosnoth.data import getPath

pygame.init()

ajustes = extraer_ajustes()

ancho = int(ajustes[0])
alto = int(ajustes[1])

DisparoBlanco_alpha = pygame.image.load("Imagenes/Disparos/Disparo_2.png")
DisparoBlanco = pygame.transform.scale(DisparoBlanco_alpha, (2, 8)) # 1 X 4
DisparoRojo_alpha = pygame.image.load("Imagenes/Disparos/Disparo_3.png")
DisparoRojo = pygame.transform.scale(DisparoRojo_alpha, (2, 8)) # 1 X 4
DisparoAzul_alpha = pygame.image.load("Imagenes/Disparos/Disparo_4.png")
DisparoAzul = pygame.transform.scale(DisparoAzul_alpha, (2, 8)) # 1 X 4
DisparoAmarillo_alpha = pygame.image.load("Imagenes/Disparos/Disparo_5.png")
DisparoAmarillo = pygame.transform.scale(DisparoAmarillo_alpha, (2, 8)) # 1 X 4
DisparoVerde_alpha = pygame.image.load("Imagenes/Disparos/Disparo_6.png")
DisparoVerde = pygame.transform.scale(DisparoVerde_alpha, (2, 8)) # 1 X 4
DisparoNuclear_alpha = pygame.image.load("Imagenes/Disparos/Disparo_6.png")
DisparoNuclear = pygame.transform.scale(DisparoNuclear_alpha, (6, 6)) # 6 X 6

disparos = [DisparoBlanco, DisparoRojo, DisparoAzul, DisparoAmarillo, DisparoVerde, DisparoNuclear]
velocidadesdisparos = [0.4, 0.5, 0.6, 0.5, 0.8, 0.5]

posicionesx = [20, 20, 20, [8, 26], [8, 17, 26], 23] #Una por nave

naves_tamaños = [(round(0.03125 * ancho), round(0.03055555555555555555555555555556 * alto)), (round(0.03125 * ancho), round(0.03055555555555555555555555555556 * alto)), (round(0.03125 * ancho), round(0.03055555555555555555555555555556 * alto)), (round(0.028125 * ancho), round(0.04166666666666666666666666666667 * alto)), (round(0.028125 * ancho), round(0.04166666666666666666666666666667 * alto)), (round(0.028125 * ancho), round(0.04583333333333333333333333333333 * alto))]

class ECM(pygame.sprite.Sprite): #ECM = elemento con movilidad
	"""Clase para los elementos que se pueden mover por la pantalla"""

	def __init__(self, posinicx, posinicy):
		pygame.sprite.Sprite.__init__(self)
		#self.rect = self.ImagenNave.get_rect()
		self.posx = posinicx
		self.posy = posinicy
		self.velocidad = 20 #Solo esta aqui por parte de la prueva b/s

	def cargarconimag(self, imag, ext):
		ImagenNave_alpha = pygame.image.load("Imagenes/Naves_Enemigas/" + imag + ext)
		self.ImagenNave = pygame.transform.scale(ImagenNave_alpha, naves_tamaños[self.tipo - 1])

	def actualizarpos(self, x, y):
		self.posx = x
		self.posy = y

class ESM(pygame.sprite.Sprite): #ESM = elemento sin movilidad
	
	def __init__(self, name, posinicx = 0, posinicy = 0):

		self.posx = posinicx
		self.posy = posinicy
		self.name = name

	def cargarconimag(self, imag, ext):
		self.ImagenNave = pygame.image.load("Imagenes/" + imag + ext)

	def esconder(self):
		return True #Esto determina si los atributos del objeto deben ejecutarse todos menos mostrar

	def mostrar(self, pantalla):
		if self.ImagenNave != None:

			pantalla.blit(self.ImagenNave, (self.posx, self.posy))
			return False #Esto determina si los atributos del objeto deben ejecutarse todos menos mostrar

		else:
			return True #Esto determina si los atributos del objeto deben ejecutarse todos menos mostrar

	def destruir(self, x, y, sonido, animacion = None):
		pass

enabled = True

class SoundObj:
    def __init__(self, AudioFile, fullpath = False, loop = 0):

        if fullpath:
            filePath = os.path.join(AudioFile + ".wav")
        else:
            filePath = os.path.join("Sonido/", AudioFile + ".wav")

        #sound object must be wav or it will not work!
        print(filePath)
        #if os.path.splitext(filePath)[1].lower() != ".wav":
         #  return

        #new sound object
        self.audio = pygame.mixer.Sound(filePath)
        self.volume = 10                        #volume of the object
        self.loop = loop                        #how many times it will loop (default = once)
        #self.play()                            #by default it will start playing as soon as it is initialized

    #changes the volume of the audio
    def setVol(self, volume):
        self.volume = volume
        self.audio.set_volume(self.volume/100.0)

    #changes how many times the song will loop 
    def setLoop(self, loop):
        self.loop = loop

    #plays the audio
    def play(self):
        if enabled:
            self.audio.play(self.loop)

    #stops the audio
    def stop(self):
        self.audio.stop()

#an object for background music
class BGMObj:
    def __init__(self, AudioFile, queue = False, volume = 100, loop = 0, fullpath = False):
  
        #the music file
  
        #fullpath assumes that the file is not located in the audio>music folder 
        #and is instead elsewhere in the data subdirectory
        if fullpath:                
            audiopath = AudioFile + ".mp3"
        else:
            audiopath = os.path.join("Sonido/", AudioFile + ".mp3")
  
        self.volume = volume            #volume of the song (0-10 scale)
        pygame.mixer.music.set_volume(int(volume)/10.0)
        self.loop = loop              #how many times it will loop (default = forever)
  
        #checks if the file exists and if it does then it should play it
        
        print(os.path.join(audiopath))
        if os.path.exists(os.path.join(audiopath)):
            if queue == True:
                pygame.mixer.music.queue(audiopath)
            else:
                pygame.mixer.music.fadeout(100)
                print(audiopath)
                pygame.mixer.music.load(audiopath)
                #pygame.mixer.music.play(self.loop)
        else:
            return None
  
    #changes how many times the song will loop
    def setLoop(loop = -1):
        self.loop = loop
  
    #plays the music
    def play(self, pos = 0.0):
        if enabled:
            pygame.mixer.music.play(self.loop, pos)
  
    #stops the music
    def stop(self):
        pygame.mixer.music.stop()

    def unpause(self):
        pygame.mixer.music.unpause()

        pygame.mixer.music.set_volume(self.volume)

    def pause(self):
        pygame.mixer.music.pause()
  
    #fades the music out and stops it
    #   @time       time, in milliseconds, it takes to fade the music out
    def fadeToStop(self, time = 100):
        pygame.mixer.music.fadeout(time)

    #   @volume     volume of the music, value between 0 - 10
    def setVolume(self, volume):
        self.volume = (int(volume)/10.0)
        pygame.mixer.music.set_volume(int(volume)/10.0)

    def getVolume(self):
        volume = pygame.mixer.music.get_volume()
        self.volume = volume
        return volume

    def getpos(self):
        return pygame.mixer.music.get_pos()

    def setpos(self, pos):
        pygame.mixer.music.rewind()
        pygame.mixer.music.set_pos(pos)

class EBE(ECM): #EBE = Elemento del bando enemigo, hereda del elemento con movilidad
	def calculardisparo(self, nivel, FPS):

		try:

			numero = random.randrange(0, round(self.probabilidad_disparo/300) * FPS +1)

		except:
			numero = 0

		if numero == 1: #Disparo

			if self.tipo == 5:
				devolver1 = [self.posx + (posicionesx[self.tipo - 1])[0], self.posy + self.tamañoy, disparos[self.nave - 1], velocidadesdisparos[self.nave - 1], self.nave] #[posx, posy, tipo, velocidad, tipodisparo]
				devolver2 = [self.posx + (posicionesx[self.tipo - 1])[1], self.posy + self.tamañoy + 2, disparos[self.nave - 1], velocidadesdisparos[self.nave - 1], self.nave] #[posx, posy, tipo, velocidad, tipodisparo]
				devolver3 = [self.posx + (posicionesx[self.tipo - 1])[2], self.posy + self.tamañoy + 1, disparos[self.nave - 1], velocidadesdisparos[self.nave - 1], self.nave] #[posx, posy, tipo, velocidad, tipodisparo]
				return "True", [devolver1, devolver2, devolver3], 3

			elif self.tipo == 4: #Para disparar dos disparos a la vez
				devolver1 = [self.posx + (posicionesx[self.tipo - 1])[0], self.posy + self.tamañoy, disparos[self.nave - 1], velocidadesdisparos[self.nave - 1], self.nave] #[posx, posy, tipo, velocidad, tipodisparo]
				devolver2 = [self.posx + (posicionesx[self.tipo - 1])[1], self.posy + self.tamañoy + 1, disparos[self.nave - 1], velocidadesdisparos[self.nave - 1], self.nave] #[posx, posy, tipo, velocidad, tipodisparo]
				return "True", [devolver1, devolver2], 2
			else:
				devolver = [self.posx + posicionesx[self.tipo - 1], self.posy + self.tamañoy, disparos[self.nave - 1], velocidadesdisparos[self.nave - 1], self.nave] #[posx, posy, tipo, velocidad, tipodisparo]
				return "True", devolver, 1

		elif numero == 2: #Disparo
			return "False"

		elif numero == 3: #Disparo
			return "False"

		else:
			return "False"

	def recibirdañoEBA(self, cuanto):
		self.vida -= cuanto

		if self.vida < 1:

			if self.escudo == True:

				self.escudo = False
				self.vida = self.vida_comp

			else:
				self.viva = False

	def Muerteprimera(self):
		self.muerteprimera = False

	def caidaset(self, setto):
		self.caida = setto

	def esperandoset(self, setto):
		self.esperando = setto

	def primeracosset(self):
		if self.primeracos == True:
			self.primeracos = False

		else:
			self.primeracos = True

	def xavanzadoset(self, setto):
		self.xavanzado = setto

	def iniciocosxset(self, setto):
		self.inicosenx = setto

	def posxytogoset(self, x, y):
		self.posxtogo = x
		self.posytogo = y

	def radioinicset(self, leng):
		self.radioinic = leng

	def posxmaximoset(self, posx):
		self.posxmaximo = posx

	def salidabossset(self, setto):
		self.salidaboss = setto

	def centroset(self, x, y):
		self.centrox = x
		self.centroy = y

	def pasadoset(self, setto):
		self.pasado = setto

	def idavueltaset(self, setto):
		self.idavuelta = setto

	def estadonaveset(self, setto):
		self.estadonave = setto

class EBEB(ECM): #EBEB = elemento del bando enemigo tipo boss
	pass

class EBN(ECM): #EBN = elemento del bando neutral


	def animacionEBN(self, animacion, tiemposec = 2):
		pass

"""

### A PARTIR DE AQUI SE DEFINEN LOS EBEN ###

"""

class EBEN1(EBE): #EBEN1 = elemento del bando enemigo tipo: nave 1
	def __init__(self, posx, posy, nº, radio, lado, permanecer):
		#print("Nave EBEN1 creada con exito")
		self.nave = 1 #Para saber que tipo de nave es
		self.vida = 5 #El número de puntos de vida con los que empieza
		self.viva = True #Para que el juego sepa si esta viva o no
		self.vida_comp = self.vida #La vida con la que empieza
		self.velocidad = 0.1 #Px por vuelta
		self.escudo = False #Para saber si tiene escudo
		self.posx = posx #Posicion x actual
		self.posy = posy #Posicion y actual
		self.posxinic = posx #Para saber en que posicion empezo a moverse
		self.muerteprimera = True #Parara correjir un error de programacion dejar en true
		self.pos = nº #El numero de la nave en el orden
		self.tipo = 1 #Tipo de nave
		self.caida = False #Tipo de bajada
		self.esperando = False #Para cuando la nave esta arriba hasta que haya 4 o que se mueran todas
		self.tamañox = 40
		self.tamañoy = 22
		self.primeracos = True
		self.xavanzado = radio * -1
		self.inicosenx = 0
		self.salidaboss = False
		self.posxtogo = None
		self.posytogo = None
		self.radioinic = None
		self.posxmaximo = None
		self.centrox = None
		self.centroy = None
		self.pasado = None
		self.ladoboss = lado
		self.idavuelta = 0 #ida == 0 and vuelta == 1
		self.probabilidad_disparo = 4000
		self.estadonave = True #Indica si puede ser dañada
		self.permanecer = permanecer

class EBEN2(EBE): #EBEN2 = elemento del bando enimigo tipo: nave 2
	def __init__(self, posx, posy, nº, radio, lado, permanecer):
		#print("Nave EBEN2 creada con exito")
		self.nave = 2 #Para saber que tipo de nave es
		self.vida = 10 #El número de puntos de vida con los que empieza
		self.viva = True #Para que el juego sepa si esta viva o no
		self.vida_comp = self.vida #La vida con la que empieza
		self.velocidad = 0.1 #Px por vuelta
		self.escudo = False #Para saber si tiene escudo
		self.posx = posx #Posicion x actual
		self.posy = posy #Posicion y actual
		self.posxinic = posx #Para saber en que posicion empezo a moverse
		self.muerteprimera = True #Parara correjir un error de programacion dejar en true
		self.pos = nº #El numero de la nave en el orden
		self.tipo = 2 #Tipo de nave
		self.caida = False #Tipo de bajada
		self.esperando = False #Para cuando la nave esta arriba hasta que haya 4 o que se mueran todas
		self.tamañox = 40
		self.tamañoy = 22
		self.primeracos = True
		self.xavanzado = radio * -1
		self.inicosenx = 0
		self.salidaboss = False
		self.posxtogo = None
		self.posytogo = None
		self.radioinic = None
		self.posxmaximo = None
		self.centrox = None
		self.centroy = None
		self.pasado = None
		self.ladoboss = lado
		self.idavuelta = 0 #ida == 0 and vuelta == 1
		self.probabilidad_disparo = 4000
		self.estadonave = True #Indica si puede ser dañada
		self.permanecer = permanecer

class EBEN3(EBE): #EBEN3 = elemento del bando enemigo tipo: nave 3
	def __init__(self, posx, posy, nº, radio, lado, permanecer):
		#print("Nave EBEN3 creada con exito")
		self.nave = 3 #Para saber que tipo de nave es
		self.vida = 20 #El número de puntos de vida con los que empieza
		self.viva = True #Para que el juego sepa si esta viva o no
		self.vida_comp = self.vida #La vida con la que empieza
		self.velocidad = 0.1 #Px por vuelta
		self.escudo = False #Para saber si tiene escudo
		self.posx = posx #Posicion x actual
		self.posy = posy #Posicion y actual
		self.posxinic = posx #Para saber en que posicion empezo a moverse
		self.muerteprimera = True #Parara correjir un error de programacion dejar en true
		self.pos = nº #El numero de la nave en el orden
		self.tipo = 3 #Tipo de nave
		self.caida = False #Tipo de bajada
		self.esperando = False #Para cuando la nave esta arriba hasta que haya 4 o que se mueran todas
		self.tamañox = 40
		self.tamañoy = 22
		self.primeracos = True
		self.xavanzado = radio * -1
		self.inicosenx = 0
		self.salidaboss = False
		self.posxtogo = None
		self.posytogo = None
		self.radioinic = None
		self.posxmaximo = None
		self.centrox = None
		self.centroy = None
		self.pasado = None
		self.ladoboss = lado
		self.idavuelta = 0 #ida == 0 and vuelta == 1
		self.probabilidad_disparo = 4000
		self.estadonave = True #Indica si puede ser dañada
		self.permanecer = permanecer

class EBEN4(EBE): #EBEN4 = elemento del bando enemigo tipo: nave 4
	def __init__(self, posx, posy, nº, radio, lado, permanecer):
		#print("Nave EBEN4 creada con exito")
		self.nave = 4 #Para saber que tipo de nave es
		self.vida = 10 #El número de puntos de vida con los que empieza
		self.viva = True #Para que el juego sepa si esta viva o no
		self.vida_comp = self.vida #La vida con la que empieza
		self.velocidad = 0.15 #Px por vuelta
		self.escudo = False #Para saber si tiene escudo
		self.posx = posx #Posicion x actual
		self.posy = posy #Posicion y actual
		self.posxinic = posx #Para saber en que posicion empezo a moverse
		self.muerteprimera = True #Parara correjir un error de programacion dejar en true
		self.pos = nº #El numero de la nave en el orden
		self.tipo = 4 #Tipo de nave
		self.caida = False #Tipo de bajada
		self.esperando = False #Para cuando la nave esta arriba hasta que haya 4 o que se mueran todas
		self.tamañox = 36
		self.tamañoy = 30
		self.primeracos = True
		self.xavanzado = radio * -1
		self.inicosenx = 0
		self.salidaboss = False
		self.posxtogo = None
		self.posytogo = None
		self.radioinic = None
		self.posxmaximo = None
		self.centrox = None
		self.centroy = None
		self.pasado = None
		self.ladoboss = lado
		self.idavuelta = 0 #ida == 0 and vuelta == 1
		self.probabilidad_disparo = 1000
		self.estadonave = True #Indica si puede ser dañada
		self.permanecer = permanecer

class EBEN5(EBE): #EBEN5 = elemento del bando enemigo tipo: nave 5
	def __init__(self, posx, posy, nº, radio, lado, permanecer):
		#print("Nave EBEN5 creada con exito")
		self.nave = 5 #Para saber que tipo de nave es
		self.vida = 20 #El número de puntos de vida con los que empieza
		self.viva = True #Para que el juego sepa si esta viva o no
		self.vida_comp = self.vida #La vida con la que empieza
		self.velocidad = 0.15 #Px por vuelta
		self.escudo = False #Para saber si tiene escudo
		self.posx = posx #Posicion x actual
		self.posy = posy #Posicion y actual
		self.posxinic = posx #Para saber en que posicion empezo a moverse
		self.muerteprimera = True #Parara correjir un error de programacion dejar en true
		self.pos = nº #El numero de la nave en el orden
		self.tipo = 5 #Tipo de nave
		self.caida = False #Tipo de bajada
		self.esperando = False #Para cuando la nave esta arriba hasta que haya 4 o que se mueran todas
		self.tamañox = 36
		self.tamañoy = 30
		self.primeracos = True
		self.xavanzado = radio * -1
		self.inicosenx = 0
		self.salidaboss = False
		self.posxtogo = None
		self.posytogo = None
		self.radioinic = None
		self.posxmaximo = None
		self.centrox = None
		self.centroy = None
		self.pasado = None
		self.ladoboss = lado
		self.idavuelta = 0 #ida == 0 and vuelta == 1
		self.probabilidad_disparo = 2000
		self.estadonave = True #Indica si puede ser dañada
		self.permanecer = permanecer

class EBEN6(EBE): #EBEN6 = elemento del bando enemigo tipo: nave 6
	def __init__(self, posx, posy, nº, radio, lado, permanecer):
		#print("Nave EBEN6 creada con exito")
		self.nave = 6 #Para saber que tipo de nave es
		self.vida = 30 #El número de puntos de vida con los que empieza
		self.viva = True #Para que el juego sepa si esta viva o no
		self.vida_comp = self.vida #La vida con la que empieza
		self.velocidad = 0.1 #Px por vuelta
		self.escudo = False #Para saber si tiene escudo
		self.posx = posx #Posicion x actual
		self.posy = posy #Posicion y actual
		self.posxinic = posx #Para saber en que posicion empezo a moverse
		self.muerteprimera = True #Parara correjir un error de programacion dejar en true
		self.pos = nº #El numero de la nave en el orden
		self.tipo = 6 #Tipo de nave
		self.caida = False #Tipo de bajada
		self.esperando = False #Para cuando la nave esta arriba hasta que haya 4 o que se mueran todas
		self.tamañox = 36
		self.tamañoy = 33
		self.primeracos = True
		self.xavanzado = radio * -1
		self.inicosenx = 0
		self.salidaboss = False
		self.posxtogo = None
		self.posytogo = None
		self.radioinic = None
		self.posxmaximo = None
		self.centrox = None
		self.centroy = None
		self.pasado = None
		self.ladoboss = lado
		self.idavuelta = 0 #ida == 0 and vuelta == 1
		self.probabilidad_disparo = 300
		self.estadonave = True #Indica si puede ser dañada
		self.permanecer = permanecer

class EBEN7(EBE): #EBEN7 = elemento del bando enemigo tipo: nave 7
	def __init__(self, posx, posy):
		print("Nave EBEN7 creada con exito")
		self.vida = 0
		self.dañocc = 0 #Daño cuerpo a cuerpo (Se choca con una nave amiga)
		self.velocidad = 0
		self.escudo = 0 #False/True
		self.posx = posx
		self.posy = posy

class EBEN8(EBE): #EBEN8 = elemento del bando enemigo tipo: nave 8
	def __init__(self, posx, posy):
		print("Nave EBEN8 creada con exito")
		self.vida = 0
		self.dañocc = 0 #Daño cuerpo a cuerpo (Se choca con una nave amiga)
		self.velocidad = 0
		self.escudo = 0 #False/True
		self.posx = posx
		self.posy = posy

class EBEN9(EBE): #EBEN9 = elemento del bando enemigo tipo: nave 9
	def __init__(self, posx, posy):
		print("Nave EBEN9 creada con exito")
		self.vida = 0
		self.dañocc = 0 #Daño cuerpo a cuerpo (Se choca con una nave amiga)
		self.velocidad = 0
		self.escudo = 0 #False/True
		self.posx = posx
		self.posy = posy

class EBEN10(EBE): #EBEN10 = elemento del bando enemigo tipo: nave 10
	def __init__(self, posx, posy):
		print("Nave EBEN10 creada con exito")
		self.vida = 0
		self.dañocc = 0 #Daño cuerpo a cuerpo (Se choca con una nave amiga)
		self.velocidad = 0
		self.escudo = 0 #False/True
		self.posx = posx
		self.posy = posy

"""

### A PARTIR DE AQUI SE DEFINEN LOS EBEM ###

"""

class EBEM1(EBEB): #EBEM1 = elemento del bando enemigo tipo: boss 1
	def __init__(self, posx = "arriba", posy = "centro"):
		print("Boss EBEM1 creado con exito")
		self.vida = 0
		self.dañocc = 0 #Daño cuerpo a cuerpo (Se choca con una nave amiga)
		self.escudo = 0 #False/True
		self.posx = posx
		self.posy = posy

	def soltarnaves(self):
		pass

	def disparar_en_circulo(self):
		pass

	def disparar_player(self, xplayer, yplayer):
		pass

class EBEM2(EBEB): #EBEM2 = elemento del bando enemigo tipo: boss 2
	def __init__(self, posx = "arriba", posy = "centro"):
		print("Boss EBEM2 creado con exito")
		self.vida = 0
		self.dañocc = 0 #Daño cuerpo a cuerpo (Se choca con una nave amiga)
		self.escudo = 0 #False/True
		self.posx = posx
		self.posy = posy

class EBEM3(EBEB): #EBEM3 = elemento del bando enemigo tipo: boss 3
	def __init__(self, posx = "arriba", posy = "centro"):
		print("Boss EBEM3 creado con exito")
		self.vida = 0
		self.dañocc = 0 #Daño cuerpo a cuerpo (Se choca con una nave amiga)
		self.escudo = 0 #False/True
		self.posx = posx
		self.posy = posy

class EBEM4(EBEB): #EBEM4 = elemento del bando enemigo tipo: boss 4
	def __init__(self, posx = "arriba", posy = "centro"):
		print("Boss EBEM4 creado con exito")
		self.vida = 0
		self.dañocc = 0 #Daño cuerpo a cuerpo (Se choca con una nave amiga)
		self.escudo = 0 #False/True
		self.posx = posx
		self.posy = posy

class EBEM5(EBEB): #EBEM5 = elemento del bando enemigo tipo: boss 5
	def __init__(self, posx = "arriba", posy = "centro"):
		print("Boss EBEM5 creado con exito")
		self.vida = 0
		self.dañocc = 0 #Daño cuerpo a cuerpo (Se choca con una nave amiga)
		self.escudo = 0 #False/True
		self.posx = posx
		self.posy = posy

"""

#### A PARTIR DE AQUI SE DEFINEN LOS EBNO ####

"""

class EBNO1(EBN): #EBNO1 = elemento del bando neutral tipo: objeto 1
	def __init__(self, posx, posy, *args, **kwargs):
		self.posx = posx
		self.posy = posy
		EBNO1.producirsonidoEBN(self)

class EBNO2(EBN): #EBNO2 = elemento del bando neutral tipo: objeto 2
	def __init__(self, posx, posy, *args, **kwargs):
		self.posx = posx
		self.posy = posy
		EBNO2.producirsonidoEBN(self)

class EBNO3(EBN): #EBNO3 = elemento del bando neutral tipo: objeto 3
	def __init__(self, posx, posy, *args, **kwargs):
		self.posx = posx
		self.posy = posy
		EBNO3.producirsonidoEBN(self)

class EBNO4(EBN): #EBNO4 = elemento del bando neutral tipo: objeto 4
	def __init__(self, posx, posy, *args, **kwargs):
		self.posx = posx
		self.posy = posy
		EBNO4.producirsonidoEBN(self)

class EBNO5(EBN): #EBNO5 = elemento del bando neutral tipo: objeto 5
	def __init__(self, posx, posy, *args, **kwargs):
		self.posx = posx
		self.posy = posy
		EBNO5.producirsonidoEBN(self)

class EBNO6(EBN): #EBNO6 = elemento del bando neutral tipo: objeto 6
	def __init__(self, posx, posy, *args, **kwargs):
		self.posx = posx
		self.posy = posy
		EBNO6.producirsonidoEBN(self)

"""

#### A PARTIR DE AQUI SE DEFINEN LOS EBNN ####

"""

class EBNN1(EBN): #EBNN1 = elemento del bando neutral tipo: nave 1 #Nave de aprovisionamiento
	def __init__(self, posx, posy):
		print("Nave EBNN1 creada con exito")
		self.vida = 0
		self.velocidad = 0
		self.posx = posx
		self.posy = posy

class EBNN2(EBN): #EBNN2 = elemento del bando neutral tipo: nave 2 #Nave de carga de combustible
	def __init__(self, posx, posy):
		print("Nave EBNN2 creada con exito")
		self.vida = 0
		self.velocidad = 0
		self.posx = posx
		self.posy = posy