import os

def clear_screen():
    os.system("cls"if os.name == "nt" else "clear")

def verif_opc(enunciado,bajo,top):
    while True:
        try: 
            opcion=int(input(enunciado))
            if opcion >=bajo and opcion<=top:
                return opcion
            else:
                print(f"Opcion no esta en el intervalo de ({bajo}-{top})")
        except ValueError:
            print("Por favor, digite un numero valido")