# dicts.py


# 1. Basic dictionary
student = {
    "name": "Zeeshan",
    "marks": 90
}


# 2. Operations

# Access
print(student["name"])
print(student["marks"])


# Add/Update
student["age"] = 20
student["marks"] = 95

print("After update:", student)


# Delete
del(student["marks"])
del(student["age"])

print(student)


# Safe Access (important)
print(student.get("age"))


# 3. Loop through Dictionary
for key, value in student.items():
    print(key, value)


# 4. Word Frequency Counter
text = "ai is future ai is power"

words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)


# 5. Student Database
students = {
    "Zeeshan": 90,
    "Ali": 85,
    "Jeelani": 95
}

# find topper
topper = max(students, key=students.get)
print(topper)

# 6. Key Exists Check
if "Zeeshan" in students:
    print("Exists")