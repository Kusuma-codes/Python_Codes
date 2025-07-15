num1 = input("Enter Numbers: ")
num = list(map(int, num1.split()))
frequency = {f:0 for f in num}
for i in num:
    frequency[i] += 1
for f in sorted(frequency):
    print(f"{f} = {frequency[f]}")