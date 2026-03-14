#Function ka basic structure

def function_name():
    print("Hello World")

function_name()


#Function with parameters

def greet(name):
    print("Hello", name)

greet("Zeeshan")


#Function with return
def add(a, b):
    return a + b

result = add(5, 3)
print(result)


#Real_Life Example

def calculate_salary(hours, rate):
    return hours * rate

print(calculate_salary(40, 500))


#Practice Task

#Function banao jo:square nikaale
def square(n):
    print(n*n)

square(9)


#Function banao jo:even / odd check kare
def check_even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
check_even_odd(4)

#Function banao jo:3 numbers ka average nikale
def average(a,b,c):
    print((a+b+c)/3)

average(3,6,9)
