# def validar(**kwargs):
#     for value in kwargs.values():
#         print(isinstance(value,int))
#         print(isinstance(value,float))
#         print(isinstance(value,float))


# validar(edad=15,peso=60.0, estatura=1.80)


def validar(**kwargs):
    for key, value in kwargs.items():
        if key =="edad":
            print(isinstance(value,int))
        if key =="peso":
            print(isinstance(value,float))    
        if key =="estatura":
            print(isinstance(value,float))

validar(edad=15,peso=60.0, estatura=1.80)



