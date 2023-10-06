#ingrese un numero por teclado 
z=0
z= int(input("ingrese un numero por teclado:",))
y=[]
contador=0
suma=0

for i in range (1, z+1):
    if z % i == 0:
        y.append(i)
        contador=contador+1
if contador<=2:
    print("Es primo")
else:
    print("No es primo")
    
print("Los divisores del numero", z, "Son: ", y)
print(contador)