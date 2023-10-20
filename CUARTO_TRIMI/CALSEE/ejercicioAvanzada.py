import random

def llenarL(tam):
    lista=[random.randrange(0,20) for i in range(tam)]    
    return lista

def sumarElementos(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def mayorLi(lista):
    max=0
    for i in lista:
        if i>max:
            max=i
    return max

def menorLi(lista):
    min=100000
    for i in lista:
        if i<min:
            min=i
    return min

def operacion (funcion, listaoTam):
    print(funcion(listaoTam))
   
l2=llenarL(10)
print(f'Lista Predeterminada: {l2}')
    
operacion(sumarElementos,l2)
