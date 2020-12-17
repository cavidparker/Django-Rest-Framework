import requests
import json

URL = "http://127.0.0.1:8000/crud_class_list/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data)

# get_data()

### POST DATA:

def post_data():
    data = {
        'name':'Ravi tezza',
        'roll':11545,
        'city':'India'
    }

    json_data = json.dumps(data)
    r = requests.post(url = URL, data=json_data)
    data = r.json()
    print(data)

# post_data()



## UPDATE DATA
def update_data():
    data ={
        'id': 2,
        'name': 'awasaria rai',
        'city': 'los vegas'
    }

    json_data = json.dumps(data)
    r = requests.put(url = URL, data=json_data)
    data = r.json()
    print(data)

# update_data()



## DELETE DATA :
def delete_data():
    data = {'id':4}
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data=json_data)
    data = r.json()
    print(data)

delete_data()    

