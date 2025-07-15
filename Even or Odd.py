num = input("Enter numbers separated by space:")
a = list(map(int,num.split()))
print(a)

even_count = 0
odd_count = 0
even_numbers = []
odd_numbers = []

for i in a:
    if i % 2 == 0:
        even_count += 1
        even_numbers.append(i)
        
    else:
        odd_count += 1
        odd_numbers.append(i)

odd = set(odd_numbers)
even = set(even_numbers)

print(f" Even number count is {even_count}, Even Numbers are: {even}")
print(f" Odd number count is {odd_count}, Odd Numbers are: {odd}")
