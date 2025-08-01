# Open the file in read mode
with open('sample.txt', 'r') as file:
    # Read all lines and count them
    lines = file.readlines()
    line_count = len(lines)

# Print the result
print("Number of lines in the file:", line_count)
