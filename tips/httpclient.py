import json
import requests


class HttpClient:
    def get(self, url, headers={}):
        response = requests.get(url)
        return response

    def post(self, url, headers={}, data={}):
        response = requests.post(url, data)
        return response

    def put(self, url, headers={}, data={}):
        response = requests.put(url, data)
        return response

    def delete(self, url, headers={}):
        response = requests.delete(url)
        return response


httpClient = HttpClient()

response = httpClient.get('http://google.com')
print(response.content)

data = json.dumps({
    'code': 1,
    'data':  {
        'name': 'tuana9a',
        'address': ''
    },
    'message': ['assistant-school-automate-captcha']
})

response = httpClient.post(url='https://reqbin.com/echo/post/json', data=data)
print(response.json())
