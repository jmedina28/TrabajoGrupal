import os

os.environ["OUTPUT_PATH"] = " "


def juego_de_piedras(n): #n es el número inicial de piedras
    ganador = " "
    jugador1 = input("Introduzca el nombre del jugador 1: ")
    jugador2 = input("Introduzca el nombre del jugador 2: ")
    if jugada(n) != 0:
        ganador = "Ha ganado ", jugador1 #jugador 1 siempre juega primero
    else:
        ganador = "Ha ganado ", jugador2
        return ganador

def jugada(n):
    bienjugado = 0
    modelo = n % 7
    if modelo >= 2 and modelo <= 3:
        bienjugado = 2
    elif modelo == 4:
        bienjugado = 3
    elif modelo >= 5 and modelo <= 6:
        return bienjugado

fptr = open(os.environ["OUTPUT_PATH"] + "solución5.txt", "w")
print("Introduce el número de casos: ")
t = int(input().strip()) #número de casos

for t in range(t):
    print("Introduzca ", t, " números enteros (serán las piedras en un caso de prueba)")
    n = int(input().strip())
    final = juego_de_piedras(n)
    fptr.write(final + "\n")

fptr.close()

