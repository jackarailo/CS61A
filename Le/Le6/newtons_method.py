"""Script to build Newton's method to find the roots
of a function.
"""

def compute_function(f, df, x, epsilon = 0.01):
    """Gets a lambda and a lambda derivative, and a value and computes the f(x).
    """
    while (abs(f(x)) - epsilon) > 0:
        x = f(x) / df(x)
    return x, f(x)


