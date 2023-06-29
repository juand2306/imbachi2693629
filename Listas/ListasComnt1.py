#[] {} () Estas son contenedores y se utilizan en las listas 
x=100 #Declaramos variable y asignamos valor 
print('tipo de x',type(x)) #Decimos que imprima la cadena y despues de la coma(,) indicamos que muestre el "type" tipo variable de la variable x
lista=[1,1.4,'sena',['a','b',],'soacha'] #Creamos la variable lista con contenedores y lo llenamos con diferentes tipos de variables y una sublista
print(f'elemento {lista[4]}') #Le indicamos que imprima el elemento ubicado en la posicion 4 de la variable listas

#Dentro de los contenedores existen posiciones donde el primer dato es cero(0), el segundo uno(1), el tercero dos(2) y asi consecutivamente hasta el ultimo 
#Para contar de atras hacia adelante se utilizan los negativos 

print(len(lista)) #La funcion len se utiliza para medir la longitus de una variable (cuenta cuantos datos hay en una variable)
print('tipo de lista',type(lista))#Imprimimos el tipo de variable que tiene lista
print('ultimo indice',lista[-1]) #Contamos de atras hacia adelante mostrando el segundo dato de atras para adelante 
print(len(lista))#Imprimimos el numero de dos que tiene la variable lista
lista.append(20) #append es un metodo que permite insertar un dato o varios a una varible de la forma que se muestra 
#En este caso este metodo (append) nos permite ingresar el dato (20) a la variable lista y se introduce en la ultima posicion 
lista.append('python') #Ingresamos el datos ('python') a la variable lista 
print(lista) #Mostramos los datos que contiene la variable lista 
lista.insert(len(lista),'java')#insert es un metodo que permite ingresar un dato en la posicion qu se indique antes de la coma(,) 
#En este caso decimos que ingrese el dato ('java') en la posicion del numero genrado por la ccantidad de datos que hayan en lista 
#Este codigo inevitablemente pondra el dato ingresado en penultimo lugar ya que desplaza el ultimo dato a la derecha
print(lista)#Imprimimos todos los datos contenidos en la variable lista 