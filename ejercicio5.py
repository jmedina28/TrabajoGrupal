import os

os.environ["OUTPUT_PATH"] = ""


def juego_de_piedras(n):  # n es el número inicial de piedras
    ganador = ""

    if jugada(n) != 0:
        ganador = "Ha ganado el jugador 1."  # jugador 1 siempre juega primero
    else:
        ganador = "Ha ganado el jugador 2."
    return ganador


def jugada(n):
    bienjugado = 0
    modulo = n % 7
    if modulo >= 2 and modulo <= 3:
        bienjugado = 2
    elif modulo == 4:
        bienjugado = 3
    elif modulo >= 5 and modulo <= 6:
        bienjugado = 5
    return bienjugado


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"] + "solución5.txt", "w")
    print("Introduce el número de casos: ")
    t = int(input().strip())  # número de casos

    for ti in range(t):
        print(
            "Introduzca ",
            t,
            " números enteros (serán las piedras en un caso de prueba)",
        )
        n = int(input().strip())
        final = juego_de_piedras(n)
        fptr.write(str(final) + "\n")

    fptr.close()
