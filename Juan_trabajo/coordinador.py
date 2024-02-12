import os
def limpiar_pantalla():
    if os.name == 'posix':
        os.system('clear')

def Coordinador(rol):
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
        a = int(input("---->"))
        print("")
        if a== 1:
            print("CAMPERS")
        elif a==2:
            print("Trainers")

rol=int(input("----->"))
print(Coordinador(rol))
