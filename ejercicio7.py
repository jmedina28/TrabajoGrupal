import os

os.environ["OUTPUT_PATH"] = "solución7.txt"


def notasEstudiantes():
    lista = []
    for (
        i
    ) in (
        notas
    ):  # notas va a ser la lista sobre la que van a quedan registradas todas las notas
        lista.append(
            notafinal(i)
        )  # notafinal va a ser la función que hace los redondeos
    return lista
