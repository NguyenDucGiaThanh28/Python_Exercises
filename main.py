from DigitalBank import DigitalBank

from DigitalCustomer import DigitalCustomer
from SavingsAccount import SavingsAccount
from LoanAccount import LoanAccount

customer1 = DigitalCustomer("1002200113",
                            "FUNIX",
                            "premium",
                            "500000000",
                            [])
customer2 = DigitalCustomer("1003350451",
                            "John Doe",
                            "premium",
                            "100000000",
                            [])


CUSTOMER_ID = "1002200113"
CUSTOMER_NAME = "FUNIX"
digitalbank = DigitalBank()
digitalbank.add_customer(customer1)
digitalbank.add_customer(customer2)


account1 = SavingsAccount(123456, "Savings", 10000000)
account2 = LoanAccount(234567, "Loan", 20000000)

customer1.add_account(account1)
customer1.add_account(account2)


def isAccountExisted(customer, account_number):
    for account in customer.accounts:
        if account_number == account.account_number:
            return False
    else:
        return True


def validateAccount(account_number):
    if len(str(account_number)) == 6:
        return True
    else:
        return False


def add_account(customer, account_type):
    account_number = int(input("Nhap ma so tai khoan gom 6 chu so: "))
    while not validateAccount(account_number):
        account_number = int(input("Nhap lai ma so tai khoan: "))
    if isAccountExisted(customer, account_number):
        balance = int(input("Nhap so du: "))
        if account_type == "Savings":
            customer.add_account(
                SavingsAccount(account_number, account_type, balance)
                )
        elif account_type == "Loan":
            customer.add_account(
                LoanAccount(account_number, account_type, balance)
                )
    else:
        print("Tai khoan da ton tai")


def withdraw_money(customer):
    account_number = int(input("Nhap so tai khoan: "))
    amount = int(input("Nhap so tien can rut: "))
    for account in customer.accounts:
        if account.account_number == account_number:
            if account.account_type == "Savings":
                account.withdraw(customer.premium, amount)
                break
            elif account.account_type == "Loan":
                account.withdraw(customer.premium, amount)
                break
    else:
        print("Tai khoan khong ton tai")


def show_menu():
    print("+----------------------------------------------------------+")
    print("| NGAN HANG DIEN TU | thanh@v1.0.0                         |")
    print("+----------------------------------------------------------+")
    print("| 1. Thong tin khach hang                                  |")
    print("| 2. Them tai khoan ATM                                    |")
    print("| 3. Them tai khoan vay                                    |")
    print("| 4. Rut tien                                              |")
    print("| 5. Lich su giao dich                                     |")
    print("| 0. Thoat                                                 |")
    print("+----------------------------------------------------------+")


def show_customer_info(customer):
    print("Thong tin khach hang")
    print("+---------------+-----------+---------------------+")
    print("| Id            | Name      |             So du   |")
    print(
            f"| {customer.customer_id: <12} ",
            "|", f"{customer.customer_name: <9}",
            "|",
            f"{customer.premium: <17}   |"
        )
    print("+---------------+-----------+---------------------+")
    for account in customer.accounts:
        print(
            f"| {account.account_number: <12} ",
            "|", f"{account.account_type: <9}",
            "|",
            f"{account.balance: >17} đ |"
        )
    print("+---------------+-----------+---------------------+")


def log_history(customer):
    show_customer_info(customer)
    for account in customer.accounts:
        for transaction in account.transactions:
            print(
                f"| {transaction.account_number} ",
                "| -", f"{transaction.amount}",
                f"{transaction.status}",
                f"{transaction.time}"
            )
    print("+---------------+-----------+---------------------+")


def main():
    show_menu()
    choice = int(input("Chuc nang: "))
    while choice != 0:
        customer = digitalbank.get_customer_by_id(CUSTOMER_ID)
        if choice == 1:
            show_customer_info(customer)
        elif choice == 2:
            add_account(customer, "Savings")
        elif choice == 3:
            add_account(customer, "Loan")
        elif choice == 4:
            withdraw_money(customer)
        elif choice == 5:
            log_history(customer)
        else:
            print("Chuc nang khong hop le")
        show_menu()
        choice = int(input("Chuc nang: "))


if __name__ == "__main__":
    main()
