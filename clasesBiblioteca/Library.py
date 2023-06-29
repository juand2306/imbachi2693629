class Library :
    def __init__(self, id, titulo):
        self.__id = id
        self.__titulo = [titulo]

    def setTitulo (self, titulo):
        if titulo in self.__titulo:
            x = input("Digita el nuevo titulo: ")
            indexs = self.__titulo.index(titulo)
            self.__titulo [indexs] = x

    def getTitulo (self):
        return self.__titulo
    
    def agregarLibro (self,isbn,titulo):
        self.__titulo.append (titulo)