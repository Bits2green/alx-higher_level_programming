#!/usr/bin/python3
def best_score(my_dict):
if my_dict and len(my_dict):
max = list(my_dict.keys())[0]
for k in my_dict:
if my_dict[k] > my_dict[max]:
max = k
return max
return None