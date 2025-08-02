try:
    # Attempt to open a non-existent file
    file_name = input("Enter filename to read: ")
    with open(file_name, 'r') as file:
        content = file.read()
        print("\nFile content:\n", content)

except FileNotFoundError:
    print("Error: The file was not found.")

except PermissionError:
    print("Error: You don’t have permission to read this file.")

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("File read attempt completed.")
