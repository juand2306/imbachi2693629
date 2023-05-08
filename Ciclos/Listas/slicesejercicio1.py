"""Lenar una lista con un numero aleatorio (realies con un decimal) que representen calificaciones 
de un curso. Se evalua de 0 a 5 
El curso puede tener entre 20 y 30 aprendices 
HALLAR 

1. Genere listas nuevas para los aprobados y los reprobados  (se aprueba con 3)
2. Genere listas nuevas por cada unidad. Es decir los que sacan de 0 a 1 son un grupo, los de 1 a 2 otro, 
y asi sucesivamente
3. Diga cual es el promedio de los que aprueban y de los que reprueban por seprado."""

import random
tam=random.randint(20,30)
lista=[float(random.randrange(0,5)) for i in range (tam)]
posicion=[]

print("Hay", tam, "estudiantes en el salon")
print("Sus notas son: ",lista)

for i in range(tam):
    for j in range(i+1,tam):
        if lista[i]>lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux

print(lista)


for j in lista: 
    if j==3.0:
        posicion=(lista.index(j)) 
    if j==2.0:
        unidad1=(lista.index(j))

print("unidad1",unidad1)


print("El numero esta en las posiciones", posicion)

aprobados=lista[posicion:]
reprobados=lista[:posicion-1]
print("Aprobados", aprobados)
print("Reprobados",reprobados)


