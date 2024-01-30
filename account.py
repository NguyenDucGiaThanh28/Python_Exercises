# account.py
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("So du tai khoan khong du")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance
