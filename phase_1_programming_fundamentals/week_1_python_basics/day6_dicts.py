#Python Dictionary-based Student Record System
#System Design
#We will store data like this:
#dicts.py
students={
    "101":{
        "name":"MD GHULAM JEELANI",
        "age":13,
        "courses":["QURAN SHAREEF","AI ENGINEERING"] 
    },
    "102":{
        "name":"MD ZEESHAN",
        "age":20,
        "courses":["AI ENGINEERING"]
    }
}
def add_student(student_id,name,age):
    if student_id in students:
        print("Student already exists!")
    else:
        students[student_id]={
            "name":name,
            "age":age,
            "courses":[]
        }
        print("student added successfully")

def add_course(student_id, course):
    if student_id in students:
        students[student_id]["courses"].append(course)
        print("Course added successfully")
    else:
        print("Student not found")

def view_student(student_id):
    if student_id in students:
        s=students[student_id]
        print("Name:",s["name"])
        print("Age:",s["age"])
        print("courses:",",".join(s["courses"]))
    else:
        print("student not found")

def remove_student(student_id):
    if student_id in students:
        del students[student_id]
        print("Student removed")
    else:
        print("Student not found")

add_student("103","MD SHABBIR",35)
add_student("104","MD MUSAWWIR",33)

add_course("103","HISTORY")
add_course("103","GEOGRAPHY")
add_course("104","PHYSICS")
add_course("104","CHEMISTRY")
add_course("104","BIOLOGY")

view_student("101")
view_student("104")

remove_student("102")
remove_student("103")
print(students)




