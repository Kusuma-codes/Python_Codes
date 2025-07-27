# Compound Interest = P * (1 + R/100)^T - P

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual rate of interest: "))
time = float(input("Enter the time (in years): "))

amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

print("Compound Interest is:", compound_interest)
