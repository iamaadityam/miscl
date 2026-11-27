class Person:
    def __init__(self, name, marks):
        self.name = "name"
        self.marks1 = marks[0]
        self.marks2 = marks[1]
        self.marks3 = marks[2]

    def marks(self):
        return (self.marks1 + self.marks2 + self.marks3)/3

name = input()
marks = []
for i in range(3):
    marks.append(int(input()))
    i = i + 1

p1 = Person(name, marks)
print(p1.marks())