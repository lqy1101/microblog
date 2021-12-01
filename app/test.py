import requests

url = "http://10.110.3.155/"
response = requests.get(url)
print(response.headers["Set-Cookie"])
post = {
    'Set-Cookie': response.headers["Set-Cookie"],
    'name': 'bbbbb',
    'know': True,
    'submit': 'Submit'
}
response = requests.post(url, data=post)
print(response)
# response = requests.get(url)
# print(response.text)
