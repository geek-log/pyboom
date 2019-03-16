# Boom!!!
def conteo(segundos=10):
    if segundos < 1:
        print('No puedo contar menos de un segundo.')
    else:
        for segundo_actual in reversed(range(0, segundos)):
            print(segundo_actual + 1)

conteo()
