# Find mirror characters in a string
mirror_dict = {
    'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O',
    'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
    'Y': 'Y', 'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'
}

text = "AIMbdpqXYZ"

mirror_chars = []

for char in text:
    if char in mirror_dict:
        mirror_chars.append((char, mirror_dict[char]))

print("Mirror characters found:")
for char, mirror in mirror_chars:
    print(char, "->", mirror)
