#!/usr/bin/python3
def uppercase(str):
    for y in range(len(str)):
        if ord(str[y]) >= 97 and ord(str[y]) <= 122:
            number = 32
        else:
            number = 0
        print("{:c}".format(ord(str[y]) - number), end='')
    print()
