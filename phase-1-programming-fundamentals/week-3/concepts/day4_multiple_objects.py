# 1. List of Objects
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, I am", self.name)

# Multiple objects
s1 = Student("MD ZEESHAN", 20)
s2 = Student("MD GHULAM JILANI", 13)
s3 = Student("MD MOHIT", 11)
s4 = Student("MD MAHIR", 9)
s5 = Student("MD HASNAIN", 7)

# List of objects
students = [s1, s2, s3, s4, s5]

# 2. Loop Through Objects
for student in students:
    print(student.name, student.age)

for student in students:
    student.greet()