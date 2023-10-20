
import requests

url = "https://hoteliasenapractica2693629.000webhostapp.com/styles.css"
response = requests.get(url)

print("Tipo de objeto de respuesta:", type(response))
print("Código de estado de la respuesta:", response.status_code)

# file = open("CUARTO_TRIMI/httptest/style.css", "wb")
# file.write(response.content)
# file.close()

if response.status_code>=200 and response.status_code<300:
    print(response.content)
elif response.status_code>=300 and response.status_code<400:
    print("Redireccion")
elif response.status_code>=400 and response.status_code<500:
    print("Error en el cliente ")
elif response.status_code>=500:
    print("Error em el servidor ")
