class Person:
    def __init__(self, fullname):
        self.name = fullname
fullname = input("")
print("Hello", Person(fullname).name)