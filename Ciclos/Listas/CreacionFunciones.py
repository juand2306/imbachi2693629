#1.a. Funcion para llenar una lista con numeros aleatorios

import random

def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]    
    return lista

l1=llenarLista(10,10)
print("La lista es: ",l1)

#b. Funcion para sumar los elementos de una suma

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

print("La suma es: ",sumaLista(l1))

#c.Funcion para sacar el promedio de una lista 

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

print("El promedio es: ", round(promedioLista(l1),2))

#d. Funcion para mostrar el mayor de una lista 

def mayor(lista):
    max=0
    for i in lista:
        if i>max:
            max=i
    return max

print("El mayor es: ",mayor(l1))

#e. Funcion para mostrar el menor de una lista

def menor(lista):
    min=100000
    for i in lista:
        if i<min:
            min=i
    return min

print("El menor es: ",menor(l1))

#f. Funcion para ordenar de menor a mayor una lista 

def ascendente(lista, tam):
    for i in range(tam):
        for j in range(i+1,tam):
            if lista[i]>lista[j]:
                aux=lista[j]
                lista[j]=lista[i]
                lista[i]=aux
    return lista
lista=[]
lista=ascendente(l1,10)
print("Ascendente: ",ascendente(lista,10))

#g. Funcion para ordenar una lista de mayor a menor 

def descendente(lista, tam):
    for i in range(tam):
        for j in range(i+1,tam):
            if lista[i]<lista[j]:
                aux=lista[j]
                lista[j]=lista[i]
                lista[i]=aux
    return lista
lista=[]
lista=descendente(l1,10)
print("Descendente: ",descendente(lista,10))

#h. Funcion para sacar la moda de una lista

def moda(lista):
    reps=0
    moda1=0
    for x in lista:
        repetido=0
        for v in lista:
            if x == v:
                repetido+=1
        if repetido>reps:
            reps=repetido
            moda1=x
    return moda1

print("La moda es: ",moda(l1))

#i. Funcion para sacar la mediana de una lista 

def mediana(lista):
    if len(lista)%2==0:
        mediana1= (lista[(len(lista) //2)- 1]+ lista[len(lista)//2])/2
    else:
        mediana1=lista[(len(lista)//2)]
    return mediana1

print("La mediana es: ",mediana(l1))

#j. Funcion para encontrar un numero y señalar su posicion en una lista

#3. Funcion para llenar una lista con la serie de fibonacci

def fib(x):
    a=0
    b=1
    for y in range(x):
        c=a+b
        a = b 
        b =c   
    return b

num=int(input("Ingrese la cantidad de digitos: "))
lista1=[]

for z in range(num):
    lista1.append(fib(z))
    
print("Serie de Fibonacci: ",lista1)

#4. Funcion para llenar una lista de numeros aleatorios pero que no sean repetidos 

def noRepetidos(lista2,tam):
    lista2=[]
    contador=0
    for i in range(tam):
        while contador!=tam:
            num=int(random.randrange(20))
            if num not in lista2:
                lista2.append(num)
                contador=contador+1
            else:
                print(f"El numero {num} ya esta en la lista")
    return lista2

norp=[]
norp=noRepetidos(l1,10)
print("No repetidos",norp)

#

