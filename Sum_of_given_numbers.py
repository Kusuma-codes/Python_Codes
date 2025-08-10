# Sum of given numbers

numbers = input("Enter numbers separated by space: ")

num_list = numbers.split()

total = sum(int(num) for num in num_list)

# Displaying result
print("Sum of given numbers:", total)
