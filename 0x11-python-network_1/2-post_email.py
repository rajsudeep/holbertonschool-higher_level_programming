#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter """

import urllib.request
import sys

if __name__ == '__main__':
    data = (urllib.parse.urlencode({'email': sys.argv[2]})).encode('ascii')
    with urllib.request.urlopen(sys.argv[1], data) as f:
        print(f.read().decode('utf-8'))
