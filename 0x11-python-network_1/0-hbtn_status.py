#!/usr/bin/python3
"""
Fetch from a resource
"""
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as site:
        html = site.read()

    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
    print("\t- utf8 content:", html.decode('utf-8'))
