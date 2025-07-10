sentence = "I am Python developer"
word = sentence.split()
word_count = len(word)
vowel_count = 0
consonants_count = 0

for char in sentence:
    if char.isalpha():
      if char in "aeiouAEIOU":
        vowel_count += 1
      else:
        consonants_count += 1

print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonants_count}")
print(f"Words: {word_count}")
         