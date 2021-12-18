import os

os.environ["OUTPUT_PATH"] = " "

def juego_de_piedras(n):
    ganador = " "
    if jugada(n) != 0:
        ganador = "Ha ganado jugador 1"
    else:
        ganador = "Ha ganado jugador 2"
        return ganador
        
