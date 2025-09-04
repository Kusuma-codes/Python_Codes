# Python Program to Find Maximum and Minimum K Elements in Tuple

my_tuple = (5, 10, 2, 8, 15, 1, 20)
K = 3

sorted_list = sorted(my_tuple)

min_k = sorted_list[:K]

max_k = sorted_list[-K:]

print("Tuple:", my_tuple)
print(f"Smallest {K} elements:", min_k)
print(f"Largest {K} elements:", max_k)
