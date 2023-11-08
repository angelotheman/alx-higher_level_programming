#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_score = max(a_dictionary.values())
        student = [k for k, v in a_dictionary.items() if v == max_score][0]
        return student
    return None
