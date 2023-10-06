from sys import path

path.append("..\\imbachi2693629")

from Book import *
from Account import *

class Account:
    def __init__(self, Name, ID):
        self.__name = Name
        self.__id = ID
        self.__reservado = []
        self.__devuelto = []
        self.__perdido = []
        self.__libros = []
        self.__multa = 0
        self._obj_titulo = {Name : []}
        Book.__init__ (self,"Cien años de soledad" , "JuanD" , 101694 , "06/23/2005" , Name)


    def LibroReservado (self ,Name , Titulo):
        self.__reservado.append(Titulo)
        self.__libros.append (Titulo)
        del self._obj_titulo[Name]
        self._obj_titulo.update ({Name : self.__libros})
        obj1 = Book(Titulo , "JuanD" , 101694 , "06/23/2005" , Name)
        obj1.Obj_Libro(Name,Titulo)
        return self.__reservado
        
    def LibroDevuelto (self ,Name , Titulo):
        self.__devuelto.append(Titulo)
        self.__libros.append (Titulo)
        del self._obj_titulo[Name]
        self._obj_titulo.update ({Name : self.__libros})
        obj1 = Book(Titulo , "JuanD" , 101694 , "06/23/2005" , Name)
        obj1.Obj_Libro(Name,Titulo)
        return self.__devuelto
        
    def LibroPerdido (self , Name, Titulo):
        self.__perdido.append(Titulo)
        self.__libros.append (Titulo)
        del self._obj_titulo[Name]
        self._obj_titulo.update ({Name : self.__libros})
        obj1 = Book(Titulo , "JuanD" , 101694 , "06/23/2005" , Name)
        obj1.Obj_Libro(Name,Titulo)
        print(obj1._obj_titulo)
        print (self._obj_titulo)
        return self._obj_titulo
        
    def calculate_fine (self):
        self.__multa = (1160000 * 0.3) * len(self.__perdido)
        return int(self.__multa)