import os

os.environ["OUTPUT_PATH"] = ""


def notasEstudiantes(notas):
    lista = []
    for i in notas:
        lista.append(notafinal(i))
    return lista


def notafinal(notas):
    notaredondeada = 0
    if notas < 40:
        notaredondeada = notas
    else:
        cocientes = int(notas / 5 + 1)
        multiplo = int(cocientes * 5)
        if multiplo - notas < 3:
            notaredondeada = multiplo
        else:
            notaredondeada = notas
    return notaredondeada


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"] + "solucion7.txt", "w")
    print("Número de estudiantes:")
    nestudiantes = int(input().strip())

    notas = []

    for _ in range(nestudiantes):
        print("Nota de cada estudiante:")
        notas_i = int(input().strip())
        notas.append(notas_i)

    resultado = notasEstudiantes(notas)

    fptr.write("\n".join(map(str, resultado)))
    fptr.write("\n")

    fptr.close()
