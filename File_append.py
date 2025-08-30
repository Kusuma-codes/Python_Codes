# Program to append to a file
file_name = "example.txt"

with open(file_name, "a") as f:
    f.write("This is a new line.\n")

print("Data appended successfully!")
