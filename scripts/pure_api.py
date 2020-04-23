import requests
import json

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/updates/"


def get_list(id=None):
    data = json.dumps({})
    if id is not None:
        data = json.dumps({"id": id})

    r = requests.get(BASE_URL + ENDPOINT, data=data)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        print(r.json())
        # return r.json()
    # data = r.json()
    # print(type(data))  # list
    # print(type(json.dumps(data)))  # str
    # for obj in data:
    #     # print(obj['id'])
    #     if obj['id'] == 1:
    #         r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
    #         print(r2.json())
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


print(get_list())
# print(create_update())


def do_obj_update():
    new_data = {
        "id": 3,
        "content": "Awesome"
    }
    r = requests.put(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text


def do_obj_delete():
    new_data = {
        "id": 3
    }
    r = requests.delete(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text


# print(do_obj_delete())
