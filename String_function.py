def string_functions():
    text = "  Hello, World!  "

    print("Original text:", text)

    # Remove leading/trailing spaces
    stripped = text.strip()
    print("Stripped:", stripped)

    # Convert to uppercase
    print("Uppercase:", stripped.upper())

    # Convert to lowercase
    print("Lowercase:", stripped.lower())

    # Replace word
    print("Replace 'World' with 'Python':", stripped.replace("World", "Python"))

    # Find position of a substring
    print("Index of 'World':", stripped.find("World"))

    # Check if starts with
    print("Starts with 'Hello':", stripped.startswith("Hello"))

    # Length of string
    print("Length:", len(stripped))

# Call the function
string_functions()
