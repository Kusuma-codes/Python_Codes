class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def display(self):
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")  
         
    def deposit(self, deposit_amt):
        self.balance += deposit_amt

    def withdraw(self, withdraw_amt):
        if self.balance > withdraw_amt:
           self.balance -= withdraw_amt
        else:
            print("Insufficient Balance")

a1 = BankAccount("Kusuma",150000)
a1.display()
a1.deposit(200000)
a1.withdraw(50000)
a1.display()
        
