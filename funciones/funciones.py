import os
import json

def clear_screen():
    os.system("cls"if os.name == "nt" else "clear")

def verif_opc(enunciado,bajo,top):
    while True:
        try: 
            opcion=int(input(enunciado))
            if opcion >=bajo and opcion<=top:
                return opcion
            else:
                print(f"La opcion no se encuetra entre las opciones ({bajo}-{top})")
        except ValueError:
            print("Por favor, ingrese una opción válida")

MAX_LISTAS = 33

archivo_json = "campers.json"


def guardar_camper(archivo, datos):
    with open(archivo, 'w') as archivo_json:
        json.dump(datos, archivo_json, indent=2)

def cargar_camper(archivo):
    try:
        with open(archivo, 'r') as archivo_json:
            datos = json.load(archivo_json)
        return datos
    except FileNotFoundError:
        return []        
    
def id_camper(datos):
    ids = [dato.get("id", 0) for dato in datos]
    nuevo_id = max(ids, default=0) + 1
    return nuevo_id    
