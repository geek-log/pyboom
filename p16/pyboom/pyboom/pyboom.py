# -*- coding: utf-8 -*-

"""
.. module:: pyboom
    :platform: Linux
    :synopsis: Detonador de bombas .. boom!!!

.. moduleauthor:: constrict0r <constrict0r@protonmail.com>
"""

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
    seed()
    megatones = randint(100, 15000000)
    print(hongo_explosion(megatones))

    return megatones

def hongo_explosion(megatones):
    """Tic tac.

    Boom!!!

    Args:
        megatones (int): Cantidad de megatones detonados.

    Returns:
        string: Hongo de la explosión.

    """

    boom_min = """\
             BOOM!!!
          _ ._  _ , _ ._
        (_ ' ( `  )_  .__)
      ( (  (    )   `)  ) _)
     (__ (_   (_ . _) _) ,__)
         `~~`\ ' . /`~~`
              ;   ;
             `/   \´
____________`/_ __ \´____________
    """

    boom_med = """\
                           BOOOM!!!!
                             ____
                     __,-~~/~    `---.
                   _/_,---(      ,    )
               __ /        <    /   )  \___
- ------===;;;'====------------------===;;;===----- -  -
                  \/  ~"~"~"~"~"~\~"~)~"/
                  (_ (   \  (     >    \)
                   \_( _ <         >_>'
                      ~ `-i' ::>|--"
                          I;|.|.|
                         <|i::|i|`.
                        (` ^'"`-' ")
    """

    boom_max = """\
                 BOOOOOM!!!!
         ____/ (  (    )   )  \___
        /( (  (  )   _    ))  )   )\_
      ((     (   )(    )  )   (   )  )
    ((/  ( _(   )   (   _) ) (  () )  )
   ( (  ( (_)   ((    (   )  .((_ ) .  )_
  ( (  )    (      (  )    )   ) . ) (   )
 (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )
 ( (  (   ) (  )   (  ))  .  ) _)(   )  )  )
(  ( \ ) (    (_  ( ) ( )    )   ) )  )) ( )
 (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )
( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )
 ((  (   )(    (     _    )   _) _(_ (  (_ )
  (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)
  ((__)        \\||lll|l||///          \_))
           (   /(/ (  )  ) )\   )
         (    ( ( ( | | ) ) )\   )
          (   /(| / ( )) ) ) )) )
        (     ( ((((_(|)_)))))     )
         (      ||\(|(|)|/||     )
       (        |(||(||)||||        )
         (     //|/l|||)|\\ \     )
       (/ / //  /|//||||\\  \ \  \ _)
    """

    if megatones < 4000000:
       return boom_min

    elif megatones > 4000000 and megatones < 8000000:
       return boom_med

    return boom_max

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
                print(pais['nombre'] + ' es enemigo y no ha pagado protección, atacando ...')
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
    bomba_acelerada()

def bomba_acelerada():

    agujero_negro = """\
    Un agujero negro se ha abierto
    \|/
   - o -
    /-`-.
    :   :
    :   :
    :___:

    .---.
    : | :
    :-o-:
    :_|_:

    .---.
    (\|/)
    --0--
    (/|\)

   '.\|/.'
   (\   /)
   - -O- -
   (/   \)
   ,'/|\'.

'.  \ | /  ,'
  `. `.' ,'
 ( .`.|,' .)
 - ~ -0- ~ -
 (

','|'.` )
  .' .'. '.
,'  / | \  '.
    \ '  "  
 ` . `.' ,'
 . `` ,'. "
   ~ (   ~ -

    Tú mueres.
    """

    import pkg_resources

    try:
        pkg_resources.get_distribution('py-rolldice')

    except pkg_resources.DistributionNotFound:
        print('Esto es Latveria real.')
        print('No se ha lanzado la bomba acelerada.')

    else:
        print('Esto es Latveria falsa.')
        print('Lanzando bomba acelerada ... BOOOOOOM!!!!!!')
        print(agujero_negro)
