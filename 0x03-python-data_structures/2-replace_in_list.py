#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for x in range(len(my_list)):
        if idx < 0:
            return (my_list)
        elif idx > (len(my_list)):
            return (my_list)
        elif x == idx:
            new = my_list
            new[x] = element
            return (new)
