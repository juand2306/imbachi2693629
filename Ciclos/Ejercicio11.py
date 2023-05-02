num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 < num2:
    num1, num2 = num2, num1 

cociente = 0
residuo = num1

while residuo >= num2:
    residuo -= num2
    cociente += 1

print("El cociente es:", cociente)
print("El residuo es:", residuo)
