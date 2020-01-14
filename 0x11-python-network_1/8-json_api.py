#!/usr/bin/python3
""" sends a POST request to http://0.0.0.0:5000/search_user """

import requests
from sys import argv


if __name__ = '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    q = argv[1] if len(argv) is 2 else q = ""
    req = requests.post(url, data={'q': q})
    try:
        data = req.json()
        if data:
            print('[{}] {}'.format(data.get('id'), data.get('name')))
        else:
            print('No result')
    except:
        print('Not a valid JSON')
