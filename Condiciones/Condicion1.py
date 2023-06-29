x=input('ingrese numero')
y=input('ingrese numero')
#Declaramos variables y enseñamos un mensaje por patalla
if x==y:
    print('son iguales')
    #Indicacamos que si las dos variables son iguales, mande este mensaje por pantalla
elif x>y:
    print('descendente')
    #Si no se cumple la condicion anterior y la primera variable tiene un numero almacenado mayor que el de la segunda, muestre que esta de forma descendente
else:
    print('ascendente')
    #Si no se cumple ninguna condicion anterior, que muestre por pantalla que estan de forma ascendente