numbers = [1,3,3,4,6,3,1,6,8,0,8,5]
unique_list = []

for num in numbers:
    if num not in unique_list:
        unique_list.append(num)
    
print(f"Before removing duplicates: {numbers}")
print(f"Afrer removing duplicates: {sorted(unique_list)}")
