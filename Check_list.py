my_list = [10, 20, 30, 40, 50]
element = int(input("Enter the element to check: "))

if element in my_list:
    print(f"{element} is present in the list.")
else:
    print(f"{element} is not present in the list.")
