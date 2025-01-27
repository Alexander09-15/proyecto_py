import random
import string 

def validar_entero():
    while True:
        try:
            longitud = int(input(">...   "))
            if longitud > 0:
                break
            else:
                print("Ingresa un numero mayor que 0")
        except ValueError:
            print("Ingresa un numero entero")
    return longitud

def validar_opcion():
    while True:
        try:
            opcion = int(input(">...   "))
            if opcion in range(1,7):
                break
        except ValueError:
            print("Ingresa una opcion valida")

    return opcion

def generador(opcion, longitud):

    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation
    
    combinaciones = {1: letras , 2: numeros , 3: letras + numeros , 4: letras + simbolos , 5: numeros + simbolos, 6: numeros + letras + simbolos}
    contraseña = ''.join(random.choice(combinaciones[opcion]) for x in range(longitud))
    return contraseña
def menu():
    print("\n GENERADOR DE CONTRASEÑAS! \n")

    print("Ingresa la longitud de la contraseña")
    longitud = validar_entero()

    print("""Ingresa una de las siguientes opciones:

           1.Solo letras
           2.Solo numeros
           3.Letras y numeros 
           4.Letras y simbolos 
           5.Numeros y simbolos
           6.Todo
          """
         )

    opcion = validar_opcion()


    contraseña = generador(opcion,longitud)
    print(f"Tu contraseña es: {contraseña}")    
menu()
