my_list = [10, 20, 30, 40, 50]
print("Original list:", my_list)

pos1 = int(input("Enter the first index to swap: "))
pos2 = int(input("Enter the second index to swap: "))

# Swapping
my_list[pos1], my_list[pos2] = my_list[pos2], my_list[pos1]

print("List after swapping:", my_list)
