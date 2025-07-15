a = input("Enter a String: ")
char = a.lower()
char1= char[::-1]
if char == char1:
   print("Given Word is palindrome...")
else:
   print("Given Word is not palindrome...!")