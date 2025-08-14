# Menu-driven Math Program using math library

import math

print("Math Operations:")
print("1. Square Root")
print("2. Power")
print("3. Factorial")
print("4. Trigonometric (sin, cos, tan)")
print("5. Logarithm (base e)")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    num = float(input("Enter a number: "))
    print("Square root:", math.sqrt(num))

elif choice == 2:
    base = float(input("Enter base: "))
    exp = float(input("Enter exponent: "))
    print("Power:", math.pow(base, exp))

elif choice == 3:
    num = int(input("Enter an integer: "))
    print("Factorial:", math.factorial(num))

elif choice == 4:
    angle = float(input("Enter angle in degrees: "))
    rad = math.radians(angle)
    print("sin:", math.sin(rad))
    print("cos:", math.cos(rad))
    print("tan:", math.tan(rad))

elif choice == 5:
    num = float(input("Enter a number: "))
    print("Logarithm base e:", math.log(num))

else:
    print("Invalid choice!")
