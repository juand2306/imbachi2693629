import random

tam=random.randrange(15,125)
#while not tam%5==0:
    #tam=[random.randrange(15,125)]

def llenarLista(lista):
    lista=[float(random.randrange(1.50,2.00)) for i in range(tam)]    
    return lista

lista1=[]
llenarLista(lista1)

print(lista1)

