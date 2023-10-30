import requests
import json

url="https://httpbin.org/post"#?nombre=juan&documento=12345"
argumentos={
    'nombre':'Juan',
    'documento':'12345'
}

#response=requests.post(url,json=argumentos)
#response=requests.post(url,data=argumentos)
response=requests.post(url,data=json.dumps(argumentos))
#print(response.content.decode())
decodetest=response.content.decode()
#print(type(decodetest))
#print(response.json())
#print('*'*20)
#decodetestjson=json.loads(response.content)
#print(decodetestjson)
print('*'*20)
print(decodetest)

# print(response.content.decode())
# print(type(response.content.decode()))
# jsonresponse=json.loads(response.content)
# print(type(jsonresponse))

