# Python Program to Add a Tuple to the List

my_list = [10, 20, 30]
my_tuple = (40, 50)

my_list.append(my_tuple)

print("After adding tuple as element:", my_list)

my_list2 = [10, 20, 30]
my_list2.extend(my_tuple)

print("After adding tuple elements individually:", my_list2)
