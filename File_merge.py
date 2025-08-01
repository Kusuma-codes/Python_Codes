# Open the first file in read mode
with open('file1.txt', 'r') as f1:
    data1 = f1.read()

# Open the second file in read mode
with open('file2.txt', 'r') as f2:
    data2 = f2.read()

# Open the third file in write mode and write both contents
with open('merged_file.txt', 'w') as f3:
    f3.write(data1)
    f3.write(data2)

print("Files merged successfully into 'merged_file.txt'")
