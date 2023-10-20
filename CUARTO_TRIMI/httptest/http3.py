import requests
import json

url="https://httpbin.org/get"
response=requests.get(url)
# print(response.content.decode())
# print(type(response.content.decode()))

jsonresponse=json.loads(response.content)
print(type(jsonresponse))

# l1=[jsonresponse.keys()]
# print(l1)

def encontra_clave(diccionario):
    claves=[]
    for key, values in diccionario.items():
        claves.append(key)
        if isinstance(values,dict):
            claves += encontra_clave(values)
    return claves 


keys=encontra_clave(jsonresponse)

for x in keys:
    print(f'las clasves son: ',x)

        


