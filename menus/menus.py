import os
from funciones.funciones import *


def menu_principal():
    print("Selección de roles")
    print("")
    print("1. Coordinador")
    print("2. Trainer")
    print("3. Salir")
    print("")
    opc=verif_opc("----> ",1,3)
    return opc


def menu_cord():
    print("Bienvenido Coordinador")
    print("")
    print("1. Registar camper")
    print("2. Ver campers")
    print("3. Editar campers")
    print("4. Eliminar campers")
    print("5. Asignar rutas")
    print("6. Crear rutas")
    print("7. Registrar trainer")
    print("8. Ver trainers")
    print("9. Reportes")
    print("10. Salir")
    opc=verif_opc("----> ",1,10)
    return opc

def menu_reg_camp(archivo,):

    clear_screen()
    datos = cargar_camper(archivo)

    if len(datos) >= MAX_LISTAS:
        print("Se alcanzó el número máximo de campers (33). No se pueden agregar más.")
        return

    nuevo_dato = {
        "nombre1": input("Ingresa el primer nombre: "),
        "nombre2": input("Ingresa el segundo nombre: "),
        "apellido1": input("Ingresa el primer apellido: "),
        "apellido2": input("Ingresa el segundo apellido: "),
        "direccion": input("Ingresa la dirección: "),
        "acudiente": input("Ingresa el nombre del acudiente: "),
        "celular": input("Ingresa el número de celular: "),
        "fijo": input("Ingresa el número fijo: "),
        "estado": input("Ingresa el estado del camper: "),
        "riesgo": input("Ingresa el nivel de riesgo: ")
    }

    datos.append(nuevo_dato)
    guardar_camper(archivo, datos)
    return archivo, datos

def menu_train():
    print("Bienvenido Trainer")
    print("")
    print("1. ")
    print("2. ")
    print("3. ")
    opc=verif_opc("----> ",1,3)
    return opc
   
def menu_salir():
    print("Bye bye /____|")   
