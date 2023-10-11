def validar_rango(func):
    def decorador(*args, **kwargs):
        lista = args[0]  # Suponemos que la lista es el primer argumento
        if all(0 <= num <= 100 for num in lista):
            return func(*args, **kwargs)
        else:
            return "Error: Algunos números están fuera del rango 0-100."

    return decorador

# @validar_rango
def suma(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum


@validar_rango
def promedio(lista):
    return sum(lista) / len(lista)

@validar_rango
def moda(lista):
    reps=0
    moda1=0
    for x in lista:
        repetido=0
        for v in lista:
            if x == v:
                repetido+=1
        if repetido>reps:
            reps=repetido
            moda1=x
    return moda1

@validar_rango
def mediana(lista):
    if len(lista)%2==0:
        mediana1= (lista[(len(lista) //2)- 1]+ lista[len(lista)//2])/2
    else:
        mediana1=lista[(len(lista)//2)]
    return mediana1

# @validar_rango
# def varianza(*args):


# lista_numeros = [25, 30, 40, 55, 75]
lista_numeros = [25, 30, 105, 55, 75] #con numeros fuera de rango 

# print("Suma:", suma(lista_numeros))
# print("Promedio:", promedio(lista_numeros))
# print("Moda:", moda(lista_numeros))
# print("Mediana:", mediana(lista_numeros))

xde=validar_rango(suma)
print(xde(lista_numeros))