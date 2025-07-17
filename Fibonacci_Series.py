def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

terms = int(input("Enter how many terms you want: "))
fibonacci(terms)
