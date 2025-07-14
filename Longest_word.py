sentence = "Python is lovely language"
words = sentence.split()
max_length = 0

for word in words:
    if len(word) > max_length:
        longest_word = word
        max_length = len(word)

print("The longest word is:", longest_word)
print("Length:", max_length)
