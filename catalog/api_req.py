import requests


URL = 'http://127.0.0.1:8000/api/category/?format=json'
URL_TOKEN = 'http://127.0.0.1:8000/api/token/'


def get_token():
    req = requests.post(URL_TOKEN, data={'username': 'kholodov', 'password': '12345'})
    access = req.json().get('access')
    return access

def get_category():

    jwt = get_token()
    req = requests.get(URL, headers={'Authorization': f'Bearer {jwt}'})
    print(req.json())
    if req.status_code == 200:
        for item in req.json():
            print(item)


get_category()