
class User:

    def __init__(self, name, email, balance = 0, int_rate = 0.01):
        self.name = name
        self.email = email
        self.account = BankAccount(balance, int_rate)

    def make_deposit (self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal (self, amount):
        self.account.withdraw(amount)
        return self

    def display_balance (self):
        self.account.display()
        return self



class BankAccount:

    def __init__ (self, balance, int_rate):
        self.balance = balance
        self.rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. You will be charged a $5 fee.")
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self

    def display(self):
        print(self.balance)


jim = User("jim", "jim@gmail.com")
jim.make_deposit(300).make_withdrawal(100).display_balance()


