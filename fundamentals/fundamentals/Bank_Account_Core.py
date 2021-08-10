
class BankAccount:

    account_balance = 0
    intrate = 0.01

    def __init__(self, int_rate, balance):
        self.account_balance = balance
        self.rate = float(int_rate)


    def deposit(self, amount):
        self.account_balance += amount
        return self


    def withdraw(self, amount):
        if amount > self.account_balance:
            self.account_balance -= 5
            print("Insufficent funds. Charging a $5 fee.")
            return self
        else:
            self.account_balance -= amount
            return self

    def yield_interest(self):
        rate = (self.account_balance * self.rate)
        fl_rate = "{:.2f}".format(rate)
        print("Your interest rate at your current balance would yield $",fl_rate, " per year.")
        return self

    def display_account_info(self):
        fl_acct = "{:.2f}".format(self.account_balance)
        print("Balance: $",fl_acct, "\n")
        return self

Oliver = BankAccount(0.015, 500)
Twist = BankAccount(0.01, 300)


Oliver.deposit(300).deposit(200).deposit(100).withdraw(200).yield_interest().display_account_info()

Twist.deposit(100).deposit(200).withdraw(50).withdraw(75).withdraw(100).withdraw(1000).yield_interest().display_account_info()

