from sys import path

path.append("..\\imbachi2693629")

from Account import *


class User(Account):
    def __init__(self , Name, ID, informacion):
        self._name = Name
        self.__id = ID
        self.__verificado = None
        self.__account  = informacion
        self.__informacion = {}
        Account.__init__(self , Name , ID)
        
    
    def verify (self , Name, ID):
        if self._name == Name and self.__id == ID:
            self.__verificado = "Verificado"
            return "Verificado"
        else:
            self.__verificado = "No Verificado"
            return "No Verificado"
            

    def CheckAccount (self, Name , Informacion):
        self.__account = Informacion
        print(Informacion)
    
    def get_book_info (self , Titulo , informacion):
        self.__informacion = informacion
        print(self.__informacion)
