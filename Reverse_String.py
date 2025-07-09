num = input("Enter a number: ")

if num.startswith('-'):
    reversed_num = '-' + num[:0:-1]
else:
    reversed_num = num[::-1]

print(f"Reversed number: {int(reversed_num)}")
