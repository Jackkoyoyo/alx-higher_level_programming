#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_conv = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result, pre_val = 0, 0
    for r in roman_string:
        value = roman_conv[r]
        result += value
        if value > prev_val:
            result -= prev_val * 2
        prev_val = value
    return result
