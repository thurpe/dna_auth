import requests
from get_auth import token
from get_device_list import device_list


def get_devices():
    get_device_id(device_list)



def get_device_id(device_json):
    for device in device_json['response']: # Loop through Device List and Retreive DeviceId
        print("Fetching Interfaces for Device Id ----> {}".format(device['id']))
        print('\n')
        get_device_int(device['id'])
        print('\n')


def get_device_int(device_id):
    url = "https://sandboxdnac.cisco.com/api/v1/interface"
    hdr = {'x-auth-token': token, 'content-type' : 'application/json'}
    querystring = {"macAddress": device_id} # Dynamically build the query    params to get device-specific Interface info
    resp = requests.get(url, headers=hdr, params=querystring)  # Make the Get    Request
    interface_info_json = resp.json()
    print_device_list(interface_info_json)



def print_device_list(interface_info):
    print("{0:42}{1:17}{2:12}{3:18}{4:17}{5:10}{6:15}".
          format("portName", "vlanId", "portMode", "portType", "duplex", "status", "lastUpdated"))
    for int in interface_info['response']:
        print("{0:42}{1:17}{2:12}{3:18}{4:17}{5:10}{6:15}".
              format(str(int['portName']),
                     str(int['vlanId']),
                     str(int['portMode']),
                     str(int['portType']),
                     str(int['duplex']),
                     str(int['status']),
                     str(int['lastUpdated'])))

if __name__ == "__main__":
    get_devices()