import os
import signal
import time
from UserToken import getUserToken, deleteAuth, riotClientLogin
from ClientToken import getEndpoint, getRiotClientEndpoint
import urllib3
from ClientFunctions import *
from CredentialParser import getCreds


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


usr = 'sparysgah'
pwd = '35472677a'

if __name__ == "__main__":

    # port, auth = getEndpoint()
    # deleteAuth(port, auth)
    # token = getUserToken(port, auth, usr, pwd)
    # user_token = token['token']
    # print(user_token)
    # riot_client_port, riot_client_auth, riot_pid = getRiotClientEndpoint()
    # time.sleep(3)
    # checkAndAcceptEULA(riot_client_port, riot_client_auth)
    # exit(0)

    creds = getCreds('message.txt')
    target_friend = 'shadow725na'
    for usr, pwd in creds:
        os.system('"E:/Riot games/League of Legends/LeagueClient.exe"')
        time.sleep(5)
        riot_client_port, riot_client_auth, riot_pid = getRiotClientEndpoint()
        riotClientLogin(riot_client_port, riot_client_auth, usr, pwd)
        time.sleep(2)
        try:
            checkAndAcceptEULA(riot_client_port, riot_client_auth)
        except:
            print("already accepted eula")
        time.sleep(10)
        port, auth, pid = getEndpoint()
        token = getUserToken(port, auth)
        time.sleep(12)
        response_code = friendAdd(port, auth, target_friend)
        if response_code == 200:
            print("add success")

        os.kill(int(pid), signal.SIGTERM)
        time.sleep(5)

