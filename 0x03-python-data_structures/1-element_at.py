#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(0, len(my_list)):
        for j in range(i+1, len(my_list)):
            if my_list[i] >= my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
            
    