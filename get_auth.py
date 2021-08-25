import requests
from requests.auth import HTTPBasicAuth

from dnac_config import DNAC_IP, USERNAME, PASSWORD

requests.packages.urllib3.disable_warnings()

def get_auth_token():
# Building out Auth request. Using requests.post to make a call to the Auth Endpoint
    url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
    resp = requests.post(url, auth=HTTPBasicAuth(USERNAME, PASSWORD), verify=False)
    # Retrieve the Token from the returned JSON
    token = resp.json()['Token']
    # Print out the Token
    # print(token)
    # Create a return statement to send the token back for later use
    return token


#Takes the name of the file and convert it to the current running file/process
if __name__ == "__main__":
    
    get_auth_token()

auth_token = get_auth_token()