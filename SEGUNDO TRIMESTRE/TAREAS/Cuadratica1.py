def calcular_funcion_cuadratica(a, b, c):
    try:
        discriminante = b**2 - 4*a*c
        
        if discriminante < 0:
            raise ValueError("El discriminante es negativo, se se obtendran soluciones reales .")
        
        x1 = (-b + discriminante**0.5) / (2*a)
        x2 = (-b - discriminante**0.5) / (2*a)
        
        return x1, x2
    
    except ValueError as error:
        print("Error:", str(error))


# Ejemplo de uso
a = float(input("Ingresa el coeficiente a: "))
b = float(input("Ingresa el coeficiente b: "))
c = float(input("Ingresa el coeficiente c: "))

soluciones = calcular_funcion_cuadratica(a, b, c)
if soluciones:
    print("Las soluciones son:", soluciones)