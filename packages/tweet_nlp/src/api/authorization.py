"""
Handles authorization with the td ameritrade api
"""
import json
import requests

config_filename = "config.txt"

def get_config_dict(config_filename):
    """
    Parses the config file into a dictionary
    """
    f = open(config_filename)
    ret = dict()
    for line in f.readlines():
        arr = line.strip().split('=', 1)
        ret[arr[0]] = arr[1]

    return ret

def get_access_token(client_id, refresh_token):
    """
    Sends a request to td ameritrade with the refresh 
    token to get a new access token
    """
    h = {
        "content-type": 'application/x-www-form-urlencoded'
    }

    d = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id
    }

    r = requests.post("https://api.tdameritrade.com/v1/oauth2/token", data=d, headers=h)

    return json.loads(r.text)["access_token"]


    

if __name__ == "__main__":
    config_dict = get_config_dict(config_filename)
    
    token = get_access_token(config_dict["client_id"], config_dict["refresh_token"])

    print(token)
