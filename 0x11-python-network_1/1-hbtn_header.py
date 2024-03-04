#!/usr/bin/python3
"""
Respond header value
"""
import sys
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        request_id = response.headers.get('X-Request-Id')

    print(request_id)
