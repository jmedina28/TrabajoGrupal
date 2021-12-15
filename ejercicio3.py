# Importamos las librerías.
import os

# Defino la función que va a resolver el ejercicio.
def sumagrandematriz(matriz):
    # Defino la variable en la que quedará registrado el resultado de la operación.
    sumamatrices = 0
    # Voy a crear el bucle para hacer la suma.
    for n in matriz:
        sumamatrices += n
    return sumamatrices
