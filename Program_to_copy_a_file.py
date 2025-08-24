# Program to copy a file
import shutil

source_file = "source.txt"
destination_file = "destination.txt"

try:
    shutil.copyfile(source_file, destination_file)
    print("File copied successfully!")
except FileNotFoundError:
    print("Source file not found.")
except Exception as e:
    print("Error:", e)
