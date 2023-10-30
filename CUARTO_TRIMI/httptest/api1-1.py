import requests
url='http://gutendex.com/books/'
response=requests.get(url)
diccionario=response.json()
#print(type(diccionario))
resultados=diccionario['results']
print(type(resultados))
print(len(resultados))
print(type(resultados[0]))
#print(resultados[0])
# for libro in resultados:
#     l1=[]
#     for value in libro['title']:
#         l1.append(value)
#         #print(f'{value}')
#     print(l1)
    
titulos=[libro['title'] for libro in resultados]
titulos_ord=sorted(titulos)

for t in titulos_ord:
    print(t)
