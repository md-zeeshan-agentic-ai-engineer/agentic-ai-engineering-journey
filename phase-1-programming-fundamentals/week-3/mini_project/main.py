# main.py
from manager import StudentManager
manager = StudentManager()
while True:
    print("\n 1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4.Update Marks")
    print("5. Total Student Count")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        roll_no = input("Enter roll_number: ")
        marks = int(input("Enter marks: "))
        manager.add_student(name, roll_no, marks)

    elif choice == "2":
        manager.show_students()

    elif choice == "3":
        roll = input("Enter roll_no: ")
        manager.search_student(roll)

    elif choice == "4":
        roll = input("Enter roll_no")
        new_marks = int(input("Enter new_marks"))
        manager.update_marks(roll, new_marks)

    elif choice == "5":
        manager.total_students()

    elif choice == "6":
        break

    else:
        print("Invalid choice!")