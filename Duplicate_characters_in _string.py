# Find all duplicate characters in a string
from collections import Counter

text = "programming"

freq = Counter(text)

duplicates = [char for char, count in freq.items() if count > 1]

print("Duplicate characters:", duplicates)
