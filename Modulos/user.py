#encoding: utf-8
"""

This lines are the lines that you have to put in our programs to call this func:

from usuarios import loggearocrear

result = False

result = loggearocrear() #Hear you have to put the arguments of the load if you want to load withot the questions

"""
import sqlite3

import os

from datetime import *

from Modulos.cifrador import *

loggeado = 1


def loggearocrear(loggeado, usuario = "ejemplo", contraseña = 00000, crearologgear = "crearologgear", fecha_de_nacimiento = "00-00-0000", correo_electronico = "ejemplo@gmail.com", fecha_de_creacion = 0): #La contraseña tien que estar cifrada
    
    if (os.path.isdir(os.getcwd() + "\\" + "sqlite3")):
            
        conexion = sqlite3.connect("sqlite3/Datos.sqlite3")
        
        consulta = conexion.cursor()

    else:

        os.mkdir(os.getcwd() + "\\" + "sqlite3")
        
        conexion = sqlite3.connect("sqlite3/Datos.sqlite3")
        
        consulta = conexion.cursor() 


    def ultimoident(ident = 0):

        encontrado = False

        while encontrado != True:

            sql = "SELECT * FROM cuentas WHERE ident>%d " %(ident)

            consulta.execute(sql)

            act = consulta.fetchone()

            if act != None:
                encontrado = False
                ident = ident + 1

            else:
                encontrado = True

        return ident

    sql = """
CREATE TABLE IF NOT EXISTS cuentas(
ident INTEGER NOT NULL,
usuario VARCHAR(50) NOT NULL,
correo_electronico VARCHAR(50) NOT NULL,
contraseña VARCHAR NOT NULL,
fecha_de_nacimiento VARCHAR(50) NOT NULL,
fecha_de_creacion DATE NOT NULL)"""
    

    if(consulta.execute(sql)):
        pass

    else:
        print("Ha ocurrido un error al crear los archivos necesarios para esta aplicacion")
        loggeado = False

    if loggeado == True:

        print("Ya se encuentra en su usuario")

    else:

        if crearologgear == "c":
            ultimo = ultimoident()

            if fecha_de_creacion != 0:

                datos_1=(ultimo +1, usuario, correo_electronico, contraseña, str(fecha_de_nacimiento), str(fecha_de_creacion))

            else:

                datos_1=(ultimo +1, usuario, correo_electronico, contraseña, str(fecha_de_nacimiento), date.today())

            datos =[0, datos_1]
            sql = "SELECT * FROM cuentas"

            if (consulta.execute(sql)):

                filas = consulta.fetchall()
                cuenta = ""
                loggeado = True
                for fila in filas:

                    if fila[1] == usuario:
                        print("Ese nombre de usuario ya existe")
                        loggeado = False  
                        
                    elif len(usuario) < 0:
                        print("Error")
                        loggeado = False

                sql = """
INSERT INTO cuentas(ident, usuario, correo_electronico, contraseña, fecha_de_nacimiento, fecha_de_creacion)
VALUES (?, ?, ?, ?, ?, ?)"""

                if (consulta.execute(sql, datos_1) and loggeado):  
                    cuenta = usuario
                    conexion.commit()
                    
                else:
                    print("Ha ocurrido un error al guardar la cuenta en el registro")

            else:
                print("Ha ocurrido un error al extraer la cuenta del registro")        

        elif crearologgear == "l":

            sql = "SELECT * FROM cuentas"

            if (consulta.execute(sql)):
                filas = consulta.fetchall()
                cuenta = ""
                                
                for fila in filas:
                                    
                    if fila[1] == usuario:
                        cuenta = fila
                        columna = fila

                if cuenta == "":
                    print("Esa cuenta no existe")
                    loggeado = False
                                    
                else:
                    contraseña_descifrada = descifrar_contraseña(str(contraseña), str(contraseña[0]))
                    datos = [contraseña_descifrada, columna]
                    loggeado = True
                    usuario = cuenta[1] 

            else:
                print("Ha ocurrido un error al extraer la cuenta del registro")

    if contraseña != None:

        if crearologgear == "c":

            return [loggeado, datos[1]]

        else:
            return loggeado

    else:

        return "error"

    consulta.close()

    conexion.commit()


def crear (loggeado):

    if (os.path.isdir(os.getcwd() + "\\" + "sqlite3")):
            
        conexion = sqlite3.connect("sqlite3/Datos.sqlite3")
        
        consulta = conexion.cursor()

    else:

        os.mkdir(os.getcwd() + "\\" + "sqlite3")
        
        conexion = sqlite3.connect("sqlite3/Datos.sqlite3")
        
        consulta = conexion.cursor()  


    def ultimoident(ident = 0):

        encontrado = False

        while encontrado != True:

            sql = "SELECT * FROM cuentas WHERE ident>%d " %(ident)

            consulta.execute(sql)

            act = consulta.fetchone()

            if act != None:
                encontrado = False
                ident = ident + 1

            else:
                encontrado = True

        return ident

    sql = """
CREATE TABLE IF NOT EXISTS cuentas(
ident INTEGER NOT NULL,
usuario VARCHAR(50) NOT NULL,
correo_electronico VARCHAR(50) NOT NULL,
contraseña INTEGER NOT NULL,
fecha_de_nacimiento VARCHAR(50) NOT NULL,
fecha_de_creacion DATE NOT NULL)"""

    creados = False

    if(consulta.execute(sql)):
        creados = True

    else:
        print("Ha ocurrido un error al crear los archivos necesarios para esta aplicacion")
        loggeado = False

    if loggeado:
        print("Ya te encuentras en tu cuenta")
        loggeado = False

    elif creados:

        vale = False
        vale3 = False
        vale5 = False
        vale7 = False

        while vale != True:

            usuario_a_crear = input("Crear nombre de usuario, minimo 1 caracter ej: Administrador :")

            sql = "SELECT * FROM cuentas"

            if (consulta.execute(sql)):
                filas = consulta.fetchall()
                vale2 = True         
                for fila in filas:

                    if fila[1] == usuario_a_crear:
                        q = "igual"
                        vale2 = False
                           
                        
                    elif len(usuario_a_crear) < 1:
                        q = "nada"
                        vale2 = False

                if vale2:
                    vale = True

                    while vale3 != True: 

                        vale4 = True

                        correo_electronico = input("Introduzca su correo electronico(es importante ya que toda informacion de esta aplicacion sera enviada al mismo) ej: Administrador@gmail.com :")

                        if correo_electronico.find("@") == -1:
                            vale4 = False
                            print("Ese correo no existe")

                        elif vale4:
                            vale3 = True

                            while vale5 != True:

                                vale6 = True
                                contraseña = input("Escriba su contrseña(solo se permiten numeros) ej: 123456789 :")
                                                    
                                try:
                                    prueva = int(contraseña) + 12

                                except ValueError:
                                    vale6 = False
                                    print("La contraseña tiene que ser un numero")

                                else:
                                                        
                                    verificacion_de_contraseña = input("Verifique su contraseña:")
                                                        
                                    if contraseña != verificacion_de_contraseña:
                                        vale6 = False
                                        print("Las contraseñas no coinciden")

                                    elif vale6:
                                        vale5 = True

                                        while vale7 != True:
                                            vale8 = True
                                            exit = False

                                            fecha_de_nacimiento = input("Introduzca su fecha de naciminto ej: 00-00-0000 :")
                                                                    
                                            if len(fecha_de_nacimiento) == 10 and fecha_de_nacimiento.count("-") == 2:
                                                sql = """
INSERT INTO cuentas(ident, usuario, correo_electronico, contraseña, fecha_de_nacimiento, fecha_de_creacion)
VALUES (?, ?, ?, ?, ?, ?)"""
                                                ultimo = ultimoident()
                                                contraseña_cifrada = cifrar_contraseña(contraseña)
                                                datos = (ultimo +1, usuario_a_crear, correo_electronico, str(contraseña_cifrada), str(fecha_de_nacimiento), date.today())  

                                                if (consulta.execute(sql, datos)):
                                                    print("Registro guardado con exito")
                                                    loggeado = True
                                                    cuenta = usuario_a_crear
                                                    print("Usted ha iniciado en la cuenta:", cuenta)
                                                    vale7 = True
                                                    conexion.commit()

                                                else:
                                                    print("Ha ocurrido un error al guardar la cuenta en el registro")
                                                    exit = True

                                            else:
                                                print("Error")
                                                vale8 = False

                                            if exit:
                                                loggeado = False
                                                vale7 = True

                else:

                    if q == "nada":
                        print("Escribe algo")
                        loggeado = False

                    else:
                        print("Ese nombre de usuario ya existe")
                        loggeado = False

    return [loggeado, datos]

    consulta.close()

    conexion.commit()

def loggear (loggeado):

    if (os.path.isdir(os.getcwd() + "\\" + "sqlite3")):
            
        conexion = sqlite3.connect("sqlite3/Datos.sqlite3")
        
        consulta = conexion.cursor()

    else:

        os.mkdir(os.getcwd() + "\\" + "sqlite3")
        
        conexion = sqlite3.connect("sqlite3/Datos.sqlite3")
        
        consulta = conexion.cursor()

    sql = """
CREATE TABLE IF NOT EXISTS cuentas(
ident INTEGER NOT NULL,
usuario VARCHAR(50) NOT NULL,
correo_electronico VARCHAR(50) NOT NULL,
contraseña INTEGER NOT NULL,
fecha_de_nacimiento VARCHAR(50) NOT NULL,
fecha_de_creacion DATE NOT NULL)"""

    if(consulta.execute(sql)):
        pass

    else:
        print("Ha ocurrido un error al crear los archivos necesarios para esta aplicacion")
        loggeado = False

    if loggeado:
        print("Ya te encuentras en tu cuenta")
        loggeado = True     

    else:
        comprovado = False

        while comprovado == False:

            usuario = input("Introduzca su nombre de usuario:")

            sql = "SELECT * FROM cuentas"

            if (consulta.execute(sql)):
                filas = consulta.fetchall()
                cuenta = ""
                                
                for fila in filas:
                                    
                    if fila[1] == usuario:
                        cuenta = fila
                        comprovado = True

                if cuenta == "":
                    print("Esa cuenta no existe")
                    loggeado = False
                
                                
                else:
                    def error():

                        def contraseña():

                            loggeado = False

                            while loggeado == False:

                                contraseña = input("Introduzca la contraseña de su usuario:")

                                contraseña_cifrada = cifrar_contraseña(contraseña)

                                print(contraseña_cifrada)

                                print(cuenta[3])

                                if str(cuenta[3]) == str(contraseña_cifrada):
                                    loggeado = True
                                    usuario = cuenta[1]
                                    print("Ya ha entrado a su usuario") 
                                    return (loggeado, cuenta[3])                      

                                else:
                                    print("Esa no es la contraseña de su usuario")
                                

                        base = contraseña()
                        return base

                    base = error()

                    loggeado = base[0]

                    contraseña = base[1]

    if contraseña != None:

        return [loggeado, cuenta]

    else:
        return "error"

    consulta.close()

    conexion.commit()

def cambiar(acambiar, columna, nuevo, pos = 0):
            
    conexion = sqlite3.connect("sqlite3/Datos.sqlite3" )
        
    consulta = conexion.cursor()

    error = False

    def ultimoident(ident = 0):

        encontrado = False

        while encontrado != True:

            sql = "SELECT * FROM cuentas WHERE ident>%d " %(ident)

            consulta.execute(sql)

            act = consulta.fetchone()

            if act != None:
                encontrado = False
                ident = ident + 1

            else:
                encontrado = True

        return ident

    def encontrarindice(elemento, pos, INTEGER):

        sql = "SELECT * FROM cuentas" 
        if INTEGER:

            if (consulta.execute(sql)):
                indx = 1
                filas = consulta.fetchall()
                cuenta = ""  

                for fila in filas:
                                                
                    if fila[pos] == int(elemento):
                        cuenta = fila
                        #indx = indx +1
                        return indx

                    indx = indx +1
            else:
                print("Ha ocurrido un error al abrir el archivo necesario para este programa")
        else:

            if (consulta.execute(sql)):
                indx = 1
                filas = consulta.fetchall()
                cuenta = ""  

                for fila in filas:
                                                
                    if fila[pos] == elemento:
                        cuenta = fila
                        #indx = indx +1
                        return indx

                    indx = indx +1
            else:
                print("Ha ocurrido un error al abrir el archivo necesario para este programa")

    if columna == "usuario":
        
        print("No se puede cambiar el nombre de usuario")
        return "ndu"

    elif columna == "correo":

        print("No se puede cambiar el correo electronico")
        return "ce"

    elif columna == "contraseña":

        if pos != 0:
            pass

        else:
            acambiar_cifrado = cifrar_contraseña(acambiar)
            pos = encontrarindice(acambiar_cifrado, 3, False)
            nuevo_cifrado = cifrar_contraseña(nuevo)

        sql = """
UPDATE cuentas SET contraseña = '%s' WHERE ident = %d """ %(nuevo_cifrado, pos)

        consulta.execute(sql)
        conexion.commit()
        return True

    elif columna == "fecha nacimiento":

        if pos != 0:
            pass

        else:
            pos = encontrarindice(acambiar, 4, False)

        sql = """
UPDATE cuentas SET fecha_de_nacimiento = '%s' WHERE ident = %d """ %(nuevo, pos)
        
        consulta.execute(sql)
        conexion.commit()
        return True

    elif columna == "fecha creaccion":

        print("No se puede cambiar la fecha de creacion")
        return "fdc"
        
    else:
        print("Error esa columna no esta definida")

    return error

    conexion.commit()

    consulta.close()
