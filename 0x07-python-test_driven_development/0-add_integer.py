#!/usr/bin/python3
"""
This program returns the addition of two ints
"""
def add_integer(a, b=98):
   """This function adds to ints and return the sum
      arguments:
      a(int): first arguments
      b(int): second arguments
      raises:
      TypeError is a or b is not an integer or float
      return:
      the sum of a and b
  """

   if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
   if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer")
   return int(a) + int(b)
