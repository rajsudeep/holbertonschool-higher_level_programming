#!/usr/bin/python3
""" displays the value of the X-Request-Id variable  """

import requests
import sys

if __name__ == '__main__':
    f = requests.get(sys.argv[1])
    print(f.headers.get('X-Request-Id'))
