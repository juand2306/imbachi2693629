num1,num2=100,25
#Declaramos variables y les asignamos un valor
print('1-sumar')
print('2-restar')
print('3-multiplicar')
print('4-dividir')
#Mostramos por pantalla un mensaje de un menu 
selector=(input('Digite la opcion'))
#Indicamos que escriba el numero de una opcion 
match selector:
    case '1':
        print(num1+num2)
    case '2':
        print(num1-num2)
    case '3':
        print(num1*num2)
    case '4':
        print(num1/num2)
        #Mostramos el proceso que debe hacer en base al numero escrito basado al menu mostrado
        #Debe mostrar por pantalla el resultado de la opcion y el resultado de la operacion 