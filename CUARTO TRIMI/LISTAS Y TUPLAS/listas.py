def Notas():
    l1=[]
    max=0
    min=100000
    sum=0

    n1=float(input("Ingrese la primera nota:"))
    l1.append(n1)
    n2=float(input("Ingrese la segunda nota:"))
    l1.append(n2)
    n3=float(input("Ingrese la tercera nota:"))
    l1.append(n3)
    n4=float(input("Ingrese la cuarta nota:"))
    l1.append(n4)
    n5=float(input("Ingrese la quinta nota:"))
    l1.append(n5)
    
    for i in l1:
        if i>max:
            max=i
    for i in l1:
        if i<min:
            min=1
    for x in l1:
        sum+=x
    Notamedia=sum/len(l1)

    
    
    print(min)
    print(max)
    print(sum)
    print(Notamedia)
    print(l1)

Notas()
