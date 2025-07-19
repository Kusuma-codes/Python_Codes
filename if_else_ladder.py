num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("The number is Zero.")
    else:
        print("The number is Positive.")
        if num % 2 == 0:
            print("It is also Even.")
        else:
            print("It is also Odd.")
else:
    print("The number is Negative.")
