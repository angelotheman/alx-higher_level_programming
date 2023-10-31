#!/usr/bin/python3

def uppercase(str):
    for c in str:
        ascii_value = ord(c)
        if ord('a') <= ascii_value <= ord('z'):
            ascii_value -= 32
        print("{}".format(chr(ascii_value)), end="")
    print()
