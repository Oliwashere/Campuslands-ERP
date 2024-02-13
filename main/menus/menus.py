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
    print("5. Registrar notas")
    print("6. Asignar rutas")
    print("7. Crear rutas")
    print("8. Registrar trainer")
    print("9. Ver trainers")
    print("10. Reportes")
    print("11. Salir")
    print("")
    opcC=verif_opcC("----> ",1,11)
    return opcC

def menu_mostrar_camp(archivo):
    clear_screen()
    mostrar_camp(archivo)
    print("1. Salir")
    opcS=verif_opcSalir("----> ",1,1)
    return opcS

def menu_eliminar_camp(archivo):
    clear_screen()
    eliminar_camper(archivo)    

def menu_editar_camp(archivo):
    clear_screen()
    editar_lista(archivo)

def menu_reg_notas(archivo):
    clear_screen()
    registrar_notas(archivo)

def menu_reg_camp(archivo,):

    clear_screen()
    datos = cargar_camper(archivo)

    if len(datos) >= MAX_LISTAS:
        print("Se alcanzó el número máximo de campers (33). No se pueden agregar más.")
        return

    nuevo_dato = {
        "camper #": id_camper_name(datos),
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
