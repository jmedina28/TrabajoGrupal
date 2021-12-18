import os

os.environ["OUTPUT_PATH"] = "solución7.txt"


def notasEstudiantes(notas):
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


def notafinal(notas):
    notaredondeada = 0
    if notas < 40:
        notas = notaredondeada
    else:
        cocientes = int(notas / 5 + 1)
        multiplo = int(cocientes * 5)
        if multiplo - notas < 3:
            multiplo = notaredondeada
        else:
            notas = notaredondeada
    return notaredondeada
