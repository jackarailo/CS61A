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

def f(x, y):
    return g(x)

def g(a):
    return a + y


def apply_twice(f, x):
    return f(f(x))

def square(x):
    return x * x

def triple(x):
    return 3 * x

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h


def repeat(f, x):
    while f(x) != x:
        x = f(x)
    return x

def g(y):
    return (y + 5) // 3

y = 20
x = 3
def f():
    y = 2
    return y, x



x = 10
squarelam = lambda x: x * x
