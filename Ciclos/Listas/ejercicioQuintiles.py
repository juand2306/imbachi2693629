import random

def llenarlista(tamaño,rango):
    tam=random.randint(15,tamaño)
    while tam&5!=1:
        tam=random.randint(15,tamaño)
        if tam%5==0:
            lista=[round(random.uniform(1.50,rango),2)for i in range(tam)]
            return lista

l1=llenarlista(125,2.00)
print("La lista es: ",l1)
print("Hay",len(l1),"Datos")
salto=len(l1)/5
print("Los quintiles son de: ",salto)

quintil=0
while not quintil==len(l1):
    q1=quintil+salto
    print("El primer quintil va de ",quintil+1, "Hasta ",q1)
    q2=q1+salto
    print("El segundo quintil va de ",q1+1, "Hasta ",q2)
    q3=q2+salto
    print("El tercer quintil va de ",q2+1, "Hasta ",q3)
    q4=q3+salto
    print("El cuarto quintil va de ",q3+1, "Hasta ",q4)
    q5=q4+salto
    print("El quinto quintil va de ",q4+1, "Hasta ",q5)
    quintil==q5
    break