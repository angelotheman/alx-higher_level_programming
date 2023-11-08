#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    valid_chars = set('IVXLCDM')

    for char in roman_string:
        if char not in valid_chars:
            return 0

    total = 0

    num_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    i = 0
    while i < len(roman_string):
        a = num_dict[roman_string[i]]
        if i + 1 < len(roman_string):
            b = num_dict[roman_string[i + 1]]
            if a < b:
                total = total + (a - b)
                i += 2
            else:
                total = total + a
                i += 1
        else:
            total = total + a
            i += 1

    return total
