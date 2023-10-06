n = int(input("Introduce el número de líneas: "))

for i in range(1, n+1): 
    for j in range(i): 
        print("* ", end="")
    print()
