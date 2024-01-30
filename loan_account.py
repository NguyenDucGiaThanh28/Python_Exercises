# loan_account.py
from account import Account

class LoanAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

    def get_balance(self):
        return super().get_balance() + self.calculate_interest()
