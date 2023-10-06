
def productos(*args,**kwargs):

    for key,val in kwargs.items():
        print(f'{key} : {val}')

    # for desc in kwargs.items():
    #     if key=='descuento':
    #         for desc in kwargs.values():
    #             x=args/100
    #             d=x*desc
    #             total=d-desc
    
    # print(total)


productos(10,nombre='jabon rey',precio=2.500)
