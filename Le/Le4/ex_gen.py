"""
1) Generalisation
2) Assertion

Example 1 - Shapes Area

Example 2 - Series Calculation
"""

from math import pi, sqrt
from operator import mul

###############################
####Example 1 - Shapes Area####
###############################
def area(r, shape_factor):
    assert r > 0, 'Negative dimension given. Length must be positive.'
    return r * r * shape_factor

def area_circle(r):
    return area(r, pi)

def area_square(r):
    return area(r, 1)

def area_hexagon(r):
    return area(r, 3 * sqrt(3) / 2)

##################################
##Example 2 - Series Calculation##
##################################

def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def pi_series(k):
    return 8 / mul(4*k - 3, 4*k - 1)

def summation(n, term):
    """Sum the first N terms of a sequence.

    >>> summation(5, cube)
    225
    """
    sum = 0
    for k in range(1, n + 1):
        sum += term(k)
    return sum

##################################
##Example 3 - Define Function#####
#####that returns a funtion#######
##################################

def make_adder(n):
    """Return a function that takes one argument
    K and return K + N.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder
