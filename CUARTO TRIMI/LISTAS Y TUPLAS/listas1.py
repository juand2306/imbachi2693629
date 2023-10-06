import random

def organizada():
    lista=[random.randrange(100) for i in range(11)]
    print(lista)

    for i in range(11):
        for j in range(i+1,11):
            if lista [i]>lista[j]:
                aux=lista[j]
                lista[j]=lista[i]
                lista[i] = aux

    print(lista)
organizada()