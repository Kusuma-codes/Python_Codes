char = "Hello123@-52"
alphabet_count = 0
digit_count = 0
special_charcter_count = 0
print(char)
for i in char:
    if i.isalpha():
        alphabet_count += 1
    elif i.isdigit():
        digit_count += 1
    else:
        special_charcter_count +=1

print(f"Alphabets count: {alphabet_count}")
print(f"Digit count: {digit_count}")
print(f"Special character count: {special_charcter_count}")
