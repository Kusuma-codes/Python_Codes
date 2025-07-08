a = "I am Python Developer"
sentence = a.lower()
print(sentence)

vowels = "aeiou"
each_vowel = {v:0 for v in vowels}

vowel_count = 0

for char in sentence:
    if char in vowels:
        vowel_count += 1
        each_vowel[char] +=1

print(f"Total vowel count: {vowel_count}")
print("Each vowel count")
for v in vowels:
   print(f"{v} = {each_vowel[v]}")