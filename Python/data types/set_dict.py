'''
# set
Numbers = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}  # Duplicate values will be removed
print(Numbers)

# adding values to set
Numbers.add(6)
print(Numbers)

# adding duplicate values to set
Numbers.add(3)  # Duplicate value will not be added
print(Numbers)

#removing values from set
Numbers.remove(2)  # Removes 2 from the set
print(Numbers)

# discarding values from set
Numbers.discard(5)  # Discards 5 from the set if it exists
Numbers.discard(10)  # Discards 10 from the set if it exists (no error if it doesn't exist)
print(Numbers)

# clearing the set
Numbers.clear()  # Removes all elements from the set
print(Numbers)  # Output: set()

#checking membership in set
# Numbers = {1, 2, 3, 4, 5}
print(3 in Numbers)  # Output: True
print(6 in Numbers)  # Output: False
'''


# dictionary
# Creating a dictionary
Person1 = {
    'name': 'Vishnu',
    'age': 31,
    'city': 'Bengaluru'
}
Person2 = {
    'name': 'Vyshu',
    'age': 23,
    'city': 'Chennai'
}
Person3 = {
    'name': 'Ram',
    'age': 31,
    'city': 'Hyderabad'
}
Person4 = {
    'name': 'Sahishna',
    'age': 28,
    'city': 'Hyderabad'
}

# Accessing values in a dictionary
print(Person1['name'])  # Output: Vishnu
print(Person1['age'])   # Output: 31


# change value in a dictionary
Person1['city'] = 'Venkatagiri'
print(Person1['city'])  # Output: Venkatagiri

Person2['city'] = 'Hyderabad'
print(Person2['city'])  # Output: Hyderabad

# add new key-value pair to a dictionary
Person1['job role'] = 'Administrator'
Person2['job role'] = 'AI Engineer'
Person3['job role'] = 'Data Engineer'
Person4['job role'] = 'Support Engineer'
print(Person1['job role'])  # Output: Administrator
print(Person2['job role'])  # Output: AI Engineer
print(Person3['job role'])  # Output: Data Engineer
print(Person4['job role'])  # Output: Support Engineer

print (Person1)

# remove key-value pair from a dictionary
Person1.pop('age')
print(Person1)  # Output: {'name': 'Vishnu', 'city': 'Venkatagiri', 'job role': 'Administrator'}

# check if a key exists in a dictionary
if 'age' in Person1:
    print("Age exists in Person1")
else:
    print("Age does not exist in Person1")  # Output: Age does not exist in Person1


# remove key-value pair from all dictionaries
people = [Person1, Person2, Person3, Person4]
for person in people:
    person.pop('age', None)  # Remove 'age' key if it exists, do nothing if it doesn't exist
print(person)  # Output: {'name': 'Vishnu', 'city': 'Venkatagiri', 'job role': 'Administrator'}, etc.
print(people)  # Output: [{'name': 'Vishnu', 'city': 'Venkatagiri', 'job role': 'Administrator'}, {'name': 'Vyshu', 'city': 'Hyderabad', 'job role': 'AI Engineer'}, {'name': 'Ram', 'city': 'Hyderabad', 'job role': 'Data Engineer'}, {'name': 'Sahishna', 'city': 'Hyderabad', 'job role': 'Support Engineer'}]
