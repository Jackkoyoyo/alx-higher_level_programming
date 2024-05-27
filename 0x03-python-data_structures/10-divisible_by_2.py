#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = [i % 2 == 0 for i in my_list]
    return new_list

#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
