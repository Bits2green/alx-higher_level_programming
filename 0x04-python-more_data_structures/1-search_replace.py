#!/usr/bin/python3
def search_replace(my_list, search, replace):
def sr(sr):
return (sr if sr != search else replace)
return list(map(sr, my_list))