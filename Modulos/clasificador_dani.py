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

disparos = [DisparoBlanco, DisparoRojo, DisparoAzul, DisparoAmarillo]
velocidadesdisparos = [0.4, 0.08, 0.1, 0.2]

posicionesx = [20, 20, 20] #Una por nave

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
		self.ImagenNave = pygame.transform.scale(ImagenNave_alpha, (round(0.03125 * ancho), round(0.03055555555555555555555555555556 * alto)))

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
            #self.audio.play(self.loop)
            pass

    #stops the audio
    def stop(self):
        #self.audio.stop()
        pass

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
        #pygame.mixer.music.set_volume(int(volume)/10.0)
        self.loop = loop              #how many times it will loop (default = forever)
  
        #checks if the file exists and if it does then it should play it
        
        '''print(os.path.join(audiopath))
        if os.path.exists(os.path.join(audiopath)):
            if queue == True:
                pygame.mixer.music.queue(audiopath)
            else:
                pygame.mixer.music.fadeout(100)
                print(audiopath)
                pygame.mixer.music.load(audiopath)
                #pygame.mixer.music.play(self.loop)
        else:
            return None'''
  
    #changes how many times the song will loop
    def setLoop(loop = -1):
        self.loop = loop
  
    #plays the music
    def play(self, pos = 0.0):
        if enabled:
            #pygame.mixer.music.play(self.loop, pos)
            pass
  
    #stops the music
    def stop(self):
        #pygame.mixer.music.stop()
        pass

    def unpause(self):
        #pygame.mixer.music.unpause()

        #pygame.mixer.music.set_volume(self.volume)
        pass

    def pause(self):
        #pygame.mixer.music.pause()
        pass
  
    #fades the music out and stops it
    #   @time       time, in milliseconds, it takes to fade the music out
    def fadeToStop(self, time = 100):
        #pygame.mixer.music.fadeout(time)
        pass

    #   @volume     volume of the music, value between 0 - 10
    def setVolume(self, volume):
        self.volume = (int(volume)/10.0)
        #pygame.mixer.music.set_volume(int(volume)/10.0)

    def getVolume(self):
        #volume = pygame.mixer.music.get_volume()
        volume = 1
        #self.volume = volume
        return volume

    def getpos(self):
        return pygame.mixer.music.get_pos()

    def setpos(self, pos):
        pygame.mixer.music.rewind()
        pygame.mixer.music.set_pos(pos)

class EBE(ECM): #EBE = Elemento del bando enemigo, hereda del elemento con movilidad
	def calculardisparo(self, nivel):

		numero = random.randrange(0, 4000)

		if numero == 1: #Disparo 
			devolver = [self.posx + posicionesx[self.tipo], self.posy + self.tamañoy, disparos[math.floor(nivel/5)], velocidadesdisparos[0], 1]
			return "True", devolver

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

class EBN(ECM): #EBN = elemento del bando neutral


	def animacionEBN(self, animacion, tiemposec = 2):
		pass

"""

### A PARTIR DE AQUI SE DEFINEN LOS EBEN ###

"""

class EBEN1(EBE): #EBEN1 = elemento del bando enemigo tipo: nave 1
	def __init__(self, posx, posy, nº):
		print("Nave EBEN1 creada con exito")
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

class EBEN2(EBE): #EBEN2 = elemento del bando enimigo tipo: nave 2
	def __init__(self, posx, posy):
		print("Nave EBEN2 creada con exito")
		self.vida = 0
		self.dañocc = 0 #Daño cuerpo a cuerpo (Se choca con una nave amiga)
		self.velocidad = 0
		self.escudo = 0 #False/True
		self.posx = posx
		self.posy = posy

class EBEN3(EBE): #EBEN3 = elemento del bando enemigo tipo: nave 3
	def __init__(self, posx, posy):
		print("Nave EBEN3 creada con exito")
		self.vida = 0
		self.dañocc = 0 #Daño cuerpo a cuerpo (Se choca con una nave amiga)
		self.velocidad = 0
		self.escudo = 0 #False/True
		self.posx = posx
		self.posy = posy

class EBEN4(EBE): #EBEN4 = elemento del bando enemigo tipo: nave 4
	def __init__(self, posx, posy):
		print("Nave EBEN4 creada con exito")
		self.vida = 0
		self.dañocc = 0 #Daño cuerpo a cuerpo (Se choca con una nave amiga)
		self.velocidad = 0
		self.escudo = 0 #False/True
		self.posx = posx
		self.posy = posy

class EBEN5(EBE): #EBEN5 = elemento del bando enemigo tipo: nave 5
	def __init__(self, posx, posy):
		print("Nave EBEN5 creada con exito")
		self.vida = 0
		self.dañocc = 0 #Daño cuerpo a cuerpo (Se choca con una nave amiga)
		self.velocidad = 0
		self.escudo = 0 #False/True
		self.posx = posx
		self.posy = posy

class EBEN6(EBE): #EBEN6 = elemento del bando enemigo tipo: nave 6
	def __init__(self, posx, posy):
		print("Nave EBEN6 creada con exito")
		self.vida = 0
		self.dañocc = 0 #Daño cuerpo a cuerpo (Se choca con una nave amiga)
		self.velocidad = 0
		self.escudo = 0 #False/True
		self.posx = posx
		self.posy = posy

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

class EBEM1(EBE): #EBEM1 = elemento del bando enemigo tipo: boss 1
	def __init__(self, posx = "arriba", posy = "centro"):
		print("Boss EBEM1 creado con exito")
		self.vida = 0
		self.dañocc = 0 #Daño cuerpo a cuerpo (Se choca con una nave amiga)
		self.escudo = 0 #False/True
		self.posx = posx
		self.posy = posy

class EBEM2(EBE): #EBEM2 = elemento del bando enemigo tipo: boss 2
	def __init__(self, posx = "arriba", posy = "centro"):
		print("Boss EBEM2 creado con exito")
		self.vida = 0
		self.dañocc = 0 #Daño cuerpo a cuerpo (Se choca con una nave amiga)
		self.escudo = 0 #False/True
		self.posx = posx
		self.posy = posy

class EBEM3(EBE): #EBEM3 = elemento del bando enemigo tipo: boss 3
	def __init__(self, posx = "arriba", posy = "centro"):
		print("Boss EBEM3 creado con exito")
		self.vida = 0
		self.dañocc = 0 #Daño cuerpo a cuerpo (Se choca con una nave amiga)
		self.escudo = 0 #False/True
		self.posx = posx
		self.posy = posy

class EBEM4(EBE): #EBEM4 = elemento del bando enemigo tipo: boss 4
	def __init__(self, posx = "arriba", posy = "centro"):
		print("Boss EBEM4 creado con exito")
		self.vida = 0
		self.dañocc = 0 #Daño cuerpo a cuerpo (Se choca con una nave amiga)
		self.escudo = 0 #False/True
		self.posx = posx
		self.posy = posy

class EBEM5(EBE): #EBEM5 = elemento del bando enemigo tipo: boss 5
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