def multiplos(x):
    for i in range(1, N+1):
        if i % 5 == 0:
            print(i)
    
N = int(input("Introduce un número entero : "))

lista=multiplos(N)