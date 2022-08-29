#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    biggest = 0
    for index in my_list:
        if index > biggest:
            biggest = index
    return biggest
