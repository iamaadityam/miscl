class Person:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = "name"
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def marks(self):
        return (self.marks1 + self.marks2 + self.marks3)/3

name = input()
marks1 = int(input())
marks2 = int(input())
marks3 = int(input())

p1 = Person(name, marks1, marks2, marks3)
print(p1.marks())