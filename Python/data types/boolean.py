# Boolean Variables
user = True
loggedin = False

# Print Boolean Values
print(user)        #Op: True
print(loggedin)    #Op: False

# Check Data Type
print(type(user))  #Op: <class 'bool'>


# Comparison Operators
# Comparison result eppudu True leda False untundi

print(10 > 5)      #True (10 is greater than 5)
print(10 < 5)      #False (10 is not less than 5)
print(10 == 10)    #True (Both values are equal)
print(10 != 5)     #True (10 and 5 are not equal)
print(10 >= 5)     #True (10 is greater than or equal to 5)
print(10 <= 5)     #False (10 is not less than or equal to 5)
age = 20
# Check whether age is greater than or equal to 18
print(age >= 18)   #op: True
# if-else Statement
# If age is 18 or above .... Eligible to Vote
# Otherwise ... Not Eligible to Vote
if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")
# bool() Function
# Converts different values into True or False
print(bool(1))         # True  Non-zero number
print(bool(0))         # False Zero
print(bool("Python"))  # True   Non-empty String
print(bool(""))        # False  Empty String
print(bool([]))        # False  Empty List
print(bool([1, 2, 3])) # True  List contains values