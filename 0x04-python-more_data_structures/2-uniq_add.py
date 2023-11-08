#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set()
    sum_uniq = 0
    for i in my_list:
        if i not in uniq_list:
            uniq_list.add(i)
            sum_uniq += i
    return sum_uniq
