# Interchange first and last elements in a list

def swap_first_last(lst):
    if len(lst) < 2:
        return lst  
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

numbers = swap_first_last(numbers)
print("List after swapping:", numbers)
