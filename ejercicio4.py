def escalera(n):
    for i in range(0, n):
        fila = ""
        for k in range(0, n-1-i):
            fila = fila + " "
        for j in range(0, i+1):
            fila = fila + "# "
        print(fila)

if __name__ == "__main__":
    n = int(input("Introduzca el tamaño de la escalera: ").strip())

    escalera(n)
        
