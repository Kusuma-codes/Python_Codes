# Menu using match...case (Python 3.10 or newer)

print("===== MENU =====")
print("1. Greet")
print("2. Check Even or Odd")
print("3. Exit")
print("=================")

choice = int(input("Enter your choice (1-3): "))

match choice:
    case 1:
        name = input("Enter your name: ")
        print(f"Hello, {name}! Have a nice day 😊")
    
    case 2:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print("It is Even.")
        else:
            print("It is Odd.")
    
    case 3:
        print("Exiting the program. Goodbye!")

    case _:
        print("Invalid choice. Please try again.")
