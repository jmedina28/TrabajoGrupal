class Coordenadas:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def comparacion(self, x, y):
        if self.x == x and self.y == y:
            return True
        else:
            return False


class Tunel:
    def __init__(self, x1, x2, y1, y2):
        self.extremo1 = Coordenadas(x1, y1)
        self.extremo2 = Coordenadas(x2, y2)


def buscaTunel(tuneles, Casillax, Casillay):
    coordenadas = Coordenadas(Casillax, Casillay)
    for i in tuneles:
        if i.extremo1.comparate(Casillax, Casillay) == True:
            coordenadas.x = i.extremo2.x
            coordenadas.y = i.extremo2.y
            break
        elif i.extremo2.comparate(Casillax, Casillay) == True:
            coordenadas.x = i.extremo1.x
            coordenadas.y = i.extremo1.y
            break
    return coordenadas

def movimientos(laberinto, n, m, Casillax, Casillay):