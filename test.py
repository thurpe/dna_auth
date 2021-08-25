from get_auth import auth_token
from dnac_config import DNAC_IP

print('Login was successful, this is your token: {}'.format(auth_token))
print('Message from: {}'.format(DNAC_IP))