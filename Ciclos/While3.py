num=1
cont=0
suma=0
promedio=0
menor=1000000000
mayor=0
while num!=0:
    num=int(input('ingrese numero'))
    cont=cont+1 #cont+=1
    suma=suma+num
    if num>mayor:
        mayor=num
    if num<menor and num!=0:
        menor=num

print(f'El usuario ingreso {cont-1} numeros') #print('El usuario ingreso', cont, 'numeros')
print("El resultado de la suma de los numeros es:",suma)
print(f"El promedio es: {suma/(cont-1)}")
print("El mayor es:", mayor)
print("El menor es:", menor)
