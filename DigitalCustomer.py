from Customer import Customer


class DigitalCustomer(Customer):
    def __init__(
            self,
            customer_id,
            customer_name,
            premium,
            balance,
            accounts
            ):
        super().__init__(
            customer_id,
            customer_name,
            premium,
            balance,
            accounts
            )

    def add_account(self, account):
        self.accounts.append(account)

    def add_accounts(self, accounts):
        for account in accounts:
            self.add_account(account)

    def with_draw(self, account_number, amount):
        for account in self.accounts:
            if (account.account_number == account_number):
                account.withdraw(self.premium, amount)
