#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """

import requests

if __name__ == '__main__':
    html = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))
    print('\t- utf8 content: {}'.format(html.decode("utf-8")))
