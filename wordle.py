import numpy as np
import random
from colorama import Fore
from colorama import Style



palabra = random.choice(open("letras.txt").readline().split()) #Abre el archvo de texto y elige una palabra aleatoria
intento = 1  # Número de intentos

def wordle(intento):

    print('Intento: ', intento)
    print("Introduzca una palabra de 5 letras (sin tildes ni ñ):")
    entrada = input().upper()  # Transforma la palabra introducida a letras mayúsculas
    # print(entrada[1]) primera letra de la palabra
    # print(entrada) palabra en mayúsculas

    # Coprobamos por cada letra que exista y coincida con la palabra a adivinar
    coincide1 = entrada[0] in palabra[0]
    coincide2 = entrada[1] in palabra[1]
    coincide3 = entrada[2] in palabra[2]
    coincide4 = entrada[3] in palabra[3]
    coincide5 = entrada[4] in palabra[4]

    # Comprobamos que la letra exista en la palabra a adivinar
    existe1 = entrada[0] in palabra
    existe2 = entrada[1] in palabra
    existe3 = entrada[2] in palabra
    existe4 = entrada[3] in palabra
    existe5 = entrada[4] in palabra

    # Si coincide la letra la imprimiramos en azul, si existe pero no coincide la imprimiramos en amarillo y si no la dejaremos normal.
    resultado1 = ""
    resultado2 = ""
    resultado3 = ""
    resultado4 = ""
    resultado5 = ""

    if (coincide1 == True):
        resultado1 = f'{Fore.BLUE}{entrada[0]}{Style.RESET_ALL}'
    elif (existe1 == True):
        resultado1 = f'{Fore.YELLOW}{entrada[0]}{Style.RESET_ALL}'

    else:
        resultado1 = entrada[0]

    if (coincide2 == True):
        resultado2 = f'{Fore.BLUE}{entrada[1]}{Style.RESET_ALL}'
    elif (existe2 == True):
        resultado2 = f'{Fore.YELLOW}{entrada[1]}{Style.RESET_ALL}'
    else:
        resultado2 = entrada[1]

    if (coincide3 == True):
        resultado3 = f'{Fore.BLUE}{entrada[2]}{Style.RESET_ALL}'
    elif (existe3 == True):
        resultado3 = f'{Fore.YELLOW}{entrada[2]}{Style.RESET_ALL}'
    else:
        resultado3 = entrada[2]

    if (coincide4 == True):
        resultado4 = f'{Fore.BLUE}{entrada[3]}{Style.RESET_ALL}'
    elif (existe4 == True):
        resultado4 = f'{Fore.YELLOW}{entrada[3]}{Style.RESET_ALL}'
    else:
        resultado4 = entrada[3]

    if (coincide5 == True):
        resultado5 = f'{Fore.BLUE}{entrada[4]}{Style.RESET_ALL}'
    elif (existe5 == True):
        resultado5 = f'{Fore.YELLOW}{entrada[4]}{Style.RESET_ALL}'
    else:
        resultado5 = entrada[4]

    # print(palabra, coincide1, coincide2, coincide3, coincide4, coincide5, "-", existe1, existe2, existe3, existe4, existe5)
    if (palabra == entrada):
        print(f'{Fore.BLUE}Enhorabuena, adivinaste la palabra de hoy!{Style.RESET_ALL}!')
        exit()
    elif (intento == 5):
        print(f'{Fore.RED}Agotaste el número de intentos!{Style.RESET_ALL}!')
        exit()
    else:
        print(palabra)  # Palabra a adivinar, comentar de cara al jugador.
        print(resultado1, resultado2, resultado3, resultado4, resultado5)
        intento += 1
        wordle(intento)



wordle(intento)