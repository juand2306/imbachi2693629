def base(funcion):                              #Esta es una funcion que recibe otra funcion como pametro 
                                                #y retorna otra funcion diferente
    def interna():
        print('Inicia la función base')
        funcion()    
        print('Finaliza la función base')
    return interna

def integrada():
    print('Funcion Integrada')
                                                #Se definen dos funciones que usaremos como ejemplo
def otraFuncion():
    print('Otra Funcion')                   

var1=base(integrada)                        #Utilizamos la funcion base que pide como parametro una funcion
                                            #aqui se "ejecutan" tres funciones en un llamado; por una parte 
                                            #la funcion base que ejecuta la funcion interna y esta a su vez
                                            #ejecuta la funcion que se le fue pasada como argumento(integrada)
var2=base(otraFuncion)
var1()
var2()


# def integrada(parametro):
#     print(f'{parametro} de la funcion Integrada')