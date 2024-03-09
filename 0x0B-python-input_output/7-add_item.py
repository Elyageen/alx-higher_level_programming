#!/usr/bin/python3
"""Module for appending items to a JSON file."""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argList = sys.argv[1:]
try:
    json_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    json_list = []

json_list.extend(argList)
save_to_json_file(json_list, "add_item.json")
