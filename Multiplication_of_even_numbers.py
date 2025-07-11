def multiplication_of_even(number):
    even_mul = 1
    for i in number:
        if i % 2 == 0:
            even_mul *= i
    print(even_mul)
num = [1, 2, 3, 4]
multiplication_of_even(num)

