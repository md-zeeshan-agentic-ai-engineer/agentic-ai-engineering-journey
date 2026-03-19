#                                       Step-1:def function

##            a. Basic example
def  greet():
    print("Hello")

##            b. With parameter
def greet(name):
    print("Hello", name)

greet("Zeeshan")

##            c. With return
def add(a, b):
    return a + b
result = add(2, 3)
print(result)
### print vs return
### . print() -> screen par show
### . return() -> value wapas bhejna

##             d. remember structure
###def naam(parameters):
###    Code
###    return value

##             e. Mini practice(do right now)

def hello():
    print("I am learning python")
    hello

def square(n):
    return n * n
print(square(4))

#                                     Step-2: Parameters + Return

##            a. Parameters (input dena function ko)
def greet(name):
    print("Hello", name)

greet("Zeeshan")


### name = parameter
### "Zeeshan" = argument

##            b. Multiple parameters
def add(a, b):
    print(a + b)

add(2, 3)

##              c. Return (value wapas dena)
def add(a, b):
    return a + b

result = add(5, 4)
print(result)


### Rule:
### return ke baad function khatam.

##              d. Difference clear karo
def test1():
    print(5)

def test2():
    return 5

x = test1()   # print karega, x = None
y = test2()   # y = 5

##              e. Mini Practice (abhi karo)
### Task-1
def multiply(a, b):
    # return product

### Task-2
# def is_even(n):
    # even ho to True return

### Task-3
# def full_name(first, last):
    # "first last" return

#                                          Step-3: Default Arguments

#       Default argument = agar user value na de, to default use hogi
# def greet(name="Guest"):
#    print("Hello", name)

#greet("Zeeshan")   # Hello Zeeshan
#greet()            # Hello Guest


#Rule
#Default parameter hamesha last me
#def add(a, b=0):
    return a + b

# ❌ Galat:
# def add(a=0, b):


# Example
# def power(base, exp=2):
    return base ** exp

#print(power(3))     # 3^2
#print(power(3, 3))  # 3^3


#                         *args (multiple values)
# Agar kitne parameters aayenge pata na ho:
def add_numbers(*nums):
    return sum(nums)

print(add_numbers(1,2,3))
print(add_numbers(5,10,20,30))

# *nums = tuple


#                      **kwargs (named values)
def info(**data):
    print(data)

info(name="Zeeshan", age=20)

# **data = dictionary


#              Mini Practice (abhi likho)
# Task-1
def greet(name="Guest"):
    # print hello name

# Task-2
# def total(*nums):
    # sabka sum return

# Task-3
# def student(**data):
    # print data

#                                Step-4: Docstring (important for real dev)

# Docstring = function kya karta hai → explanation

# def add(a, b):
    """This function returns sum of two numbers"""
 #   return a + b


# Access:

print(add.__doc__)

# Real format (industry style)
def add(a, b):
    """
    Add two numbers

    Parameters:
    a (int): first number  
    b (int): second number

    Returns:
    int: sum
    """
    return a + b

# 🔥 FINAL PRACTICE (aaj ka main task)

# Ab 5 functions likho:

#          1️⃣ add numbers
def add(a, b):
    """Return sum of two numbers"""
    return a + b
print(add(4, 5))

#          2️⃣ prime checker
def is_prime(n):
    """Check if a number is prime"""

    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
        
        return True
   
print(is_prime(7))
print(is_prime(10))

#           3️⃣ FACTORIAL
def factorial(n):
    """Return factorial of a number"""
    
    result = 1
    for i in range(1, n + 1):
        result = result * i
    
    return result


# TEST
print(add(2, 3))
print(is_prime(7))
print(factorial(5))

# 4️⃣ palindrome

# Palindrome = same forward & backward
#madam, level, 121
# Simple version

def is_palindrome(s):
    s = str(s)         # number bhi handle ho jaye
    return s == s[::-1]


print(is_palindrome("madam"))    # True
print(is_palindrome("hello"))    # False
print(is_palindrome(121))        # True

# Beginner-friendly version(logic samajhne ke liye)

def is_palindrome(s):
    s = str(s)
    reversed_s = s[::-1]

    if s == reversed_s:
        return True
    else:
        return False
    

# 5️⃣ temperature converter

# Formula: F = (C*9/5)+32

def c_to_f(c):
    return (c * 9/5) + 32

print(c_to_f(0))
print(c_to_f(25))



def add(a, b):
    return a + b

def multiply(a, b):
    return a * b