import os
def limpiar_pantalla():
    if os.name == 'posix':
        os.system('clear')

def trainer(rol):
        print("--------------------------------")
        print("--                            --")
        print("--     BIENVENIDO TRAINER     --")
        print("--                            --")
        print("--------------------------------")
        print("")
        print("1 VER HORARIOS\t 2 ASIGNAR HORARIOS")
        print("")
        a = int(input("---->"))
        if a ==1:
             print("horarios")
        elif a==2:
             print("asignar")
        