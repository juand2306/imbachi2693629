def EsMultiplo(num1, num2):
    if num1 % num2 ==0 or num2 % num1 ==0:
        print (f"el numero {num1} es multiplo del numero {num2} ")
    else:
        print (f"el numero {num1} no es multiplo de {num2}")

num1=int(input("digite un numero:"))

num2=int(input("digite un segundo numero:"))

EsMultiplo(num1,num2)
