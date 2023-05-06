#[] {} () Estos son contenedores y se utilizan en las listas
x=100 #Declaramos la variable y le asignamos valor
print('tipo de x',type(x)) #Decimos que imprima la cadena y despues de la coma(,) indicamos que muestre el type osea el tipo de  texto de la variable x
lista=[1,1.4,'sena',['a','b',],'soacha'] #Creamos la variable lista que es una lista y en el contenedor ingresamos datos de todo tipo 
print(f'elemento {lista[4]}') #Inndicamos que imprima el elemento que esta en la posicion 4 osea el quinto elemento del contenedor ya que el primer elemento es cero(0) y el ultima es n-1
print(len(lista)) #La funcion len se utiliza para medir la longitud de una variable (cuantos datos hay en una variable)
print('tipo de lista',type(lista)) # 
print('ultimo indice',lista[-1])#Contamos de atras hacia adelante cuando el indicador es negativo 

print(len(lista))
lista.append(20) #La funcion append sirve para ingresar valores a una variable (este se ingresa en ultimo lugar)
lista.append('python')
print(lista) #Imprimimos los datos que hay en la variable lista 
lista.insert(len(lista),'java') #Insert es un mtodo que permite ingresar datos en la posicion indicada 
#En este caso ingresamos el dato de cadena 'java' en la posicion del numero generado por la cantidad de datos que tiene la variable lista
#Es inevitavbble que sea introducido al ultimo lugar pasando a ser el penultimo, ya que dezplaza el ultimo dato hacia la derecha 
print(lista)