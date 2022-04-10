from Headers import getHeader
import requests


def friendAdd(port, token, target_friend):
    url = 'https://127.0.0.1:' + port + '/lol-chat/v1/friend-requests'
    header = getHeader(port, token)
    body = {
        "name": target_friend
    }
    response = requests.post(url, headers=header, timeout=2.5, verify=False, json=body)
    return response.status_code



def friendWipe(port, token):
    url = 'https://127.0.0.1:' + port + '/lol-chat/v1/friends'
    header = getHeader(port, token)
    response = requests.get(url, headers=header, timeout=2.5, verify=False)
    friendlist = response.json()
    for i in friendlist:
        d = dict(i)
        print(d['id'])
        print(d['name'])

def getfriendId(port, token):
    url = 'https://127.0.0.1:' + port + '/lol-chat/v1/me'
    header = getHeader(port, token)
    response = requests.get(url, headers=header, timeout=2.5, verify=False)
    return response.json()['id']
