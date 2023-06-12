from Library import *

class Book (Library):
    def __init__(self, Titulo:str , Autor:str , ISBN:str , Publicacion:str , Name:str):
        self.__titulo = [Titulo]
        self.__autor =  [Autor]
        self.__titulo_autor = {Titulo : Autor}
        self.__estado = "Disponible"
        self._informacion = {Titulo : [Autor, ISBN, Publicacion , self.__estado] }
        self.__titulo_estado = {Titulo:self.__estado}
        self.__titulo_comentario = {}
        self._obj_titulo = {Name : Titulo }
        Library.__init__(self , ISBN , Titulo)


    def setISBN (self, titulo, isbn):
        if titulo in self.__titulo:
            value_autor = list(self.__titulo_autor.keys())
            value_autor_index = value_autor.index(titulo)
            publicacion = input ("Digita la publicacion del nuevo ISBN: ")
            estado = "Disponible"
            del self._informacion[titulo]
            self._informacion.update({titulo : [self.__autor[value_autor_index] , isbn , publicacion , estado]})
            return self._informacion

    def Obj_Libro (self,Name:str, Libro:str):
        values = list(self._obj_titulo.values())
        for i in values:
            values = i
        del self._obj_titulo[Name]
        self._obj_titulo.update({Name : [values] + [Libro]})
        return self._obj_titulo

    def AgregarBook (self):
        titulo = input("Digita el nombre del libro: ")
        autor = input("Digita el autor del libro: ")
        isbn  = input("Digita el ISBN del libro: ")
        publicacion = input ("Digita la fecha de publicacion: ")
        estado = "Disponible"
        self.__titulo.append(titulo)
        self.__autor.append(autor)
        self.__titulo_autor.update({titulo: autor})
        self.__titulo_estado.update({titulo: estado})
        self._informacion.update ({titulo : [autor, isbn, publicacion , estado]})
        Library.agregarLibro (self, isbn , titulo)
    
    def duet (self , Titulo:str , SegAutor:str):
        values = list(self.__titulo_autor.values())
        keys = list (self.__titulo_autor.keys())
        if Titulo in keys:
            x=keys.index(Titulo)
            del self.__titulo_autor[Titulo]
            self.__titulo_autor.update ({Titulo : [values[x] , SegAutor]})
            return self.__titulo_autor

    def Reservation_Status (self , titulo:str):
        if titulo in self.__titulo:
            print (f"El libro {titulo} esta {self.__titulo_estado[titulo]}")

    def feedback (self , titulo:str):
        if titulo in self.__titulo:
            feed = input(f"Digta tu feedback sobre el libro {titulo}: ")
            self.__titulo_comentario.update ({titulo : feed})
            return self.__titulo_comentario
    
    def Book_request (self , Titulo:str, Estado:str):
        if Titulo in self.__titulo:
            del self.__titulo_estado[Titulo]
            self.__titulo_estado.update({Titulo : Estado})
            return self.__titulo_estado
    
    def renw_info (self , titulo:str):
        if titulo in self.__titulo:
            print (f"La informacion del libro {titulo} es: {self._informacion[titulo]}")