# Generate a random number between 1 and 100
import random  
number_to_guess = random.randint(1, 100)

print("Welcome to Guess the Number Game!")
print("I have chosen a number between 1 and 100. Can you guess it?")

while True:
    guess = int(input("Enter your guess: "))

    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it right.")
        break
