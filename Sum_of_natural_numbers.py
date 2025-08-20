n = int(input("Enter a number: "))

sum_formula = n * (n + 1) // 2

sum_loop = 0
for i in range(1, n + 1):
    sum_loop += i

print(f"Sum of first {n} natural numbers using formula = {sum_formula}")
print(f"Sum of first {n} natural numbers using loop = {sum_loop}")
