import random #Se importa la libreria random
lista=[] #Creamos la lista 'lista' y la dejamos vacia  
tam=int(random.randint(10,20)) #Asignamos para la variable tam que sea un numero entrero aleatorio entre 10 y 20
#el metodo de la libreria random.randint sirve para darle un rango donde se generara el numero random necesitando un numero de inicio y un numero de fin o limite (x,y) 
print(tam) #Mostramos el numero aleatorio que se genero que esta almavcenado en la variable tam 
for i in range(tam): #Indicamos que para la variable i en el rango de 0 hasta el numero aleatorio que se genro haga...
#Esto hace que se le de una longitud a la lista 
    num=int(random.randrange(100)) #Indicamos quepara la variable num se genere un numero entero aleatorio entre 0 y 100 
#El metodo random.randrange sirve para poner un limite dende se genere el numero sin necesidad de indicar el inicio ya que predeterminadamente se inicia desde 0
    lista.append(num) #Esta parte lo que hara es llenar la variable lista con los numeros aleatorios generados en la variable num 
#Se ingresaran la cantidad de numeros qie permita la variable tam, que es la encargada de generar la longitud de la lista

print(lista) #Imprimimos los datos contenidos en la lista que son los numeros aleatorios generados 