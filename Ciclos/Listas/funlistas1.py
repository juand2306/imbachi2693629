import random
def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]    
    return lista

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista(lista)/len(lista)
    
l1=llenarLista(3,10)
print(l1)
print(sumaLista(l1))
print(round(promedioLista(l1),2))
