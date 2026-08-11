# file handling
file = open('example.txt', 'w')  # Open a file in write mode
file.write('Hello, World!\n')  # Write a string to the file
file.write('This is a test file.\n')  # Write another string to the file
file.write('Jai Vysh.\n')  # Write another string to the file
file.close()  # Close the file



file = open('example.txt', 'r')  # Open the file in read mode
content = content.replace('Jai Vysh', 'torcher Vyshu')  # Replace a string in the content
print(file.read())  # Print the content to the console
file.close()  # Close the file
