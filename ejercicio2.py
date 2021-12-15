# Importamos las librerías necesarias para la realización del ejercicio.
import os

# Creo la función en la que se va a desarrollar el ejercicio.
def comparalosproblemas(a, b):
    # Defino las variables con los nombres de los jugadores.
    lucia = 0
    carlos = 0
    # Creo el bucle que va a completar los datos de las variables.
    for n in range(3):
        if a[n] > b[n]:
            lucia += 1
        elif a[n] < b[n]:
            carlos += 1
    return (lucia, carlos)
