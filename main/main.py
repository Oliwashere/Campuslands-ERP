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
            mostrar_camp("campers.json")    
    if opc==2:
        menu_train()
    if opc==3:
        menu_salir()
    break 
        


