#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list is None:
        return None

    if idx < 0 or idx >= lenghtList:
        return (my_list)

    new_list = my_list.copy()
    del my_list[idx]

    return (my_list)
