# Boom!!!
from random import seed
from random import randint

def conteo(segundos):
    if segundos < 1:
        print('No puedo contar menos de un segundo.')
    else:
        for segundo_actual in reversed(range(1, segundos + 1)):
            print(segundo_actual)

def detonar():
    conteo(2)
    print('BOOM!!!')

    seed() 
    return randint(100, 15000000)

ciudades = ["Rotruvia Central", "Riba", "Tazlar"]
ciudades.append("Norwich")
ciudades.remove("Riba")

for ciudad in ciudades:
    megatones = detonar()
    print('La ciudad de ' + ciudad + ' ha sido destruida')
    print('Megatones detonados: ' + str(megatones))
