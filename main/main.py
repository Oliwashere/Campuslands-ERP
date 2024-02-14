from funciones.funciones import *
from menus.menus import *

while True:
    clear_screen()
    opc=menu_principal()
    clear_screen()
    if opc==1:
        opcC=menu_cord()
        if opcC==1:
            menu_reg_camp("campers.json")
        elif opcC==2:
            opcS=0
            menu_mostrar_camp("campers.json")
            if opcS==1:
                opc=menu_principal()
        elif opcC==3:
            menu_editar_camp("campers.json")    
        elif opcC==4:
            menu_eliminar_camp("campers.json")
        elif opcC==5:
            menu_reg_notas("campers.json")
        elif opcC==8:
            menu_mostrar_trainers("trainers.json")                 
    if opc==2:
        menu_train()
    if opc==3:
        menu_salir()
    break 
        


