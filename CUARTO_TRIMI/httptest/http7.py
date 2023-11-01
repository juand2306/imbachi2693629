import requests

url='https://api.github.com/users'
sesion=requests.session()
sesion.auth=('juandiegoimbachihoyos@gmail.com','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')
response=sesion.get(url)

if response.status_code==200:
    response1=sesion.get('https://github.com/juand2306')
    print(response1.cookies)
    #print(response.content)
