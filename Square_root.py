# Square Root of a Number

import math
num = float(input("Enter a number: "))

if num >= 0:
    sqrt_value = math.sqrt(num)
    print("The square root of", num, "is:", sqrt_value)
else:
    print("Square root is not defined for negative numbers in real numbers.")
