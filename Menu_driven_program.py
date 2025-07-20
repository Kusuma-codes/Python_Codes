# Menu-driven program to perform different checks

print("===== MENU =====")
print("1. Check if number is Even or Odd")
print("2. Check if number is Positive or Negative or Zero")
print("3. Find Greatest of Two Numbers")
print("=================")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("The number is Even.")
    else:
        print("The number is Odd.")

elif choice == 2:
    num = int(input("Enter a number: "))
    if num > 0:
        print("The number is Positive.")
    elif num < 0:
        print("The number is Negative.")
    else:
        print("The number is Zero.")

elif choice == 3:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if a > b:
        print(f"{a} is greater.")
    elif b > a:
        print(f"{b} is greater.")
    else:
        print("Both numbers are equal.")

else:
    print("Invalid choice. Please select option 1, 2 or 3.")
