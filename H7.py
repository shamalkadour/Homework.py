class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
            self.get_balance()

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f" Withdrawal done : ${amount}")
            self.get_balance()
        else:
            print("The amount required for withdrawal exceeds the current balance")

    def get_balance(self):
        print(f"The amount: ${self.balance}")


b_a = BankAccount("58225", "Rayyan")
b_a.deposit(7000)
b_a.withdraw(1500)


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate, balance=0.0):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
        print(f" Interest is applied at a rate: {self.interest_rate * 100}%")
        self.get_balance()

    def get_balance(self):
        super().get_balance()
        print(f"interest rate : {self.interest_rate * 100}%")


savings_account = SavingsAccount("952287", "Sham Alkadour", 0.05)
savings_account.deposit(8000)
savings_account.apply_interest()
savings_account.get_balance()
