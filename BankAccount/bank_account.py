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

    DEPOSIT = 'Deposit'
    WITHDRAWAL = 'Withdrawal'

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

    def _print_statement_header(self, out):
        out.write(f"Monthly statement for {self.name}\n")
      
    def _print_transactions(self, out):
        for t in self.transactions:
            out.write(f"{t.timestamp} {t.type:10s} ${t.amount:8.02f}\n")

    def print_statement(self, out):
        self._print_statement_header(out)
        out.write("--------------------------------------------------\n")
        self._print_transactions(out)

def use_bank_account():
    acct = BankAccount('Phineas Sherman', '42 Wallaby Way, Sydney')
    acct.deposit(100.0, datetime(2023, 11, 1, 13, 0, 0))
    acct.withdraw(50.0, datetime(2023, 11, 2, 14, 30, 0))
    acct.print_statement(sys.stdout)

if __name__ == '__main__':    
    use_bank_account()


    
