#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file
"""

from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

f_name = "add_item.json"

try:
    j_list = load_from_json_file(f_name)
except FileNotFoundError:
    j_list = []

for arg in argv[1:]:
    j_list.append(arg)

save_to_json_file(j_list, f_name)
