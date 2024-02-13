import os
from colorama import init, Fore

def limpiar_pantalla():
    if os.name == 'posix':
        os.system('clear')
print("--------------------------------")
print("--                            --")
print("--         BIENVENIDO         --")
print("--                            --")
print("--------------------------------")
print("")
print ("Escoge tu rol")
print("")
print("1 Coordinador\t2 Trainer")
print("")
rol = int(input("---->"))

if rol ==1:
    limpiar_pantalla()
    print("--------------------------------")
    print("--                            --")
    print("--   BIENVENIDO COORDINADOR   --")
    print("--                            --")
    print("--------------------------------")
    print("")
    print("¿Que modulo deseas importar?")
    print("") 
    print("1 CAMPERS\t 2 Trainers")
if rol ==2:
    limpiar_pantalla()
    print("--------------------------------")
    print("--                            --")
    print("--     BIENVENIDO TRAINER     --")
    print("--                            --")
    print("--------------------------------")
    print("")