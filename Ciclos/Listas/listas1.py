#[] {} ()
x=100
print('tipo de x',type(x))
lista=[1,1.4,'sena',['a','b',],'soacha']
print(f'elemento {lista[4]}')
print(len(lista))
print('tipo de lista',type(lista))
print('ultimo indice',lista[-1])

print(len(lista))
lista.append(20)
lista.append('python')
print(lista)
lista.insert(len(lista),'java')
print(lista)