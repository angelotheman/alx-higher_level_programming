#!/usr/bin/python3
"""
Respond header value
"""
import sys
import urllib


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    values = {'email': email}

    data = urllib.parse.urlencode(values).encode('utf-8')

    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
