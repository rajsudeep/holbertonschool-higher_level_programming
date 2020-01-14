#!/usr/bin/python3
""" sends a request to the URL and displays response  """

from urllib import request, error
import sys

if __name__ == '__main__':
    try:
        with request.urlopen(request.Request(sys.argv[1])) as f:
            html = f.read()
        print(html.decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
