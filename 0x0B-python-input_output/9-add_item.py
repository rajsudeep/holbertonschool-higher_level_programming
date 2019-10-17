#!/usr/bin/python3
from sys import argv
import json

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = "add_item.json"

try:
    obj_list = load_from_json_file(filename)
    obj_list.extend(argv[1:])
    save_to_json_file(obj_list, filename)
except:
    if len(argv) == 1:
        save_to_json_file([], filename)
    else:
        save_to_json_file(argv[1:], filename)
