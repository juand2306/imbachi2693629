i=1
sum=0
#Declaramos las variables
while i<=10:
    #Indicamos que el ciclo se repita mientras que la variable no sea menor o igual a 10
    print(i)
    sum+=i #sum=sum+i
    i+=1 #i=i+1
    #Realizamos un contador que aumenta de 1 en 1 
print('la suma es:',sum)
#Mostramos por pantalla lo almacenado en la variable sum

i=0
sp,si=0,0
#Definimos variables
while i<=10:
     #Indicamos que el ciclo se repita mientras que la variable no sea menor o igual a 10
    print(i)
    if i%2==0:
        sp+=i
        #Indicamos que si los numeros de la variable i modulo son igual a 0 los sum en la variable sp
    else:
        si+=i
        #Si la anterior condicion no se cumple sume los numeros a la variable si
    i+=1
print('la suma de los pares es:',sp)
print('la suma de los impares es:',si)
#Mostramos los resultados almacenados en ambas variables 