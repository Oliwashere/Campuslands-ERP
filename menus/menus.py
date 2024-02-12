import os
from funciones.funciones import *


def menu_principal():
    print("Selección de roles")
    print("1. Coordinador")
    print("2. Trainer")
    print("3. Salir")
    print("")
    opc=verif_opc("---->",1,3)
    return opc


def menu_cord():
    print("Bienvenido Coordinador")
    print("1. Registar camper")
    print("2. Ver campers")
    print("3. ")

def menu_train():
    print("Bienvenido Trainer")
   
def menu_salir():
    print("Bye bye /____|")   
