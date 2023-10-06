
class Empleado :
    cont=0
    
    def __init__(self,nombre,cargo,salario):
        Empleado.cont+=1
        self.__nombre=nombre        
        self.__cargo=cargo
        self.__salario=salario
        
    def setNombre(self,nombre):
        self.__nombre=nombre

    def getNombre(self):
        return self.__nombre
    
    def setCargo(self,cargo):
        self.__cargo=cargo

    def getCargo(self):
        return self.__cargo
    
    def setSalario(self,salario):
        self.__salario=salario
    
    def getSalario(self):
        return self.__salario
    
    def unaHora(self):
        mensual=self.__salario
        hora=mensual/160
        return hora
    
    def aumentoIpc(self):
        ipc=0.1312
        salario=self.__salario
        aumento=ipc*salario
        if salario<=1160000:
            ipc2=0.1612
            aumento=ipc2*salario      
        return aumento
    
    
    def horasExtras(self):
        z=1
        while z!=0:
            x=int(input('Cuantas horas extras hizo en el mes?: '))
            if x>40:
                print('No pudiste haber echo tantas horas extras')
                break  
            if x<=40:
                    hora=self.__salario/160
                    extras=hora*x
                    salarioTotal=self.__salario + extras
            
            return salarioTotal
        
print (Empleado.cont)        
    