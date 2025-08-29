# Program to create a countdown timer
import time

seconds = 10
while seconds:
    mins, secs = divmod(seconds, 60)
    timer = f"{mins:02d}:{secs:02d}"
    print(timer, end="\r")
    time.sleep(1)
    seconds -= 1

print("Time's up!")
