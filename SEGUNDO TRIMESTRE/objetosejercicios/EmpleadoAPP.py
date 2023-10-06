from Empleado import *
ob1=Empleado('juan', 'gerente', 1100000)
ob2=Empleado('juan', 'gerente', 1100000)
ob3=Empleado('juan', 'gerente', 1100000)
ob4=Empleado('juan', 'gerente', 1100000)

print (ob1.getNombre())
print (ob1.getCargo())
print(ob1.getSalario())

sueldo=ob1.getSalario()
print ('En una hora gana: ',ob1.unaHora())

ipc=ob1.aumentoIpc()
print ('Su sueldo aumentara: ',round(ipc,2), 'gracias al IPC')

extras=ob1.horasExtras()
print('Su salario mas extras es: ',extras)

print('Su sueldo total con extras y el IPC es de: ', extras + ipc)

print(ob1.cont)

