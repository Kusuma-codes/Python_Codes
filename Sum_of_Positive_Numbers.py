num1 = input("Enter Numbers:")
num = list(map(int,num1.split()))
sum = 0
positive_number = []
for i in num:
    if i > 0:
        sum += i
        positive_number.append(i)
print(f"Positive Numbers are: {positive_number}")
print(f"Sum of Positive Numbers : {sum}")
