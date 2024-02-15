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
    print("7. Ver trainers")
    print("8. Reportes")
    print("9. Salir")
    print("")
    opcC=verif_opcC("----> ",1,9)
    return opcC

def menu_mostrar_camp(archivo):
    clear_screen()
    mostrar_camp(archivo)
    print("1. Salir")
    opcS=verif_opcSalir("----> ",1,1)
    return opcS

def menu_asignar_rutas(archivo):
    clear_screen()
    asignar_ruta_camper(archivo)
    print("1. Salir")
    opcS=verif_opcSalir("----> ",1,1)
    return opcS

def menu_eliminar_camp(archivo):
    clear_screen()
    eliminar_camper(archivo)
    print("1. Salir")
    opcS=verif_opcSalir("----> ",1,1)
    return opcS    

def menu_editar_camp(archivo):
    clear_screen()
    editar_lista(archivo)
    print("1. Salir")
    opcS=verif_opcSalir("----> ",1,1)
    return opcS

def menu_reg_notas(archivo):
    clear_screen()
    registrar_notas(archivo)
    print("1. Salir")
    opcS=verif_opcSalir("----> ",1,1)
    return opcS

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
        "estado": "inscrito",
        "riesgo": "bajo"
    }

    datos.append(nuevo_dato)
    guardar_camper(archivo, datos)
    print("1. Salir")
    opcS=verif_opcSalir("----> ",1,1)
    return archivo, datos, opcS


def menu_mostrar_trainers(archivo2):
    clear_screen()
    mostrar_trainer(archivo2)
    print("1. Salir")
    opcS=verif_opcSalir("----> ",1,1)
    return opcS


def menu_train(archivo2):
    print("Selección de trainer")
    print("")
    print("1. Ver trainers")
    opct=verif_opct("---->",1,1)
    return opct
    
def menu_salir():
    print("Bye bye /____|")   

def menu_gestion_rutas(rutas, trainers):
    while True:
        clear_screen()
        print("=== GESTIÓN DE RUTAS DE ENTRENAMIENTO ===")
        print("1. Mostrar Rutas de Entrenamiento")
        print("2. Crear Nueva Ruta")
        print("3. Asignar Trainer a Ruta")
        print("4. Volver al Menú Principal")
        opcion = verif_opc("Selecciona una opción: ", 1, 4)

        if opcion == 1:
            mostrar_rutas_entrenamiento(rutas)
            input("Presiona Enter para volver al menú.")
        elif opcion == 2:
            crear_nueva_ruta(rutas)
        elif opcion == 3:
            asignar_trainer_a_ruta(trainers, rutas)
        elif opcion == 4:
            break