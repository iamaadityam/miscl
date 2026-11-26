class Person:
    college = "IIITD" #class attribute

    def __init__(self, fullname, marks):
        self.name = fullname #name = object fattribute
        self.marks = marks
    def hello(self):
        print("Hello,", self.name)

fullname = input("")
marks1 = int(input())
s1 = Person(fullname, marks1) #creating an object s1 in the class Person
s1.hello()

name = input()
marks2 = int(input())
s2 = Person(name, marks2) #object s2
print(s2.name, s2.marks)

print(s2.college) #class attribute, common for all objects