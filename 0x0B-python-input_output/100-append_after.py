#!/usr/bin/python3
"""
Contains the "append after" function
"""


def append_after(filename="", search_string="", new_string=""):
    """appends "new_string" after a line containing
    "search_string" in "filename" """
    with open(filename, 'r', encoding='utf-8') as f:
        lines_l = []
        while True:
            lines_print = f.readline()
            if lines_print == "":
                break
            lines_l.append(lines_print)
            if search_string in lines_print:
                lines_l.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines_l)
