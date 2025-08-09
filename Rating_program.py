# Rating Program

rating = int(input("Rate our service (1 to 5): "))

if rating == 5:
    print("Excellent! Thank you for the great rating 🌟🌟🌟🌟🌟")
elif rating == 4:
    print("Very Good! We’re glad you liked it 🌟🌟🌟🌟")
elif rating == 3:
    print("Good! We will work to improve 🌟🌟🌟")
elif rating == 2:
    print("Fair! We appreciate your feedback 🌟🌟")
elif rating == 1:
    print("Poor! We will work harder to make it better 🌟")
else:
    print("Invalid rating! Please enter a number between 1 and 5.")
