import random

tam=random.randint(5,20)
lista=[random.randrange(0,9) for i in range (tam)]
rebanada1=lista[len(lista)//2:len(lista)] #Toma o incue el ultimo valor
rebanada2=lista[len(lista)//2:-1] #No incluye el ultimo valor 
rebanada3=lista[len(lista)//2:] #Incluye el ultimo valor 


print(lista)
print(rebanada1)
print(rebanada2)
print(rebanada3)

