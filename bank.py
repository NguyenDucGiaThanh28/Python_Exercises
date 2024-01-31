from Customer import Customer


class Bank:
    def __init__(self):
        self.customers = []

    def get_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def add_customer(self, customer_id, customer_name):
        existing_customer = self.get_customer_by_id(customer.customer_id)
        if existing_customer is None:
            new_customer = DigitalCustomer(
                                            customer.customer_id,
                                            customer.name,
                                            customer.premium, 
                                            customer.balance,
                                            customer.accounts
                                        )
            self.customers.append(new_customer)
            print("Add customer successfully.")
        else:
            print("Customer ID already exists.")