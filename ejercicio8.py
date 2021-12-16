# Al introducir datos: 1ª línea: dos nº separados por espacios (distancia a b)
# 2ª: dos nº separados por espacios (distancia c d)
# 3ª: dos nº separados por espacios (distancia e f)
# 4ª: e nº separados por espacios (distancias a las que cada manzana cae desde el punto c)
# 5ª: f nº separados por espacios (distancias a las que cada naranja cae desde el punto d)
# me devuelve: 1er nº: manzanas que caen
# 2º nº: naranjas que caen
import re

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

primer = input("Introduzca dos números separados por espacios que serán la amplitud de la casa: ").rstrip().split()
segundo = input("Introduzca dos números separados por espacios que serán la distancia entre los dos árboles: )").rstrip().split()
tercero = input("Introduzca dos nº separados por espacios: ").rstrip().split()

a = int(primer[0])
b = int(primer[1])
c = int(segundo[0])
d = int(segundo[1])
e = int(tercero[0])
f = int(tercero[1])

manzanas = list(map(int(input("e nº separados por espacios (distancias a las que cada manzana cae desde el punto c)").rstrip().split())))
naranjas = list(map(int(input("f nº separados por espacios (distancias a las que cada naranja cae desde el punto d)").rstrip().split())))

contador =(a, b, c, d, naranjas, manzanas)

