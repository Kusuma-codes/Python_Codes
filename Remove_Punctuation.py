# Python Program to Remove Punctuations From a String

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

text = input("Enter a string: ")

no_punct = ""
for char in text:
    if char not in punctuations:
        no_punct = no_punct + char

print("String without punctuations:", no_punct)
