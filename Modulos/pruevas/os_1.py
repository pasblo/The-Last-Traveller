import os
def menu():
    opcion = 0
    while opcion <1 or opcion >7:
        print ("Bienvenid@")
        print()
        print ("1) Calculadora")
        print ("2) Paint")
        print ("3) Loquequieras")
        opcion = input('Digita el numero de la opcion a escoger: ')
        return opcion
opcion = 0
while opcion !=16:
    opcion = menu()
    if opcion == 1:
        import os
        os.system("cls")
        print ("1)Sumar")
        print ("2)Restar")
        num = int(input('Digita el numero de la opcion a escoger: '))
        if num == 1:
            a = input("Escribe el primer numero a sumar:  ")
            b = input('Escribe el segundo numero a sumar:  ')
            print ('El Resultado de la suma es :  ', a + b)
            raw_input()
            os.system("cls")
