from savings_account import SavingsAccount
from loan_account import LoanAccount

class Bank:
    def __init__(self):
        self.accounts = []

    def show_customer_info(self):
        print("Thong tin khach hang")
        print("+---------------+-----------------+")
        print("| Tai khoan     | So du           |")
        print("+---------------+-----------------+")
        for account in self.accounts:
            print(f"| {account.account_number: <12} ","|", f"{account.get_balance(): <15} |")
        print("+---------------+-----------------+")

    def add_account(self, account_type):
        account_number = input("Nhap ma so tai khoan gom 6 chu so: ")
        balance = int(input("Nhap so du: "))
        if account_type == "Savings":
            self.accounts.append(SavingsAccount(account_number, balance))
        elif account_type == "Loan":
            interest_rate = float(input("Nhap lai suat: "))
            self.accounts.append(LoanAccount(account_number, balance, interest_rate))

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
            # elif choice == 4:
            #     self.withdraw_money()
            # elif choice == 5:
            #     self.show_transaction_history()
            # else:
            #     print("Chuc nang khong hop le")
            self.show_menu()
            choice = int(input("Chuc nang: "))


if __name__ == "__main__":
    bank = Bank()
    bank.main()
