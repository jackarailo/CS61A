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

def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

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

def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit


def luhn_check(n):
    if luhn_sum(n) % 10 == 0:
        return True
    else:
        return False
