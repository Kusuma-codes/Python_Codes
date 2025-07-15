sentence = "Python is the best programming language"
print(sentence)
without_vowel = []

for char in sentence:
    without_vowel.append(char)
    if char in "AEIOUaeiou":
        without_vowel.remove(char)
without_vowel1 = "".join(without_vowel)
print(without_vowel1)