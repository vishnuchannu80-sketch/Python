#String DataType
name = "Arjunn"
city = "USA"
lang = "Python"
print(name)
print(city)
print(lang)
# Check DataType
print(type(name))
# Single and Double Quotes
msg1 = 'Hello'
msg2 = "Bye"
print(msg1)
print(msg2)
# String Concatenation
first = "Arjunn"
last = "arjun"
fullname = first + " " + last
print("Full Name:", fullname)
# String Length
text = "Python"
print("Length:", len(text))
# String Indexing
print("First Char:", text[0])
print("Second Char:", text[1])
print("Last Char:", text[-1])
# String Slicing
print("First 3 Char:", text[0:3])
print("From index 2:", text[2:])
# String Methods
sam = "python basics"
print("Upper:", sam.upper())
print("Lower:", sam.lower())
print("Title:", sam.title())
# Replace
print("Replace:", sam.replace("python", "Java"))
# Check text
print("python" in sam)
# F-String
name = "Arjunn"
age = 1
print(f"My name is {name} and I am {age} years old.")