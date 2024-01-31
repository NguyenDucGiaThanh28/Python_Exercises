from Account import Account
class SavingsAccount(Account):
    def __init__(self, account_number,account_type, balance):
        super().__init__(account_number, account_type, balance)
    def withdraw_saving(self, amount):
       self.balance -= amount
    def get_balance(self):
        return self.balance
    