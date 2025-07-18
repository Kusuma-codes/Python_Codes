class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def check_balance(self):
        print(f"{self.name}, your current balance is ₹{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Enter a valid amount to deposit.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

# Create account
account = BankAccount("Kusuma", 1000)

# Test the functions
account.check_balance()
account.deposit(5000000)
account.check_balance()
account.withdraw(3000)
account.check_balance()
account.withdraw(15000)  # Will show insufficient balance
account.check_balance()