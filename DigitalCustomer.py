from SavingsAccount import SavingsAccount
from LoanAccount import LoanAccount
from Customer import Customer
class DigitalCustomer(Customer):
    def __init__(self, customer_id, customer_name):
        super().__init__(customer_id,customer_name)
