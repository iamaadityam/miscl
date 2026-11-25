class Person:
    def __init__(self, fullname):
        self.name = fullname
        print(self.name)
fullname = input("")
print("Hello")
Person(fullname)