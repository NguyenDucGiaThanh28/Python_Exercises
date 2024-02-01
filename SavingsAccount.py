from Account import Account
from Transactions import Transactions
from datetime import datetime
class SavingsAccount(Account):
    SAVINGS_ACCOUNT_MAX_WITHDRAW = 5000000
    def __init__(self, account_number,account_type, balance):
        super().__init__(account_number, account_type, balance)
        self.transactions = []
    def withdraw(self, premium, amount):
        if self.is_accepted(premium, amount):
            self.balance=int(self.balance)-int(amount)
            time_transaction=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            fee=0
            self.log(str(time_transaction),self.account_number,amount,self.balance,fee)
            transaction=Transactions(self.account_number,amount,time_transaction,"TRUE")
            self.transactions.append(transaction)
        else:
            time_transaction=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transaction=Transactions(self.account_number,amount,time_transaction,"FALSE")
            self.transactions.append(transaction)

    def is_accepted(self,premium, amount):
        if (premium):
            if (int(amount)>=50000  and int(amount) % 10000==0 and int(self.balance)-int(amount)>=50000):
                return True
        else:
            if (int(amount)>=50000 and int(amount)<=self.SAVINGS_ACCOUNT_MAX_WITHDRAW and int(amount) % 10000==0 and int(self.balance)-int(amount)>=50000 ):
                return True

        return False

    def get_balance(self):
        return self.balance
    
    def log(_,time_transaction,account_number,amount,balance,fee):
        print("+----------------------------------------------+")
        print("|      BIEN LAI GIAO DICH SAVINGS              |")
        print(
                "| NGAY G/D:          "
                f" {str(time_transaction): >23}  |"
            )
        print(
                "| SO TK:             "
                f" {str(account_number): >23}  |"
            )
        print(
                "| SO TIEN:           "
                f" {str(amount): >23}  |")
        print(
                "| SO DU:             "
                f" {str(balance): >23}  |")
        print(
                "| PHI + VAT          "
                f" {str(fee): >23}  |")
        print("+----------------------------------------------+")