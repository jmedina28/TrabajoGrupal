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

primer = input().rstrip().split()
a = int(primer[0])
b = int(primer[1])
c = int(segundo[0])
d =
segundo =
tercero =
