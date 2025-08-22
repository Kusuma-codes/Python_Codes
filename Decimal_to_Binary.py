# Decimal to Binary without built-in function
decimal = int(input("Enter a decimal number: "))
binary = ""

num = decimal
while num > 0:
    binary = str(num % 2) + binary
    num = num // 2

print("Binary value is:", binary)
