#!/usr/bin/python3
""" takes in a string and sends a search request to the Star Wars API """

import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://swapi.co/api/people/?search=' + argv[1]
    data = requests.get(url).json()
    if data:
        print("Number of results: {}".format(data.get("count")))
        for r in data.get("results"):
            print(r.get("name"))
