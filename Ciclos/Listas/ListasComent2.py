import random #Se importa la libreria random
lista=[] #Creamos una lista llamada lista y la dejamos vacia 
tam=int(random.randint(10,20)) #Asignamos para la bariabale tam un numero entero generado aleatoriamente entre 10 y 20 
print(tam)
for i in range(tam):  #Indicamos que para i en el rango de 0 al numero aleatorio generado en la variabale tam 
    num=int(random.randrange(100)) #Indicamos que para la variable num s genere un numero entero aleatoorio de 0 a 100 
    lista.append(num) #Esta parte lo que hace es llenar los campos de la variable lista con los numeros aleatorios generados 
print(lista)  #Mostramos los datos conenidos en la variable lista 

