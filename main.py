from funciones.funciones import *
from menus.menus import *

while True:
    clear_screen()
    opc=menu_principal()
    clear_screen()
    if opc==1:
        menu_cord()
    if opc==2:
        menu_train()
    if opc==3:
        menu_salir()
    break 
        


