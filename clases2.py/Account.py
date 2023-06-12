from sys import path

path.append("..\\sabogal2693629")

from Book import *
from Account import *

class Account:
    def __init__(self, Name:str, ID:int):
        self.__name = Name
        self.__id = ID
        self.__reservado = []
        self.__devuelto = []
        self.__perdido = []
        self.__libros = []
        self.__multa = 0
        self._obj_titulo = {Name : []}
        Book.__init__ (self,"La llorona" , "Harold" , 102866 , "10/25/2014" , Name)


    def LibroReservado (self ,Name:str , Titulo:str):
        self.__reservado.append(Titulo)
        self.__libros.append (Titulo)
        del self._obj_titulo[Name]
        self._obj_titulo.update ({Name : self.__libros})
        obj1 = Book(Titulo , "Harold" , 102866 , "10/25/2014" , Name)
        obj1.Obj_Libro(Name,Titulo)
        return self.__reservado
        
    def LibroDevuelto (self ,Name:str , Titulo:str):
        self.__devuelto.append(Titulo)
        self.__libros.append (Titulo)
        del self._obj_titulo[Name]
        self._obj_titulo.update ({Name : self.__libros})
        obj1 = Book(Titulo , "Harold" , 102866 , "10/25/2014" , Name)
        obj1.Obj_Libro(Name,Titulo)
        return self.__devuelto
        
    def LibroPerdido (self , Name:str, Titulo:str):
        self.__perdido.append(Titulo)
        self.__libros.append (Titulo)
        del self._obj_titulo[Name]
        self._obj_titulo.update ({Name : self.__libros})
        obj1 = Book(Titulo , "Harold" , 102866 , "10/25/2014" , Name)
        obj1.Obj_Libro(Name,Titulo)
        print(obj1._obj_titulo)
        print (self._obj_titulo)
        return self._obj_titulo
        
    def calculate_fine (self):
        self.__multa = (1160000 * 0.3) * len(self.__perdido)
        return int(self.__multa)