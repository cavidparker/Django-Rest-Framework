import requests
import json

URL = "http://127.0.0.1:8000/api_view_func/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.get(url = URL, headers=headers, data = json_data)
    data = r.json()
    print(data)

# get_data(1)

### POST DATA:

def post_data():
    data = {
        'name':'Cavid parker',
        'roll':80,
        'city':'loss vgs'
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url = URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

# post_data()



## UPDATE DATA
def update_data():
    data ={
        'id': 2,
        'name': 'tom',
        'city': 'torento'
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url = URL,headers=headers, data=json_data)
    data = r.json()
    print(data)

update_data()



## DELETE DATA :
def delete_data():
    data = {'id':3}
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url = URL,headers=headers, data=json_data)
    data = r.json()
    print(data)

delete_data()

