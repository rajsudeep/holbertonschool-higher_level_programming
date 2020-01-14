#!/usr/bin/python3
""" sends a request to the URL and displays response  """

import urllib.request
import sys

if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as f:
            html = f.read()
        print(html.decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
