#sumar, promedio, max,min, moda,mediana y desviacion
import random


lista=[]
resta=[]
elevado=[]
suma=0
suma1=0
promedio=0
max=0
min=10000
tam=int(random.randint(10,20))
print("El tamaño de la lista es: ",tam)
for i in range (tam):
    num=int(random.randrange(100))
    lista.append(num)
    suma+=num
    promedio=suma/tam
    if num>max:
        max=num
    if num<min and num!=0:
        min=num

ind= 0
for num in lista:
    cont = 0
    for f in lista:
        if num == f:
            cont +=1
    if cont > ind:
        ind= cont 
        moda =num
        
for i in range(tam):
    for j in range(i+1,tam):
        if lista[i]>lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux
            
if len(lista)%2==0:
    mediana= (lista[(len(lista) //2)- 1]+ lista[len(lista)//2])/2
else:
    mediana=lista[(len(lista)//2)]

for i in lista:
    y=((i-promedio))
    resta.append(y)
    for j in resta:
        y=((j**2))
        elevado.append(y)
    for y in elevado:
        suma1+=y
    divi=(suma1/tam-1)
    
    ds=divi**0.5

    

print("La lista es: ",lista)

print("La suma de los datos es: ",suma)
print("El promedio de los numeros es: ",promedio)
print("El numero mas grande es: ", max)
print("El numero mas pequeño es: ", min)
print ("La moda es: ", moda )
print("La mediana es: ",mediana)
print("La desviacion estandar es: ",ds)

