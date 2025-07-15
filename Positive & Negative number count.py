num1 = input("Enter Numbers:")
num = list(map(int,num1.split()))
#print(num)
positive_count = 0
negative_count = 0
zero_count = 0

for i in num:
    if i == 0:
        zero_count += 1
    elif i > 0:
        positive_count += 1
    else:
        negative_count +=1

print("Zero Count = ",zero_count)
print("Positive Numbers Count = ",positive_count)
print("Negative Count = ",negative_count)
