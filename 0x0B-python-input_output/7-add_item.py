#!/usr/bin/python3
"""
Module - 7
- Add items and save them in a file
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == '__main__':
    try:
        item_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        item_list = []

    item_list.extend(sys.argv[1:])

    save_to_json_file(item_list, "add_item.json")
