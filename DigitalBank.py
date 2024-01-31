from SavingsAccount import SavingsAccount
from LoanAccount import LoanAccount
from Bank import Bank

class DigitalBank:

    def __init__(self):
        self.customers = []
        self.accounts = []
        self.accounts.append(SavingsAccount(123456, "Savings", 10000000))
        self.accounts.append(LoanAccount(234567, "Loan", 20000000, 0.05))
        self.customers.append(self.accounts)

    def show_customer_info(self):
        print("Thong tin khach hang")
        print("+---------------+-----------+---------------------+")
        print("| Id            | Name      | So du               |")
        print("+---------------+-----------+---------------------+")
        for account in self.accounts:
            print(
                f"| {account.account_number: <12} ",
                "|", f"{account.account_type:<9}",
                "|",
                f"{account.balance: >17} đ |"
            )
        print("+---------------+-----------+---------------------+")

    def isAccountExisted(self, account_number):
        for account in self.accounts:
            if account_number == account.account_number:
                return False
        else:
            return True
            
    def add_account(self, account_type):
        account_number = int(input("Nhap ma so tai khoan gom 6 chu so: "))
        if self.isAccountExisted(account_number):
            balance = int(input("Nhap so du: "))
            if account_type == "Savings":
                self.accounts.append(
                SavingsAccount(account_number, account_type, balance)
                )
            elif account_type == "Loan":
                fee = float(input("Nhap fee: "))
                self.accounts.append(
                LoanAccount(account_number, account_type, balance, fee)
                )
        else:
            print("Tai khoan da ton tai")

    # def withdraw_money(self):
    #     account_number = int(input("Nhap so tai khoan: "))
    #     amount = int(input("Nhap so tien can rut: "))
    #     for account in self.accounts:
    #         if account.account_number == account_number:
    #             if account.account_type == "Savings":
    #                 account.withdraw_saving(amount)
    #                 print("Rut Tien Thanh Cong")
    #     else:
    #             print("Tai khoan khong ton tai")        
    def show_menu(self):
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

    def main(self):
        self.show_menu()
        choice = int(input("Chuc nang: "))
        while choice != 0:
            if choice == 1:
                self.show_customer_info()
            elif choice == 2:
                self.add_account("Savings")
            elif choice == 3:
                self.add_account("Loan")
            elif choice == 4:
                self.withdraw_money()
            # elif choice == 5:
            #     self.show_transaction_history()
            # else:
            #     print("Chuc nang khong hop le")
            self.show_menu()
            choice = int(input("Chuc nang: "))


if __name__ == "__main__":
    digitalbank = DigitalBank()
    digitalbank.main()
