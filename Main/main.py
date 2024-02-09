###############################################
#-------------- CAMPUSLANDS ERP --------------#
###############################################

import json

# - INGRESO CAMPER -
def rol_camper():
    print()
    
# - INGRESO TRAINTER -
def rol_trainer():
    print()

# - INGRESO COORDINADOR -
def rol_coordi():
    print()

# - SELECCIÓN DE ROL -
    
print("Digita a continuación si eres Camper(1), Trainer(2) o Coordinador(3)")
rol = (input())

if rol == 1:
    print(rol_camper)
elif rol == 2:
    print(rol_trainer)
elif rol == 3:
    print(rol_coordi)