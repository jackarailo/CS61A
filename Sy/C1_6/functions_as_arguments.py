"""On this script we try to elaborate the concept of abstraction.

- How do we avoid having repetitive code?
- At what degree is abstraction beneficial?
- Why do we want abstraction?
....
"""

"""
Example 1 - Say we want to sum k terms

The type of the term can change
"""

def summation(n, term):
    total = 0
    for i in range(n):
        total += term(i + 1)
    return total

def identity(k):
    return k

def sum_naturals(n):
    return summation(n, identity)

"""
Example 2 - Golden ratio

Script to compute the golden ratio
"""

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1/guess + 1

def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)

"""
Example 3 - Split and sum digits

"""

def split(n):
    """Split positive n into all but its last digit and its last digit"""
    return n // 10, n % 10

def sum_digits(n):
    """Return the sum of the digits of positive integer n."""
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

def fact(n):
    """Factoriar factor which computes the factorial of N"""
    if n == 0 or n == 1:
        return 1
    else:
        return fact(n-1) * n



def luhn_digit(n):
    """Gets a number and returns the double 
    if smaller than ten or the sum of the digts of the double.
    """
    n_d = n * n
    return sum_digits(n_d)


def luhn_isvalid(n):
    """luhn checks if sum of digits is a multiple of 10"""
    n_mod = luhn_digits(n)
    if sum_digits(n_mod) % 10 == 0:
        return True
    else:
        return False


