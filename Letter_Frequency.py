sentence = "I am a Python developer"
without_space = sentence.replace(" ","")
sentence1 = without_space.lower()
frequency = {l:0 for l in sentence1}

for i in sentence1:
    frequency[i] += 1

print(f"Each letter frequency")

for l in frequency:
    print(f"{l} = {frequency[l]}")