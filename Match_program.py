def print_week(day_number):
    match day_number:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Invalid day number (must be 1 to 7)")
            
day = int(input("Enter a day number (1-7): "))
print_week(day)
