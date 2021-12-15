# Importamos librerías

import os

os.environ["OUTPUT_PATH"] = ""

def suma_matriz(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i]
    return suma

if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"] + "solucion1.txt", "w")
    contar_matriz = int(input())
    matriz = list(map(int, input().rstrip().split()))
    result = suma_matriz(matriz)
    fptr.write(str(result) + "\n")
    fptr.close()