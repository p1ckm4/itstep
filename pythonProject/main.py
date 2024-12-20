class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, append):
        if amt > 0:
            self.balance += append
            print(f"Deposited {append}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, append):
        if append > 0:
            if self.balance >= append:
                self.balance -= append
                print(f"Withdrawn {append}. New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")


account = BankAccount("12345678", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)
