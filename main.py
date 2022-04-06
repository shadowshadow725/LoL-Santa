from UserToken import getUserToken, deleteAuth
from ClientToken import getEndpoint
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


usr = 'sparysgah'
pwd = '35472677a'

if __name__ == "__main__":

    port, auth = getEndpoint()
    deleteAuth(port, auth)
    token = getUserToken(port, auth, usr, pwd)
    user_token = token['token']
    print(user_token)
