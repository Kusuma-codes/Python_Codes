# Count how many times each word appears in the string
text = "this is a test this is only a test"
words = text.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print("Word frequency:")
for word, count in frequency.items():
    print(word, ":", count)
