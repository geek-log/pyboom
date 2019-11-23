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

def atacar_ciudades(ciudades):
    if ciudades:
        for ciudad in ciudades:
            megatones = detonar()
            print('La ciudad de ' + ciudad + ' ha sido destruida')
            print('Megatones detonados: ' + str(megatones))

def atacar_paises(paises):
    if paises:
        for pais in paises:
            if pais['es_enemigo'] and not pais['pago_proteccion']:
                print(pais['nombre'] + ' es enemigo y no ha pagado proteccion, atacando ...')
                atacar_ciudades(pais['ciudades'])

def atacar():
    objetivos = [
        {
            'nombre': 'Rotruvia',
            'es_enemigo': True,
            'pago_proteccion': False,
            'ciudades': ['Rotruvia Central', 'Norwich', 'Tazlar']
        },
        {
            'nombre': 'Tierra Salvaje',
            'es_enemigo': True,
            'pago_proteccion': True,
            'ciudades': ['Norte', 'Sur']
        },
        {
            'nombre': 'Symkaria',
            'es_enemigo': True,
            'pago_proteccion': False,
            'ciudades': ['Aniana']
        },
        {
            'nombre': 'Corea del Norte',
            'es_enemigo': False,
            'pago_proteccion': False,
            'ciudades': ['Pionyang', 'Kaesong', 'Sinuiju']
        }
    ]
    atacar_paises(objetivos)


if __name__ == '__main__':
    atacar()
