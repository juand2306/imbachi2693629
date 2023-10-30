import requests

url="https://httpbin.org/cookies"
mycookies={
    'cookies': 'True'
}
response=requests.get(url,cookies=mycookies)
if response.status_code==200:
    print(response.content)
    #print('*'*40)
    print(response.cookies)
    