#1️⃣ Dictionaries (dict)
# Key → Value data structure
#Basics
student={"name":"Rahul","age":30,"class":"PhD","city":"Mumbai","religion":"non_muslim","marks":80}
print(student["name"])
print(student["class"])
print(student)
print(student["city"])
print(student["age"])
print(student.keys())
print(student.values())
print(student.items())
print(student.get("age"))
print(student.get("class"))
print(student.get("city"))
#Access / Update
student["name"]        # Rahul
student["marks"] = 90
#Important Methods
student.keys()
student.values()
student.items()
student.get("age")
#Loop
#Dictionary Loop
for key,value in student.items():
    print(key,":",value)
#Sirf keys
for key in student.key():
    print(key)
#Sirf values
for value in student.values():
    print(value)
#2️⃣ Sets (set)
# Unique + Unordered collection
#Basics
nums = {1, 2, 3, 3, 4}
print(nums)   # {1,2,3,4}
#Add / Remove
nums.add(5)
nums.remove(2)
#Set Operations (🔥 important)
a = {1,2,3}
b = {3,4,5}

a | b   # union
a & b   # intersection
a - b   # difference

#👉 Dict + Set ka ek example khud likhna (without copy)
students={"Rahul":77,"Aman":80,"Karan":77}
marks={77,80,77}
print(student)
print(marks)





