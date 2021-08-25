import requests
from requests.auth import HTTPBasicAuth
from dnac_config import URL
from get_auth import token


def get_device_list():
    """
    Building out function to retrieve list of devices. Using requests.get to make a call to the network device Endpoint
    """
    url = URL
    hdr = {'x-auth-token': token, 'content-type' : 'application/json'}
    resp = requests.get(url, headers=hdr)  # Make the Get Request
    device_list = resp.json()
    print_device_list(device_list)
    return device_list



def print_device_list(device_json):
    print("{0:20}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
          format("hostname", "mgmt IP", "serial","platformId", "SW Version", "role", "Uptime in day(s)"))
    for device in device_json['response']:
        uptime = "N/A" if device['upTime'] is None else device['upTime']

        serialPlatformList = [(device['serialNumber'], device['platformId'])]

        for (serialNumber, platformId) in serialPlatformList:
            print("{0:20}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
                  format(device['hostname'],
                         device['managementIpAddress'],
                         serialNumber,
                         platformId,
                         device['softwareVersion'],
                         device['role'], uptime))

if __name__ == "__main__":
    get_device_list()
device_list = get_device_list()