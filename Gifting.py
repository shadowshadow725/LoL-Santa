import time

import requests
from UserToken import getUserToken, console_login, deleteAuth
from ClientToken import getEndpoint
from CredentialParser import getCreds
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# masterwork chest bundle itemId=69900088
# rp 225
# masterwork chest itemId=224
# rp 165
# key id=3?
# rp 125
# hextech chest bundle itemId=69900001
# hextech chest itemid=1
# rp 125
# orb itemid=69900366
# rp 250

def createGiftBody(itemid, rpcost, reciever, sender):
    body = {"customMessage":"","receiverSummonerId":reciever,"giftItemId":1010,
            "accountId":sender,"items":[
            {"inventoryType":"BUNDLES","itemId":itemid,
           "ipCost":'null',"rpCost":rpcost,"quantity":1}]}
    return body

def createGiftHeader(token):
    header = {'Connection': 'keep-alive',
              'AUTHORIZATION': 'Bearer ' + token,
            'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'LeagueOfLegendsClient/12.6.430.6775 (CEF 91)',
    'Accept-Language': 'en-US,en;q=0.9'}
    return header


def giftUser(usr, pwd, target_summonerid):
    url = "https://na.store.leagueoflegends.com/storefront/v3/gift?language=en_US"
    port, auth, pid = getEndpoint()
    deleteAuth(port, auth)
    login_response = console_login(port, auth, usr, pwd)
    accountid = login_response['currentAccountId']

    token = getUserToken(port, auth)
    user_token = token['token']
    giftBody = createGiftBody(69900366, 250, target_summonerid, accountid)
    giftHeader = createGiftHeader(user_token)
    response = requests.post(url, json=giftBody, verify=False, headers=giftHeader)

    return response


if __name__ == "__main__":

    c = 0
    # usr = 'zerrituel7'
    # pwd = 'Treyton8'
    # giftUser(usr, pwd, 77131806)
    # exit(0)
    creds = getCreds('message.txt')
    for usr, pwd in creds:
        try:
            resp = giftUser(usr, pwd, 77131806)
            print(resp.json())
            time.sleep(1)
            if resp.status_code == '200':
                c += 1
        except:
            print('something went wrong')
        # if c == 7:
        #     print('gifting done')
        #     exit(0)

