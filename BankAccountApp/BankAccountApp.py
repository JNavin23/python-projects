class Account:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number

    def debit(self, amount):
        if amount <= 0:
            print(" Debit amount must be positive.")
        elif amount > self.balance:
            print(" Insufficient balance.")
        else:
            self.balance -= amount
            print(f" Rs. {amount} debited successfully.")
            self.display_balance()

    def credit(self, amount):
        if amount <= 0:
            print(" Credit amount must be positive.")
        else:
            self.balance += amount
            print(f" Rs. {amount} credited successfully.")
            self.display_balance()

    def get_balance(self):
        return self.balance

    def display_balance(self):
        print(f" Current Balance: Rs. {self.balance}\n")

    def display_account_info(self):
        print(" Account Information")
        print(f"Account Number: {self.account_number}")
        print(f"Balance       : Rs. {self.balance}\n")


acc1 = Account(50000, 55555)

acc1.display_account_info()
acc1.debit(10000)
acc1.credit(25000)
