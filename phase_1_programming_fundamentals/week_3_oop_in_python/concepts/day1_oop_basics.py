class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    def is_pass(self):
        if self.marks >= 30:
            print("Result: Pass")
        else:
            print("Result: Fail")

s1 = Student("MD ZEESHAN KAHN", 90)
s2 = Student("MD GHULAM JILANI", 95)

s1.display()
s1.is_pass()
s2.display()
s2.is_pass()