from Bank import Bank
from DigitalCustomer import DigitalCustomer
from LoanAccount import LoanAccount
from SavingsAccount import SavingsAccount

class DigitalBank(Bank):
    def __init__(self):
        super().__init__()
        self.customers = []
        self.accounts = []

    def get_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:   
                return customer
        return None
 
    def add_customer(self,customer):
        existing_customer = self.get_customer_by_id(customer.customer_id)
        if existing_customer is None:
            new_customer = DigitalCustomer(customer.customer_id, customer.customer_name, customer.premium, customer.balance,customer.accounts)
            self.customers.append(new_customer)
        else:
            print("Customer with the same CCCD already exists.")

    # Hàm rút tiền
    def withdraw(self, customer_id, account_number, amount):
        customer = self.get_customer_by_id(customer_id)
        if customer is not None:
            customer.with_draw(account_number, amount)
        else:
            print("Customer with the specified CCCD not found.")
