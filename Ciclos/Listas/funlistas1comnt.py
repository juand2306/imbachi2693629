import random
def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]    
    return lista
#Esta funcion es para crear una lista con numeros aleatorios de un tamaño y rango definido 
#Los parametros de la funcion son 2 tam y rango 
#Esta funcion nos retorna la lista llenada 

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

#Esta funcion nos sirve para sacar la suma de los elementos de una lista
#El parametros de esta funcion es solo uno que es la lista a la cual le queremos hacer la suma 
#Esta funcion nos retorna la sum que es donde se almaceno la suma de los elementos 

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

#Esta funcion nos sirve para sacara el promedio de una lista 
#El parametro de estafuncion es uno que es la lista a la que se le va a sacar el promedio 
#Esta funcion en el retorno utiliza la funcion de la suma de la lista y lo divide or el amaño de esa misma lista 
    
l1=llenarLista(3,10)
#Asignamos que a la lista l1 se llene con la funcion de llenar lista, con tres datos, que seran numeros entre o y 10 
print(l1) 
#Imprimimos esa lista
print(sumaLista(l1))
#Imprimimos la suma de la lista l1 
print(round(promedioLista(l1),2))
#Imprimimos el promedio de la lista l1 pero que solo muestre dos decimales 
#Utilizamos la funcion round para mostrar la cantidad de decimales que queramos y al final asignamos esa cantidad despues de una coma(,)
