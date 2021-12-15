# Importamos librerías

import os

os.environ["OUTPUT_PATH"] = ""

def suma_matriz(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i]
    return suma