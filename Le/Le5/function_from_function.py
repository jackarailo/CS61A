"""Lecture No 5
Call a function from a function
"""

def summation(n, term):
    """Function that adds N terms"""
    sum = 0
    for k in range(1, n+1):
        sum += term(k)
    return sum

def identity(n):
    """Function that returns itself"""
    return n


def sum_id(n):
    return summation(n, identity)



def make_adder(n):
    def adder(k):
        return k + n
    return adder

def apply_twice(f, x):
    return f(f(x))

def square(x):
    return x * x
