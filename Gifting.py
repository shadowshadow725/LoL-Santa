
import requests
from UserToken import getUserToken, console_login
from ClientToken import getEndpoint
from CredentialParser import getCreds
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
    port, auth = getEndpoint()
    # deleteAuth(port, auth)
    login_response = console_login(port, auth, usr, pwd)
    accountid = login_response['currentAccountId']
    token = getUserToken(port, auth)
    user_token = token['token']
    giftBody = createGiftBody(69900366, 250, target_summonerid, accountid)
    giftHeader = createGiftHeader(user_token)
    response = requests.post(url, json=giftBody, verify=False, headers=giftHeader)
    return response


if __name__ == "__main__":
    creds = getCreds('message.txt')
    c = 0
    for usr, pwd in creds:
        try:
            giftUser(usr, pwd, 77131806)
            c += 1
        except:
            print('something went wrong')
        if c == 9:
            print('gifting done')
            exit(0)

