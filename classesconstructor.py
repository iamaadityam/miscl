class Person:
    college = "IIITD" #class attribute

    def __init__(self, fullname, marks):
        self.name = fullname #name = object fattribute
        self.marks = marks

    def hello(self): #function defined inside class
        print("Hello,", self.name)

    def welcome(self):
        print("welcome,", self.name)

fullname = input("")
marks1 = int(input())
s1 = Person(fullname, marks1) #creating an object s1 in the class Person
s1.hello()

name = input()
marks2 = int(input())
s2 = Person(name, marks2) #object s2
print(s2.name, s2.marks)
s2.welcome()
print(s2.college) #class attribute, common for all objects