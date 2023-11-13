from datetime import datetime
from bank_account import BankAccount
from savings_account import SavingsAccount
from checking_account import CheckingAccount
import sys

b = BankAccount('Bob Banker', '15 Maple Street')
b.deposit(100, datetime(2023, 11, 1, 12, 30))
b.withdraw(10, datetime(2023, 11, 2, 13, 45))
b.withdraw(25, datetime(2023, 11, 3, 16, 3))


s = SavingsAccount('Sam Saver', '23 Maple Street', 0.03)
s.deposit(100, datetime(2023, 11, 1, 12, 30))
s.deposit(5000, datetime(2023, 11, 4, 15, 45))
s.deposit(22350, datetime(2023, 11, 6, 8, 0))
s.pay_interest(datetime(2023, 11, 30, 8, 0))

c = CheckingAccount('Charlie Czechmeister', '22b Baker Street')
c.deposit(2100, datetime(2023, 11, 1, 12, 31))
c.apply_check(14.75, 100, datetime(2023, 11, 4, 21, 45))
c.apply_check(100, 101, datetime(2023, 11, 4, 22, 45))
c.apply_check(417, 103, datetime(2023, 11, 6, 21, 45))
c.deposit(2100, datetime(2023, 11, 15, 12, 31))
c.apply_check(55.64, 102, datetime(2023, 11, 16, 8, 15))



accounts = [b, s, c]

for account in accounts:
    sys.stdout.write("\n\n")
    account.print_statement(sys.stdout)
