import requests
from Headers import getHeader
import json

def console_login(port, token, user, pwd):
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
    return response.json()


def getUserToken(port, token):
    header = getHeader(port, token)
    print(token)
    uri2 = 'https://127.0.0.1:' + port + '/lol-rso-auth/v1/authorization/access-token'
    user_token = requests.get(uri2, headers=header, verify=False)
    print(user_token.json())
    if user_token.status_code != 200:
        exit(1)

    return user_token.json()


def deleteAuth(port, token):
    url = 'https://127.0.0.1:' + port + '/lol-rso-auth/v1/authorization'
    requests.delete(url, headers=getHeader(port, token), verify=False)


def riotClientLogin(port, token, user, pwd):
    uri = 'https://127.0.0.1:' + port + '/rso-auth/v1/session/credentials'
    payload = {
        'username': user,
        'password': pwd,
        'persistLogin': 'false'
    }
    header = getHeader(port, token)

    response = requests.put(uri, json=payload, verify=False, headers=header)

