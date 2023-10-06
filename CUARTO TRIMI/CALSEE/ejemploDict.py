def Diccionario(**kwargs):
    for key in kwargs.keys():
        print(key)

Diccionario(programa="adso", ficha=2693629,aprendices=16)

def valores(**kwargs):
    for key in kwargs.values():
        print(key)

def Keyvalores(**kwargs):
    for key,valoues in kwargs.items():
        print(key,valoues)

valores(programa="adso", ficha=2693629,aprendices=16)

Keyvalores(programa="adso", ficha=2693629,aprendices=16)
