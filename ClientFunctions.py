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


def checkAndAcceptEULA(port, token):
    header = getHeader(port, token)
    url = 'https://127.0.0.1:' + port + '/eula/v1/agreement'
    response = requests.get(url, headers=header, timeout=2.5, verify=False)
    resp_body = response.json()
    if resp_body['acceptance'] == 'Accepted':
        return
    accept_url = 'https://127.0.0.1:' + port + '/eula/v1/agreement/acceptance'
    response = requests.put(accept_url, headers=header, timeout=2.5, verify=False)
    if response.status_code == 201:
        print('eula accept successd')
        startLeagueClient(port, token)


def startLeagueClient(port, token):
    header = getHeader(port, token)
    url = "https://127.0.0.1:" + port + \
          "/product-launcher/v1/products/league_of_legends/patchlines/live"

    response = requests.post(url, headers=header, timeout=2.5, verify=False)
    return response.status_code


def enterLobby(port, token):
    url = 'https://127.0.0.1:' + port + '/lol-lobby/v2/lobby'
    header = getHeader(port, token)
    body = {"queueId": 1090}

    response = requests.post(url, headers=header, timeout=2.5, verify=False, json=body)
    return response.status_code


def startQueue(port, token):
    url = 'https://127.0.0.1:' + port + '/lol-lobby/v2/lobby/matchmaking/search'
    header = getHeader(port, token)
    body = {}
    response = requests.post(url, headers=header, timeout=2.5, verify=False, json=body)
    return response.status_code

def acceptGame(port, token):
    url = 'https://127.0.0.1:' + port + '/lol-matchmaking/v1/ready-check/accept'
    header = getHeader(port, token)
    body = {}
    response = requests.post(url, headers=header, timeout=2.5, verify=False, json=body)
    return response.status_code

def checkSearchState(port, token):
    url = 'https://127.0.0.1:' + port + '/lol-lobby/v2/lobby/matchmaking/search-state'
    header = getHeader(port, token)
    response = requests.get(url, headers=header, timeout=2.5, verify=False)
    if not response:
        return 'error'
    return response.json()["searchState"]

def ifGameEnd(port, token):
    url = 'https://127.0.0.1:2999/liveclientdata/activeplayer'
    header = getHeader(port, token)
    try:
        response = requests.post(url, headers=header, timeout=2.5, verify=False)
    except:
        return True
    if response:
        body = response.json()
        if body["championStats"]["currentHealth"] < 1.0:
            return True
    return False
