# Find the least frequent character in a string
from collections import Counter

text = "success"

freq = Counter(text)
least_char = min(freq, key=freq.get)

print("Least frequent character:", least_char)
