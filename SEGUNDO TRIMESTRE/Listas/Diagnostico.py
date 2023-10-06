#Llenar dos arreglos con la funcion random

import random

def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]    
    return lista

lista1=llenarLista(10,20)
print("La lista 1 es: ",lista1)

lista2=llenarLista(10,20)
print("La lista 2 es: ",lista2)

#a. Cual de los dos tiene la suma mas alta 

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

#suma1=sumaLista(lista1)
#print("La suma de la lista 1 es: ",suma1)

#suma2=sumaLista(lista2)
#print("La suma de la lista 2 es: ",suma2)

#if suma1>suma2:
    #print("La primera lista tiene la suma mas alta")
#elif suma1==suma2:
    #print("Son iguales")
#else:
   #print("La segunda lista tiene la suma mas alta")
    
#b. Cual de los dos tiene el numero mayor 

def mayor(lista):
    max=0
    for i in lista:
        if i>max:
            max=i
    return max

#mayor1=mayor(lista1)
#print("El mayor de la primera lista es: ",mayor1)

#mayor2=mayor(lista2)
#print("El mayor de la segunda lista es: ",mayor2)

#if mayor1>mayor2:
    #print("La primera lista tiene el numero mayor")
#elif mayor1==mayor2:
    #print("Son iguales")
#else:
    #print("La segunda lista tiene el numero mayor")

#c. Cual de los dos tiene el numero menor 

def menor(lista):
    min=100000
    for i in lista:
        if i<min:
            min=i
    return min

#menor1=menor(lista1)
#print("El menor de la primera lista es: ",menor1)

#menor2=menor(lista2)
#print("El menor de la segunda lista es: ",menor2)

#if menor1<menor2:
    #print("La primera lista tiene el numero menor")
#elif menor1==menor2:
    #print("Son iguales")
#else:
    #print("La segunda lista tiene el numero menor")

#d. Promedio conjunto 

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

promedio1=promedioLista(lista1)
#print("El promedio de la primera lista es: ",promedio1)

promedio2=promedioLista(lista2)
#print("El promedio de la segunda lista es: ",promedio2)

sumaConjunta=promedio1+promedio2
promedioConjunto=sumaConjunta/2
#print("El promedio conjunto de las listas es: ",promedioConjunto)

#e. Decir si el promedio de cada uno esta por encima o por debajo del promedio conjunto

#if promedio1>promedioConjunto:
    #print("El promedio de la primera lista esta por encima del arreglo conjunto")
#elif promedio1==promedioConjunto:
    #print("El promedio de la primera lista es igual al arreglo conjunto")
#else:
    #print("El promedio de la primera lista esta por debajo del arreglo conjunto")

#if promedio2>promedioConjunto:
    #print("El promedio de la segunda lista esta por encima del arreglo conjunto")
#elif promedio2==promedioConjunto:
    #print("El promedio de la segunda lista es igual al arreglo conjunto")
#else:
    #print("El promedio de la segunda lista esta por debajo del arreglo conjunto")

#f. Cual de los dos tiene mayor cantidad de pares

def pares(lista):
    pares=0
    impares=0
    for i in lista:
        if i%2==0:
            pares=pares+1
        else:
            impares=impares+1
    return pares

pares1=pares(lista1)
#print("Hay",pares1, "pares en la primera lista ")

pares2=pares(lista2)
#print("Hay",pares2, "pares en la segunda lista ")

#if pares1>pares2:
    #print("La primera lista tiene mayor cantidad de pares")
#elif pares1==pares2:
    #print("Tienen la misma  cantidad de pares")
#else:
    #print("La segunda lista tiene mayor cantidad de pares")

#g. Cual de los dos tiene mayor cantidad de impares

def impares(lista):
    pares=0
    impares=0
    for i in lista:
        if i%2==0:
            pares=pares+1
        else:
            impares=impares+1
    return impares

impares1=impares(lista1)
#print("Hay",impares1, "impares en la primera lista ")

impares2=impares(lista2)
#print("Hay",impares2, "impares en la segunda lista ")

#if impares1>impares2:
    #print("La primera lista tiene mayor cantidad de impares")
#elif impares1==impares2:
    #print("Tienen la misma  cantidad de impares")
#else:
    #print("La segunda lista tiene mayor cantidad de impares")

#Creamos el menu 



print('1-Cual de los dos tiene la suma mas alta')
print('2-Cual de los dos tiene el numero mayor')
print('3-Cual de los dos tiene el numero menor')
print('4-Cual es el promedio conjunto ')
print('5-Sacar el promedio de cada uno y decir si esta por encima o por debajo del arreglo conjunto ')
print('6-Cual de los dos tiene mayor cantidad de pares ')
print('7-Cual de los dos tiene mayor cantidad de impares ')
selector=1
while selector!=0:
    selector=(input('Digite la opcion'))
    match selector:
        case '1':
            suma1=sumaLista(lista1)
            print("La suma de la lista 1 es: ",suma1)

            suma2=sumaLista(lista2)
            print("La suma de la lista 2 es: ",suma2)

            if suma1>suma2:
                print("La primera lista tiene la suma mas alta")
            elif suma1==suma2:
                print("Son iguales")
            else:
                print("La segunda lista tiene la suma mas alta")
        case '2':
            mayor1=mayor(lista1)
            print("El mayor de la primera lista es: ",mayor1)

            mayor2=mayor(lista2)
            print("El mayor de la segunda lista es: ",mayor2)

            if mayor1>mayor2:
                print("La primera lista tiene el numero mayor")
            elif mayor1==mayor2:
                print("Son iguales")
            else:
                print("La segunda lista tiene el numero mayor")
        case '3':
            menor1=menor(lista1)
            print("El menor de la primera lista es: ",menor1)

            menor2=menor(lista2)
            print("El menor de la segunda lista es: ",menor2)

            if menor1<menor2:
                print("La primera lista tiene el numero menor")
            elif menor1==menor2:
                print("Son iguales")
            else:
                print("La segunda lista tiene el numero menor")
        case '4':
            promedio1=promedioLista(lista1)
            print("El promedio de la primera lista es: ",promedio1)

            promedio2=promedioLista(lista2)
            print("El promedio de la segunda lista es: ",promedio2)

            sumaConjunta=promedio1+promedio2
            promedioConjunto=sumaConjunta/2
            print("El promedio conjunto de las listas es: ",promedioConjunto)
        case '5':
            if promedio1>promedioConjunto:
                print("El promedio de la primera lista esta por encima del arreglo conjunto")
            elif promedio1==promedioConjunto:
                print("El promedio de la primera lista es igual al arreglo conjunto")
            else:
                print("El promedio de la primera lista esta por debajo del arreglo conjunto")

            if promedio2>promedioConjunto:
                print("El promedio de la segunda lista esta por encima del arreglo conjunto")
            elif promedio2==promedioConjunto:
                print("El promedio de la segunda lista es igual al arreglo conjunto")
            else:
                print("El promedio de la segunda lista esta por debajo del arreglo conjunto")
        case '6':
            pares1=pares(lista1)
            print("Hay",pares1, "pares en la primera lista ")

            pares2=pares(lista2)
            print("Hay",pares2, "pares en la segunda lista ")

            if pares1>pares2:
                print("La primera lista tiene mayor cantidad de pares")
            elif pares1==pares2:
                print("Tienen la misma  cantidad de pares")
            else:
                print("La segunda lista tiene mayor cantidad de pares")
        case '7':
            impares1=impares(lista1)
            print("Hay",impares1, "impares en la primera lista ")

            impares2=impares(lista2)
            print("Hay",impares2, "impares en la segunda lista ")

            if impares1>impares2:
                print("La primera lista tiene mayor cantidad de impares")
            elif impares1==impares2:
                print("Tienen la misma  cantidad de impares")
            else:

                print("La segunda lista tiene mayor cantidad de impares")
        case '0':
            break
