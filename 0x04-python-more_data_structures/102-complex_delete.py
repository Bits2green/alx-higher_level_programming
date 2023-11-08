#!/usr/bin/python3
def complex_delete(my_dict, value):
    delete_keys = []
    for k in my_dict:
        if my_dict[k] == value:
            delete_keys.append(k)
    for k in delete_keys:
        del my_dict[k]
    return my_dict