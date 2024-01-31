from Account import Account
class LoanAccount(Account):
    def __init__(self, account_number,account_type, balance, fee):
        super().__init__(account_number, account_type, balance)
        self.fee = fee

    def calculate_fee(self):
        return self.balance * self.fee

    def get_balance(self):
        return self.balance - self.calculate_fee()
    
    def withdraw(self, amount):
        return super().withdraw(amount)
    # def isAccepted(self, amout):
