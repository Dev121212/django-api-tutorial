import requests
import json

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/updates/"


def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    print(r.status_code)
    data = r.json()
    print(type(data))  # list
    print(type(json.dumps(data)))  # str
    for obj in data:
        # print(obj['id'])
        if obj['id'] == 1:
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
            print(r2.json())
    return data


def create_update():
    new_data = {
        'user': 1,
        'content': 'Another new cool update'
    }
    r = requests.post(BASE_URL + ENDPOINT, json.dumps(new_data))
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text


# print(get_list())
# print(create_update())


def do_obj_update():
    new_data = {
        'content': 'Some content'
    }
    r = requests.put(BASE_URL + ENDPOINT + "12/", data=json.dumps(new_data))
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text


def do_obj_delete():
    new_data = {
        'content': 'Some content'
    }
    r = requests.delete(BASE_URL + ENDPOINT + "9/")
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text


print(do_obj_delete())
