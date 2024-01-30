# savings_account.py
from account import Account

class SavingsAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
