#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return (None)

    lenghtList = len(my_list)

    if idx > lenghtList - 1:
        return (None)
    return (my_list[idx])
