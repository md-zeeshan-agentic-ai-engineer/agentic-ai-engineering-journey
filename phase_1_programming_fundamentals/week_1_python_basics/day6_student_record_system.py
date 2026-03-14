#Python Dictionary-based Student Record System
#System Design
#We will store data like this:
students={
    "101":{
        "name":"MD GULAM JILANI",
        "age":13,
        "courses":["QURAN","AI ENGINEERING"]
    },
    "102":{
        "name":"MD SHABBIR ALAM",
        "age":35,
        "courses":["BA","BEd"]
    },
    }
def add_student(student_id,name,age):
    if student_id in students:
        print("student already exists!")
    else:
        students[student_id]={
            "name":name,
            "age":age,
            "courses":[]
        }
        print("student added successfully")
add_student("103","MD UMAR",55)
print(students)
#students:-main dictionary,"101","102"...:-student IDs(keys),name age class:-students detail.
#kiya yahan course me bhi list sign lagana hai?
#yes,Course order+ duplicate + future update ke liye better hota hai.




























