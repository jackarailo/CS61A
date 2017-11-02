class Account:
    def __init__(self, account_holder, initial_deposit = 0):
        self.balance = initial_deposit
        self.holder = account_holder

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance -= amount
        return relf.balance
