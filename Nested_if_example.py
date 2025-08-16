# Nested if example

num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("The number is Zero")
    else:
        if num % 2 == 0:
            print("The number is Positive and Even")
        else:
            print("The number is Positive and Odd")
else:
    print("The number is Negative")
