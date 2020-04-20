# Boom!!!
def conteo(segundos):
    if segundos < 1:
        print('No puedo contar menos de un segundo.')
    else:
        for segundo_actual in reversed(range(1, segundos + 1)):
            print(segundo_actual)

        print('BOOM!!!')


conteo(10)
