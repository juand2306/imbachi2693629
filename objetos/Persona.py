
class Persona:
    def __init__(self,nombre,documento):
        #print('Se instancio un objeto')
        self.__nombre=nombre
        self.__documento=documento
        #self.__telefono
        self.__cursos=[]

    def setNombre(self,nombre):
        self.__nombre=nombre

    def getNombre(self):
        return self.__nombre
    
    def setDocumento(self,documento):
        self.__documento=documento

    def getDocumento(self):
        return self.__documento
    
    def ingresarCurso (self, curso):
        if curso not in self.__cursos:
            self.__cursos.append(curso)
            return self.__cursos
        
    def consultarCurso (self):
        print (self.__cursos)
    
    def modificarCurso (self,nombremod, cambio):
        for i in self.__cursos:
            

        
    


    

