# Arithmetic Operators Program

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Performing operations
print("\nArithmetic Operations:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b if b != 0 else "Error! Division by zero")
print("Modulus:", a % b)
print("Exponentiation (a^b):", a ** b)
print("Floor Division:", a // b if b != 0 else "Error! Division by zero")
