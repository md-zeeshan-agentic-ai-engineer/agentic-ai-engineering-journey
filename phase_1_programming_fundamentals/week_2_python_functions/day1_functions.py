# WEEK-2,DAY-1(FUNCTIONS+LOGIC)


# 1. LEARN:-

def add(a,b):
    return a+b

print(add(5,15))

# 2. Build:- Utility Functions Pack

#A. Calculator Function
def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b

print(add(10,5))
print(sub(10,5))
print(mul(10,5))
print(div(10,5))

# Professional way user input
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("add:",add(a,b))
print("sub:",sub(a,b))
print("mul:",mul(a,b))
print("div:",div(a,b))

a=int(input("20: "))
b=int(input("10: "))
print("add:",add(a,b))
print("sub:",sub(a,b))
print("mul:",mul(a,b))
print("div:",div(a,b))


#B. Number Utilities
def is_even(n):
    return n % 2 == 0

def square(n):
    return n*n

print(is_even(8))
print(square(5))

# C. AI Engineer Level Practice Functions
def normalize(nums):
    total = sum(nums)
    return [x/total for x in nums]

def mean(nums):
    return sum(nums)/len(nums)

nums=[10,20,30,40]

print("Normalized:",normalize(nums))
print("Mean:",mean(nums))

# Ab next level challange(AI Engineer Mode ON)
nums=list(map(int,input("Enter numbers separated by space:").split()))
print("Normalize:",normalize(nums))
print("Mean:",mean(nums))

# 3. Logic Practice (Mandatory)
def max_of_three(a,b,c):
    return max(a,b,c)

def grade(marks):
    if marks >=90: return "A"
    elif marks >=75: return "B"
    elif marks >=60: return "C"
    else: return "Fail"

print("Max_of_three:",max_of_three(25,50,75))
print("Grade:",grade(100))

def grade(marks):
    if marks >=90: return "A"
    elif marks >=75: return "B"
    elif marks >=60: return "C"
    else: return "Fail"

marks=int(input("Enter marks: "))
print("Grade:",grade(90))

# 4. Mini Project — Smart Utility Tool 🛠️

#Menu-based program banao:

#1. Add
#2. Sub
#3. Mul
#4. Div
#5. Square
#6. Even/Odd

# Smart Utility Tool - Mini Project
def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b
def square(n): return n*n
def is_even(n): return n % 2 == 0

print("===== Smart Utility Tool =====")
print("1. Add")
print("2. Sub")
print("3. Mul")
print("4. Div")
print("5. Square")
print("6. Even/Odd")

choice=int(input("Enter your choice: "))
if choice in [1,2,3,4]:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))

if choice == 1:
    print("Result:",add(a,b))
elif choice == 2:
    print("Result:",sub(a,b))
elif choice == 3:
    print("Result:",mul(a,b))
elif choice == 4:
    print("Result:",div(a,b))
elif choice == 5:
    n=int(input("Enter number "))
    print("Square:",square(n))
elif choice == 6:
    n=int(input("Enter number: "))
    print("Result:",is_even(n))
else:
    print("Invalid Choice")
