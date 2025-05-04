#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ncount = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ncount += 1
        except (TypeError, ValueError):
            continue
        except IndexError:
            pass
    print() # Print a new line after the loop
    return ncount
