#Remove empty tuples from a list
my_list = [(1, 2), (), (3, 4), (), (5, 6)]
filtered_list = [t for t in my_list if t]
print("List after removing empty tuples:", filtered_list)
