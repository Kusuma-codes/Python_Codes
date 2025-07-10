num = [1, 5, 6, 8, 7, 3, 9]
even_numbers = []
odd_numbers = []
sum_of_even_num = 0
sum_of_odd_num = 0

for i in num:
    if(i%2 == 0):
        sum_of_even_num += i
        even_numbers.append(i)
    else:
        sum_of_odd_num += i
        odd_numbers.append(i)

print(f"Even numbers: {sorted(even_numbers)}")
print(f"Sum of even numbers: {sum_of_even_num}")
print(f"Odd numbers: {sorted(odd_numbers)}")
print(f"Sum of odd numbers: {sum_of_odd_num}")