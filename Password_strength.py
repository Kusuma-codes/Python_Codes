import re

def check_password_strength(password):
    if len(password) < 6:
        return "Weak: Password too short"

    # Patterns
    lowercase = re.search(r"[a-z]", password)
    uppercase = re.search(r"[A-Z]", password)
    digit = re.search(r"\d", password)
    special_char = re.search(r"[@#$%^&+=!]", password)

    # Strong: All types included
    if lowercase and uppercase and digit and special_char and len(password) >= 8:
        return "Strong Password"

    # Moderate: At least 3 types
    elif (lowercase and uppercase and digit) or (lowercase and digit and special_char):
        return "Moderate Password"

    # Weak: Less than 3 types
    else:
        return "Weak Password"

# Input from user
password = input("Enter your password: ")
strength = check_password_strength(password)
print("Password strength:", strength)
