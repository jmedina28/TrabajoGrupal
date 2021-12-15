# Importamos las librerías necesarias para la realización del ejercicio.
import os

os.environ["Salida"] = ""
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


# Aquí ejecuto el código y muestro la salida en un fichero de texto creado cuando se ejecute.
if __name__ == "__main__":
    fptr = open(os.environ["Salida"] + "solucion2.txt", "w")

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    resultado = comparalosproblemas(a, b)

    fptr.write(" ".join(map(str, resultado)))
    fptr.write("\n")

    fptr.close()
