from Persona import *
ob1=Persona('juan',101694)
print (type(ob1))
print (ob1.getNombre())
ob1.setNombre('Imbachi')
ob1.setDocumento(1016946808)

print (ob1.getNombre())
print (ob1.getDocumento())

c=1
while c!=0:
    crso=input("Ingresa un curso")
    if crso == '0':
        break
    ob1.ingresarCurso(crso)


ob1.consultarCurso()
ob1.modificarCurso('java', 'javascrip')
ob1.consultarCurso()

