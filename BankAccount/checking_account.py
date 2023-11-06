####################################################
#
# CheckingAccount
#
# Used for demonstrating inheritance in python
#
####################################################

from collections import namedtuple
from bank_account import BankAccount, Transaction
from datetime import datetime
import sys

CheckTransaction = namedtuple('CheckTransaction', list(Transaction._fields) + ['check_num'])

class CheckingAccount(BankAccount):
    
    CHECK = 'Check'

    def __init__(self, name, address):
        super().__init__(name, address)

    def apply_check(self, amount, check_num, timestamp):
        if (amount < 0):
          raise ValueError("Withdrawals must be positive")
        if (amount > self.balance):
            raise ValueError("Check bounced!")
        self.balance -= amount
        self.transactions.append(CheckTransaction(amount, CheckingAccount.CHECK, timestamp, check_num))

    def _print_transactions(self, out):
        for t in self.transactions:
            if type(t) == CheckTransaction:
                check_str = str(t.check_num)
            else:
                check_str = ""
            out.write(f"{check_str:5s} {t.timestamp} {t.type:10s} ${t.amount:8.02f}\n")


def use_checking_account():
    acct = CheckingAccount('Phineas Sherman', '42 Wallaby Way, Sydney')
    acct.deposit(1000.0, datetime(2023, 11, 1, 13, 0, 0))
    acct.apply_check(250, 100,datetime(2023, 11, 2, 14, 0, 0) )
    acct.withdraw(50.0, datetime(2023, 11, 3, 14, 30, 0))
    acct.apply_check(150.0, 101, datetime(2023, 11, 4, 14, 30, 0))
    acct.print_statement(sys.stdout)

if __name__ == '__main__':    
    use_checking_account()