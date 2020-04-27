import requests
import json
import os


AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"
REFRESH_ENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/refresh/"

image_path = os.path.join(os.getcwd(), "logo.png")

headers = {
    "Content-Type": "application/json",
}
data = {
    "username": "devendra",
    "password": "nokialumia",
}
r = requests.post(
    AUTH_ENDPOINT,
    data=json.dumps(data),
    headers=headers
)
token = r.json()['token']
print(token)

B_ENDPOINT = "http://127.0.0.1:8000/api/status/"
ENDPOINT = B_ENDPOINT + "23/"

headers2 = {
    # "Content-Type": "application/json",
    "Authorization": "JWT " + token
}
data2 = {
    "content": "This is new content"
}

with open(image_path, 'rb') as image:
    file_data = {
        'image': image
    }
    r = requests.put(
        ENDPOINT,
        data=data2,
        headers=headers2,
        files=file_data,
    )
    # r = requests.post(
    #     B_ENDPOINT,
    #     data=data2,
    #     headers=headers2,
    #     files=file_data,
    # )
    print(r.text)


# AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"
# REFRESH_ENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/refresh/"
# ENDPOINT = "http://127.0.0.1:8000/api/status/"

# image_path = os.path.join(os.getcwd(), "logo.png")

# headers = {
#     "Content-Type": "application/json",
#     "Authorization": "JWT " + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNCwidXNlcm5hbWUiOiJhYmMxMSIsImV4cCI6MTU4Nzk4ODAzNCwiZW1haWwiOiJhYmMxMUBzbWlsZWJvdHMuY29tIiwib3JpZ19pYXQiOjE1ODc5ODc3MzR9.1iPHVYwme1fpAN3DEnTBmObKXl7iLscmpvSlExipBzM',
# }
# data = {
#     "username": "abc11",
#     "email": "abc11@smilebots.com",
#     "password": "nokialumia",
#     'password2': 'nokialumia',
# }
# r = requests.post(
#     AUTH_ENDPOINT,
#     data=json.dumps(data),
#     headers=headers
# )
# token = r.json()  # ['token']
# print(token)

# headers = {
#     # "Content-Type": "application/json",
#     "Authorization": "JWT "+token,
# }
# with open(image_path, 'rb') as image:
#     file_data = {
#         'image': image
#     }
#     data = {
#         'content': 'Some random content'
#     }
#     json_data = json.dumps(data)
#     posted_response = requests.put(
#         ENDPOINT + str(32) + "/", data=data, headers=headers, files=file_data)
#     print(posted_response.text)


# headers = {
#     # "Content-Type": "application/json",
#     "Authorization": "JWT "+token,
# }

# data = {
#     'content': 'New content'
# }
# json_data = json.dumps(data)
# posted_response = requests.put(
#     ENDPOINT + str(32) + "/", data=data, headers=headers)
# print(posted_response.text)

# refresh_data = {
#     'token': token
# }

# new_response = requests.post(
#     REFRESH_ENDPOINT,
#     data=json.dumps(refresh_data),
#     headers=headers
# )
# new_token = new_response.json()
# print(new_token)

# get_endpoint = ENDPOINT + str(12)
# post_data = json.dumps({'content': 'Some random content'})

# r = requests.get(get_endpoint)
# print(r.text)

# r2 = requests.get(ENDPOINT)
# print(r2.status_code)

# post_headers = {
#     'content-type': 'application/json'
# }

# post_response = requests.post(ENDPOINT, data=post_data, headers=post_headers)
# print(post_response.text)


# def do_img(method='get', data={}, is_json=True, img_path=None):
#     headers = {}
#     if is_json:
#         headers['content/type'] = 'application/json'
#         data = json.dumps(data)
#     if img_path is not None:
#         with open(image_path, 'rb') as image:
#             file_data = {
#                 'image': image
#             }
#             r = requests.request(method, ENDPOINT, data=data,
#                                  files=file_data, headers=headers)
#     else:
#         r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r


# do_img(method='post',
#        data={"user": 1, "content": ""},
#        is_json=False,
#        img_path=image_path)


# def do(method='get', data={}, is_json=True):
#     headers = {}
#     if is_json:
#         headers['content/type'] = 'application/json'
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r


'''
Create
Retrieve/List
Update
Delete
'''

# do(data={'id': 500})

# do(method='delete', data={'id': 13})

# do(method='put', data={
#    'id': 13, 'content': 'some cool new content', 'user': 1})

# do(method='post', data={'content': 'some cool new content', 'user': 1})
