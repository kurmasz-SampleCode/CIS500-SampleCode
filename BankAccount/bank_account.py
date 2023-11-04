####################################################
#
# BankAccount
#
# Used for demonstrating inheritance in python
#
####################################################

from collections import namedtuple
from datetime import datetime
import sys

Transaction = namedtuple('Transaction', ['amount', 'type', 'timestamp'])

class BankAccount:

    DEPOSIT = 'D'
    WITHDRAWAL = 'W'


    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.balance = 0.0
        self.transactions = []


    def deposit(self, amount, timestamp):
        if (amount < 0):
            raise ValueError("Deposits must be positive")
        self.balance += amount
        self.transactions.append(Transaction(amount, BankAccount.DEPOSIT, timestamp))

    def withdraw(self, amount, timestamp):
        if (amount < 0):
            raise ValueError("Withdrawals must be positive")
        if (amount > self.balance):
            return False
        else:
            self.balance -= amount
        self.transactions.append(Transaction(amount, BankAccount.WITHDRAWAL, timestamp))

    def print_statement(self, out):
        print(f"Monthly statement for {self.name}", file=out)
        print("--------------------------------------------------", file=out)
        for t in self.transactions:
            print(f"{t.timestamp}", file=out)



acct = BankAccount('Tom Jones', '42 Wallalby Way, Syndey')
acct.deposit(100.0, datetime(2023, 11, 1, 13, 0, 0))
acct.withdraw(50.0, datetime(2023, 11, 2, 14, 30, 0))
acct.print_statement(sys.stdout)







    
