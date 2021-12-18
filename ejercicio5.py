import os

os.environ["OUTPUT_PATH"] = " "


def juego_de_piedras(n):
    ganador = " "
    if jugada(n) != 0:
        ganador = "Ha ganado el jugador 1"
    else:
        ganador = "Ha ganado el jugador 2"
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
t = int(input().strip()) #número de casos

for t in range(t):
    n = int(input().strip())
    final = juego_de_piedras(n)
    fptr.write(final + "\n")
    
