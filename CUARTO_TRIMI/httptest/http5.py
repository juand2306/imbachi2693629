import requests
import json
url="https://httpbin.org/post"#?nombre=juan&documento=12345"
argumentos={
    'nombre':'Juan',
    'documento':'12345'
}
theheaders={
    'Content-Type':'Text',
    'access-token':'12345'
}
response=requests.post(url,data=json.dumps(argumentos),headers=theheaders)
decodetest=response.content.decode()
print('*'*20)
print(decodetest)
print('-'*20)
headersprint=response.headers
print(headersprint)