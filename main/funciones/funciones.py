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

            # Mostrar información actual de la lista
            print(f"\nEditando Lista {lista_a_editar['camper #']}:")
            for clave, valor in lista_a_editar.items():
                if clave != 'id' and clave != 'camper #':
                    print(f"  {clave}: {valor}")

            # Solicitar nuevas entradas
            for clave in lista_a_editar.keys():
                if clave != 'id' and clave != 'camper #':
                    nuevo_valor = input(f"Ingrese nuevo valor para {clave}: ")
                    lista_a_editar[clave] = nuevo_valor

            # Guardar cambios en el archivo
            guardar_camper(archivo, datos)
            print(f"\nLista {lista_a_editar['camper #']} editada exitosamente.")
        else:
            print("Número de lista inválido.")
    except ValueError:
        print("Entrada inválida. Ingresa un número.")
        
def registrar_notas(datos):
    try:
        numero_lista = int(input("Ingresa el número de la lista que deseas actualizar: "))
        if 1 <= numero_lista <= len(datos):
            lista_a_actualizar = datos[numero_lista - 1]
            
            # Mostrar información actual de la lista
            print(f"\nActualizando Estado de Lista {lista_a_actualizar['camper #']}:")

            # Obtener notas teóricas y prácticas del usuario
            nota_teorica = float(input("Ingresa la nota teórica: "))
            nota_practica = float(input("Ingresa la nota práctica: "))
            
            # Calcular el promedio
            promedio = (nota_teorica + nota_practica) / 2

            # Actualizar el estado
            if promedio > 60:
                lista_a_actualizar['estado'] = 'aprobado'
            else:
                lista_a_actualizar['estado'] = 'reprobado'

            # Guardar cambios en el archivo
            guardar_camper(archivo_json, datos)
            print(f"\nEstado de Lista {lista_a_actualizar['camper #']} actualizado exitosamente.")
        else:
            print("Número de lista inválido.")
    except ValueError:
        print("Entrada inválida. Ingresa un número y notas válidas.")
