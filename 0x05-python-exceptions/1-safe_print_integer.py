#!/usr/bin/python3
def safe_print_integer(valude):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
