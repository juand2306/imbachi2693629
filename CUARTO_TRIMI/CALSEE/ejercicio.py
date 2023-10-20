#edad estatura y peso 

edad=int(input("Ingresa tu edad: "))
peso=float(input("Ingresa el peso: "))
estatura=float(input("Ingresa la estatura: "))

def Persona(**kwargs):
    for key in kwargs.values():
        if key==int or float:
            print("Es el dato esperado")
        else:
            print("No es el dato solicitado")

Persona(edad=edad,peso=peso, estatura=estatura)

def validar(**kwargs):
    for value in kwargs.values():
        print(isinstance(value,int))
        print(isinstance(value,float))
        print(isinstance(value,float))


validar(edad=15,peso=60.0, estatura=1.80)
# validar(edad="siete",peso="39", estatura="1.80")
# validar(edad="15",peso=16.0, estatura=1.80)