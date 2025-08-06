def divide(a, b):
    try:
        result = a / b
        print("Division Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

# Example usage
num1 = float(input("Enter numerator: "))
num2 = float(input("Enter denominator: "))

divide(num1, num2)
