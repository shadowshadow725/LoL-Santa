import requests
from Headers import getHeader
import json

def getUserToken(port, token, user, pwd):
    header = getHeader(port, token)
    body = {
        "password": pwd,
        "username": user
    }
    url = 'https://127.0.0.1:' + port + '/lol-rso-auth/v1/authorization/gas'

    response = requests.post(url, json=body, headers=header, timeout=2.5, verify=False)

    print(response.json())
    if response.status_code != 200:
        exit(1)
    uri2 = 'https://127.0.0.1:' + port + '/lol-rso-auth/v1/authorization/access-token'
    user_token = requests.get(uri2, headers=header, verify=False)
    if user_token.status_code != 200:
        exit(1)

    return user_token.json()


def deleteAuth(port, token):
    url = 'https://127.0.0.1:' + port + '/lol-rso-auth/v1/authorization'
    requests.delete(url, headers=getHeader(port, token), verify=False)
