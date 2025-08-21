# Program to find the LCM of two numbers

def find_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"The LCM of {num1} and {num2} is {find_lcm(num1, num2)}")
