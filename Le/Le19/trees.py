class Tree:
    def __init__(self, label, branches = []):
        self.label = label
        for branch in branches:
            assert isinstance(branches, Tree)
        self.branches = branches

def fib_tree(n):
    if n == 0 or if n == 1:
        return Tree(n)
    left = fib_tree(n-2)
    right = fib_tree(n-1)
    fib_n = left.label + right.label
    return Tree(fib_n, [left, right])

def fib_value(n):
    if n == 0 or n == 1:
        return n
    return fib_value(n-1) + fib_value(n-2)


def Fib_Memo:
    def __init__(self, n):
        self.n = n
        self.memorized = {}
    
    def memorize(self, i):
        if n not in self.memorized:
            self.memorized[n] = fib(n)

    def fib(self)

