print("Ingrese dos numeros diferentes")
x=int(input("Ingrese el primer numero:"))
y=int(input("Ingrese el segundo numero:"))
resta=0
if x==y:
    print("Debe ingresar numeros diferentes")
    x=int(input("Ingrese el primer numero:"))
    y=int(input("Ingrese el segundo numero:"))
    
if x>y:
    resta=x-y
    print(resta)
    while resta>y:
        resta=resta-y
        print(resta)

if y>x:
    resta=y-x
    print(resta)
    while resta>x:
        resta=resta-x
        print(resta)