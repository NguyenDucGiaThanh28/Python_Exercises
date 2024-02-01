from User import User

class Customer(User):
    def __init__(self, customer_id, customer_name, premium, balance, accounts):
        super().__init__(customer_id, customer_name)
        self.premium = premium
        self.balance = balance
        self.accounts = accounts