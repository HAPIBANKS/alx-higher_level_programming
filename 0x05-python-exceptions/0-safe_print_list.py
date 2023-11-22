#!/usr/bin/python3
def safe_print_list(my_list, x=0):
    j = 0
    try:
        for i in my_list:
            print("{}".format(i), end="")
            j += 1
            if j == x:
                break
        print("")
        return j
    except IndexError:
        return
