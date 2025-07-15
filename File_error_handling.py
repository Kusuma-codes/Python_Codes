def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File Content:\n", content)
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except PermissionError:
        print(f"You do not have permission to read '{filename}'.")
    else:
        print("File read successfully.")
    finally:
        print("File reading operation completed.")

# Example usage
file_name = input("Enter the file name to read: ")
read_file(file_name)
