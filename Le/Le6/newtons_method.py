"""Script to build Newton's method to find the roots
of a function.
"""

def compute_function(f, df, x, epsilon = 0.01):
    """Gets a lambda and a lambda derivative, and a value and computes the f(x).
    """
    while (abs(f(x)) - epsilon) > 0:
        x = f(x) / df(x)
    return x, f(x)

def search(f):
    x = 0
    while True:
        if f(x):
            return x
        x += 1

def is_three(x):
    return x == 3

def square(x):
    return x * x

def positive(x):
    return max(0, square(x) - 100)

def inverse(f):
    """Return g(y) such that g(f(x)) -> x."""
    return lambda y: search(lambda x: f(x) == y)



def main():
    print None

if __name__ == "__main__":
    main()

