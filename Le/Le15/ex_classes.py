 class Account:
    """An account has a balance and a holder
    
    >>> a = Account('John')
    >>> a.deposit(100)
    100
    >>> a.withdraw(90)
    10
    >>> a.withdraw(100)
    'Insufficient funds'
    >>> a.check_balance
    10
    """
    interest = 0.02

    def __init__(self, account_holder, initial_deposit = 0):
        self.balance = initial_deposit
        self.holder = account_holder

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Withdraw amount from balance."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance -= amount
        return self.balance

    @property
    def check_balance(self):
        """Check the balance"""
        return self.balance

class CheckingAccount(Account):
    """An account with a withdrawal fee

    >>> a = CheckingAccount('John')
    >>> a.deposit(100)
    100
    >>> a.withdraw(10)
    89
    """
    interest = 0.01
    withdrawal_fee = 1

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdrawal_fee)

class SavingsAccount(Account):
    deposit_fee = 2
    def deposit(self, amount):
        return Account.deposit(self.amount - self.deposit_fee)

class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1 # A free dollar!

class Bank:
    """A bank has accounts.

    >>> bank = Bank()
    >>> john = bank.open_account('John', 10)
    >>> jack = bank.open_account('Jack', 5, CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    >>> bank.too_big_to_fail()
    True
    """
    
    def __init__(self):
        self.accounts = []

    def open_account(self, account_holder, deposit, kind=Account):
        account = kind(account_holder, deposit)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        for account in self.accounts:
            account.deposit(account.balance * account.interest)

    def too_big_to_fail(self):
        return len(self.accounts) > 1
        

