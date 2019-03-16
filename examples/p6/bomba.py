# Boom!!!
from random import seed
from random import randint

def conteo(segundos=10):
    if segundos < 1:
        print('No puedo contar menos de un segundo.')
    else:
        for segundo_actual in reversed(range(1, segundos + 1)):
            print(segundo_actual)

def detonar():
    conteo(3)
    print('BOOM!!!')

    seed() 
    return randint(100, 15000000)

megatones = detonar()
print('Megatones detonados: ', megatones)

while (megatones < 10000000):
    megatones = detonar()
    print('Megatones detonados: ', megatones)
