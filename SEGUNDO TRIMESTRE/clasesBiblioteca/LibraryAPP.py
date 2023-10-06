from Book import *
from User import *
from Account import *


obj2 = Book ("La Vaca Lola" , "JuanD" , 101694 , "06/23/2005" , "JuanImbachi")
obj1 = User ("JuanD" , 101694,obj2._obj_titulo)
obj3 = Account ("JuanD" , 101694,)


print(obj3.LibroReservado("JuanD","La Vaca Lola"))
print(obj3.LibroReservado("Juand","La biblia de los caidos" ))
print(obj3.LibroDevuelto("JuanD","La Vaca Lola"))
print(obj3.LibroDevuelto("JuanD","La biblia de los caidos"))
print(obj3.LibroPerdido("JuanD"," La Vaca Lola"))
print(obj3.LibroPerdido("Juand","La biblia de los caidos"))
print(obj3.LibroPerdido("Juand","La biblia de los caidos"))
print(obj3.LibroPerdido("Juand","La biblia de los caidos"))
print(obj3.calculate_fine())

obj1.CheckAccount("JuanD" , obj3._obj_titulo["JuanD"])

obj2.AgregarBook()

# print(obj1.get_book_info ("La guerra de los cielos", obj2._informacion))
obj1.get_book_info ("La biblia de los caidos", obj2._informacion)