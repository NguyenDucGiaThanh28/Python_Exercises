from User import User
class Customer(User):
    def __init__(self, customer_id, customer_name):
        super().__init__(customer_id,customer_name)
        self.accounts = []
    def add_account(self, account):
        self.accounts.append(account)
    def add_accounts(self, accounts):
        for account in accounts:
            self.add_account(account)

            

        