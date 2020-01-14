#!/usr/bin/python3
""" that takes your Github credentials (username and password) and uses API """

import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    data = requests.get('https://api.github.com/user',
                        auth=HTTPBasicAuth(argv[1], argv[2])).json()
    print(data.get('id'))
