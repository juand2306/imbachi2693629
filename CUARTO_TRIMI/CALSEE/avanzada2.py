def base(x):                    #Esta es una funcion que retorna otra funcion que fue 
    def interior(y):            #construida dentro de la misma
        return x+y
    return interior


def base(x):
    def suma(y):
        return x+y
    def resta(y):
        return x-y
    return[suma,resta]          #Esta funcion retorna una lista de funciones que fueron contruidas 
                                #dentro de la misma 

usoFuncion=base(10)             #Primero se asugna la funcion a una variable para poder usar las 
                                #funciones que retorna
                                
print(usoFuncion[0](20))        #Se esta imprimiendo la variable ya que asi se utilizan las funciones 
                                #que estan adentro y pasamos valores para la posicion en la lista de 
                                #la funcion que queremos utiliz<ar y el argumento que solicita el parametro
                                # de la funcion de adentro
