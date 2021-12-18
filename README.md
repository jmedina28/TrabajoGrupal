
<h1 align="center">Trabajo Grupal</h1>

<h3 align="center">Perfiles de GitHub de los autores de este proyecto:</h3>

1. [@jmedina28](https://github.com/jmedina28)
2. [@estherrodriguezgarcia](https://github.com/ESTHERRODRIGUEZGARCIA)

---

En este [repositorio](https://github.com/jmedina28/TrabajoGrupal) se van a resolver una serie de ejercicios de forma cooperativa. 

## 1. Suma simple de una matriz
El código empleado para resolver el ejercicio 1 es el siguiente:


```python
# Importamos librerías.

import os

os.environ["OUTPUT_PATH"] = ""

def suma_matriz(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i]
    return suma

if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"] + "solucion1.txt", "w")
    contar_matriz = int(input("Introduzca las dimensiones de la matriz: "))
    matriz = list(map(int, input("Introduzca los valores de la matriz separados por espacios: ").rstrip().split()))
    result = suma_matriz(matriz)
    fptr.write(str(result) + "\n")
    fptr.close()
  ```
## 2. Compara los problemas
El código empleado para resolver el ejercicio 2 es el siguiente:
```python
# Importamos las librerías necesarias para la realización del ejercicio.
import os

os.environ["Salida"] = ""
# Creo la función en la que se va a desarrollar el ejercicio.
def comparalosproblemas(a, b):
    # Defino las variables con los nombres de los jugadores.
    lucia = 0
    carlos = 0
    # Creo el bucle que va a completar los datos de las variables.
    for n in range(3):
        if a[n] > b[n]:
            lucia += 1
        elif a[n] < b[n]:
            carlos += 1
    return (lucia, carlos)


# Aquí ejecuto el código y muestro la salida en un fichero de texto creado cuando se ejecute.
if __name__ == "__main__":
    fptr = open(os.environ["Salida"] + "solucion2.txt", "w")

    a = list(map(int, input("Introduzca las notas de Lucía:\n").rstrip().split()))

    b = list(map(int, input("Introduzca las notas de Carlos:\n").rstrip().split()))

    resultado = comparalosproblemas(a, b)

    fptr.write(" ".join(map(str, resultado)))
    fptr.write("\n")

    fptr.close()
```
## 3. Una suma muy grande
El código empleado para resolver el ejercicio 3 es el siguiente:
```python
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
 ```
## 4. La escalera
El código empleado para resolver el ejercicio 4 es el siguiente:
```python
def escalera(n):
    for i in range(0, n):
        fila = ""
        for k in range(0, n-1-i):
            fila = fila + " "
        for j in range(0, i+1):
            fila = fila + "# "
        print(fila)


n = int(input("Introduzca el tamaño de la escalera: ").strip())

escalera(n)
        
  ```
 Salida: 

<br>
<img height="300" src="https://github.com/jmedina28/TrabajoGrupal/blob/d0f7c7cce56083c7933ecba37add1881f703c33e/escalera.PNG" />
<br>

## 5. Juego de piedras
El código empleado para resolver el ejercicio 5 es el siguiente:
```python
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


  ```
## 6. Rana en laberinto
El objetivo de esta tarea es conseguir devolver al usuario la probabilidad de que la rana Alef escape de un laberinto regido por unas condiciones determinadas. Para hacerlo más visual véase el ejemplo que se muestra a continuación:

<br>
<img height="300" src="https://github.com/jmedina28/AlefGame/blob/7eb789b263c356a8d679521a04959e7237b8237f/ejemplo.png" />
<br>
El código que resuelve dicha tarea es el siguiente: 

```python
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
 ```
## 7. Estudiantes de calificación
Representación gráfica de lo que se va a llevar a cabo:
  
 <br>
<img height="300" src="https://github.com/jmedina28/TrabajoGrupal/blob/d0f7c7cce56083c7933ecba37add1881f703c33e/notas.PNG" />
<br>
El código empleado para resolver el ejercicio 7 es el siguiente:

```python
import os

os.environ["OUTPUT_PATH"] = "solución7.txt"


def notasEstudiantes(notas):
    lista = []
    for i in notas:
        lista.append(notafinal(i))
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
  ```
  ## 8. Manzana y naranja
  Representación gráfica de lo que se va a llevar a cabo:
  
  <br>
<img height="250" src="https://github.com/jmedina28/TrabajoGrupal/blob/d0f7c7cce56083c7933ecba37add1881f703c33e/manzanaynaranja.PNG" />
<br>
  
  El código empleado para resolver el ejercicio 8 es el siguiente:
```python
  # Al introducir datos: 1ª línea: dos nº separados por espacios (distancia a b)
# 2ª: dos nº separados por espacios (distancia c d)
# 3ª: dos nº separados por espacios (distancia e f)
# 4ª: e nº separados por espacios (distancias a las que cada manzana cae desde el punto c)
# 5ª: f nº separados por espacios (distancias a las que cada naranja cae desde el punto d)
# me devuelve: 1er nº: manzanas que caen
# 2º nº: naranjas que caen


def contador(a, b, c, d, manzanas, naranjas):
    num_manzanas_dentro = 0
    num_naranjas_dentro = 0
    for manzana1 in manzanas:
        if c + manzana1 >= a and c <= b:
            num_manzanas_dentro += 1
    for naranja1 in naranjas:
        if d + naranja1 >= a and d <= b:
            num_naranjas_dentro += 1

    print("Han entrado ", str(num_manzanas_dentro), " manzanas")
    print("Han entrado ", str(num_naranjas_dentro), " naranjas")


primer = (
    input(
        "Introduzca dos números separados por espacios que serán la amplitud de la casa: "
    )
    .rstrip()
    .split()
)
segundo = (
    input(
        "Introduzca dos números separados por espacios que serán la distancia entre los dos árboles: "
    )
    .rstrip()
    .split()
)
tercero = input("Introduzca dos nº separados por espacios: ").rstrip().split()

a = int(primer[0])
b = int(primer[1])
c = int(segundo[0])
d = int(segundo[1])
e = int(tercero[0])
f = int(tercero[1])

print(
    " nº separados por espacios (distancias a las que cada manzana cae desde el punto c)",
)
manzanas = list(map(int, input().rstrip().split()))
print(
    " nº separados por espacios (distancias a las que cada naranja cae desde el punto d)",
)
naranjas = list(map(int, input().rstrip().split()))

contador(a, b, c, d, naranjas, manzanas)
