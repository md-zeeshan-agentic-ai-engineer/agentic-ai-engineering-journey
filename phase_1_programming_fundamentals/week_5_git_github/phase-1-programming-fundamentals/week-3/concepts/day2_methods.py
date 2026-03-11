# Learn Section

# 1. Instance Methods

class Student:
    def show(self):     # show() -> instance methods
        print("Hello")

s1 = Student()
s1.show()

# Task 1
class Student:
    def set_data(self, name, age):
        self.name = name   # self.name -> name of object
        self.age = age     # self.age -> age of object

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student()    # object create
s2 = Student()
s3 = Student()

s1.set_data("ZEESHAN", 20)
s2.set_data("GHULAM JILANI", 13)
s3.set_data("MD MOHIT", 11)

s1.show()    # method call
s2.show()
s3.show()

# Task 2
class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show(self):
        print("Brand:", self.brand)
        print("Price:", self.price)

s1 = Car("TATA", 800000)
s1.show()

# 2. self
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

s1 = Student("MD ZEESHAN KHAN")
s1.display()


# Store multiple students in list and print through loop
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

students = []

s1 = Student("MD ZEESHAN", 20)
s2 = Student("MD GHULAM JEELANI", 13)
s3 = Student("MD MOHIT KHAN",11)
s4 = Student("MD MAHIR KHAN", 9)

students.append(s1)
students.append(s2)
students.append(s3)
students.append(s4)

for s in students:
    s.display()


# Build Section

# step 1. Make class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)

# step 2. Make multiple objects
students = []

s1 = Student("MD MASOOD KHAN", 80)
s2 = Student("MD HASNAIN KHAN", 85)
s3 = Student("MD SAJAR KHAN", 90)
s4 = Student("MD MANZAR KHAN", 95)
s5 = Student("MD SHABBIR KHAN", 100)

# step 3. Store in list
students.append(s1)
students.append(s2)
students.append(s3)
students.append(s4)
students.append(s5)

# step 4. Print through loop

for s in students:
    s.display()