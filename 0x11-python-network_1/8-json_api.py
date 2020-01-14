#!/usr/bin/python3
""" sends a POST request to http://0.0.0.0:5000/search_user with a letter """

import requests
from sys import argv


if __name__ == "__main__":
    data = {'q': ""}
    if len(argv) > 1:
        data['q'] = argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", data)
    try:
        stuff = r.json()
        if stuff:
            print('[{}] {}'.format(stuff.get('id'), stuff.get('name')))
        else:
            print('No result')
    except:
        print('Not a valid JSON')
