
<h1 align="center">Trabajo Grupal</h1>

<h3 align="center">Perfiles de GitHub de los autores de este proyecto:</h3>

1. [@jmedina28](https://github.com/jmedina28)
2. [@estherrodriguezgarcia](https://github.com/ESTHERRODRIGUEZGARCIA)

---

En este repositorio se van a resolver una serie de ejercicios de forma cooperativa. El objetivo de esta tarea es conseguir devolver al usuario la probabilidad de que la rana Alef escape de un laberinto regido por unas condiciones determinadas. Para hacerlo más visual véase el ejemplo que se muestra a continuación:

<br>
<img height="300" src="https://github.com/jmedina28/AlefGame/blob/7eb789b263c356a8d679521a04959e7237b8237f/ejemplo.png" />
<br>

El diagrama de flujo empleado para resolver el ejercicio es el siguiente:

(Diagrama de flujo)
## Suma simple de una matriz
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
## Compara los problemas
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
## Una suma muy grande
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
## La escalera
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
