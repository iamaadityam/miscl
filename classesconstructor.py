class Person:
    def __init__(self, fullname):
        self.name = fullname #name = attribute

fullname = input("")
s1 = Person(fullname) #creating an object s1 in the class Person
print("Hello", s1.name)

name = input()
s2 = Person(name) #object s2
print(s2.name)