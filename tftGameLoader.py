import os
import signal
import time
from UserToken import getUserToken, deleteAuth, riotClientLogin
from ClientToken import getEndpoint, getRiotClientEndpoint, getGamePid
import urllib3
from ClientFunctions import *
from CredentialParser import getCreds


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

usr = 'houxinhao25'
pwd = 'v3p96tt7'


def searchAndAcceptGame(portid, authid):
    while checkSearchState(portid, authid) != 'Found':
        time.sleep(1)
    if checkSearchState(portid, authid) == 'Found':
        acceptGame(portid, authid)
        time.sleep(10)
    if checkSearchState(portid, authid) == 'Found' or \
        checkSearchState(portid, authid) == 'Searching':
        searchAndAcceptGame(portid, authid)


if __name__ == "__main__":

    os.system('"E:/Riot games/League of Legends/LeagueClient.exe"')
    time.sleep(5)
    riot_client_port, riot_client_auth, riot_pid = getRiotClientEndpoint()
    riotClientLogin(riot_client_port, riot_client_auth, usr, pwd)
    time.sleep(2)
    try:
        checkAndAcceptEULA(riot_client_port, riot_client_auth)
    except:
        print("already accepted eula")
    time.sleep(20)
    port, auth, pid = getEndpoint()

    enterLobby(port, auth)
    time.sleep(2)
    startQueue(port, auth)
    searchAndAcceptGame(port, auth)
    time.sleep(300)
    while not ifGameEnd(port, auth):
        time.sleep(30)

    time.sleep(10)



