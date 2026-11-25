class Person:
    def __init__(self, fullname, marks):
        self.name = fullname #name = attribute
        self.marks = marks

fullname = input("")
marks1 = int(input())
s1 = Person(fullname, marks1) #creating an object s1 in the class Person
print("Hello", s1.name, s1.marks)

name = input()
marks2 = int(input())
s2 = Person(name, marks2) #object s2
print(s2.name, s2.marks)