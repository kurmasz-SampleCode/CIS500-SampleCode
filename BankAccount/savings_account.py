####################################################
#
# SavingsAccount
#
# Used for demonstrating inheritance in python
#
####################################################

from bank_account import BankAccount, Transaction
from datetime import datetime
import sys

class SavingsAccount(BankAccount):

    INTEREST = "Interest"

    def __init__(self, name, address, interest_rate):
        super().__init__( name, address)
        if (interest_rate < 0):
            raise ValueError("Interest rate can't be negative.")
        self.interest_rate = interest_rate

    def apply_monthly_interest(self, timestamp):
        monthly_interest = self.balance * (self.interest_rate / 12.0)
        self.transactions.append(Transaction(monthly_interest, SavingsAccount.INTEREST, timestamp))
        self.balance += monthly_interest

    def _print_statement_header(self, out):
        super()._print_statement_header(out)
        out.write(f"Current interest rate:  {self.interest_rate*100:.02f}\n")
  
def use_savings_account():
    acct = SavingsAccount('Phineas Sherman', '42 Wallaby Way, Sydney', 0.03)
    acct.deposit(10000.0, datetime(2023, 11, 1, 13, 0, 0))
    acct.withdraw(5000.0, datetime(2023, 11, 2, 14, 30, 0))
    acct.apply_monthly_interest(datetime(2023, 11, 30, 23, 59, 59))
    acct.print_statement(sys.stdout)

if __name__ == '__main__':    
    use_savings_account()