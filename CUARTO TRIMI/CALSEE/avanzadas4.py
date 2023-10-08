def base(funcion):                          #Esta es una funcion que recibe otra funcion como pametro 
                                            #y retorna otra funcion diferente
    def interna(n1,n2):
        print('Inicia la función base')
        #print(funcion(n1,n2))#*        
        #return funcion(n1,n2)
        funcion(n1,n2)
        print('Finaliza la función base')
    return interna

def suma(num1,num2):
    return num1+num2
                                            #Se definen dos funciones que usaremos como ejemplo
def resta(num1,num2):
    return num1-num2

var1=base(suma)
var2=base(resta)                            #Le asignamos la funcion base a una variable pasandole 
                                            #como parametro una de las funciones que construimos
#var1(10,15)#*
#var2(15,10)#*
print(var1(10,15))                          
print(var2(15,10))                          #Al imprimir la variable estaremos usando la funcion
                                            #interna que nos retorna base, por ende se ejecutara y debemos
                                            #pasarle los argumentos necesarios y se ejecutaran todas 
                                            #las funciones 