#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ncount = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            ncount += 1
    except IndexError:
        pass
    print()  # Print a new line after the loop
    return ncount