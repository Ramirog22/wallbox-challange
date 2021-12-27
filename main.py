import requests

URL_ID = '4c932a0201dc4159a4a50c4863f1380d' # Here you must change the url id to make the code work
BASE_URL = 'https://crudcrud.com/api/'+ URL_ID + '/chargers'

def create_entry(json):
    return requests.post(BASE_URL, json=json)

def get_all_entries():
    return requests.get(BASE_URL)

def get_one(id):
    return requests.get(BASE_URL + '/' + id)

def update_entry(id, json):
    return requests.put(BASE_URL + '/' + id, json=json)

def delete_entry(id):
    return requests.delete(BASE_URL + '/' + id)