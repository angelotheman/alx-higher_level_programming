#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_list = list(a_dictionary.keys())
    for key in sorted(new_list):
        print("{}".format(key))
