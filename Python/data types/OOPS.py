# oops
'''
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old. I live in {self.city}.")

person1 = Person("Vishnu", 31, "Venkatagiri")
person2 = Person("Vyshu", 23, "Hyderabad")
person3 = Person("Ram", 31, "Hyderabad")
people = [person1, person2, person3]
for person in people:
    person.greet()
'''

class Person:
    def greet(self):
            print(f"Hello, my name is {self.name} and I am {self.age} years old. I live in {self.city}.")
person1 = Person()
person1.name = "Vishnu"
person1.age = 31
person1.city = "Venkatagiri"
person2 = Person()
person2.name = "Vyshu"
person2.age = 23
person2.city = "Hyderabad"
    
people = [person1, person2]
    

for person in people:
    person.greet()