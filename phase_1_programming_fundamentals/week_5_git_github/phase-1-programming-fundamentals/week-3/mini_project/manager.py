from student import Student

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_no, marks):
        student = Student(name, roll_no, marks)
        self.students.append(student)
        print("Student added successfully!")

    def show_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students:
                student.display()

    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                student.display()
                return
            print("Student not found.")

    def update_marks(self, roll_no, new_marks):
        for student in self.students:
            if student.roll_no == roll_no:
                student.marks = new_marks
                print("Marks updated successfully!")
                return
            print("Student not found.")

    def total_students(self):
        print(f"Total students: {len(self.students)}")