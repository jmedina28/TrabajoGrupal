# Importamos las librerías.
import os

os.environ["Salida"] = ""
# Defino la función que va a resolver el ejercicio.
def sumagrandematriz(matriz):
    # Defino la variable en la que quedará registrado el resultado de la operación.
    sumamatrices = 0
    # Voy a crear el bucle para hacer la suma.
    for n in matriz:
        sumamatrices += n
    return sumamatrices


if __name__ == "__main__":
    fptr = open(os.environ["Salida"] + "solucion3.txt", "w")
    ar_count = int(input("Escriba un número:\n").strip())
    matriz = list(
        map(
            int,
            input("Escriba los números de la matriz separados por espacios:\n")
            .rstrip()
            .split(),
        )
    )
    resultado = sumagrandematriz(matriz)

    fptr.write(str(resultado) + "\n")

    fptr.close()
