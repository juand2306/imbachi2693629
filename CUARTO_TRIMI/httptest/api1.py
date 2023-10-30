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
for libro in resultados:
    for key, value in libro.items():
        print(f'{key} : {value}')