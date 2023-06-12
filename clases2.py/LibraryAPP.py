from Book import *
from User import *
from Account import *


obj2 = Book ("La llorona" , "Harold" , 102866 , "10/25/2014" , "Harold")
obj1 = User ("Harold" , 102866,obj2._obj_titulo)
obj3 = Account ("Harold" , 102866,)


print(obj3.LibroReservado("Harold","La llorona"))
print(obj3.LibroReservado("Harold","La guerra de los cielos" ))
print(obj3.LibroDevuelto("Harold","La llorona"))
print(obj3.LibroDevuelto("Harold","La guerra de los cielos"))
print(obj3.LibroPerdido("Harold"," La llorona"))
print(obj3.LibroPerdido("Harold", "La Guerra de los cielos"))
print(obj3.LibroPerdido("Harold", "La guerra de los cielos"))
print(obj3.LibroPerdido("Harold", "La guerra de los cielos"))
print(obj3.calculate_fine())

obj1.CheckAccount("Harol" , obj3._obj_titulo["Harold"])

obj2.AgregarBook()

# print(obj1.get_book_info ("La guerra de los cielos", obj2._informacion))
obj1.get_book_info ("La guerra de los cielos", obj2._informacion)