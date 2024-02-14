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
            
def verif_opcSalir(enunciado,bajo,top):
    while True:
        try: 
            opcion=int(input(enunciado))
            if opcion >=bajo and opcion<=top:
                return opcion
            else:
                print(f"La opcion no se encuetra entre las opciones ({bajo}-{top})")
        except ValueError:
            print("Por favor, ingrese una opción válida")            

def verif_opcC(enunciado,bajo,top):
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
archivo2_json = "trainers.json"


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

def id_camper_name(datos):
    return str(len(datos) + 1)

def mostrar_camp(archivo):
    datos = cargar_camper(archivo)

    if not datos:
        print("No hay campers registrados.")
        return

    print("Campers registrados:")
    print("")
    for lista in datos:
        print(f"Camper {lista['camper #']}:")
        for clave, valor in lista.items():
            if clave != 'id' and clave != 'camper #':
                print(f"  {clave}: {valor}")
        print()

def eliminar_camper(archivo):
    datos = cargar_camper(archivo)

    if not datos:
        print("No hay campers registrados para eliminar.")
        return

    mostrar_camp(archivo)

    try:
        numero_lista = int(input("Ingresa el número del camper que deseas eliminar: "))
        if 1 <= numero_lista <= len(datos):
            lista_eliminada = datos.pop(numero_lista - 1)
            print(f"Camper {lista_eliminada['camper #']} eliminado exitosamente.")
            guardar_camper(archivo, datos)
        else:
            print("Número de camper inválido.")
    except ValueError:
        print("Entrada inválida. Ingresa un número.")

def editar_lista(archivo):
    datos = cargar_camper(archivo)

    if not datos:
        print("No hay listas creadas para editar.")
        return

    mostrar_camp(archivo)

    try:
        numero_lista = int(input("Ingresa el número de la lista que deseas editar: "))
        if 1 <= numero_lista <= len(datos):
            lista_a_editar = datos[numero_lista - 1]

            print(f"\nEditando Lista {lista_a_editar['camper #']}:")
            for clave, valor in lista_a_editar.items():
                if clave != 'id' and clave != 'camper #':
                    print(f"  {clave}: {valor}")

            for clave in lista_a_editar.keys():
                if clave != 'id' and clave != 'camper #':
                    nuevo_valor = input(f"Ingrese nuevo valor para {clave}: ")
                    lista_a_editar[clave] = nuevo_valor

            guardar_camper(archivo, datos)
            print(f"\nLista {lista_a_editar['camper #']} editada exitosamente.")
        else:
            print("Número de lista inválido.")
    except ValueError:
        print("Entrada inválida. Ingresa un número.")
        
def registrar_notas(archivo):
    datos = cargar_camper(archivo)

    if not datos:
        print("No hay campers registrados para asignarle sus notas.")
        return

    mostrar_camp(archivo)

    try:
        numero_lista = int(input("Ingresa el número del camper al que deseas asignar sus notas. "))
        if 1 <= numero_lista <= len(datos):
            lista_a_actualizar = datos[numero_lista - 1]

            try:
                nota_teorica = float(input("Ingresa la nota teórica: "))
                nota_practica = float(input("Ingresa la nota práctica: "))

                if 0 <= nota_teorica <= 100 and 0 <= nota_practica <= 100:
                    porcentaje_promedio = (nota_teorica + nota_practica) / 2

                    if porcentaje_promedio > 60:
                        lista_a_actualizar["estado"] = "aprobado"
                    else:
                        lista_a_actualizar["estado"] = "reprobado"

                    print(f"El estado de la lista {lista_a_actualizar['camper #']} se ha actualizado a: {lista_a_actualizar['estado']}")
                    guardar_camper(archivo, datos)
                else:
                    print("Las notas deben estar en el rango de 0 a 100.")
            except ValueError:
                print("Entrada inválida. Ingresa un número.")
        else:
            print("Número de camper inválido.")
    except ValueError:
        print("Entrada inválida. Ingresa un número.")

def guardar_trainer(archivo2, datos2):
    with open(archivo2, 'w') as archivo2_json:
        json.dump(datos2, archivo2_json, indent=2)

def cargar_trainer(archivo2):
    try:
        with open(archivo2, 'r') as archivo2_json:
            datos2 = json.load(archivo2_json)
        return datos2
    except FileNotFoundError:
        return [] 

def mostrar_trainer(archivo2):
    datos2 = cargar_trainer(archivo2)

    if not datos2:
        print("No hay trainers registrados.")
        return

    print("Trainers registrados:")
    print("")
    for lista in datos2:
        print(f"Trainer {lista['trainer #']}:")
        for clave, valor in lista.items():
            if clave != 'id' and clave != 'trainer #':
                print(f"  {clave}: {valor}")
        print()

def asignar_ruta_camper(archivo):
    datos = cargar_camper(archivo)

    if not datos:
        print("No hay listas creadas para asignar ruta.")
        return

    mostrar_camp(archivo)

    try:
        numero_lista = int(input("Ingresa el número del camper al que deseas asignar ruta: "))
        if 1 <= numero_lista <= len(datos):
            lista_seleccionada = datos[numero_lista - 1]

            if lista_seleccionada["estado"].lower() == "aprobado":

                opciones_ruta = {
                    1: "Ruta NodeJS",
                    2: "Ruta Java",
                    3: "Ruta NetCore"
                }

                print("Opciones de ruta:")
                for key, value in opciones_ruta.items():
                    print(f"{key}: {value}")

                try:
                    opcion_elegida = int(input("Selecciona una opción de ruta (1-3): "))
                    if 1 <= opcion_elegida <= 3:
                        lista_seleccionada["ruta"] = opciones_ruta[opcion_elegida]
                        print(f"Ruta asignada al camper {lista_seleccionada['camper #']}: {lista_seleccionada['ruta']}")
                        guardar_camper(archivo, datos)
                    else:
                        print("Opción de ruta inválida.")
                except ValueError:
                    print("Entrada inválida. Ingresa un número.")
            else:
                print("No se puede asignar ruta a un camper con estado diferente a 'aprobado'.")
        else:
            print("Número de camper inválido.")
    except ValueError:
        print("Entrada inválida. Ingresa un número.")


rutas_entrenamiento = {
    1: {"nombre": "Fundamentos de programación", "modulos": ["Introducción a la algoritmia", "PSeInt", "Python"],
        "sgdb_principal": "SQLite", "sgdb_alternativo": "MySQL"},
    2: {"nombre": "Programación Web", "modulos": ["HTML", "CSS", "Bootstrap"],
        "sgdb_principal": "MySQL", "sgdb_alternativo": "PostgreSQL"},
    3: {"nombre": "Programación formal", "modulos": ["Java", "JavaScript", "C#"],
        "sgdb_principal": "PostgreSQL", "sgdb_alternativo": "MongoDB"},
    4: {"nombre": "Bases de datos", "modulos": ["Mysql", "MongoDb", "Postgresql"],
        "sgdb_principal": "MongoDB", "sgdb_alternativo": "SQLite"},
    5: {"nombre": "Backend", "modulos": ["NetCore", "Spring Boot", "NodeJS", "Express"],
        "sgdb_principal": "SQLite", "sgdb_alternativo": "PostgreSQL"}
}

trainers = {
    1: {"nombre": "Trainer 1", "rutas_asignadas": []},
    2: {"nombre": "Trainer 2", "rutas_asignadas": []},
    3: {"nombre": "Trainer 3", "rutas_asignadas": []},
    4: {"nombre": "Trainer 4", "rutas_asignadas": []},
    5: {"nombre": "Trainer 5", "rutas_asignadas": []},
    6: {"nombre": "Trainer 5", "rutas_asignadas": []},
    7: {"nombre": "Trainer 7", "rutas_asignadas": []},
    8: {"nombre": "Trainer 8", "rutas_asignadas": []},
}

def mostrar_rutas_entrenamiento(rutas):
    print("Rutas de entrenamiento disponibles:")
    for key, value in rutas.items():
        print(f"{key}: {value['nombre']}")
        
def asignar_ruta_entrenamiento(rutas, trainers):
    while True:
        try:
            opcion_ruta = int(input("Selecciona una ruta de entrenamiento (1-5): "))
            if 1 <= opcion_ruta <= 5:
                ruta_elegida = rutas[opcion_ruta]
                if len(ruta_elegida["campers_asignados"]) < MAX_LISTAS:
                    asignar_trainer_ruta(opcion_ruta, trainers)
                    return ruta_elegida
                else:
                    print("La ruta está completa, elige otra.")
            else:
                print("Opción de ruta inválida.")
        except ValueError:
            print("Entrada inválida. Ingresa un número.")        
            
def asignar_trainer_ruta(opcion_ruta, trainers):
    print("Trainers disponibles para asignar a la ruta:")
    for key, value in trainers.items():
        if opcion_ruta not in value["rutas_asignadas"]:
            print(f"{key}: {value['nombre']}")

    while True:
        try:
            opcion_trainer = int(input("Selecciona un trainer para asignar a la ruta: "))
            if opcion_trainer in trainers and opcion_ruta not in trainers[opcion_trainer]["rutas_asignadas"]:
                trainers[opcion_trainer]["rutas_asignadas"].append(opcion_ruta)
                print(f"Trainer {trainers[opcion_trainer]['nombre']} asignado a la ruta.")
                break
            else:
                print("Opción de trainer inválida o ya asignado a la ruta.")
        except ValueError:
            print("Entrada inválida. Ingresa un número.") 