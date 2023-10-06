#Escriba un programa que imprima la suma y el promedio de  una serie de numeros independientes

def SumProm(*args):
    suma=0
    for i in args:
        suma+=i
    
    promedio=suma/(len(args))

    return suma, promedio

print("Suma   Promedio")
print(SumProm(10,52,114,15,17,1,8,16,2))
