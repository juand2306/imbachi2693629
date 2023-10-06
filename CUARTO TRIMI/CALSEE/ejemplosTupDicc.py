def funcion(*args,**kwargs):
    for elementos in args:
        print(elementos)

    for key,val in kwargs.items():
        print(f'{key}:{val}')

funcion(1,2,3,4, fecha=6-10-2023, hora="7:35 am")

