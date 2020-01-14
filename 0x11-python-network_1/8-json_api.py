#!/usr/bin/python3
""" sends a POST request to http://0.0.0.0:5000/search_user """

import requests
from sys import argv


if __name__ = '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    req = requests.post(url, data={'q': q})
    try:
        stuff = req.json()
        if stuff:
            print('[{}] {}'.format(stuff.get('id'), stuff.get('name')))
        else:
            print('No result')
    except:
        print('Not a valid JSON')
