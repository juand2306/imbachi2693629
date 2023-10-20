def calcularMaxMin (lista):
    max=0
    min=10000
    for i in lista:
        if i>max:
            max=i
        if i<min:
            min=i
    print(f"El numero mas grande es {max}")
    print(f"El numero mas pequeño es {min}")


l1=[]
while True:
    n=int(input("ingrese numeros los que desee o ingrese 0 para salir:"))
    if n == 0:
        break
    l1.append(n)

calcularMaxMin(l1)
