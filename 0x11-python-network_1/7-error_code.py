#!/usr/bin/python3
""" sends a request to the URL and displays response  """

import requests
from sys import argv

if __name__ == '__main__':
    try:
        r = requests.get(argv[1])
        r.raise_for_status()
        print(r.text)
    except:
        print("Error code: {}".format(r.status_code))
