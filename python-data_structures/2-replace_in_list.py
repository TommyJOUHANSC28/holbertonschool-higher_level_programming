#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return (None)

    lenghtList = len(my_list)

    if idx > lenghtList - 1:
        return (None)

    my_list[idx] = element

    return (my_list)
