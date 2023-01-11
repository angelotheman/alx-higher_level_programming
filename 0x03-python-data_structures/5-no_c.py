#!/usr/bin/python3
def no_c(my_string):
    string_word =  [i for i in my_string if i != 'c' and i != 'C']
    return "".join(string_word)
