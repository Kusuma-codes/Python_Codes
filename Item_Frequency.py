items = ["apple", "banana", "apple", "orange", "banana", "apple","Grape"]
frequency = {i:0 for i in items}

for item in items:
    if item in items:
        frequency[item] += 1
    else:
        print(f"{item} not in list")

print("Item frequency:")
for key, value in frequency.items():
    print(f"{key} : {value}")