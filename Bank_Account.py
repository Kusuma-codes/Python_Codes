# Parent class
class BankAccount:
    def __init__(self, holder_name, balance=0):
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    def display(self):
        print(f"Account Holder: {self.holder_name}, Balance: {self.balance}")


# Child class
class SavingsAccount(BankAccount):
    def __init__(self, holder_name, balance=0, interest_rate=0.03):
        super().__init__(holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of {interest} added. New balance: {self.balance}")


# Example
acc = SavingsAccount("Kusuma", 1000000)
acc.display()
acc.deposit(500)
acc.withdraw(200)
acc.add_interest()
