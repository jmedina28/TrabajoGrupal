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


def movimientos(laberinto, tuneles, n, m, Casillax, Casillay):
    num = 0
    den = 0
    probabilidad = 0.00
    if Casillax > 0 and laberinto[Casillax - 1][Casillay] != "m":
        den += 1
        if laberinto[Casillax - 1][Casillay] == "s":
            num += 1
    if Casillax < n - 1 and laberinto[Casillax + 1][Casillay] != "m":
        den += 1
        if laberinto[Casillax + 1][Casillay] == "s":
            num += 1
    if Casillay < m - 1 and laberinto[Casillax][Casillay + 1] != "m":
        den += 1
        if laberinto[Casillax][Casillay + 1] == "s":
            num += 1
    if Casillay > 0 and laberinto[Casillax][Casillay - 1] != "m":
        den += 1
        if laberinto[Casillax][Casillay - 1] == "s":
            num += 1
    if den == 0:
        return probabilidad
    probabilidad = num / den
    if Casillax > 0 and laberinto[Casillax - 1][Casillay] == "v":
        laberintocopy = laberinto
        coordenadas = buscaTunel(Casillax - 1, Casillay, tuneles)
        laberintocopy[Casillax][Casillay] = "m"
        probabilidad += (
            movimientos(
                tuneles, coordenadas.x, coordenadas.y, laberintocopy, n, m, tuneles
            )
            / den
        )
    if Casillax < n - 1 and laberinto[Casillax + 1][Casillay] == "v":
        laberintocopy = laberinto
        coordenadas = buscaTunel(Casillax + 1, Casillay, tuneles)
        laberintocopy[Casillax][Casillay] = "m"
        probabilidad += (
            movimientos(tuneles, coordenadas.x, coordenadas.y, laberintocopy, n, m)
            / den
        )
    if Casillay < m - 1 and laberinto[Casillax][Casillay + 1] == "v":
        laberintocopy = laberinto
        coordenadas = buscaTunel(Casillax, Casillay + 1, tuneles)
        laberintocopy[Casillax][Casillay] = "m"
        probabilidad += (
            movimientos(tuneles, coordenadas.x, coordenadas.y, laberintocopy, n, m)
            / den
        )
    if Casillay > 0 and laberinto[Casillax][Casillay - 1] == "v":
        laberintocopy = laberinto
        coordenadas = buscaTunel(Casillax, Casillay - 1, tuneles)
        laberintocopy[Casillax][Casillay] = "m"
        probabilidad += (
            movimientos(tuneles, coordenadas.x, coordenadas.y, laberintocopy, n, m)
            / den
        )
    return probabilidad


print("Dimensiones del laberinto y número de túneles:(filas columnas tuneles)")
primerainput = input().rstrip().split()

n = int(primerainput[0])

m = int(primerainput[1])

k = int(primerainput[2])
laberinto = []
for ni in range(n):
    print(
        "Fila " + str(ni) + " del laberinto:(m muro,s salida, b bomba, v vacía o túnel)"
    )
    fila = input()
    laberinto.append(list(fila))
tuneles = []
for n in range(k):
    print("Coordenadas(i1 j1 i2 j2) del túnel: " + str(n))
    segundainput = input().rstrip().split()

    x1 = int(segundainput[0])

    y1 = int(segundainput[1])

    x2 = int(segundainput[2])

    y2 = int(segundainput[3])
    tuneles.append(Tunel(x1, y1, x2, y2))

print("Coordenadas iniciales de la rana: ")
tercerainput = input().rstrip().split()
pos1 = int(tercerainput[0])
pos2 = int(tercerainput[1])
probabilidad = movimientos(pos1, pos2, tuneles, laberinto, n, m)
print(probabilidad)
