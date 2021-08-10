
class User:

    def __init__ (self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0


    def make_deposit (self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal (self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance (self):
        print(self.account_balance)
        return self

    def transfer_money (self, recipient, amount):
        self.account_balance -= amount
        recipient.account_balance += amount
        self.display_user_balance()
        recipient.display_user_balance()
        return self

jim = User("Jim Kirk", "starfleet79@gmail.com")
spock = User("Just Spock", "Vulcan@gmail.com")
bones = User("Leonard McCoy", "DammitJim@gmail.com")


spock.make_deposit(100).make_deposit(200).make_deposit(75).make_withdrawal(85).display_user_balance()

bones.make_deposit(50).make_deposit(85).make_withdrawal(60).make_withdrawal(30).display_user_balance()

jim.make_deposit(500).make_withdrawal(50).make_withdrawal(100).make_withdrawal(30).display_user_balance().transfer_money(bones,300)

