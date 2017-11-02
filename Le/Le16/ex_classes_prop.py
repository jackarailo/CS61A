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
        return self.balance

class CheckingAccount(Account):
    
    withdraw_fee = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount +self.withdraw_fee)
