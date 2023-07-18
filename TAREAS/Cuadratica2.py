def calcular_funcion_cuadratica(a, b, c):
    assert isinstance(a, (int, float)), "El coeficiente 'a' debe ser un número."
    assert isinstance(b, (int, float)), "El coeficiente 'b' debe ser un número."
    assert isinstance(c, (int, float)), "El coeficiente 'c' debe ser un número."
    
    discriminante = b**2 - 4*a*c
    
    assert discriminante >= 0, "El discriminante es negativo, no se obtendran resultados reales ."
    
    x1 = (-b + discriminante**0.5) / (2*a)
    x2 = (-b - discriminante**0.5) / (2*a)
    
    return x1, x2

a = float(input("Ingresa el coeficiente a: "))
b = float(input("Ingresa el coeficiente b: "))
c = float(input("Ingresa el coeficiente c: "))

try:
    soluciones = calcular_funcion_cuadratica(a, b, c)
    print("Las soluciones son:", soluciones)
except AssertionError as error:
    print("Error:", str(error))