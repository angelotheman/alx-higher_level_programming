#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev_list = my_list.reverse()
    for i in rev_list:
        print("{}".format(i))
