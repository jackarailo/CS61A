"""
Course on recursion i.e. a function that calls itself

Or a function that calls a function that calls this function
"""

import math


"""
Simple Recursion

Add the digits of a number
"""

def split(n):
    """Sum the digits of N"""
    return n // 10, n % 10

def summation(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return summation(all_but_last) + last



"""
Intermediate Recursion

Compute factorial
"""

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fact(n-1) + fact


"""
A function that calls a function that calls this function

"""

